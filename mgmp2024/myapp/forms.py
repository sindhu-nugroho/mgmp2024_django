from django import forms
from .models import StudentRecord

class StudentRecordForm(forms.ModelForm):
    class Meta:
        model = StudentRecord
        fields = ['name', 'school', 'position', 'description', 'image']
