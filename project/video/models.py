from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=120)
    docfile = models.FileField(null = True, blank=True)

    def __str__(self):
        return self.title
    
