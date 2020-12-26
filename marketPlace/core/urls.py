from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from core.views import *

app_name = 'core'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("services/<slug:slug>", ServiceDetailView.as_view(), name="service-detail"),
    # path('search/', autocomplete, name='autocomplete'),
]

