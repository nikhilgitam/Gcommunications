from django.db import models

# Create your models here.
class PushNotification(models.Model):
    role = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    type_of_communication = models.CharField(max_length=100, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    campus = models.TextField(null=True, blank=True)
    institute = models.TextField(null=True, blank=True)
    department = models.TextField(null=True, blank=True)
    batch = models.TextField(null=True, blank=True)
    degree = models.TextField(null=True, blank=True)
    student_type = models.TextField(null=True, blank=True)
    hosteler = models.BooleanField(null=True, blank=True)
    group = models.TextField(null=True, blank=True)
    sent_by = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=10, null=True, blank=True)
    is_web = models.BooleanField(null=True, blank=True)
    is_schedule = models.BooleanField(null=True, blank=True)
    attachments = models.CharField(max_length=100, null=True, blank=True)
    attachment_url = models.TextField(blank=True, null=True)
    scheduled_time = models.DateTimeField(null=True, blank=True)
    repeat_message = models.IntegerField(null=True, blank=True)
    dt_time = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'pushnotification'

    def save(self, *args, **kwargs):
        if self.attachments:
            self.attachment_url = f"https://gcommunications.gitam.edu/media/{self.attachments.name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else "Push Notification"