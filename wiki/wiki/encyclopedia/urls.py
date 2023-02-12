from django.urls import path, include

from . import views

app_name ="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("links", views.links, name="links"),
    path("add_page", views.newPage, name="add_page"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("random", views.random, name="random"),
   
]
