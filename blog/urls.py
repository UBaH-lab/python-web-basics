from django.urls import path
from .views import (
    BlogEntryListView,
    BlogEntryDetailView,
    BlogEntryCreateView,
    BlogEntryUpdateView,
    BlogEntryDeleteView
)

app_name = 'blog'

urlpatterns = [
    path('', BlogEntryListView.as_view(), name='blogentry_list'),
    path('<int:pk>/', BlogEntryDetailView.as_view(), name='blogentry_detail'),
    path('create/', BlogEntryCreateView.as_view(), name='blogentry_create'),
    path('<int:pk>/update/', BlogEntryUpdateView.as_view(), name='blogentry_update'),
    path('<int:pk>/delete/', BlogEntryDeleteView.as_view(), name='blogentry_delete'),
]