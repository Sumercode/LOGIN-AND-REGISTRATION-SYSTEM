from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),

    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),

    #######app urls
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_complete"),
    #######



]


'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''