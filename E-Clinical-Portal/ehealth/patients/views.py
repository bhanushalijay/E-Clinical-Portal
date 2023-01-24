from django.shortcuts import redirect, render
from .models import Patients
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from doctor.models import Doctor
# Create your views here.
def index(request):
    return render(request, 'patients/index.html')
def signup(request):
    return render(request, 'patients/signup.html')
def portal(request):
    return render(request,'patients/portal.html')
def back(request):
    return render(request,'patients/index.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        lastname = request.POST['lastname']
        password1 = request.POST['psw']
        password2 = request.POST['confirm_password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:

                user = User.objects.create_user(username=username, last_name=lastname, first_name=first_name,
                                                password=password1, email=email)
                user.save()
                messages.info(request, "You have sucessfully registered yourself! Please login here.")
                return redirect('back')

        else:
            messages.info(request, 'Password not Matching')
            return redirect('register')
    else:
        return render(request, 'patients/signup.html')
def check(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # print(user)
        try:
            pat=Patients.objects.get(uname=username)
        except:
            pat=None

        if user is not None:
            #print(user.doctor.speciality)
            messages.info(request, 'Hi ' + user.first_name + ' you have sucessfully Logged in ',
                          extra_tags='login_error')

            return render(request,'patients/portal.html',{'patient':pat})

        else:
            print('login error')
            # u = User.objects.get(username=username)
            # print(u.password)
            messages.info(request, 'Invalid credentials! Please try again', extra_tags='login_error')

            return redirect('back')
    else:
        return render(request, 'patients/index.html')
def savedata(request):
    if request.method=="GET":
        return render(request,'patients/portal.html')
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
        messages.info(request, 'Hi ' + fname + ' you have sucessfully saved your details ',
                      extra_tags='Changes are not saved yet')
        return render(request,'patients/portal.html')
def loginn(request):
    return render(request, 'patients/index.html')


def home(request):
    return redirect('/')
def bookappointment(request):
    doctors=Doctor.objects.filter(isfree="True")
    return render(request,'patients/appointment.html',{'doctors':doctors})
def bookin(request):
    if request.method=="POST":
        date=request.POST['pickup_date']
        doctor=request.POST['choice']
        name=request.POST['name']
        u = User.objects.get(first_name=doctor)
        u.doctor.isfree="You have an appointment with "+name+ " on "+date
        u.save()
        u.doctor.save()
        messages.info(request, 'Hi your appointment have been successfully made on '+date+' with Dr. '+doctor,
                      extra_tags='Changes are not saved yet')
        return render(request,'patients/portal.html')

    else:
        return render(request,'patients/appointment.html')
