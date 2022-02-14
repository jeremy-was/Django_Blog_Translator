from . import views
from django.urls import path

# JW Created e.g. blog and home view, see views.py for class creation
urlpatterns = [
    path('', views.translator_view, name='translator_view')
]