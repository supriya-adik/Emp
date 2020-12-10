from django.shortcuts import render, get_object_or_404
from crudApp.forms import EmpForm
from crudApp.models import Emp
# Create your views here.

def show_view(request) :
    employee=Emp.objects.all()
    return render(request,'display.html',{'employee':employee})
def create_view(request) :
    form=EmpForm()
    if request.method=='POST' :
        form=EmpForm(request.POST)
        if form.is_valid() :
            form.save()
        return show_view(request)
    return  render(request,'insert.html',{'form':form})

def delete_view(request,id) :
  employee=Emp.objects.get(id=id)
  employee.delete()
  return show_view(request)

def update_view(request,id) :
   employee=get_object_or_404(Emp,id=id)
   form=EmpForm(request.POST or None,instance=employee)
   if form.is_valid():
           form.save()
           return show_view(request)
   return render(request,'update.html',{'employee':employee})