from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=150)
    message = models.TextField('Mensagem')

    send = models.DateTimeField('Enviado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.name