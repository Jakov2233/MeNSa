from .views import kolicina_guzve
from django.urls import path


urlpatterns = [
    path('kolicinaGuzve/', kolicina_guzve, name='kolicinaGuzve'),

]