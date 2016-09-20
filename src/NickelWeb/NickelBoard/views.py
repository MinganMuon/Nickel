from django.shortcuts import render
from django.http import HttpResponse
import json

import CheckerGame.CheckerBoard as Cb
import AIswitchboard.switchboard as sb


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


def gapmoves(request):
    board = json.loads(request.GET['board'])
    color = json.loads(request.GET['color'])
    return HttpResponse(json.dumps(Cb.getallpossiblemoves(board, color)), content_type = "application/json")


def gaim(request):
    ai = json.loads(request.GET['ai'])
    board = json.loads(request.GET['board'])
    color = json.loads(request.GET['color'])
    return HttpResponse(json.dumps(sb.getaimove(ai, board, color)), content_type = "application/json")


def gais(request):
    return HttpResponse(json.dumps(sb.SWITCHABLE_AIS), content_type = "application/json")


def domakemove(request):
    board = json.loads(request.GET['board'])
    move = json.loads(request.GET['move'])
    return HttpResponse(json.dumps(Cb.makemove(board, move)), content_type = "application/json")
