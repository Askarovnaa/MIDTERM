from django.shortcuts import render

# Create your views here.

from .models import Employee, Department, Location

def index(request):
    """
    ������� ����������� ��� �������� �������� �����.
    """
    # ��������� "���������" ��������� ������� ��������
    num_employees=Employee.objects.all().count()
    num_locations=Location.objects.all().count()
    num_departments=Department.objects.count()
    # ����� 'all()' �������� �� ���������.
    #  ��������� HTML-������� index.html � ������� ������
    #  ���������� ��������� context
    return render(
        request,
        'index.html',
        context={'num_employees':num_employees,'num_locations':num_locations,'num_departments':num_departments},
    )

from django.views import generic

class EmployeeListView(generic.ListView):
    model = Employee

class EmployeeDetailView(generic.DetailView):
    model = Employee