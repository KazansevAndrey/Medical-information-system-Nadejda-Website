from django.urls import path
from .views import diary_view

app_name = 'diary'

urlpatterns = [
    path('<int:diary_id>/', diary_view, name='diary'),
]