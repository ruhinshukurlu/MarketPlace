from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic import DetailView, UpdateView, TemplateView
from account.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from worker.models import *
from worker.forms import *

from django.views.generic.edit import FormMixin


User = get_user_model()


class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerRegisterForm
    template_name = 'register-user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('core:home')


class WorkerCreateView(CreateView):
    model = User
    form_class = WorkerRegisterForm
    template_name = "worker-register.html"

    def form_valid(self, form):
        print('okkk')
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
       
        return redirect('account:complete')


class CompletedView(TemplateView):
    template_name = "register-complete.html"



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('core:home')
        else:
            messages.error(request,'Email or password is not correct')
            return redirect('account:login')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




class ChangePasswordView(PasswordChangeView):
    template_name = 'change-password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('core:home')


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'change_password_done.html'


class CustomerProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user-profile.html'
    context_opject_name = 'user'

   
    def get_object(self):
        return self.request.user


class WorkerDetailView(FormMixin, DetailView):
    model = Worker
    template_name = "worker-detail.html"
    context_object_name = 'worker'
    form_class = TaskForm
    success_url = reverse_lazy('core:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.request.session['service']
        print(service)
        skill = self.request.GET.get('skill')
        context["skills"] = Skill.objects.filter(service__id=service, user=self.object.user)
        if skill:
            context["skills"] = Skill.objects.filter(service__slug = skill, user=self.object.user)
        
        return context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        # task = Task.objects.create(
        #     user=self.request.user
        # )
        print('okkk')
        service = self.request.session['service']
        skill = self.request.GET.get('skill')

        task = form.save(commit=False)
        task.user = self.request.user
        task.worker = self.object.user
        if skill:
            task.skill = Skill.objects.get(service__slug=skill, user=self.object.user)
        else:
            task.skill = Skill.objects.get(service__id=service, user=self.object.user)
        task.save()
       
        return redirect('account:request-complete')

   
class CompletedRequest(TemplateView):
    template_name = "task-sent-complete.html"
    


class CustomerUpdateView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user-update.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('account:user-profile', kwargs={'pk': self.object.pk})


