from django.contrib.auth import models as auth_models
from django.db import models

from django_final_project.authentication.managers import AppUsersManager


# Create your models here.
# from django_final_project import AppUsersManager


class ClimbingGuideUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    # TODO
    # email
    # password
    # is_staff
    # is_active

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


class Profile(models.Model):
    # TODO
    # first_name
    # last_name
    # profile_image
    # date_of_birth

    first_name = models.CharField(
        max_length=25,
    )

    last_name = models.CharField(
        max_length=25,
    )

    user = models.OneToOneField(
        ClimbingGuideUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
