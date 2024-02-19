from django.shortcuts import render
from django.views import View

class PageAuth(View):
    def get(self, request):
        return render(request, 'appAuth/auth/index.html')