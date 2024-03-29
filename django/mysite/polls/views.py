from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from .models import Vote, Choice

# Create your views here.
def index(request):
    latest_vote_list = Vote.objects.order_by("id")
    context = {
        'latest_vote_list': latest_vote_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        v = Vote.objects.get(pk=question_id)
    except Vote.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': v})

def vote(request, question_id):
    question = get_object_or_404(Vote, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Vote, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})