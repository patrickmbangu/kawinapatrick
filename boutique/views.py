from django.shortcuts import render
from django.shortcuts import render, redirect, get_list_or_404
from .models import Etudiant
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import reverse
from .forms import StudentForm
from django.template.loader import get_template

import io
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    student_object = Etudiant.objects.all()
    item = request.GET.get('item')
    if item !='' and item is not None:
        student_object = Etudiant.objects.filter(nom__icontains=item)
    return render(request, 'students/index.html', { 'students': student_object })



def view_student(request, id):
    student = Etudiant.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['matricule']
            new_first_name = form.cleaned_data['nom']
            new_last_name = form.cleaned_data['post_nom']
            new_prenom = form.cleaned_data['prenom']
            new_email = form.cleaned_data['email']
            new_age = form.cleaned_data['age']
            new_promotion = form.cleaned_data['field_of_study']

            new_student = Etudiant(
                matricule = new_student_number,
                nom = new_first_name,
                post_nom = new_last_name,
                prenom = new_prenom,
                email = new_email,
                age = new_age,
                promotion = new_promotion
           )
            new_student.save()
            return render(request, 'students/add.html', 
                          {'form': StudentForm(), 'success': True})
        
        
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': StudentForm()})

def edit(request, id):
    if request.method == 'POST':
        student = Etudiant.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {'form': form, 'success': True})
        
    else:
        student = Etudiant.objects.get(pk=id)
        form = StudentForm(instance=student)

    return render(request, 'students/edit.html', {'form': form})

def delete(request, id):
    if request.method == 'POST':
        student = Etudiant.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))


def SignupPage(request):
    if request.method == 'POST':
        nam = request.POST.get('nom')
        emai = request.POST.get('email')
        passw = request.POST.get('password')
        passw2 = request.POST.get('password2')

        if passw!=passw2:
            return HttpResponse("Les deux mots de passe ne sont pas conformes!!")
        else:
            my_user=User.objects.create_user(nam,emai,passw)
            my_user.save()
            return redirect('login')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index/')
        else:
            return HttpResponse("Nom utilisateur ou mot de passe incorrect!!!")

    return render(request, 'students/login.html')




    


