from django.shortcuts import render
from django.http import HttpResponse
from.models import Student
# Create your views here.

def view_details(request):
   
   obj=Student.objects.all()
   return render(request,'view_data.html',{'x':obj})


def student(request):
   if request.method == 'POST':
     obj=Student()
     obj.Name=request.POST.get('name')
     obj.Couse=request.POST.get('course')
     obj.Gender=request.POST.get('gender')
     obj.Dob=request.POST.get('dob')
     obj.Address=request.POST.get('address')
     obj.Image=request.POST.get('filename')
     obj.save()
     return view_details(request)
   return render(request,'student.html')

def delete_row(request,pk):
   obj=Student.objects.get(id=pk).delete()
   return view_details(request)

def update_row(request,pk):
   obj=Student.objects.get(id=pk)
   if request.method == 'POST':
     obj=Student.objects.get(id=pk)
     obj.Name=request.POST.get('name')
     obj.Couse=request.POST.get('course')
     obj.Gender=request.POST.get('gender')
     obj.Dob=request.POST.get('dob')
     obj.Address=request.POST.get('address')
     obj.Image=request.POST.get('filename')
     obj.save()
     return view_details(request)
   return render(request,'update_student.html',{'x':obj})

