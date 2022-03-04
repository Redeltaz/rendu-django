from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from .models import Question
from .forms import QuestionForm

def index(request):
    context ={}
    context["dataset"] = Question.objects.all()

    return render(request,'exemple/index.html', context)

def create(request):
    context ={}
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/exemple")

    context['form']= form
    return render(request, "exemple/create.html", context)

def details(request, id):
    context ={}

    context["data"] = Question.objects.get(id = id)

    return render(request, "exemple/details.html", context)

def update(request, id):
    context ={}
    obj = get_object_or_404(Question, id = id)
    form = QuestionForm(request.POST or None, instance = obj)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f"/exemple/{id}")

    context["form"] = form
    return render(request, "exemple/update.html", context)

def delete(request, id):
    context ={}
    obj = get_object_or_404(Question, id = id)
    
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/exemple")

    return render(request, "exemple/delete.html", context)