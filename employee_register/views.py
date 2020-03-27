from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def emplyee_list(request):
    # cara pertama
    # employees = Employee.objects
    context = {'employee_list': Employee.objects.all()}
    # cara pertama
    # return render(request, 'employee_register/employee_list.html',{ 'employees' : employees})
    return render(request, 'employee_register/employee_list.html', context)
    # Create your views here.


def emplyee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
    # Create your views here.


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
