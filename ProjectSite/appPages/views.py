from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import News

class HomePage(View):
    def get(self, request):
        data = {
            'block_css': 'home'
        }
        return render(request, 'appPages/home/index.html', data)
class NewsPage(View):
    def get(self, request):
        data = {
            'block_css': 'news',
            'list_news': News.objects.order_by('-date')
        }
        return render(request, 'appPages/news/index.html', data)
class OfferPage(View):
    def get(self, request):
        data = {
            'header':{
            'block_css': 'offer'
            }
        }
        return render(request, 'appPages/offer/index.html', data)
class ContactsPage(View):
    def get(self, request):
        data = {
            'block_css': 'contacts'
        }
        return render(request, 'appPages/contacts/index.html', data)


