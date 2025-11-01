from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # estamos asociando una vista (view) llamada post_list a la URL raíz. name='post_list' es el nombre de la URL que se utilizará para identificar a la vista.
]
'''
Este patrón le dirá 
a Django que views.post_list es el lugar 
correcto al que ir si alguien entra a tu sitio web con la dirección 'http://127.0.0.1:8000/'.
'''