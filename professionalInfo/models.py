from django.db import models
from account.models import Account

class Organization(models.Model):
    organization_name = models.CharField(max_length=40)
    organization_type = models.CharField(max_length=40)

    def __str__(self):
        return self.organization_name

class ProfessionalInfo(models.Model):
    designation = models.CharField(max_length=40, blank=True, null=True)
    organization = models.ForeignKey(Organization,on_delete=models.PROTECT)
    date_join = models.DateField()
    profile = models.ForeignKey(Account, on_delete=models.CASCADE)
