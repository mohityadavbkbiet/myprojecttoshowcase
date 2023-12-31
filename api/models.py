from django.db import models

# Create your models here.
class Invoice(models.Model):
     invoice_id = models.AutoField(primary_key=True)
     invoice_date = models.DateField(auto_now_add=True)
     invoice_customer_name = models.CharField(max_length=50)

class InvoiceDetails(models.Model):
       invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)     
       description=models.CharField(max_length=50)
       quantity = models.IntegerField()
       unit_price = models.IntegerField()
       unit_price=models.IntegerField()
       price = models.IntegerField()
