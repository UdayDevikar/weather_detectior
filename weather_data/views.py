from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
from .forms import city_form
from .models import City
# Create your views here.


def home(request):
	form = city_form()
	if request.method == "POST":
		city_name = request.POST.get('name')
		# form=city_form()
		url=('http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7ea32f8e87fc4f3e6b4868da4594479f'.format(city_name ))	
		r=requests.get(url)
		text=r.json()									# cretaing a object python dictionary 
		new=json.dumps(text, indent=10)		
		context = {

		'city': text['name'],
		'country':text['sys']['country'],
		'temperature':text['main']['temp'],
		'form': form

		}			
		
		return render (request,'home.html', context)
		
	return render (request, 'home.html', {'form': form } )
		

	