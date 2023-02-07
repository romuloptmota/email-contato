from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForms

from django.views.generic import TemplateView


def contato(request):
    form = ContatoForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso')
            form = ContatoForms()  # limpar formulario
        else:
            messages.error(request, 'Erro ao enviar email')

    context = {
        'form': form
    }

    return render(request, 'contato.html', context)


class HomeView(TemplateView):
    template_name = 'home.html'
