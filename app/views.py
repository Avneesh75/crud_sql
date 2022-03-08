from django.shortcuts import render,redirect,HttpResponse
from .models import *
# Create your views here.
        
def Insert(request):
    #return HttpResponse("hello world")
   return render(request,'insert.html')

def InsertData(request):
    #Data come from HTML to view
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    #creating object of model class
    #insert Data into Table
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)

    #after insert render on show page
    return redirect('showdata')

#show page view
def Show(request):
    # select * from tablename
    # for fetching all the data of the table
    all_data = Student.objects.all()
    return render(request,"show.html",{'key1':all_data})

#edit page view
def Edit(request,pk):
    get_data= Student.objects.get(id=pk)
    return render(request,"edit.html",{'key2':get_data})

#Update Data View
def Update(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    #Query for Update
    udata.save()

    return redirect('showdata')

# Delete View
def Delete(request,pk):
    ddata= Student.objects.get(id=pk)
    # query for delete
    ddata.delete()
    return redirect('showdata')