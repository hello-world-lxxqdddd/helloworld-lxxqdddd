#_*_coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from .models import HomePage
from photo.models import Photo
# Create your views here.

class IndexView(View):
    def get(self,request):
        home_pages = HomePage.objects.all()
        home_page_photos = Photo.objects.all()
        home_page_photo = home_page_photos.order_by("create_data")[:6]
        for i in home_pages:
            home_page = i
        return render(request,'index.html',{"homepage":home_page,"home_page_photo":home_page_photo})

