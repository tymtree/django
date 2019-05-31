from django.shortcuts import render
from django.views import generic
from .models import Plant

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'prac1/index.html'
	context_object_name = 'plants_list'
	paginate_by = 20

	def get_queryset(self):
		return Plant.objects.order_by('pub_date')[:20]

class DetailView(generic.DetailView):
	model = Plant
	template_name = 'prac1/details.html'
	#context_object_name = 'plant_data'
