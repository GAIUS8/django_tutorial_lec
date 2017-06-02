from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # question_id가 pk인 Question객체를 가져와 context라는 이름을 가진 dict에 question이라는 키 값으로 위 변수를 할당
    # 이후 polls/detail.html과 context를 랜더한 결과를 리턴
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist as e:
        raise Http404('That Question does not exist')

    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context=context)

def results(request, question_id):
    resoponse = "you're looking at the results of question {}"
    return HttpResponse(resoponse.format(question_id))


def vote(request, question_id):
    return HttpResponse("you're voting on question {}".format(question_id))
