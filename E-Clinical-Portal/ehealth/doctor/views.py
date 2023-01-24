from django.shortcuts import render,redirect
from .models import Doctor
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User, auth
from .models import Doctor
from django.contrib import messages
from patients.models import Patients


#from django.db.models.loading import get_model
from django.core.mail import send_mail,BadHeaderError
def index(request):

    return render(request, 'doctor/index.html')

def check(request):
    if request.method == 'GET':
        return render(request, 'doctor/index.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)
        #print(user)
        if user is not None:
            #print(user.doctor.speciality)
            a=user.doctor.isfree
            if a=="True":
                a="You dont have any appointment scheduled yet"
            messages.info(request, 'Hi Dr. ' + user.first_name + ' you have sucessfully Logged in ', extra_tags='login_error')
            return render(request,'doctor/portal.html',{'text':a})
        else:
            print('login error')
            # u = User.objects.get(username=username)
            # print(u.password)
            messages.info(request, 'Invalid credentials! Please try again', extra_tags='login_error')

            return render(request,'doctor/index.html')

def signup(request):
    return render(request, 'doctor/signup.html')
def back(request):
    return render(request,'doctor/index.html')
def portal(request):
    print("Hello World")
    return render(request,'doctor/portal.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        lastname = request.POST['lastname']
        agee=request.POST['age']
        password1 = request.POST['psw']
        password2 = request.POST['confirm_password']
        speciality=request.POST['choice']
        try:
            u = User.objects.get(username=username)
        except:
            u = None

        #freds_department = u.employee.department
        if password1 == password2:
            if u!=None:
                messages.info(request, 'Username Taken')
                print("user none")
                return redirect('register')
            elif u != None and u.doctor.email==email:
                messages.info(request, 'Email Taken')
                print("Email Taken")
                return redirect('register')
            else:
                print("done")
                user = User.objects.create_user(username=username, last_name=lastname, first_name=first_name,
                                                password=password1, email=email)
                user.save()
                Doctor.objects.create(user=user, age=agee, speciality=speciality)

                messages.info(request, "You have sucessfully registered yourself")
                return render(request,'doctor/index.html')

        else:
            messages.info(request, 'Password not Matching')
            return redirect('register')




    else:

        return render(request, 'doctor/signup.html')
def home(request):
    return redirect('/')
def patientcheck(request):
    if request.method=="GET":
        return render(request,'doctor/portal.html')
    else:
        fname=request.POST['firstname']
        date=request.POST['date']


        #print(fname,date)

        try:
            pat = Patients.objects.get(fname=fname,date=date)
        except:
            pat = None
        print(pat)
        if pat==None:
            messages.info(request, "This user has not filled the details properly or Invalid credentials.")
            return render(request,'doctor/portal.html')

        else:
            messages.info(request, "The below are the details of the patient "+pat.fname)
            bd=pat.bloodreport,print(pat.bloodreport=="")
            hr=pat.healthreport
            orr=pat.otherreport
            if bd=="":
                if hr=="":
                    if orr=="":
                        return render(request, 'doctor/patientsinfo.html', {'patient': pat})
                    else:
                        return render(request, 'doctor/patientsinfo.html', {'patient': pat,'orr':orr})
                else:
                    if orr=="":
                        return render(request, 'doctor/patientsinfo.html', {'patient': pat,'hr':hr})
                    else:
                        return render(request, 'doctor/patientsinfo.html', {'patient': pat,'orr':orr,'hr':hr})
            else:
                if hr=="":
                    if orr=="":
                        return render(request, 'doctor/patientsinfo.html', {'patient': pat,'bd':bd})
                    else:
                        return render(request, 'doctor/patientsinfo.html', {'patient': pat,'orr':orr,'bd':bd})
                else:
                    if orr=="":
                        return render(request, 'doctor/patientsinfo.html', {'patient': pat,'hr':hr,'bd':bd})
                    else:
                        return render(request, 'doctor/patientsinfo.html', {'patient': pat,'orr':orr,'hr':hr,'bd':bd})





def savedata(request):
    if request.method=="GET":
        return render(request,'Doctor/patientsinfo.html')
    else:
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        uname=request.POST['username']
        email=request.POST['email']
        date=request.POST['date']
        number=request.POST['number']
        city=request.POST['city']
        state=request.POST['state']
        symptoms=request.POST['symptoms']
        problem=request.POST['w3review']
        try:
            bloodreport=request.FILES['bloodreport']
        except:
            bloodreport=None
        try:
            healthreport=request.FILES['healthreport']
        except:
            healthreport=None
        try:
            otherreport=request.FILES['otherreport']
        except:
            otherreport=None
        try:
            pat = Patients.objects.get(uname=uname)
        except:
            pat = None
        if pat==None:
            #print("hellow")
            Patients.objects.create(uname=uname,fname=fname,lname=lname,email=email,date=date,phone=number,city=city,state=state,symptoms=symptoms,problem_in_breif=problem,
                                    bloodreport=bloodreport,healthreport=healthreport,otherreport=otherreport)
        else:
            #print("world")
            pat.fname=fname
            pat.lname=lname
            pat.uname=uname
            pat.email=email
            pat.phone=number
            pat.date=date
            pat.city=city
            pat.state=state
            pat.symptoms=symptoms
            pat.problem_in_breif=problem
            #print(bloodreport)
            if bloodreport!=None:
                pat.bloodreport=bloodreport
            if healthreport!=None:
                pat.healthreport=healthreport
            if otherreport!=None:
                pat.otherreport=otherreport
            pat.save()
        messages.info(request, 'Hi Doctor you have sucessfully made the changes of your patient '+uname,
                      extra_tags='Changes are not saved yet')
        return render(request,'doctor/patientsinfo.html',{'patient':pat})
def loginn(request):
    return render(request,'doctor/index.html')






