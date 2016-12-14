from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	context = {
		"usuario": "Diego"
	}

	return render(request, 'home.html', context)