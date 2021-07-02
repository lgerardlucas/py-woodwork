from django.db import models

class Furniture(models.Model):
    name = models.CharField('Nome do Móvel', max_length=100, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'Móvel'    
        verbose_name_plural = 'Móveis'
        ordering = ['name']

    def __str__(self):
        return self.name    