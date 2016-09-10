from django.shortcuts import render
from django.http import HttpResponse
import json

import CheckerGame.CheckerBoard as Cb

def index(request):
    return render(request, "mainui.html")


def gsb(request):
    return HttpResponse(json.dumps(Cb.getstartingboard()), content_type = "application/json")


def iswon(request):
    board = json.loads(request.GET['board'])
    return HttpResponse(json.dumps(Cb.iswon(board)), content_type = "application/json")


def gpmoves(request):
    board = json.loads(request.GET['board'])
    tile = json.loads(request.GET['tile'])
    return HttpResponse(json.dumps(Cb.getpossiblemoves(board, tile)), content_type = "application/json")
