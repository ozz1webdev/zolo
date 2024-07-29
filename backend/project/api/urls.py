from django.urls import path, include
from . import views

urlpatterns = [
    path('notes/', views.NotesListCreate.as_view(), name="note-list"),
    path('notes/delete/<int:pk>/', views.NoteDelete.as_view(), name="note-delete"),
    path('notes/update/<int:pk>/', views.NoteUpdate.as_view(), name="note-update"),
]
