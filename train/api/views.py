from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests

# Create your views here.

token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTM3MTkyOTksImNvbXBhbnlOYW1lIjoiVHJhaW4gQ2VudHJhbCIsImNsaWVudElEIjoiMzQwMWVjZDktZTBmMC00NTRkLTlhMGMtNDUzOGUwYzVhYWU0Iiwib3duZXJOYW1lIjoiIiwib3duZXJFbWFpbCI6IiIsInJvbGxObyI6IjEyNDAwNDEzNiJ9.fElu81AhZq9LHK8YrPCQ5u_V5-2ZTLiDNSW41Za5ZaM"

data={
    "companyName": "Train Central",
    "clientID": "3401ecd9-e0f0-454d-9a0c-4538e0c5aae4",
    "clientSecret": "NSJkMStsVPJvwuxL",
    "ownerName": "karthi",
    "ownerEmail": "124004136@sastra.ac.in",
    "rollNo": "124004136"
}

def home(request):
    result={}
    global token

    url="http://20.244.56.144/train/trains"
    headers = {"Authorization": "Bearer "+token}
    response=requests.get(url,headers=headers)
    response_data=response.json()
    try:
        if("message" in response_data and response_data['message'].find('token is expired')!=-1):
            auth_response=requests.post("http://20.244.56.144/train/auth",json=data)
            token=auth_response.json()['access_token']
            print(token)
    except:
        pass
    response=requests.get(url,headers=headers)
    response_data=response.json()
    print(response_data)
    return JsonResponse(response.json(),safe=False)