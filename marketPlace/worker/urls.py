from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from worker.views import *

app_name = 'worker'

urlpatterns = [
    path("add-skill", AddSkill, name="add-skill"),
]

