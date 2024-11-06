from django.urls import path
from .views import (
    StudentRecordListView,
    StudentRecordCreateView,
    StudentRecordUpdateView,
    StudentRecordDeleteView,
)

urlpatterns = [
    path('', StudentRecordListView.as_view(), name='student-list'),
    path('create/', StudentRecordCreateView.as_view(), name='student-create'),
    path('<int:pk>/update/', StudentRecordUpdateView.as_view(), name='student-update'),
    path('<int:pk>/delete/', StudentRecordDeleteView.as_view(), name='student-delete'),
]
