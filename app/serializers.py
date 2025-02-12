from rest_framework import serializers
from .models import PushNotification

class PushNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotification
        fields = ['id', 'campus', 'institute', 'department', 'batch', 'degree', 'student_type']