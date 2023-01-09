from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, ListView
from django.http import HttpResponse
from worker.models import *
from account.models import *
import json

from datetime import datetime
# Create your views here.

class HomeView(TemplateView):
    template_name = "home-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context
    

# def autocomplete(request):
#     if request.is_ajax():
#         query = request.GET.get("term", "")
#         places = WorkPlace.objects.filter(title__istartswith=query)
#         results = []
#         for place in places:
#             place_json = place.title
#             results.append(place_json)
#         data = json.dumps(results)
#     mimetype = "application/json"
#     return HttpResponse(data, mimetype)


class ServiceDetailView(ListView):
    context_object_name = 'skills'
    template_name = "service-detail.html"

    def get_queryset(self):
        service = get_object_or_404(Service, slug=self.kwargs['slug'])
        print(service)
        self.request.session['service'] = service.pk
        queryset = Skill.objects.filter(service = service)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(user__worker__work_place__icontains = search)
        
        return queryset
    

class TaskListView(ListView):
    model = Task
    template_name = "task-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["upcoming_tasks"] = Task.objects.filter(worker=self.request.user, accept=False, denied=False)
        context["accepted_tasks"] = Task.objects.filter(worker=self.request.user, accept=True, date__gt = datetime.today())
        context["past_tasks"] = Task.objects.filter(worker=self.request.user, accept=True, date__lt = datetime.today())

        return context
    
    

def accept(request, pk):

    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        task.accept = True
        task.save()
        
        return redirect('core:task-list')

def denied(request, pk):

    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        task.denied=True
        task.save()
        
        return redirect('core:task-list')


class PaymenyView(TemplateView):
    template_name = "payment.html"
 
