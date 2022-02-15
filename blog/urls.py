from . import views
from django.urls import path

# JW Created e.g. blog and home view, see views.py for class creation
urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('', views.PostList.as_view(), name='home'),
    path('admin/', views.AdminView.as_view(), name='admin_view')
]