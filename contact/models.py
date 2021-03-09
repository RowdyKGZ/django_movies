from django.db import models


class Contact(models.Model):
    """Модели для контактов рассылки по email"""
    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
