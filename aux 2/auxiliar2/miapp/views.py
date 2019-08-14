from django.shortcuts import render

def index(request):
	return render(request, 'miapp/index.html')

def pestaña(request):
	return render(request, 'miapp/pestaña.html')
	
def quiensomos(request):
	return render(request, 'miapp/quiensomos.html')

