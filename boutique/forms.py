from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['matricule', 'nom', 'post_nom', 'prenom', 'email', 'age', 'promotion']
        
        labels = {
            'matricule': 'matricule',
            'nom': 'nom',
            'post_nom': 'post_nom',
            'prenom': 'prenom',
            'email': 'email',
            'age': 'age',
            'promotion': 'promotion'
        }

        widgets = {
            'matricule': forms.NumberInput(attrs={'class':'form-control'}),
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'post_nom': forms.TextInput(attrs={'class':'form-control'}),
            'prenom': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'promotion': forms.TextInput(attrs={'class':'form-control'}),

        }


class EtudiantFormm(forms.Form):
    class Meta:
        model = Etudiant

        fields = '__all__'