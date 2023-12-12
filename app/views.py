import pickle

import sweetify
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from email.message import EmailMessage
from email.mime.text import MIMEText
import base64

from exponent_server_sdk import PushMessage, PushClient

from app.models import *
from datetime import datetime

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
    return redirect('/')


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
    if User.objects.filter(u_id=empid).exists():
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

def ADMIN(request):
    request.session['gname'] = "ADMIN"
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
    data = PushNotification.objects.all().values('group', 'body', 'title', 'sent_by',
                                                 'dt_time', 'data', 'attachments','type')
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
    gfor = request.GET['gfor']
    if gfor == "staff":
        institute = EmployeeMaster.objects.using('GITAM').filter(campus__in=campus, emp_status="A").exclude(
            college_code__isnull=True).distinct().values_list('college_code', flat=True)
    else:
        institute = StudentMaster.objects.using('GITAM').filter(campus__in=campus, status="S").exclude(
            college_code__isnull=True).distinct().values_list('college_code', flat=True)

    institute = list(institute)
    institute = list(filter(None, institute))
    if request.session['gname'] == "DEAN":
        intersection = [value for value in institute if value in request.session['dean_list']]
        return JsonResponse({'data': intersection})

    return JsonResponse({'data': institute})


def get_department(request):
    if request.method != "GET":
        return JsonResponse({'data': "Error"})
    gfor = request.GET['gfor']
    campus = request.GET.getlist('campus[]')
    institute = request.GET.getlist('institute[]')
    if gfor == "staff":
        df2 = EmployeeMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                           emp_status="A").exclude(dept_code__isnull=True).values_list(
            'dept_code', flat=True).distinct()
    else:
        df2 = StudentMaster.objects.using('GITAM').filter(campus__in=campus, college_code__in=institute,
                                                          status="S").exclude(dept_code__isnull=True).values_list(
            'dept_code', flat=True).distinct()
    df2 = list(df2)
    df2 = list(filter(None, df2))
    return JsonResponse({'data': df2})


def get_batch(request):
    if request.method != "GET":
        return JsonResponse({'data': "Error"})
    gfor = request.GET['gfor']
    if request.session['gname'] == "HOD" or request.session['gname'] == "HOI":
        campus = request.GET.get('campus')
        institute = request.GET.get('institute')
        if request.session['gname'] == "HOD":
            department = request.GET.get('department')
            department = [department]
        else:
            department = request.GET.getlist('department[]')
        campus = [campus]
        institute = [institute]
    else:
        campus = request.GET.getlist('campus[]')
        institute = request.GET.getlist('institute[]')
        department = request.GET.getlist('department[]')
    degree = request.GET.getlist('degree[]')
    print(campus)
    print(institute)
    print(department)
    print(degree)
    if gfor == "student" or gfor == "parent":
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
    gfor = request.GET['gfor']
    campus = request.GET.getlist('campus[]')
    institute = request.GET.getlist('institute[]')
    department = request.GET.getlist('department[]')
    degree = request.GET.getlist('degree[]')
    batch = request.GET.getlist('batch[]')
    print(batch)

    if gfor == "student":
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


def boardcast(request):
    if request.method == "POST":

        title = request.POST['title']
        body = request.POST['body']
        data = request.POST['message']
        sent_by = '501235'
        push_for = request.POST['gfor']
        visibility = request.POST['visibility']
        print(visibility)
        circular = 0
        if 'circular' in request.POST:
            circular = int(request.POST['circular'])

        campus = request.POST.getlist('campus[]')
        college = request.POST.getlist('institute[]')
        department = request.POST.getlist('department[]')
        degree = ""
        if 'degree' in request.POST:
            degree = request.POST.getlist('degree[]')
        batch = ""
        if 'batch' in request.POST:
            batch = request.POST.getlist('batch[]')
        role = ""
        if 'role' in request.POST:
            role = request.POST.getlist('role[]')
        upload = ''
        if 'upload' in request.FILES:
            upload = request.FILES['upload']
        if push_for == "student":
            role_ = 'S'
        elif push_for == "parent":
            role_ = 'P'
        else:
            role_ = 'E'
        if push_for == "student" or push_for == "parent":
            students = StudentMaster.objects.using("GITAM").filter(campus__in=campus, college_code__in=college,
                                                                   dept_code__in=department)
            if degree != "":
                students.filter(degree_code__in=degree)
            if batch != "":
                students.filter(batch__in=batch)

            push_list = list(students.values_list('regdno', flat=True))
        else:
            employees = EmployeeMaster.objects.using("GITAM").filter(campus__in=campus, college_code__in=college,
                                                                     dept_code__in=department)
            if role != "":
                employees.filter(job_status=role)
            push_list = list(employees.values_list('empid', flat=True))
        group = "[" + ', '.join(campus) + '],[' + ', '.join(college) + '],[' + ', '.join(
            department) + '],'
        if degree != "":
            group += '[' + ', '.join(degree) + '],'
        if batch != "":
            group += '[' + ', '.join(batch) + '],'
        if role != "":
            group += '[' + ', '.join(role) + '],'
        group += push_for

        notification = PushNotification.objects.create(title=title, body=body, data=data, group=group, sent_by=sent_by, type='Push')
        notification.campus = campus
        notification.institute = college
        notification.department = department
        notification.save()
        if circular:
            notification.type = 'Circular'

        if upload != '':
            notification.attachments = upload
            notification.save()
        push_tokens = PushToken.objects.using('G-comm').filter(userid__in=push_list, role=role_).values_list('token', flat=True)

        try:
            push_client = PushClient()
            for push_token in push_tokens:
                if push_token:
                    print('push_token')
                    print(push_token)
                    push = PushNotificationStatus.objects.create(notification=notification, role=role_,
                                                                 userid=PushToken.objects.using('G-comm').get(token=push_token,
                                                                                              role=role_).userid)
                    push.visibility_timer = visibility
                    push.save()

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
                sweetify.success(request, "Push Notified Successfully!!")
        except Exception as e:
            print(str(e))
            sweetify.error(request, str(e))
        #sweetify.success(request, "Message Sent Successfully")
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
