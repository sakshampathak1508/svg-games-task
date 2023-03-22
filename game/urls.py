from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GameDetailView,GameListView

urlpatterns = [
    path('game/', GameListView.as_view()),
    path('game/<int:pk>/', GameDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)