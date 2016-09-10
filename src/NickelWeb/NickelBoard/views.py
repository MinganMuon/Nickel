from django.shortcuts import render
from django.http import HttpResponse
import json

import CheckerGame.CheckerBoard as Cb
import RandomAI.RandomAI


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


def graim(request):
    board = json.loads(request.GET['board'])
    color = json.loads(request.GET['color'])
    return HttpResponse(json.dumps(RandomAI.RandomAI.getrandomaimove(board, color)), content_type = "application/json")