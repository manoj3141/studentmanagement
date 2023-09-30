from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import User_reg,Student_reg,user_login
from .models import Student
from django.db.models import Q
from django.contrib.auth import login,authenticate,logout
from datetime import datetime,date
# Create your views here.
def home(request):
    if request.method=="POST":
        pu=Student_reg(request.POST)
        if pu.is_valid():
            pu.save()
            pu=Student_reg()    
    else:
          pu=Student_reg()      
    return render(request,'home.html',{"pu":pu})

def table(request):
    d=Student.objects.all()
    return render(request,'table.html',{"d":d})

def update(request,id):
    if request.method=='POST':
        d=Student.objects.get(pk=id)
        pu=Student_reg(request.POST,instance=d)
        if pu.is_valid:
          pu.save()
          return HttpResponseRedirect('/')
    else:   
     d=Student.objects.get(pk=id)
     #print(d)
     pu=Student_reg(instance=d)
    return render (request,'update.html',{'pu':pu})    

def delete(request,id):
    if request.method=="POST" :
      d=Student.objects.get(pk=id)
      d.delete()
      return HttpResponseRedirect('/view')
def show(request):
    if request.method=='POST':
        s=request.POST.get("search")
        if s!=None:
            d=Student.objects.filter(Q(fname__icontains=s)|Q(lname__icontains=s)|Q(email__icontains=s)|Q(subject__icontains=s))  
            return render (request,'table.html',{'d':d})      
        
        
def reg(request):
    if request.method=='POST':
        f=User_reg(request.POST)
        print('yes')
        if f.is_valid():
            k=f.save()
            login(request,k)
            return redirect('home')
        else:
            ur=User_reg()
            return render(request,'reg.html',{'ur':ur})
    else:        
        ur=User_reg()
        
        return render(request,'reg.html',{'ur':ur})        
    
def user_log(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=user_login(request,data=request.POST) 
            if form.is_valid():
                n=form.cleaned_data['username']
                p=form.cleaned_data['password']
                user=authenticate(username=n,password=p)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
            else:
                form=user_login()    
                return render(request,'login.html',{'f':form})
        else:
            form=user_login()    
        return render(request,'login.html',{'f':form}) 
    else:
        return HttpResponseRedirect("/")    
     
     
def user_logout(request):
         logout(request)
         return HttpResponseRedirect('/login')  
     
def showDate(request):

     e = datetime.now()
     '''print ("Current date and time = %s" % e)
     print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
     print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))'''
     return render (request,'time.html',{'e':e})    
 
def wish(request):
    e = datetime.now()
    t=int(e.hour)
    if t<12:
        w='Good Morning'
    else:
        w='Good Evening'    
    return render (request,'time.html',{'e':e,'w':w})    
def showstd(request):
    data={"l1":{'name':'manoj','age':22,'subject':'ece'},"l2":{'name':'manoj','age':22,'subject':'ece'}}
    return render (request,'time.html',{'data':data}) 