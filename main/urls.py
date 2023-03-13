from django.urls import path
from main import views
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

    path('register/', views.register_page, name='register'),
    path('reset_password/', PasswordResetView.as_view(template_name='reset_password.html'), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name='password_reset_complete')
]