from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from .models import Question, Choice


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')
    latest_question_list = get_list_or_404(Question.objects.order_by('-pub_date'))
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # question_id가 pk인 Question객체를 가져와 context라는 이름을 가진 dict에 question이라는 키 값으로 위 변수를 할당
    # 이후 polls/detail.html과 context를 랜더한 결과를 리턴
    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context=context)


def vote(request, question_id):
    if request.method == 'POST':
        data = request.POST
        try:
            choice_id = data['choice']
            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            # return HttpResponse('Choice is {}'.format(choice_id))
            return redirect('polls:results', question_id)
        except (KeyError, Choice.DoesNotExist):
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice",
            )
            return redirect('polls:detail', question_id)

    else:
        return HttpResponse('wrong')


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context=context)
