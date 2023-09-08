from django.urls import path
from . import views

app_name = 'encuesta'  # Esto define el espacio de nombres 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página principal
    path('enviar', views.enviar, name='enviar'),  # Ruta para procesar el formulario
    # Otras rutas aquí si las tienes
    path('calcular/', views.calcular, name='calcular'),
    path('calcular_volumen/', views.calcular_volumen, name='calcular_volumen'),
]
