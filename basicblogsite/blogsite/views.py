from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	return HttpResponse("Bonjour et Bienvenue!</p>This is a test homepage view until I learn frontend to make it pretty.")

#def singlepost(request):
#	return 

#def mooddumps

#def slideshow

#def todolist

#def calendar - whoa hahahaha