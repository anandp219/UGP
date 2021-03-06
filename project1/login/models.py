from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class Role(models.Model):
	role = models.IntegerField(default=1, primary_key=True )
	designation = models.CharField(max_length=255)
	def __unicode__(self):
		return self.designation

class Departments(models.Model):
	dep_id = models.IntegerField(default=0, primary_key=True )
	dep_name = models.CharField(max_length=255)
	def __unicode__(self):
		return self.dep_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True,max_length=13)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    role = models.ForeignKey(Role)
    def __unicode__(self):
    	return self.user.username


class Student(models.Model):
	roll = models.CharField(max_length=24,primary_key=True )
	user = models.OneToOneField(UserProfile)
	dept = models.ForeignKey(Departments,blank=True)
	def __unicode__(self):
		return self.user.user.username

class TA(models.Model):
	roll = models.CharField(max_length=24,primary_key=True )
	user = models.OneToOneField(UserProfile)
	dept = models.ForeignKey(Departments,blank=True)
	def __unicode__(self):
		return self.user.user.username

class Instructor(models.Model):
	i_id = models.CharField(max_length=24 ,primary_key=True )
	user = models.OneToOneField(UserProfile)
	dept = models.ForeignKey(Departments,blank=True)
	def __unicode__(self):
		return self.user.user.username
