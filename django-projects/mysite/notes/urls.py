from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.notes, name='notes'),
    path('<int:note_id>', views.note, name='note'),
]