from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
   ('billing','Billing'),
   ('shipping','Shipping'),

	)
# Create your models here.
class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile)
    address_type    = models.CharField(max_length=120, choices= ADDRESS_TYPES)
    address_line_1  = models.CharField(max_length=120,blank=True)
    address_line_2  = models.CharField(max_length=120,null=True,blank=True)
    Area            = models.CharField(max_length=120)
    Block           = models.CharField(max_length=120)
    Road_No         = models.CharField(max_length=120)
    House_No        = models.CharField(max_length=120)
    Flat_No         = models.CharField(max_length=120)
    City            = models.CharField(max_length=120)
    Phone           = models.CharField(max_length=120)
    Country         = models.CharField(max_length=120,default='Bangladesh')


    def __str__(self):
    	return str(self.billing_profile)

    def get_address(self):
    	return "{Area}\n {Block}\n  {Road_No}\n  {House_No}\n  {Flat_No}\n  {City}\n {line1}\n {Phone}\n,{Country}.".format(

        
        
        Area=self.Area,
        Block=self.Block,
        Road_No=self.Road_No,
        House_No=self.House_No,
        Flat_No=self.Flat_No,
        City =self.City,
        line1=self.address_line_1,
        Phone = self.Phone,
        Country =self.Country



    		)