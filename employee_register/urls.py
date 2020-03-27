from django.urls import path, include
from . import views

urlpatterns = [
    # localhost:8000/employee
    path('', views.emplyee_form, name='employee_insert'),
    path('<int:id>/', views.emplyee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('list/', views.emplyee_list, name='employee_list')
]
