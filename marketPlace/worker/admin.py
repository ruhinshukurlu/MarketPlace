from django.contrib import admin
from worker.models import *
# Register your models here.

admin.site.register([Tool, Task, Vehicle, SkillPhoto, Skill, Service])

