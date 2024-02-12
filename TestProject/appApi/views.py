from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import random

class ApiHome(View):
    def get(self, request):
        return render(request, 'appApi/index.html')
    
    def post(self, request):
        len_password = request.POST['len_password']
        count_password = request.POST['count_password']
        data_chars = 'vnfnhfgknnjvgdvfddlknvgn1514514514514'
        data = []
        
        for psw in range(int(count_password)):
            password = ''
            for char in range(int(len_password)):
                password += data_chars[random.randint(0, len(data_chars)-1)]
            data.append(password)    
        
        return JsonResponse({
            'status' : 'ok',
            'data_password' : data
        })

