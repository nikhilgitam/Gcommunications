import pickle
from django.db import close_old_connections
from threading import Thread
import sweetify
from django.contrib import messages
from django.contrib.auth import logout, login,authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from email.message import EmailMessage
from email.mime.text import MIMEText
from mobile_app.models import PushNotification as PNotification
import base64

from rest_framework.views import APIView

from exponent_server_sdk import PushMessage, PushClient
from users.models import *
from app.models import *
from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response

import os

import sys
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
import os
import clr
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
abs_path = os.path.abspath(os.path.join(os.getcwd()))
abs_path = abs_path.replace('\\', '\\\\')
clr.AddReference(r"" + abs_path + "\\\\ClassLibrary1.dll")
from django.db import connections

from testDLLApp import Class1

SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
          'https://www.googleapis.com/auth/admin.directory.group.readonly',
          'https://www.googleapis.com/auth/admin.directory.group',
          'https://www.googleapis.com/auth/admin.directory.group.member',
          'https://www.googleapis.com/auth/gmail.modify',
          'https://www.googleapis.com/auth/gmail.compose',
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.metadata',
          'https://www.googleapis.com/auth/apps.groups.settings'

          ]


# Create your views here.
def logout2(request):
    logout(request)
    return redirect('https://login.gitam.edu/Login.aspx')


def login2(request):
    return render(request, 'login.html')


def dashboard(request):
    if request.session['gname'] == "ADMIN":
        return render(request, 'dashboard.html')
    if request.session['gname'] == "HOD":
        pass
    if request.session['gname'] == "DEAN":
        ddata = Dean.objects.filter(college=request.user.institution).values('stream')
        stream = ddata[0]['stream']
        inst = Dean.objects.filter(stream=stream).values_list('college', flat=True)
        inst = list(inst)
        request.session['dean_list'] = inst

    if request.session['gname'] == "HOI":
        dept = EmployeeMaster.objects.using('GITAM').filter(campus=request.user.campus,college_code=request.user.institution).values_list('dept_code',flat=True).distinct()
        dept = list(dept)
        context = dict()
        context['dept'] = dept
        return render(request,'dashboard.html',context)
    return render(request, 'dashboard.html')


def index(request):
    empid = request.POST['empid']
    password = request.POST['password']

    user = authenticate(username=empid, password=password)
    if user:
        user = User.objects.get(u_id=empid)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        gname = request.user.groups.all().values()
        gname2 = gname[0]['name']
        request.session['gname'] = gname2
        return redirect('dashboard')
    else:
        messages.error(request,'You are not authorized to access')
        return redirect('/')
def index2(request):
    empid = request.GET['empid']
    # empid = "aDiOLO07yvk=" # 501244
    # empid = 'jAvl39XOUfE=' #501618
    # id = empid
    id = Class1.Decrypt(empid, True, 'Cums$dHs')
    try:
        id = id.split('#')
        id = id[0]
    except:
        id = id

    print(id)
    if User.objects.filter(u_id=id).exists():
        user = User.objects.get(u_id=id)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        gname = request.user.groups.all().values()
        gname2 = gname[0]['name']
        request.session['gname'] = gname2
        return redirect('dashboard')
    else:
        messages.error(request,'You are not authorized to access')
        return redirect('/')

def ADMIN(request):
    request.session['gname'] = "ADMIN"
    return redirect('dashboard')

def LEADER(request):
    request.session['gname'] = "LEADER"
    return redirect('dashboard')

def HOD(request):
    request.session['gname'] = "HOD"
    return redirect('dashboard')

def HOI(request):
    request.session['gname'] = "HOI"
    return redirect('dashboard')

def CAMPUS(request):
    request.session['gname'] = "CAMPUS"
    return redirect('dashboard')

def DEAN(request):
    request.session['gname'] = "DEAN"
    return redirect('dashboard')

def get_groupname(request):
    if request.method != "GET":
        return JsonResponse({'data': "Error"})
    group_name = request.GET['group_name']
    group_name = 'no-reply' + group_name.lower() + "@gitam.edu"
    data = GroupList.objects.filter(user__email=request.user.email).values('group_name', 'group_email')

    group_list = [data[i]['group_email'] for i in range(len(data))]
    if group_name in group_list:
        return JsonResponse({'data': 1})
    else:
        return JsonResponse({'data': 0})


def view_history(request):
    data = PushNotification.objects.all().values('group', 'body', 'title', 'sent_by','id',
                                                 'dt_time', 'data', 'attachments','type').order_by('-id')
    context = {"data": data}
    return render(request, 'history.html', context)


def get_sentemail_data(request):
    try:
        from django.utils.timezone import localtime
        id = request.GET['id']
        data = PushNotification.objects.filter(id=id).values('group__group_email', 'group__group_name', 'message',
                                                             'subject', 'email_sent_date')
        group = data[0]['group__group_email']
        group_name = data[0]['group__group_name']
        message = data[0]['message']
        subject = data[0]['subject']
        email_sent_date = str(localtime(data[0]['email_sent_date']))
        return JsonResponse({'group': group, 'group_name': group_name, 'message': message, 'subject': subject,
                             'email_sent_date': email_sent_date[:16]})
    except:
        return JsonResponse(data=0)


def get_groupsettings(request):
    eid = request.GET['emailid']
    email = GroupList.objects.filter(group_name=eid).values('group_email')
    email = email[0]['group_email']
    file = request.session['random']
    picklefile = open(str(file), 'rb')
    # unpickle the dataframe
    service = pickle.load(picklefile)
    print(service)
    request = service.groups().get(groupKey="no-replydante@gitam.edu")
    data = request.execute()
    print(data)
    return JsonResponse(data=0)


def get_user_email(request):
    fname = request.GET['fname']
    lname = request.GET['lname']
    f1 = fname[0]
    f2 = lname[:7]
    gemail = f1 + f2 + "@gitam.edu"
    if data := EmployeeMaster.objects.using('GITAM').filter(emailid=gemail).values('emailid'):
        gemail = data[0]['emailid']
        gemail = gemail.split('@')
        fname = gemail[0]
        fname1 = fname + str(1) + "@gitam.edu"
        fname2 = fname + str(12) + "@gitam.edu"
        fname3 = fname + str(123) + "@gitam.edu"
        return JsonResponse({'data': [fname1, fname2, fname3]})

    return JsonResponse({'data': [gemail]})


def get_institute(request):
    if request.method != "GET":
        return JsonResponse({'data': "Error"})
    campus = request.GET.getlist('campus[]')
    gfor = request.GET.getlist('gfor[]')

    if ('student' in gfor) or ('parent' in gfor):
        institute = StudentMaster.objects.using('GITAM').filter(campus__in=campus, status="S").exclude(
            college_code__isnull=True).distinct().values_list('college_code', flat=True)
        institute = list(institute)
        institute = list(filter(None, institute))

    if 'staff' in gfor:
        institute = EmployeeMaster.objects.using('GITAM').filter(campus__in=campus, emp_status="A").exclude(
            college_code__isnull=True).distinct().values_list('college_code', flat=True)
        institute = list(institute)
        institute = list(filter(None, institute))
    if 'leaders' in gfor:
        institute = User.objects.filter(campus__in=campus,userOf__group__name='LEADER').exclude(
            institution__isnull=True).distinct().values_list('institution', flat=True)
        institute = list(institute)
        institute = list(filter(None, institute))

    if 'deans' in gfor:
        institute = User.objects.filter(campus__in=campus,userOf__group__name='DEAN').exclude(
            institution__isnull=True).distinct().values_list('institution', flat=True)
        institute = list(institute)
        institute = list(filter(None, institute))

    if all(item in gfor for item in ['staff', 'student']):
        institute1 = EmployeeMaster.objects.using('GITAM').filter(campus__in=campus, emp_status="A").exclude(
            college_code__isnull=True).distinct().values_list('college_code', flat=True)
        institute = StudentMaster.objects.using('GITAM').filter(campus__in=campus, status="S").exclude(
            college_code__isnull=True).distinct().values_list('college_code', flat=True)
        institute = list(institute)
        institute = list(filter(None, institute))
        institute1 = list(institute1)
        institute1 = list(filter(None, institute1))
        institute = institute1 + institute
        institute = list(set(institute))

    if request.session['gname'] == "DEAN" and not ('deans' in gfor):
        intersection = [value for value in institute if value in request.session['dean_list']]
        return JsonResponse({'data': intersection})
    return JsonResponse({'data': institute})


def get_department(request):
    if request.method != "GET":
        return JsonResponse({'data': "Error"})
    gfor = request.GET.getlist('gfor[]')
    campus = request.GET.getlist('campus[]')
    institute = request.GET.getlist('institute[]')
    if 'leaders' in gfor:
        df2 = User.objects.filter(campus__in=campus, institution__in=institute).exclude(dept_code__isnull=True).values_list(
            'dept_code', flat=True).distinct()
    if 'deans' in gfor:
        df2 = User.objects.filter(campus__in=campus, institution__in=institute).exclude(dept_code__isnull=True).values_list(
            'dept_code', flat=True).distinct()
    if 'staff' in gfor:
        df2 = EmployeeMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                           emp_status="A").exclude(dept_code__isnull=True).values_list(
            'dept_code', flat=True).distinct()
    if 'student' in gfor:
        df2 = StudentMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                          status="S").exclude(dept_code__isnull=True).values_list(
            'dept_code', flat=True).distinct()
    if all(item in gfor for item in ['staff', 'student']):
        df2 = StudentMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                          status="S").exclude(dept_code__isnull=True).values_list(
            'dept_code', flat=True).distinct()
        df3 = EmployeeMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                           emp_status="A").exclude(dept_code__isnull=True).values_list(
            'dept_code', flat=True).distinct()
        df2 = list(df2)
        df2 = list(filter(None, df2))

        df3 = list(df3)
        df3 = list(filter(None, df3))
        df2 = df2 + df3
        df2 = set(df2)

    df2 = list(df2)
    df2 = list(filter(None, df2))
    return JsonResponse({'data': df2})

@csrf_exempt
def get_batch(request):
    gfor = request.POST.getlist('gfor[]')
    if request.session['gname'] == "HOD" or request.session['gname'] == "HOI":
        campus = request.POST.get('campus')
        institute = request.POST.get('institute')
        if request.session['gname'] == "HOD":
            department = request.POST.get('department')
            department = [department]
        else:
            department = request.POST.getlist('department[]')
        campus = [campus]
        institute = [institute]
    else:
        campus = request.POST.getlist('campus[]')
        institute = request.POST.getlist('institute[]')
        department = request.POST.getlist('department[]')
    degree = request.POST.getlist('degree[]')

    if ('student' in gfor) or ('parent' in gfor):
        df2 = StudentMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                          dept_code__in=department, status="S",
                                                          degree_code__in=degree).exclude(
            dept_code__isnull=True).values_list('class_field', flat=True).distinct()
    df2 = list(df2)
    print(df2)
    df2 = list(filter(None, df2))
    return JsonResponse({'data': df2})


def get_student_emails(request):
    if request.method != "GET":
        return JsonResponse({'data': "Error"})
    gfor = request.GET.getlist('gfor[]')
    campus = request.GET.getlist('campus[]')
    institute = request.GET.getlist('institute[]')
    department = request.GET.getlist('department[]')
    degree = request.GET.getlist('degree[]')
    batch = request.GET.getlist('batch[]')


    if 'student' in  gfor:
        df2 = StudentMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                          dept_code__in=department, class_field__in=batch,
                                                          degree_code__in=degree, status="S").exclude(
            dept_code__isnull=True).values_list('emailid', flat=True).distinct()
    df2 = list(df2)
    df2 = list(filter(None, df2))

    return JsonResponse({'data': df2})


def get_email_ids(request):
    if request.method != "GET":
        return JsonResponse({'data': "Error"})
    campus = request.GET.getlist('campus[]')
    institute = request.GET.getlist('institute[]')
    department = request.GET.getlist('department[]')
    role = request.GET['role']
    print(role)
    if role != "all":
        ins = EmployeeMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                           dept_code__in=department, job_status=role,
                                                           emp_status="A").exclude(emailid__isnull=True).values_list(
            'emailid', flat=True).distinct()
    else:
        ins = EmployeeMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                           dept_code__in=department, emp_status="A").exclude(
            emailid__isnull=True).values_list('emailid', flat=True).distinct()

    df2 = list(ins)
    df2 = list(filter(None, df2))

    return JsonResponse({'data': df2})


def send_push_notification(push_list, role_, notification, visibility, request, circular, title, body, data):
    try:
        close_old_connections()
        push_tokens = PushToken.objects.using('G-comm').filter(userid__in=push_list, role=role_, is_active=1).values_list('token', flat=True)

        push_client = PushClient()
        for push_token in push_tokens:
            if push_token:

                print('push_token')
                print(push_token)
                push = PushNotificationStatus.objects.create(notification=notification, role=role_,
                                                             userid=PushToken.objects.using('G-comm').get(token=push_token, role=role_).userid)
                push.visibility = visibility
                push.save()
                if request.user.category:
                    push.category = request.user.category
                    if request.user.category == "PROVC":
                        push.sub_category = request.user.campus
                    if request.user.category == "HOD":
                        push.sub_category = request.user.dept_code
                    if request.user.category == "HOI":
                        push.sub_category = request.user.institution

                    push.save()
                web = WebNotificationStatus.objects.create(notification=notification, role=role_,
                                                             userid=PushToken.objects.using('G-comm').get(token=push_token, role=role_).userid)
                web.visibility = visibility
                web.save()
                if request.user.category:
                    web.category = request.user.category
                    web.save()

                if circular:
                    message = PushMessage(
                        to=push_token,
                        title=title,
                        body=body,
                        data={"id": push.id, "data": data},
                    )
                else:
                    message = PushMessage(
                        to=push_token,
                        title=title,
                        body=body,
                        data={"id": None},
                    )
                response = push_client.publish(message)
                print('--------------')
                print(response)
                print(push_token)
                print('--------------')

    except Exception as e:
        print(str(e))


from threading import Thread


def boardcast(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        data = request.POST['message']
        type_of_communication = request.POST['type_of_communication']
        sent_by = request.user.u_id
        push_for = request.POST.getlist('gfor')
        schedule = request.POST.get('schedule_dt', False)
        circular = int(request.POST.get('circular', 0))

        campus = request.POST.getlist('campus[]')
        college = request.POST.getlist('institute[]')
        department = request.POST.getlist('department[]')
        student_type = request.POST.getlist('type_student[]')

        degree = request.POST.getlist('degree[]') if 'degree[]' in request.POST else []
        batch = request.POST.getlist('batch[]') if 'batch[]' in request.POST else []
        role = request.session['gname']

        upload = request.FILES.get('upload', '')

        role_map = {
            "student": 'S',
            "parent": 'P',
            "staff": 'E',
            "leaders": 'E',
            "deans": 'E'
        }
        role_ = next((role_map[r] for r in push_for if r in role_map), '')

        push_list = []

        if any(group in push_for for group in ['student', 'parent']):
            students = StudentMaster.objects.using("GITAM").filter(
                campus__in=campus, college_code__in=college, dept_code__in=department
            )
            if degree:
                students = students.filter(degree_code__in=degree)
            if batch:
                students = students.filter(batch__in=batch)
            push_list += list(students.values_list('regdno', flat=True))

        if 'staff' in push_for:
            employees = EmployeeMaster.objects.using("GITAM").filter(
                campus__in=campus, college_code__in=college, dept_code__in=department
            )
            if role:
                employees = employees.filter(job_status__in=role)
            push_list += list(employees.values_list('empid', flat=True))

        if 'leaders' in push_for:
            push_list += list(
                User.objects.filter(
                    campus__in=campus, institution__in=college, dept_code__in=department, userOf__group__name='LEADER'
                ).values_list('u_id', flat=True)
            )

        if 'deans' in push_for:
            push_list += list(
                User.objects.filter(
                    campus__in=campus, institution__in=college, dept_code__in=department, userOf__group__name='DEAN'
                ).values_list('u_id', flat=True)
            )

        # Create notification in the default database
        notification = PushNotification.objects.create(
            type_of_communication=type_of_communication,
            title=title,
            body=body,
            data=data,
            group=push_for,
            sent_by=sent_by,
            type='Circular' if circular else 'Push',
            campus=campus,
            batch=batch,
            degree=degree,
            student_type=student_type,
            institute=college,
            department=department,
            category=request.user.category,
            role=role,
            hosteler="hosteler" in student_type,
            scheduled_time=schedule if schedule else None,
            is_schedule=bool(schedule),
            attachments=upload  # Save the file first
        )

        # Now update the attachments_url with the actual stored filename
        if notification.attachments:
            notification.attachment_url = f"https://gcommunications.gitam.edu/media/{notification.attachments.name}"
            notification.save(update_fields=['attachment_url'])  # Save only this field to avoid unnecessary updates

        # Insert into 'mobile' database
        PNotification.objects.using('mobile').create(
            **{field.name: getattr(notification, field.name) for field in PushNotification._meta.fields}
        )

        visibility = 1

        # Start push notification in a thread
        push_thread = Thread(
            target=send_push_notification,
            args=(push_list, role_, notification, visibility, request, circular, title, body, data)
        )
        push_thread.start()

        sweetify.success(request, "Message Sent Successfully")

    return redirect('/dashboard')


@csrf_exempt
def upload(request):
    data = request.FILES['file']
    obj = UploadImage(image=data)
    obj.save()
    print(obj.image.url)

    return JsonResponse({"location": obj.image.url})


def delete_group(request):
    try:
        eid = request.GET['emailid']
        email = GroupList.objects.filter(group_name=eid).values('group_email')
        email = email[0]['group_email']
        file = request.session['random']
        picklefile = open(str(file), 'rb')
        # unpickle the dataframe
        service = pickle.load(picklefile)
        service.groups().delete(groupKey=email).execute()
        li = request.session['groups']
        for i in li.copy():
            if i['group_email'] == email:
                li.pop()

        request.session['groups'] = li
        return JsonResponse({"data": 1, "status": 1})
    except:
        return JsonResponse({"data": 0, "status": 0})


def update_group(request):
    try:
        eid = request.GET['emailid']
        print("hello")
        print(eid)
        print("jarugu")
        email = GroupList.objects.filter(group_name=eid).values('group_email')
        email = email[0]['group_email']
        file = request.session['random']
        picklefile = open(str(file), 'rb')
        # unpickle the dataframe
        service = pickle.load(picklefile)
        request = service.members().list(groupKey=email)
        data = request.execute()
        print(data)
        return JsonResponse({"data": 1, "status": 1})

    except:
        return JsonResponse({"data": 0, "status": 0})


def boardcast_1(request):
    if request.method == "POST":
        messages_ = request.POST['message']
        subject = request.POST['subject']

    return redirect('index')

@login_required
def get_hoi_dept(request):
    df2 = EmployeeMaster.objects.using('GITAM').filter(campus=request.user.campus, college_code=request.user.institution,
                                                       emp_status="A").exclude(dept_code__isnull=True).values_list(
        'dept_code', flat=True).distinct()
    df2=list(df2)
    df2 = list(filter(None, df2))
    return JsonResponse({"data":df2})


def add_user_d(request):
    pass
