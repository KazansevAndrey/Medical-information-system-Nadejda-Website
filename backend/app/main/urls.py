from django.urls import path
import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='profile')
]
