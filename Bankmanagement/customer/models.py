from django.db import models
from django.forms.widgets import Widget



class Customer(models.Model):
    card_company = (
        ('Visa', 'Visa'),
        ('MasterCard', 'MasterCard'),
        ('Rupay', 'Rupay'),
        ('NA', 'NA')
    )

    id = models.AutoField(db_column='ID',primary_key=True) 
    name = models.CharField(db_column='Name', max_length=30)  
    cust_image = models.ImageField(db_column='Photo_customer',upload_to='')
    cardcompany = models.CharField(choices=card_company, max_length=10, default="NA")
    typeofCust = models.BooleanField(db_column='cust_type')
    age = models.IntegerField(db_column='Age')
    opening_date = models.DateField(db_column='openingDate') 
    balance_left = models.FloatField(db_column='Balance')
    email = models.EmailField(db_column='Email', max_length=60)
    phno = models.CharField(db_column='Ph_number', max_length=20)
    Address = models.TextField(db_column='Address')
    Type_loans = models.TextField()
    
    class Meta:
        db_table = 'bankingsystem'
        