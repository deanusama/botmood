from django.urls import path, include
from django.contrib.auth import views as auth_views
from pages import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about_us'),
    path('contact', views.contact, name='contact'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    path('financial_support', views.financial_support, name='financial_support'),

    path('accounts/login', views.login_user, name='login'),
    path('accounts/logout', views.user_logout, name='logout'),
    path('accounts/signup', views.signup_user, name='signup'),
    path('accounts/profile', views.edit_profile, name='profile'),
    path('accounts/edit_password', views.edit_password, name='password'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent"
                                                                                        ".html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts"
                                                                                              "/password_reset_form"
                                                                                              ".html"),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts"
                                                                                                "/password_reset_done"
                                                                                                ".html"),
         name="password_reset_complete"),

]


'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''