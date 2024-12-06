from django.http import HttpResponse # to directly return HTML code in String format
from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = 'My Page'
    my_context = {
        "page_title" : my_title,
        "queryset" : queryset.count()
        }
    path = request.path
    print('path',path)
    PageVisit.objects.create()
    return render(request, 'home.html', my_context)