from django.shortcuts import render, redirect
from django.http import JsonResponse # отображение словаря для API
from django.views import View
from .models import Product, Category, ProductPhotos


class HomeKey(View):
    def get(self, request):
        data = {
            'product': Product.objects.get(id=1)
        }
        return render(request, 'appKey/product/index.html', data)
    def post(self, request):
        if request.POST['method'] == 'addCategory':
            Category.objects.create(
                title = request.POST['text']
            )
        if request.POST['method'] == 'updateCategory':
            Category.objects.filter(title = request.POST['text']).update(
                title = request.POST['new_text']
            )
        if request.POST['method'] == 'deleteCategory':
            Category.objects.filter(
                title = request.POST['text']).delete(
            )
        return redirect('urlHomeKey')