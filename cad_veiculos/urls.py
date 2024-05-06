
from django.urls import path
from app_veiculos import views

urlpatterns = [
    # Rota, views responsável, nome de referencia
    # greenwheels.com
    path('',views.home,name='home'),

    # grewheels.com/veiculos
    path('veiculos', views.veiculos, name='listagem_veiculos')

]
