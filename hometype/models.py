from django.db import models

class HomeType(models.Model):
    name = models.CharField('Nome do Imóvel', max_length=100, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'Imóvel'    
        verbose_name_plural = 'Imóveis'
        ordering = ['name']

    def __str__(self):
        return self.name    