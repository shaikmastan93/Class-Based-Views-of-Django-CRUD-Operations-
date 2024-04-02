# views.py

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee


class EmployeeListView(ListView):
    model = Employee
    context_object_name= 'employees'
    template_name = 'employee_list.html'

class EmployeeDetailView(DetailView):
    model= Employee
    template_name= 'employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    template_name= 'employee_form.html'
    success_url= reverse_lazy('employee_list')
    fields = ['name', 'position', 'department']

class EmployeeUpdateView(UpdateView):
    model=Employee
    template_name='employee_form.html'
    success_url=reverse_lazy('employee_list')
    fields= ['name', 'position', 'department']

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')


    
 





