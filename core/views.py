from django.shortcuts import render

from django.views.generic import TemplateView

from .forms import ContatoForms


def contato(request):
    form = ContatoForms()

    context = {
        'form': form
    }

    return render(request, 'contato.html', context)


class HomeView(TemplateView):
    template_name = 'home.html'
