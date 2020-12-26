from django.shortcuts import render
from django.views.generic import TemplateView
from worker.models import *


# Create your views here.

class HomeView(TemplateView):
    template_name = "home-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context
    

