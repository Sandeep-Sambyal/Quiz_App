from django.shortcuts import render
from django.http.response import HttpResponse
from .models import quiz_allocation, Quiz, Question
from itertools import chain


def homepage(request):
    quiz_assigned = quiz_allocation.objects.filter(user=request.user)
    print(quiz_assigned)
    content = {'quizes':quiz_assigned}
    return render(request, 'quizes/home.html', content)

def quiz_page(request, pk):
    
    quiz = Quiz.objects.get(pk=pk)
    # print(pk)
    # print(quiz)
    easy_ques = Question.objects.filter(difficulty='easy', quiz=quiz).order_by('?')[:5]
    med_ques = Question.objects.filter(difficulty='medium', quiz=quiz).order_by('?')[:3]
    hard_ques = Question.objects.filter(difficulty='hard', quiz=quiz).order_by('?')[:2]
    question_list = list(chain(easy_ques, med_ques, hard_ques))
    # print(easy_ques, med_ques, hard_ques)
    questions = []
    for que in question_list:
        answer = []
        for ans in que.get_answers():
            answer.append(str(ans.option))
        questions.append({str(que): answer})
    context = {'questions': questions}
    print(context)
    # return HttpResponse(context)

    return render(request, 'quizes/quiz.html', context)

