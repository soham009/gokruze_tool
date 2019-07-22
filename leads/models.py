from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone

class Leads(models.Model):
    LEAD_STATUS = (('Interested','Interested'),
                   ('Undecided','Undecided'),
                   ('Uncontacted','Uncontacted'),
                   ('Converted','Converted'))
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    City = models.CharField(max_length=264,blank=True)
    Name = models.CharField(max_length=264)
    Gender	=	models.CharField(max_length=264,blank=True)
    EmailId	=	models.CharField(max_length=264,blank=True)
    ContactNo	=	models.CharField(max_length=264,blank=True)
    LocationFrom	=	models.CharField(max_length=264,blank=True)
    LocationTo	=	models.CharField(max_length=264,blank=True)
    LoginTime	=	models.CharField(max_length=264,blank=True)
    LogoutTime	=	models.CharField(max_length=264,blank=True)
    CompanyName	=	models.CharField(max_length=264,blank=True)
    TravalToWork	=	models.CharField(max_length=264,blank=True)
    TravelToWorkOther	= models.CharField(max_length=264,blank=True)
    MonthlySpend	=	models.CharField(max_length=264,blank=True)
    HearAboutUs	=	models.CharField(max_length=264,blank=True)
    SubmittedOn	=	models.CharField(max_length=264,blank=True)
    Lead_Status = models.CharField(choices=LEAD_STATUS,max_length=264,default="Uncontacted")
    Remark = models.TextField(blank=True)
    LocationFromOther = models.CharField(max_length=264,blank=True)
    SubmittedOnDate	=	models.DateTimeField(default=timezone.now)
    is_valid = models.BooleanField(default=False)
    password_change_request = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Leads Collected"
        verbose_name = "Lead"

# Create your models here.
class CustomUser(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    NORMAL_USER = 1
    RESTAURANT_1_ADMIN = 2
    SUPER_ADMIN = 13
    ROLE_CHOICES = (
      (NORMAL_USER,'normal_user'),
      (RESTAURANT_1_ADMIN,'admin'),
      (SUPER_ADMIN,'super_admin'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=NORMAL_USER)
    name = models.CharField(max_length=264, blank='True')