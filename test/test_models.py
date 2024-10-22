import pytest
from django.contrib.auth import get_user_model
from authentapp.models import Employee, Company, Degree, EmployeeDegree

User = get_user_model()

@pytest.mark.django_db
def test_create_custom_user():
    user = User.objects.create_user(username="testuser", password="password123", phone="123456789", country_code="1")
    assert user.username == "testuser"
    assert user.phone == "123456789"
    assert user.country_code == "1"
    assert user.is_employee is False
    assert user.is_company is False

@pytest.mark.django_db
def test_create_employee():
    user = User.objects.create_user(username="employeeuser", password="password123")
    employee = Employee.objects.create(user=user, doc="123456")
    assert employee.user == user
    assert employee.doc == "123456"

@pytest.mark.django_db
def test_unique_employee_doc():
    user1 = User.objects.create_user(username="emp1", password="password123")
    user2 = User.objects.create_user(username="emp2", password="password123")
    Employee.objects.create(user=user1, doc="123456")
    
    with pytest.raises(Exception):
        Employee.objects.create(user=user2, doc="123456")

@pytest.mark.django_db
def test_create_company():
    user = User.objects.create_user(username="companyuser", password="password123")
    company = Company.objects.create(user=user, nit="123456789")
    assert company.user == user
    assert company.nit == "123456789"

@pytest.mark.django_db
def test_create_employee_degree():
    user = User.objects.create_user(username="degreeuser", password="password123")
    employee = Employee.objects.create(user=user, doc="654321")
    degree = Degree.objects.create(name="Engineering")
    employee_degree = EmployeeDegree.objects.create(employee=employee, degree=degree)
    
    assert employee_degree.employee == employee
    assert employee_degree.degree == degree

@pytest.mark.django_db
def test_str_methods():
    user = User.objects.create_user(username="strtestuser", password="password123")
    employee = Employee.objects.create(user=user, doc="654321")
    company = Company.objects.create(user=user, nit="123456789")
    degree = Degree.objects.create(name="Engineering")
    
    assert str(employee) == str(user)
    assert str(company) == str(user)
    assert str(degree) == "Engineering"
