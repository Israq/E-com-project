from django import forms

from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model  = Address
		fields = [
         	#'billing_profile', 
		    #'address_type',    
		    'address_line_1',  
		    'address_line_2',  
		    'Area',            
		    'Block',           
		    'Road_No',         
		    'House_No',       
		    'Flat_No',         
		    'City',            
		    'Phone',           
		    'Country'         


		]