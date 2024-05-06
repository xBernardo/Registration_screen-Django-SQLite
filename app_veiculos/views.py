from django.shortcuts import render
from .models import Veiculo

# Create your views here.

def home(request):
    return render(request, 'veiculos/home.html')

def veiculos(request):
    # Salvar os dados da tela para o banco de dados.
    novo_veiculo = Veiculo()
    novo_veiculo.nome = request.POST.get('nome')
    novo_veiculo.marca = request.POST.get('marca')
    novo_veiculo.valor = request.POST.get('valor')
    novo_veiculo.save() # Salvar todos os POST dessa lista
    # Exibir todos veiculos em uam nova página
    veiculos = {
        'veiculos': Veiculo.objects.all()
    }


    # Retornar dados para pagina de listagem
    return render(request, 'veiculos/veiculos.html', veiculos)
