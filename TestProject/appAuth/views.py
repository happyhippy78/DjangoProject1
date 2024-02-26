from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class PageAuth(View):
    def get(self, request):
        print(request.user.is_authenticated)
        return render(request, 'appAuth/auth/index.html')
    def post(self, request):
        _login = request.POST['login']
        _password = request.POST['password']
        user = authenticate(
            username = _login,
            password = _password
        )
        status = ''
        if user is not None:
            if user.is_active:
                login(request, user)
                status += 'ok'
        else:
            status += "errorNotUser"
        return JsonResponse({
            'status': status
        })
    
class PageReg(View):
    def get(self, request):
        return render(request, 'appAuth/registration/index.html')
    def post(self, request):
        login = request.POST['login']
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        status = ''
        try:
            status += 'NoLogin'
            User.objects.get(username=login)
        except:
            status += 'ok' 
            User.objects.create(
                first_name = name,
                last_name = surname, 
                email = email,
                username = login,
                password = password
            )
        return JsonResponse({
            'status': status
        })
       
        