from django.urls import path

from . import views

urlpatterns = [
    path('apicalls/', views.apicalls, name='apicalls'),
]