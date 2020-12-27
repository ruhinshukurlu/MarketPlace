from django.urls import path
from account.views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views 
from django.urls import reverse_lazy


app_name = 'account'

urlpatterns = [
    path('user/register', CustomerRegisterView.as_view(), name= 'user-register'),
    path('worker/register', WorkerCreateView.as_view(), name= 'worker-register'),
    path('worker/register/complete', CompletedView.as_view(), name= 'complete'),

    
    path('login', login_view, name='login'),
    path('logout', LogoutView.as_view(), name = 'logout'),

    path('change_password/',ChangePasswordView.as_view(), name = 'change-password'),
    path('change_password_done/',ChangePasswordDoneView.as_view(), name = 'change-password-done'),

    path("user/<int:pk>", CustomerProfileView.as_view(), name="user-profile"),
    path("user/<int:pk>/update", CustomerUpdateView.as_view(), name="user-update"),

    path("worker/<int:pk>", WorkerDetailView.as_view(), name="worker-detail"),

    path("/request/sent", CompletedRequest.as_view(), name="request-complete"),

]

