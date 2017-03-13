#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento
from django.shortcuts import render_to_response
from template import *
def home(request):
    listaEventos= Evento.objects.all()
    retorno = ''
    for evento in listaEventos:
        retorno+='<li>' + evento.nome + evento.local + evento.email + str(evento.qtdInscricoes) + '</li>'
    return HttpResponse(retorno)
def mostrarUrl(request, name):
	nome = name
	if nome.lower()=="ronicley":
		return HttpResponse('<center>'+'<h1>'+nome+' e um gostoso'+'</h1>'+'</center>')
	return HttpResponse("Nao é um gostoso")



def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('template/index.html', {'latest_poll_list': latest_poll_list})
