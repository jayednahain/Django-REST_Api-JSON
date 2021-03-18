
from django.urls import path
from rest_api import views

urlpatterns = [
    path('emp_data/',views.employeeView)
]
