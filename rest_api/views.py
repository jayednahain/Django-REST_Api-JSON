from django.http import JsonResponse
from django.shortcuts import render
from rest_api.models import Employee

# Create your views here.


#creating a function based view !
def employeeView(request):
   #creating a static employee object ! which return back as jason !

   #testing data !
   emp_data = {
      'id':'1234',
      'name':'nahian',
      'salrey':200
   }
   data = Employee.objects.all()

   response = {
      'employees':list(data.values('id','name','salrey')) #defining database field we want to show !
   }


   return JsonResponse(response) #dictionary serialize as json format !

