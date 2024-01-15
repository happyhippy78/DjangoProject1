from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.HomePage.as_view(), name="url-home"),
    re_path(r'news/?$', views.NewsPage.as_view(), name="url-news"),
    re_path(r'offer/?$', views.OfferPage.as_view(), name="url-offer"),
    re_path(r'contacts/?$', views.ContactsPage.as_view(), name="url-contacts"),
]