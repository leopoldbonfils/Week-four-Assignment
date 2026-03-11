# inventory/urls.py

from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    # List  →  /inventory/
    path(
        '',
        views.ItemListView.as_view(),
        name='list'
    ),

    # Detail  →  /inventory/3/
    path(
        '<int:pk>/',
        views.ItemDetailView.as_view(),
        name='detail'
    ),

    # Create  →  /inventory/new/
    path(
        'new/',
        views.ItemCreateView.as_view(),
        name='create'
    ),

    # Update  →  /inventory/3/edit/
    path(
        '<int:pk>/edit/',
        views.ItemUpdateView.as_view(),
        name='update'
    ),

    # Delete  →  /inventory/3/delete/
    path(
        '<int:pk>/delete/',
        views.ItemDeleteView.as_view(),
        name='delete'
    ),
]