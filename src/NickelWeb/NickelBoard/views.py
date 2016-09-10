from django.shortcuts import render
from django.http import HttpResponse
import json

import CheckerGame.CheckerBoard as Cb

def index(request):
    return render(request, "mainui.html")

def gsb(request):
    return HttpResponse(json.dumps(Cb.getstartingboard()), content_type = "application/json")
