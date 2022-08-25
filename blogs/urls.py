
# Определяет схемы url для blogs

from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    # Homepage
    path("", views.index, name="index"),
    # Add new entry
    path("add_new",views.add_new, name="add_new"),
    # Edit entry
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]