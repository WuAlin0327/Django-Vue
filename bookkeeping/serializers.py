from bookkeeping import models
from rest_framework import serializers


class OfconsumptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Ofconsumption
        fields = '__all__'

class ChargeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Charge
        fields = '__all__'