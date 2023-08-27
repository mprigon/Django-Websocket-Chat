from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Letter(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', verbose_name='Пользователь')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    dateCreation = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('letter_id', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Letter from {self.sender.username} for {self.recipient.username} : {self.text[:128]}'
