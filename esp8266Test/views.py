from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode("utf-8"))
        value = data.get("value")
        print(value)
    return HttpResponse("5")
