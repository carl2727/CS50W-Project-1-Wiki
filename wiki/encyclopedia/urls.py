from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("<str:entry>/edit/", views.edit, name="edit"),
    path("random/", views.rand_entry, name="rand_entry")
]
