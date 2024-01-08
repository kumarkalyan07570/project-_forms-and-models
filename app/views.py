from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse

def  insert_data(request):
 

    OPDT=Data1()
    d={'OPDT':OPDT}

    if request.method=='POST':
        TFDO=Data1(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic is done Successfully')
        
    return render(request,'insert_data.html',d)


def web_data (request):
    OWDT=Web()
    d1={'OWDT':OWDT}

    if request.method=='POST':
        WTO=Web(request.POST)
        if WTO.is_valid():
            WTO.save()


    return render(request,'web.html',d1)
