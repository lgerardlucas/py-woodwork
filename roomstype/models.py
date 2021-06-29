from django.db import models

class RoomsType(models.Model):
    name = models.CharField('Nome do Ambiente', max_length=100, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'Ambiente'    
        verbose_name_plural = 'Ambientes'
        ordering = ['name']

    def __str__(self):
        return self.name    