from django.db import models

class TextureType(models.Model):
    name = models.CharField('Nome da Texture', max_length=100, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'Textura'    
        verbose_name_plural = 'Texturas'
        ordering = ['name']

    def __str__(self):
        return self.name    