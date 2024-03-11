from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import StaticLink
from collections import Counter



class StaticLinkPage(View):
    def get(self, request, name_link):
        statics_obj = StaticLink.objects.filter(
            pub_news__name_url= name_link
        )
        object_browser = dict(Counter(statics_obj.values_list('browser', flat=True)))
        print(object_browser)
        object_os = dict(Counter(statics_obj.values_list('os', flat=True)))
        object_pub_news = dict(Counter(statics_obj.values_list('pub_news', flat=True)))
        

        return render (
            request,
            'appAnalytics/base.html',
            {
                'browsers': object_browser,
                'os': object_os,
                'pub_news': object_pub_news,
                
            }
        )