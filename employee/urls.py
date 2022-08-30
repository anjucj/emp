from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowAllProducts, name='showProducts'),
   
   
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('show/', views.show, name='show'),
    path('edit/<int:id>', views.edit,name='edit'),

    path('delete/<int:id>', views.destroy),

    path('Student/', views.addStudent, name='Student'),
    path('studentshow/', views.studentshow, name='studentshow'),

    
]