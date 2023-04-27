from django.shortcuts import render, redirect, HttpResponse



def home(request):
	return render(request, "home.html")



def register(request):
	return render(request, "register.html")
