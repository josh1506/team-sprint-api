from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Organization(models.Model):
    name = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="org_owned", null=False
    )
    members = models.ManyToManyField(
        User, related_name="org_member", blank=True, null=True
    )
    logo = models.ImageField(
        upload_to="team_sprint/static/images/organizations/logo", null=True, blank=True
    )
    code = models.CharField(max_length=255, default="", null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
