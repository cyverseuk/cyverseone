from django.db import models

# Create your models here.

class UserQuota(models.Model):
	cpu = models.IntegerField()
	storage = models.IntegerField()
	username = models.CharField(max_length=20)
	vmname = models.CharField(max_length=20)
	ram = models.IntegerField()
	key = models.TextField()

class VM(models.Model):
	cpu = models.IntegerField()
	storage = models.IntegerField()
	username = models.CharField(max_length=20)
	vmname = models.CharField(max_length=20)
	ram = models.IntegerField()	
	key = models.TextField()
