from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.login_view, name='login'),

    path('logout', views.logout_view, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name = 'accounts/resetPassword.html',
        html_email_template_name = 'accounts/passwordResetEmail.html',
        email_template_name = 'accounts/passwordResetEmail.txt',
        subject_template_name = 'accounts/passwordResetSubject.txt',
        success_url = reverse_lazy('accounts:reset_done')
    ),name='reset_password'), 

    path('reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'accounts/resetDone.html',
    ),name='reset_done'),

    path('reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'accounts/resetConfirm.html',
        success_url = reverse_lazy('accounts:reset_complete')
    ), name='reset_confirm'),

    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'accounts/resetComplete.html',
    ), name='reset_complete'),
]