from django.urls import path

from . import views

urlpatterns = [
    path('', views.CEOListView.as_view(), name='ceos'),
]