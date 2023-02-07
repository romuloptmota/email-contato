from django.shortcuts import render

from django.views.generic import TemplateView


def contato(request):
    return render(request, 'contato.html')


class HomeView(TemplateView):
    template_name = 'home.html'
