from django.shortcuts import render
from django.http.response import HttpResponse
from .models import quiz_allocation, Quiz, Question
from itertools import chain
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def homepage(request):
    quiz_assigned = quiz_allocation.objects.filter(user=request.user)
    print(quiz_assigned)
    content = {'quizes':quiz_assigned}
    return render(request, 'quizes/home.html', content)

def quiz_page(request, pk):
    print("QUIZ PAGE VIEW")
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

def save_quiz(request, pk):
    try:
        print("----------------RESULT PAGE VIEW ENTRYY-----")
        print("VIEW DATA-----",request.POST)
        data = request.POST
        cnt_correct = 0
        for x in data:
            print(x)
            # import pdb
            # pdb.set_trace()
            try:
                que = Question.objects.get(title=x)
            except ObjectDoesNotExist:
                continue
            correct = que.get_correct_answer()
            print(correct)
            if data[x] == correct[0].option:
                cnt_correct += 1
        context = {'total': len(data), 'score':cnt_correct, 'message': f"Your Score: {cnt_correct}/{len(data)}"}
        return JsonResponse(context)

    except Exception:
        import traceback
        print(traceback.format_exc())
