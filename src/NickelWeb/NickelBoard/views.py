from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # return HttpResponse("NickelBoard/views/index")
    return render(request, "board.html")
