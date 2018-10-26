from django.shortcuts import render
from django.core import serializers
import json
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from NLP.models import NLP_MAPS
from NLP.audio2text import *
from NLP.text2info import *
# Create your views here.
import googlemaps
from . import text2info

from .models import NLP_MAPS

def index(location):
    template = 'NLP/index.html'
    map = NLP_MAPS()
    res = {}
    res['Address'] = locations
    res['Intensity']=1
    #res = text2info.get_info()
    print("here ", res)
    gmaps = googlemaps.Client(key='AIzaSyBdl9Xvi8Yipfx-ldaB9RtluwGEyuU1KHM')
    print("kiops")
    geocode_result = gmaps.geocode(res['Address'])
    print("asaasa")
    print(geocode_result)
    # print(geocode_result)
    map.Address = res['Address']
    map.x = geocode_result[0]['geometry']['location']['lat']
    map.y = geocode_result[0]['geometry']['location']['lng']
    map.intensity = res['Intensity']
    map.save()
    #return render(request,template,{'res':res})

def dashboard(request):
    address = NLP_MAPS.objects.all()
    return render(request,'dashboard.html',{'address': address})

def home(request):
    return render(request,'Home/home.html')

def maps(request):
    address = NLP_MAPS.objects.values('id','x','y','Address')
    # serial = serializers.serialize('json', [ address, ])
    json_data = json.dumps(list(address))
    return render(request,'NLP/maps.html',{'address':json_data})

def upload(request):
    if request.method == 'GET' :
        return render(request,'NLP/upload.html')

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        converted_text= get_text_from_audio(uploaded_file_url)
        #print(converted_text)
        info= get_info(converted_text['DisplayText'])
        #print(info)
        #Passing function to google map api
        #index(info[][])
        return render(request, 'NLP/upload.html', {
            'converted_text':converted_text,
            'info': info,
            })
