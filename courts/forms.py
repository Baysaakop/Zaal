from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from bootstrap_datepicker_plus import DatePickerInput

from .models import Court, City, District, Address

class CourtForm(forms.ModelForm):
	like = forms.IntegerField(disabled=True)	
	rating = forms.FloatField(disabled=True)
	class Meta:
		model = Court
		fields = ('name', 'description', 'phone_number', 'price', 'like', 'rating')
		widgets = {
			'description': forms.Textarea(attrs={'rows':9, 'cols':15}),
		}

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ('city', 'district', 'address1', 'address2')

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['district'].queryset = District.objects.none()

			if 'city' in self.data:
				try:
					city_id = int(self.data.get('city'))
					self.fields['district'].queryset = District.objects.filter(city_id=city_id).order_by('name')
				except (ValueError, TypeError):
					pass
			elif self.instance.pk:
				self.fields['district'].queryset = self.instance.city.district_set.order_by('name')