from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import modelformset_factory
from django.db.models import Q

from .forms import CourtForm, AddressForm
from .models import Court, City, District, Address, CourtPhoto

def home(request):
	courts = Court.objects.order_by('-created_at')[:4]
	return render(request, 'home.html', {'courts': courts})

def is_owner(user):
	return user.groups.filter(name='Court owner').exists()

def load_districts(request):
	city_id = request.GET.get('city')
	districts = District.objects.filter(city_id=city_id).order_by('name')
	return render(request, 'address/district_list.html', {'districts': districts})

def mycourt(request, pk):	
	court = get_object_or_404(Court, pk=pk)
	court_form = CourtForm(instance=court)
	if court :
		address = court.address
	else:
		address = None
	address_form = AddressForm(instance=address)
	photos = CourtPhoto.objects.filter(court=court)
	courts = Court.objects.filter(owner=request.user)

	if request.method == 'POST':
		court_form = CourtForm(request.POST, instance=court)
		address_form = AddressForm(request.POST, instance=address)	
		image_list = request.FILES.getlist('imgInput')
		
		if court_form.is_valid() and address_form.is_valid():
			court = court_form.save(commit=False)
			address = address_form.save(commit=False)
			address.save()
			court.owner = request.user
			court.address = address
			court.save()
			##CourtPhoto.objects.filter(court=court).delete()
			for image in image_list:
				print (image.name)
				CourtPhoto.objects.create(court=court, photo=image)

	return render(request, 'profile/mycourt.html', {
		'courts': courts,
		'court_form': court_form,
		'address_form': address_form,
		'photos': photos
	})

def courts(request):
	cities = City.objects.all()

	if request.method == 'POST':		
		## 1. Filter by address
		city_id = request.POST.get('city')
		district_id = request.POST.get('district')
		city = getCity(city_id)
		district = getDistrict(district_id)
		courts = filterByAddress(city, district)
		## 2. Filter by price
		price_min = request.POST.get('price_min')
		price_max = request.POST.get('price_max')
		courts = filterByPrice(courts, price_min, price_max)
		## 3. Sort
		sort_type = request.POST.get('sort')		
		courts = sort(courts, sort_type)
		queryset = courts
	else:	
		courts = Court.objects.all()
		city = None
		district = None
		price_min = None
		price_max = None
		sort_type = 'dateAsc'
		queryset = courts.order_by('created_at')

	districts = District.objects.filter(city=city)
	page = request.GET.get('page', 1)

	paginator = Paginator(queryset, 6)

	try:
		courts = paginator.page(page)
	except PageNotAnInteger:
		courts = paginator.page(1)
	except EmptyPage:
		courts = paginator.page(paginator.num_pages)

	return render(request, 'court/courts.html', {
		'courts': courts, 
		'cities': cities, 
		'districts': districts, 
		'city': city, 
		'district': district,
		'price_min': price_min,
		'price_max': price_max,
		'sort_type': sort_type
	})

def filterByAddress(city, district):
	if city is None:	
		courts = Court.objects.all()
	else:
		if district is None:		
			courts = Court.objects.filter(address__city=city)
		else:
			courts = Court.objects.filter(address__district=district)

	return courts

def getCity(city_id):
	if int(city_id) == -1:
		return None
	else:
		city = City.objects.get(pk=city_id)
		return city

def getDistrict(district_id):
	if int(district_id) == -1:
		return None
	else:
		district = District.objects.get(pk=district_id)
		return district

def filterByPrice(courts, price_min, price_max):
	if price_min == '' or price_max == '':
		return courts
	else:
		courts = courts.filter(price__gte=price_min, price__lt=price_max)
		return courts

def sort(courts, sort_type):
	if sort_type == 'dateAsc':
		courts = courts.order_by('created_at')
	elif sort_type == 'dateDesc':
		courts = courts.order_by('-created_at')
	elif sort_type == 'nameAsc':
		courts = courts.order_by('name')
	elif sort_type == 'nameDesc':
		courts = courts.order_by('-name')
	elif sort_type == 'priceAsc':
		courts = courts.order_by('price')
	elif sort_type == 'priceDesc':
		courts = courts.order_by('-price')

	return courts

def court(request, pk):
	court = Court.objects.get(pk=pk)
	photos = CourtPhoto.objects.filter(court=court)
	return render(request,  'court/court.html', {'court': court, 'photos': photos})