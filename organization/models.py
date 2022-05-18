from django.db import models
from account.models import Account
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Organization(models.Model):
    owner = models.ManyToManyField(Account)
    name = models.CharField(max_length=64)

class OrganizationMember(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ManyToManyField(Account)
    
    class Status(models.TextChoices):
        invited = 'invited', _('Invited')
        confirmed = 'confirmed', _('Confirmed')
    
    status = models.CharField(
        max_length=10, 
        choices=Status.choices,
        default=Status.invited
    )

class GCPCloudProvider(models.Model):
    credentials = models.CharField(max_length=1024)

class AWSCloudProvider(models.Model):
    access_key_id = models.CharField(max_length=64)
    secret_access_key = models.CharField(max_length=64)

class CloudProvider(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    provider = models.IntegerField()
    name = models.CharField(max_length=64)

    class ProviderType(models.TextChoices):
        aws = 'aws', _('AWS')
        google = 'google', _('Google')

    provider_type = models.CharField(
        max_length=10,
        choices = ProviderType.choices,
        default=ProviderType.google
    )

class GithubProvider(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    repo_name = models.CharField(max_length=64)
    repo_organization = models.CharField(max_length=64)
    api_url = models.CharField(max_length=255)
    http_url = models.CharField(max_length=255)
    personal_access_token = models.CharField(max_length=64)