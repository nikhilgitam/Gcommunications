from django.shortcuts import render
from .encryption_util import decrypt
from app.models import *
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from app.models import PushNotification, StudentMaster,EmployeeMaster
import ast
from rest_framework import status
import json
#
# class GETUSERS(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     @staticmethod
#     def get(request):
#         id = request.get.data('id')
#         # id = decrypt(id)
#         data = PushNotification.objects.get(id=id)
#         pass

class GETUSERS(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        id = request.GET.get('id')

        if not id:
            return Response({"error": "id parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            push_notification = PushNotification.objects.get(id=id)
            print(f"Group value: {push_notification.group}")
            response_data = {
                'id': push_notification.id,
                'role': push_notification.role,
                'body': push_notification.body,
                'title': push_notification.title,
                'data': push_notification.data,
            }

            group_list = ast.literal_eval(push_notification.group) if isinstance(push_notification.group, str) else push_notification.group
            group_list = [g.strip().lower() for g in group_list]

            filter_args = {}
            if push_notification.campus:
                campus = ast.literal_eval(push_notification.campus)
                filter_args['campus__in'] = campus
                print(filter_args['campus__in'])
            if push_notification.institute:
                institute = ast.literal_eval(push_notification.institute)
                filter_args['college_code__in'] = institute
                print(filter_args['college_code__in'])
            if push_notification.department:
                department = ast.literal_eval(push_notification.department)
                filter_args['dept_code__in'] = department
                print(filter_args['dept_code__in'])

            students_regdno = []
            employees_empid = []

            if 'student' in group_list:
                students_queryset = StudentMaster.objects.using('GITAM').filter(**filter_args).exclude(dept_code__isnull=True).distinct()
                students_regdno = students_queryset.values_list('regdno', flat=True)

            if 'staff' in group_list:
                employees_queryset = EmployeeMaster.objects.using('GITAM').filter(**filter_args).distinct()
                employees_empid = employees_queryset.values_list('empid', flat=True)

            if students_regdno:
                response_data['students'] =  list(students_regdno)

            if employees_empid:
                response_data['staff'] = list(employees_empid)

            return Response(response_data, status=status.HTTP_200_OK)

        except PushNotification.DoesNotExist:
            return Response({"error": "PushNotification not found with the given id."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


