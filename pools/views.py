from django.http import HttpResponse,HttpResponseRedirect
from pools.models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
	template_name = 'pools/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	template_name = 'pools/detail.html'
	model = Question

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'pools/results.html'

def vote(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'pools/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('pools:results', args=(question.id,)))