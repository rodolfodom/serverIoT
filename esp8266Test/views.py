from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_http_methods, require_safe
import json

@require_http_methods(["POST"])
@csrf_exempt
def index(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode("utf-8"))
        value = data.get("value")
        print(value)
    return HttpResponse("5")
