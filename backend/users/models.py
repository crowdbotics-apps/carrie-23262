from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.
    """
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
    )
    rank = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        null=True,
        blank=True,
    )
    location = models.ForeignKey(
        "users.Location",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user_location",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Location(models.Model):
    "Generated Model"
    address1 = models.CharField(
        max_length=256,
    )
    address2 = models.CharField(
        max_length=256,
    )
    state = models.CharField(
        max_length=2,
    )
    city = models.CharField(
        max_length=5,
    )
    zip = models.IntegerField()
