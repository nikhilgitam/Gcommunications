from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="login"),
    path('dashboard', dashboard, name="dashboard"),
    path('index', index, name='index'),
    path('get_institute', get_institute, name='get_institute'),
    path('get_department', get_department, name='get_department'),
    path('get_emails', get_email_ids, name='get_emails'),
    path('get_groupname', get_groupname, name='get_groupname'),
    path('broadcast', boardcast, name='broadcast'),
    path('broadcast_1', boardcast_1, name='broadcast_1'),
    path('upload', upload, name='upload'),
    path('logout', logout, name='logout'),
    path('view_history', view_history, name='view_history'),
    path('get_sentemail_data', get_sentemail_data, name='get_sentemail_data'),
    path('delete_group', delete_group, name='delete_group'),
    path('update_group', update_group, name='update_group'),
    path('get_groupsettings', get_groupsettings, name='get_groupsettings'),
    path('get_batch', get_batch, name='get_batch'),
    path('get_student_emails', get_student_emails, name='get_student_emails'),
    path('get_user_email', get_user_email, name='get_user_email'),

]
