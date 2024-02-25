from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageAuth.as_view(), name="urlPageAuth"),
    path('/registration/', views.PageReg.as_view(), name="urlPageReg")
]