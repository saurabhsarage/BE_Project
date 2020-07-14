from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from . import databaseFile
from . import Models
def index(request):
    return render(request, 'index.html')


def welcome(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        passw = request.POST.get('password')
        password = databaseFile.logs(user)
        if password == passw:
            para = {'user' : user} #, 'welcome': "Welcomme"}
            request.session['user'] = user
            #print("Session Set")
            return render(request, 'in1.html', para)
        else:
            para = {'user' : 'User Not '}#, 'welcome' : 'Found'}
            return render(request, 'index.html', {'MSG' : "Invalid Username Or Password"})
    return render(request, "index.html", {'MSG' : "LOGIN FIRST"})

def check_sess(request):
    if request.session.has_key('user'):
        usname = request.session['user']
        ele = request.POST.get("display")
        print(ele)
        #Models.cause(ele)
        disease = ['allergy', 'Cancer']
        sel = {"Symptoms": ele, "Disease" : disease}
        return render(request, "new.html", sel)
    else:
        return render(request, "index.html", {'MSG' : "LOGIN FIRST"})



def log_out(request):
    try:
        del request.session['user']
    except:
        pass
    return render(request, "Index.html")

def newuser(request):

    return render(request, 'newuser.html')
def register(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    bd = request.POST.get('bdate')
    gen = request.POST.get('gender')
    username = request.POST.get('username')
    password = request.POST.get('pass')
    conpass = request.POST.get('confpass')
    count = databaseFile.check_user_name(username)
    if count == 0:
        if(password == conpass):
            fn,suc = databaseFile.insert1(fname,lname,bd,gen,username,password)
            print("Inserted")
            para = {'fname': fn, 'Sucess': suc}
            return render(request,'sucessful.html', para)
        else:
            para = {'pas': "Password Doesn't Match"}
            return render(request,'newuser.html', para)
    else:
        para = {'pas': "Username Not Available"}
        return render(request, 'newuser.html', para)
