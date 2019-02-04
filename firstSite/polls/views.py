from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
#from django.template import loader
from .models import Question

def index(req):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    #output = ','.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, req))
    return render(req, 'polls/index.html', context)
# Create your views here.
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
