from django.shortcuts import render
from django.http import HttpResponse 
from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    output = [{"question:":q.question_text, "pop_time:":q.pop_time, "total_vote_cnt:":q.total_vote_cnt} for q in latest_question_list]
    return HttpResponse(output)