
from rest_framework import serializers
from api.models import Invoice,InvoiceDetails


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
          model = Invoice
          fields = '__all__'

class InvoiceDetailsSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
          model = InvoiceDetails
          fields = '__all__'