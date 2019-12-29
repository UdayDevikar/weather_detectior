from .models import City 
from django.forms import ModelForm, TextInput



class city_form(ModelForm):
	class Meta:
		model= City
		fields=['name']
		widget = {

			'name': TextInput(attrs= { 'class': 'TextInput', 'placeholder': 'Enter city' })

		}