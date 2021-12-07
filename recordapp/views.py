from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request, 'index.html')


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html')


def registration(request):
    error = None
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        empcode = request.POST['empcode']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(
                first_name=fn, last_name=ln, username=email, password=password)
            EmployeeDetail.objects.create(user=user, empcode=empcode)
            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)
            error = "no"

        except:
            error = "yes"

    return render(request, 'registration.html', locals())


def emp_login(request):
    error = None

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"

    return render(request, 'login.html', locals())


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = None
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)

    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        empcode = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        joindate = request.POST['joindate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = empcode
        employee.dept = dept
        employee.designation = designation
        employee.contact = contact
        employee.joindate = joindate
        employee.gender = gender

        if joindate:
            employee.joindate = joindate

        try:
            employee.save()
            employee.user.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'profile.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')


def admin_login(request):
    error = None

    user = request.user

    if not user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            try:
                if user.is_staff:
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        return render(request, 'admin_login.html', locals())
    else:
        return redirect('admin_home')


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def myexperience(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    return render(request, 'myexperience.html', locals())


def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = None
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    if request.method == "POST":
        company1name = request.POST['company1name']
        company1designation = request.POST['company1designation']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2designation = request.POST['company2designation']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3designation = request.POST['company3designation']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        print("1...", company1name)
        experience.company1name = company1name
        experience.company1designation = company1designation
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        print("2...", company2name)
        experience.company2name = company2name
        experience.company2designation = company2designation
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        print("3...", company3name)
        experience.company3name = company3name
        experience.company3designation = company3designation
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'edit_myexperience.html', locals())


def my_education(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user = request.user
    education = EmployeeEducation.objects.get(user=user)
    return render(request, 'my_education.html', locals())


def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = None
    user = request.user
    education = EmployeeEducation.objects.get(user=user)

    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagepggra = request.POST['percentagepggra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagepgssc = request.POST['percentagepgssc']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagepggra = percentagepggra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagepgssc = percentagepgssc

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        try:
            education.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'edit_myeducation.html', locals())


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = None
    user = request.user

    if request.method == 'POST':
        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']
        try:
            if user.check_password(currentpassword):
                user.set_password(newpassword)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'change_password.html', locals())


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = None
    user = request.user

    if request.method == 'POST':
        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']
        try:
            if user.check_password(currentpassword):
                user.set_password(newpassword)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, 'change_passwordadmin.html', locals())


def all_employees(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    employee = EmployeeDetail.objects.all()

    return render(request, 'all_employees.html', locals())


def delete_employee(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    user = User.objects.get(id=id)
    user.delete()
    return redirect('all_employees')


def edit_profile(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = None

    employee = EmployeeDetail.objects.get(id=id)

    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        empcode = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        joindate = request.POST['joindate']
        gender = request.POST['gender']

        if joindate:
            employee.joindate = joindate
        else:
            joindate = None

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = empcode
        employee.dept = dept
        employee.designation = designation
        employee.contact = contact
        employee.joindate = joindate
        employee.gender = gender

        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'profile.html', locals())


def edit_education(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    error = None
    user_id = User.objects.get(id=id)
    education = EmployeeEducation.objects.get(user=user_id)

    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']

        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassinggra = request.POST['yearofpassinggra']
        percentagepggra = request.POST['percentagepggra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagepgssc = request.POST['percentagepgssc']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg

        education.coursegra = coursegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagepggra = percentagepggra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagepgssc = percentagepgssc

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc

        try:
            education.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'edit_education.html', locals())



def edit_experience(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    error = None
    user = User.objects.get(id=id)
    experience = EmployeeExperience.objects.get(user=user)

    if request.method == "POST":
        company1name = request.POST['company1name']
        company1designation = request.POST['company1designation']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']

        company2name = request.POST['company2name']
        company2designation = request.POST['company2designation']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']

        company3name = request.POST['company3name']
        company3designation = request.POST['company3designation']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        print("1...", company1name)
        experience.company1name = company1name
        experience.company1designation = company1designation
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        print("2...", company2name)
        experience.company2name = company2name
        experience.company2designation = company2designation
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        print("3...", company3name)
        experience.company3name = company3name
        experience.company3designation = company3designation
        experience.company3salary = company3salary
        experience.company3duration = company3duration

        try:
            experience.save()
            error = "no"

        except:
            error = "yes"

    return render(request, 'edit_experience.html', locals())