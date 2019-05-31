from django.db import models
#from django.utils import timezone

# Create your models here.
class Plant(models.Model):
	plants_name = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	thumb = models.ImageField('img', upload_to='plant_pics', null=True)


	def __str__(self):
		return self.plants_name

class PlantDetails(models.Model):
	plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
	plant_image = models.ImageField('img', upload_to='plant_pics/large/', null=True)
