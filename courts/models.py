from django.db import models
from django.contrib.auth.models import User

## ADDRESS SECTION:
class City(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.name

class District(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Address(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	district = models.ForeignKey(District, on_delete=models.CASCADE)
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)

	def __str__(self):
		return self.address1 + ", " + self.address2;

## COURT SECTION:
class Court(models.Model):
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(blank=True)
	address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='court_address')
	phone_number = models.CharField(max_length=8, unique=True)
	owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='court_owner')
	created_at = models.DateTimeField(auto_now_add=True)
	price = models.PositiveIntegerField(default=0)
	like = models.PositiveIntegerField(default=0)
	rating = models.FloatField(default=0)

	def __str__(self):
		return self.name;

def user_directory_path(instance, filename):
    return 'img/courts/{0}/{1}'.format(instance.court.id, filename)

class CourtPhoto(models.Model):
	court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name="photos")
	photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.court.name + " photo";