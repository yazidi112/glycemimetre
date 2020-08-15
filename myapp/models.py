from django.db import models
from django.utils import timezone

class Article(models.Model):
    valeur = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date ")
    
    class Meta:
        verbose_name = "valeur"
        
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.valeur