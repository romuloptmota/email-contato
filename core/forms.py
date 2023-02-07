from django import forms
from django.core.mail import EmailMessage


class ContatoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):  # lendo o conteudo digitado
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        # formatando como sera exibido
        conteudo = f'Nome: {nome}\nE-mail: {email}\n Assunto: {assunto}\nMensagem: {mensagem}'

        # para onde seta sendo enviado
        mail = EmailMessage(
            subject='E-mail enviado por qua Sitema?',  # assunto
            body=conteudo,
            from_email='quem_esta_enviando@seudominio.com.br',
            to=['quem_recebe_email@seudominio.com.br'],
            headers={'Reply-to': email}  # se alguem for responder, para quem ira responder
        )
        mail.send()
