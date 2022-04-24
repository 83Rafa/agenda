from django.shortcuts import render
from core.models import Evento
# Create your views here.

def lista_eventos(request):
    evento = Evento.objects.all()#posso alterar p/ .alfilter(usuario=usuario) no lugar de .all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)