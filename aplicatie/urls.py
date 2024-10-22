from django.urls import path
from . import views
#from django.urls import path: Importă funcția path din modulul django.urls. 
# Funcția path este folosită pentru a defini rutele URL.
#from . import views: Importă modulul views din directorul curent. 
# Acest modul conține funcțiile de vizualizare (views) care vor fi mapate la rutele URL.

app_name = "aplicatie"

urlpatterns = [
    path("", views.index, name="index"),
    path("pag1", views.pag1, name="f"),
    path("pag2", views.pag2, name="g"),
    path("nr_accesari", views.pag3, name="a"),
    path("suma", views.pag4, name="b"),
    path("mesaj", views.mesaj, name="l"),
    path("data", views.data, name="h"),
    path("text", views.pag5, name="c"),
    path("nr_parametri", views.pag6, name="d"),
    path("operatie", views.pag7, name="e"),
    path("tabel", views.pag8, name="i"),
    path("tabel2", views.index1, name="j"),
    path("tabel3", views.index2, name="k"),
    path("tabel4", views.form_name_view, name="m"),
    path("tabel5", views.users, name="n"),
    path("tabel6",  views.relative, name="o"),
    path("tabel7", views.base, name="p"),
    path("tabel8", views.ceva, name="q"),
    path("register", views.register, name="r"),
    path("user_login", views.user_login, name="s"),
    path("logout", views.user_logout, name="t"),
]
