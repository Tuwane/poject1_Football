from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.players, name='players'),
    path('player/details/<int:id>', views.detalils, name='details'),
]
