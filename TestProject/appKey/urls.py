from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HomeKey.as_view(), name="urlHomeKey"),
    path('', views.CategorysPage.as_view(), name="urlCategorys"),
    path('category/<int:id>', views.ProductPage.as_view(), name="urlProduct"),
    
]