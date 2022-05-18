from django.db import models
from account.models import Account
from organization.models import CloudProvider, GithubProvider, Organization
# Create your models here.

class Workspace(models.Model):
    name = models.CharField(max_length=64)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    cloud_provider = models.ManyToManyField(CloudProvider)
    github_provider = models.ManyToManyField(GithubProvider)
    github_repo = models.CharField(max_length=128)


class WorkspaceParameter(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    parameter_key = models.CharField(max_length=64)
    parameter_value = models.CharField(max_length=255)
