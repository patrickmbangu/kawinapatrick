from django.db import models

# Create your models here.
class Etudiant(models.Model):
    matricule = models.PositiveBigIntegerField()
    nom = models.CharField(max_length=50)
    post_nom = models.CharField(max_length=50)
    prenom= models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    promotion = models.CharField(max_length=50)
    

    def __str__(self):
        return f'Student: {self.nom} {self.post_nom}'
