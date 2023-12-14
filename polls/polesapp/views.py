from django.http import Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice


# Create your views here.

def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions_list': latest_questions_list}
    return render(request, 'index.html', context)

# show specific choices and question
def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!")
    return render(request, 'details.html', {'question': question })

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'details.html',{
            'question': question,
            'error_message': "You didn't select a choice.",        
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirct after successfully dealing
        # with POST data. This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polesapp:results', args=(question.id,)))
    