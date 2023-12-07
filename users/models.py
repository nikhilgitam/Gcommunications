from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class User(AbstractUser):
    email = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    campus = models.CharField(max_length=100, null=True, blank=True)
    institution = models.CharField(max_length=100, null=True, blank=True)
    dept_code = models.CharField(max_length=100, null=True, blank=True)
    u_id = models.CharField(max_length=50, blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user",
        related_query_name="user",
        through="UserGroups"
    )

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return str(self.username)


class UserGroups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userOf")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="groupOf")
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="User Groups"
        db_table = "user_group"
