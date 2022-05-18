from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.models import Group as AuthGroup
# Create your models here.
# https://docs.djangoproject.com/en/4.0/ref/contrib/auth/


class Organization(models.Model):
    org_name = models.CharField(max_length=64)

class User(AuthUser):
    pass

class Team(AuthGroup):
    org = models.ManyToManyField(Organization)

class TeamMember(models.Model):
    team = models.ManyToManyField(Team)
    user = models.ManyToManyField(User)

class TeamAdmin(models.Model):
    team = models.ManyToManyField(Team)
    user = models.ManyToManyField(User)

class OrganizationMember(models.Model):
    org = models.ManyToManyField(Organization)
    user = models.ManyToManyField(User)

class OrganizationAdmin(models.Model):
    org = models.ManyToManyField(Organization)
    user = models.ManyToManyField(User)

class OrganizationInvite(models.Model):
    org = models.ManyToManyField(Organization)
    email = models.EmailField()