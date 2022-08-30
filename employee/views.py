
# Create your views here.
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.

from . models import Employee,Student
from . forms import EmployeeForm,StudentForm


@login_required(login_url='accounts/login')
def ShowAllProducts(request):
    
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = EmployeeForm()

    context = {
        "form":form
    }

    return render(request, 'showProducts.html', context)




@login_required(login_url='accounts/login')
def addEmployee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = EmployeeForm()

    context = {
        "form":form
    }

    return render(request, 'addEmployee.html', context)



def show(request):
    form=Employee.objects.all()
    print("hi",form)
    return render(request,'show.html',{'form':form})




def edit(request, id):
    fm=None
    # if request.method == 'POST':
    fm=Employee(request.POST or None)
    pi=Employee.objects.get(pk=id)
    fm=EmployeeForm(request.POST, instance=pi)  
    if fm.is_valid():
        fm.save()
        return redirect('show')
        return render(request, 'edit.html',{'forms':fm})
    else:
        pi=Employee.objects.get(pk=id)
        fm=EmployeeForm(instance=pi)
        return render(request, 'edit.html',{'forms':fm})




def destroy(request,id):
    employe=Employee.objects.get(id=id)
    employe.delete()
    return redirect('show')


@login_required(login_url='accounts/login')
def addStudent(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studentshow')
    else:
        form = StudentForm()

    context = {
        "form":form
    }

    return render(request, 'addStudent.html', context)

def studentshow(request):
    form=Student.objects.all()
    print("hi",form)
    return render(request,'studentshow.html',{'form':form})








