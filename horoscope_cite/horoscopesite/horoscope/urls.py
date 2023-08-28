from django.urls import path

from . import views

app_name = 'horoscope'
urlpatterns = [
    path('', views.index, name='index'),
    path('horoscope/aqua', views.aqua, name='aqua'),
]
