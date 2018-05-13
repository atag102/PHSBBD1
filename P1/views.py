from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class vista1(TemplateView):
	template_name='P1/prueba1.html'