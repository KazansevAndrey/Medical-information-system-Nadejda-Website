from django.urls import path
from .views import diary_view, update_diary, delete_diary

app_name = 'diary'

urlpatterns = [
    path('<int:diary_id>/', diary_view, name='diary'),
    path('<int:diary_id>/update', update_diary, name='update_diary'),
    path('<int:diary_id>/delete', delete_diary, name='delete_diary')

]