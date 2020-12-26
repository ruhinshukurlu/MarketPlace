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


class CustomerUpdateView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user-update.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('account:user-profile', kwargs={'pk': self.object.pk})


