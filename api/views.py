from django.shortcuts import render
from rest_framework import viewsets
from api.models import InvoiceDetails,Invoice 
from api.serializers import InvoiceDetailsSerializer, InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
     queryset = Invoice.objects.all()
     serializer_class=InvoiceSerializer


class InvoiceDetailsViewSet(viewsets.ModelViewSet):
     queryset = InvoiceDetails.objects.all()
     serializer_class=InvoiceDetailsSerializer