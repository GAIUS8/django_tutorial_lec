from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello world')


def detail(request, question_id):
    return HttpResponse("you're looking at the question {}".format(question_id))


def results(request, question_id):
    resoponse = "you're looking at the results of question {}"
    return HttpResponse(resoponse.format(question_id))


def vote(request, question_id):
    return HttpResponse("you're voting on question {}".format(question_id))
