from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
# Create your views here.

def home(request):
    print(request.GET)
    urls=dict(request.GET)['url']
    # print(urls)

    merged_unique=[]
    totalNumbers=[]
    for url in urls:
        response=requests.get(url)
        if response.status_code==200:
            response_data=response.json()
            numbers=response_data['numbers']
            totalNumbers.extend(numbers)
    
    merged_unique=list(set(totalNumbers))
    merged_unique.sort()
    return JsonResponse({
        'numbers':merged_unique
    })