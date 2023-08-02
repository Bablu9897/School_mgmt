from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from .models import *
# Create your views here.

@login_required
def home(request):
  return render(request, "home.html")

def regi_form(request):
  context = {
    'forms':CreateStudent(),
  }
  return render(request, 'students/registration.html', context)

def StudentEdit(request,pk=None):
  sid = StudentInfo.objects.get(id=pk)
  edit_forms = CreateStudent(instance=sid)
  return render(request, 'students/edit_student.html',{'edit_forms':edit_forms,'id':sid.id})
  

class StudentOp(APIView):
  def post(self,request):
    print(request.data)
    creat_s = StudentInfoSerializer(data = request.data)
    
    if creat_s.is_valid():
      creat_s.save()
      messages.success(request,"submitted succefully")
      return redirect('student_regi')
    else:
      return Response(creat_s.errors)
  def get(self, request):
    context = {}
    context['students'] = StudentInfo.objects.all()
    return render(request,"students/student_list.html", context)
  
class StudentDetails(APIView):
  def get(self, request, pk):
    context = {}
    try:
      context['single_student'] = StudentInfo.objects.get(id=pk)
    except StudentInfo.DoesNotExist:
      messages.warning("student not fount")
      return render(request,"students/student_list.html")
    return render(request, 'students/student_details.html', context)
  
  def patch(self, request, pk):
    messages.success(request, "update successfully")
    return render(request, 'students/edit_student.html')
  def delete(self, request, pk):
    sid = StudentInfo.objects.get(id=pk)
    sid.delete()
    messages.success(request, "delete success")
    return render(request,"students/student_list.html")
    
  
    
    
    
    
 