from django import forms

from . models import Employee,Student



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['eid', 'ename', 'email', 'econtact', 'ecompany']
        widgets = {
        'eid': forms.TextInput(attrs={'class': 'form-control'}),
        'ename': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'econtact': forms.TextInput(attrs={'class': 'form-control'}),
        'ecompany': forms.TextInput(attrs={'class': 'form-control'}),
        
        
        

        }
        labels = {
            'eid' : 'Enter Employee code:',
            'ename': 'Name: ',
            'email': 'Email',
            'econtact':'Contact',
            'ecompany': 'Company Name: ',
            
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['sname', 'sreg', 'smark']
        widgets = {
        
        'sname': forms.TextInput(attrs={'class': 'form-control'}),
        'sreg': forms.TextInput(attrs={'class': 'form-control'}),
        'smark': forms.TextInput(attrs={'class': 'form-control'}),
         

        }
        labels = {
            'sname' : 'Enter Name:',
            'sreg': 'Enter RegisterNo: ',
            
            'smark': 'Enter Mark: ',
            
        }
