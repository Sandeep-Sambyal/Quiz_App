from django.shortcuts import render
from .models import quiz_allocation

def homepage(request):
    quiz_assigned = quiz_allocation.objects.filter(user=request.user)
    print(quiz_assigned)
    content = {'quizes':quiz_assigned}
    return render(request, 'quizes/home.html', content)