from django.urls import path
from .views import AlarmList, AlarmPost, AlarmEdit

urlpatterns = [
    path('get/alarms/',AlarmList.as_view(),name="get_alarms"),
    path('post/alarms/', AlarmPost.as_view(),name="post_alarms"),
    path('edit/alarms/<int:pk>/', AlarmEdit.as_view(),name="edit_alarms")
]