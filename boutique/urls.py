from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.LoginPage, name='login'),
    path('signup/', views.SignupPage, name='signup'),
    path('index/', views.index, name='index'),
    path('<int:id>', views.view_student, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),


]