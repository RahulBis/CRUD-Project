from django.shortcuts import render,HttpResponseRedirect
from .forms import stu_signup
from .models import Signup
# Create your views here.
#Details
def stu_details(request):
    stud = Signup.objects.all()
    return render(request,'enroll/details.html',{'stu':stud})
#Signup
def Signup_det(request):
    if request.method == 'POST':
        fm=stu_signup(request.POST)
        if fm.is_valid():
            fm.save()
            fm=stu_signup()
            return HttpResponseRedirect('/success/')         
    else:
        fm=stu_signup()
        
    return render(request,'enroll/index.html',{'form':fm})

#Update
def update_data(request,id):
    if request.method == 'POST':
        p_id=Signup.objects.get(pk=id)
        fm=stu_signup(request.POST, instance=p_id)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/success/')

    else:
        p_id=Signup.objects.get(pk=id)
        fm=stu_signup(instance=p_id)
    return render(request,'enroll/updatestu.html',{'form':fm})

#Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = Signup.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/success/')