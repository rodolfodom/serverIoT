from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_http_methods, require_safe
import json

def distancia(adc):
    distancia_cm = 27.86 / (adc - 0.1)
    return distancia_cm



@require_http_methods(["POST"])
@csrf_exempt
def index(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode("utf-8"))
        value = float(data.get("value"))
        distancia_cm = distancia(value)
        
    return HttpResponse(distancia_cm)
