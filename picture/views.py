from django.shortcuts import render,HttpResponse
from .models import Picture,Location,Category

# Create your views here.
def welcome(request):
    pictures = Picture.objects.all()
    kenya=Picture.filter_by_location(location='Kenya')
    japan=Picture.filter_by_location(location='Japan')
    mozambique=Picture.filter_by_location(location='Mozambique')
    iceland=Picture.filter_by_location(location='Iceland')
    return render(request,'all-pictures/index.html',{'pictures':pictures, 'kenya':kenya,'japan':japan,'mozambique':mozambique,'iceland':iceland})
