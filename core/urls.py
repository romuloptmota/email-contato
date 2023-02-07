from django.urls import path

from .views import HomeView, contato

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contato', contato, name='contato')
]
