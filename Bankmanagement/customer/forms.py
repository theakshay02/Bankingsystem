from django import forms  
from customer.models import Customer  


class CustomerForm(forms.ModelForm):
    class Meta:

        customer_type = (
            ('Yes', True),
            ('No', False)
        )
        Loans_taken = (
            ('Home', 'Home'), 
            ('Vehicle', 'Vehicle'), 
            ('Gold', 'Gold'), 
            ('None', 'None')
        )

        model = Customer
        fields = ("id","name","email","phno","cardcompany","typeofCust",'age','opening_date', 'balance_left', 'Type_loans', 'Address', 'cust_image')
        widgets = {
        'id':forms.HiddenInput(),
        'name': forms.TextInput(),
        'email': forms.EmailInput(),
        'phno': forms.NumberInput(),
        'typeofCust': forms.RadioSelect(choices=customer_type),
        'age': forms.NumberInput(),
        'opening_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date','required':True}),
        'Type_loans': forms.CheckboxSelectMultiple(choices=Loans_taken),
        'Address': forms.Textarea(attrs={'rows': 5, 'cols': 30}),
        'cust_image': forms.FileInput(),
        }