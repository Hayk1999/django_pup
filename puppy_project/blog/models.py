from django.db import models
from django.urls import reverse

# Create your models here.
class Puppy(models.Model):
	name = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.name
		
	def get_absolute_url(self):
		return reverse('detail_pup', args=[str(self.id)])