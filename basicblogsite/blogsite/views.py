from django.shortcuts import render
from django.http import HttpResponse

from blogsite.models import Blog,Blogpost

# Create your views here.
def homepage(request):
	#return HttpResponse("Bonjour et Bienvenue!</p>This is a test homepage view until I learn frontend to make it pretty.")
	posts = Blogpost.objects.order_by('-pub_date')[:5]
	output = ', '.join([p.posttitle for p in posts])
	return HttpResponse(output)

#def singlepost(request):
#	return 

#def mooddumps

#def slideshow

#def todolist

#def calendar - whoa hahahaha