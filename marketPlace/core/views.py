from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from django.http import HttpResponse
from worker.models import *
from account.models import *
import json

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
    
    

