from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template("polls/index.html")
    context = {}
    return HttpResponse(template.render(context, request))
