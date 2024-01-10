from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomePage(View):
    def get(self, request):
        return render(request, 'appPages/index.html')



