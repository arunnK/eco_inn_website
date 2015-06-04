from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

# Create your views here.

def blog(request):
	return render_to_response("blog/blog.html")

def post1(request):
	return render_to_response("blog/post1.html")

def post2(request):
	return render_to_response("blog/post2.html")

def post3(request):
	return render_to_response("blog/post3.html")

def post4(request):
	return render_to_response("blog/post4.html")

def post5(request):
	return render_to_response("blog/post5.html")

def post6(request):
	return render_to_response("blog/post6.html")