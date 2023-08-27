from django.urls import path

from .views import LetterListView, LetterCreateView, LetterDetailView

urlpatterns = [
    # path('', views.letters, name='letters'),
    path('', LetterListView.as_view(), name='letters'),
    path('send/', LetterCreateView.as_view(), name='new_letter'),
    path('<int:pk>/', LetterDetailView.as_view(), name='letter_id'),
]
