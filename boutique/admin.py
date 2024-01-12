from django.contrib import admin
from .models import Etudiant

# Register your models here.
class AdminEtudiant(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'post_nom', 'prenom', 'email', 'age', 'promotion')

admin.site.register(Etudiant, AdminEtudiant)