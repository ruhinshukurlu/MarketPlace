from django.shortcuts import render, redirect
from worker.models import *
from worker.forms import *
from django.forms import modelformset_factory

# Create your views here.


def AddSkill(request):
    image_formset = modelformset_factory(SkillPhoto, fields=('image', ), extra=10, form=SkillImageForm, validate_max=2)
    
    if request.method == 'POST':
        skill_form = AddSkillForm(request.POST or None, request.FILES or None)
        
        image_form = image_formset(request.POST or None, request.FILES or None)

        # print(tour_form.errors, image_form.errors, schedule_form.errors)
        if skill_form.is_valid() and image_form.is_valid():
            
            skill = skill_form.save(commit=False)
            skill.user = request.user
            print(skill_form.cleaned_data['vehicles'])

            skill.save()

            for i in skill_form.cleaned_data['vehicles']:
                
                skill.vehicles.add(i.id)

            for i in skill_form.cleaned_data['tools']:
               
                skill.tools.add(i.id)

            
            
            for i in image_form:
                if i.cleaned_data:
                    image = i.save(commit=False)
                    image.skill = skill
                    image.save()

            return redirect('core:home')
        else:
            messages.error(request, "Error")
    else:
        context = {
            'skill_form': AddSkillForm,
            'image_form': image_formset(queryset=SkillPhoto.objects.none()),
        }
        return render(request, 'add-skill.html', context)




