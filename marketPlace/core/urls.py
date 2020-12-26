from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from core.views import *

app_name = 'core'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]

