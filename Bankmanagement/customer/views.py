from django.shortcuts import render,redirect
from customer.forms import CustomerForm  
from customer.models import Customer  
from django.views import View

# Addcust your views here.  

class Index(View):
    def get(self, request):
        return redirect('/display')

class Addcust(View):
    def get(self, request):
        form = CustomerForm()  
        return render(request,'addcust.html',{'form':form})  

    def post(self, request):
        form = CustomerForm(request.POST,request.FILES) 
        if form.is_valid():  
            form.save()  
            return redirect('/display')  
            
class Display(View):
    def get(self, request):
        customers = Customer.objects.all()  
        return render(request,"display.html",{'customers':customers}) 


class Update(View):
    def get(self, request,id):
        customer = Customer.objects.get(id=id)  
        return render(request,'update.html', {'customer':customer})  

    def post(self,request,id):
        customer = Customer.objects.get(id=id)  
        for i in request.POST:
            if i == 'name':
                if customer.name != request.POST['name']:
                    customer.name = request.POST['name']
            if i == 'email':
                if customer.email != request.POST['email']:
                    customer.email = request.POST['email']
            if i == 'phno':
                if customer.phno != request.POST['phno']:
                    customer.phno = request.POST['phno']
            if i == 'cardcompany':
                if customer.cardcompany != request.POST['cardcompany']:
                    customer.cardcompany = request.POST['cardcompany']
            if i == 'typeofCust':
                if customer.typeofCust != request.POST['typeofCust'] and request.POST['typeofCust'] != '':
                    customer.typeofCust = request.POST['typeofCust']
            if i == 'age':
                if customer.age != request.POST['age']:
                    customer.age = request.POST['age']
            if i == 'opening_date':
                if customer.opening_date != request.POST['opening_date'] and request.POST['opening_date'] != '':
                    customer.opening_date = request.POST['opening_date']
            if i == 'balance_left':
                if customer.balance_left != request.POST['balance_left']:
                    customer.balance_left = request.POST['balance_left']
            if i == 'Address':
                if customer.Address != request.POST['Address']:
                    customer.Address = request.POST['Address']
            if i == 'cust_image':
                if request.POST['cust_image'] != '':
                    customer.cust_image = request.FILES['cust_image']
        for i in request.FILES:
            if i == 'cust_image':
                if request.FILES['cust_image'] != '':
                    customer.cust_image = request.FILES['cust_image']
        customer.save()
        return redirect("/display")  



class Delete(View):
    def get(self,request,id):
        customer = Customer.objects.get(id=id)  
        customer.delete()  
        return redirect("/display")      

