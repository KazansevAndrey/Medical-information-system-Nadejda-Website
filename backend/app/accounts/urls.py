from django.urls import path
from .views import user_login, user_logout, redirect_view

app_name = 'accounts'

urlpatterns = [
    path('', redirect_view, name='redirect'),
    path('accounts/login/', user_login, name='login'),
    path('accounts/logout/', user_logout, name='logout')
]
