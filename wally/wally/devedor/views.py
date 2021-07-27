from os import name
from django.shortcuts import render
from devedor.models import Devedor


def lista_devedores(request):
    devedor = Devedor.objects.all()
    dados= {'devedor':devedor}
    return render(request, 'devedor.html',dados)
