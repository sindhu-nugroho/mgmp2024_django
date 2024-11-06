from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import StudentRecord
from .forms import StudentRecordForm

class StudentRecordListView(ListView):
    model = StudentRecord
    template_name = 'myapp/student_list.html'

class StudentRecordCreateView(CreateView):
    model = StudentRecord
    form_class = StudentRecordForm
    template_name = 'myapp/student_form.html'
    success_url = '/'

class StudentRecordUpdateView(UpdateView):
    model = StudentRecord
    form_class = StudentRecordForm
    template_name = 'myapp/student_form.html'
    success_url = '/'

class StudentRecordDeleteView(DeleteView):
    model = StudentRecord
    template_name = 'myapp/student_confirm_delete.html'
    success_url = '/'
