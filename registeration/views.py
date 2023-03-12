from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Person
from .forms import *
import pandas as pd
from django.core.mail import send_mail
from datetime import date
from django.conf import settings
from django.core.mail import send_mail

def valss(request):
    # result_list = list(Person.objects.all().values('name','dob', 'email', 'phone_no'))
    d = Person.objects.all()
    p = pd.DataFrame(d)
    columns = [{'field': f, 'title': f} for f in Person._Meta.fields]
    json = p.to_json(orient='records')
    context = {
            'data': json,
            'columns': columns
        }
    return render(request=request, template_name="registration/home.html", context=context)

def vals():
    qs = Person.objects.all().values('name','dob', 'email', 'phone_no')
    df = pd.DataFrame(qs)
    html= df.to_html()
    return html
    
def home(request):
    v = vals()
    # st = {'a': v}
    return HttpResponse(v)
    # return render(request=request, template_name="registration/home.html",content_type='html',context=st)

def registerForm(request):
    form = Mainform
    para = {
        'form':form
    }
    return render(request =request, template_name="registration/form.html",context=para)

def save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')

        year = str(dob).split('-')[0]
        to = str(date.today()).split('-')[0]
        
        if not int(to)-int(year) < 18:
            messages.error(request, "age should not be less than 18.")
            
        newuser = Person()
        newuser.name = name
        newuser.dob = dob
        newuser.email = email
        newuser.phone_no = phone_no
        newuser.save()
        
        
        subject = 'Company.XXXX'
        message = f'Hi {name}, thank you for registering.\n' + "click to add another response 'http://127.0.0.1:8000/userForm/'"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
        
        return home(request=request)
    