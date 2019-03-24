from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from bookkeeping import serializers
from rest_framework.response import Response
from bookkeeping import models
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from accont.Auth import UserAuth

class OfconsumptionAPIViwe(generics.ListCreateAPIView):
    queryset = models.Ofconsumption.objects.all()
    serializer_class = serializers.OfconsumptionSerializers


class ChargeAPIView(generics.ListCreateAPIView):
    authentication_classes = [UserAuth,]
    queryset = models.Charge.objects.filter()
    serializer_class = serializers.ChargeSerializers


    def get(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(user_id=request.user.id)
        response = []
        for obj in self.queryset.all().order_by('-ofconsumption_date'):
            dic = {}
            dic['income_or_outlay'] = obj.ofconsumption.get_income_or_outlay_display()
            dic['doughy'] = obj.doughy
            dic['consume_date'] = obj.ofconsumption_date
            dic['consume_title'] = obj.ofconsumption.title
            dic['consume_icon'] = obj.ofconsumption.icon
            response.append(dic)


        return Response(response)

    def post(self, request, *args, **kwargs):
        response = {
            'status':True,
            'msg':'上传成功'
        }
        try:
            ofconsumption_id = request.data.get('ofconsumption_id')
            money = request.data.get('doughy')
            models.Charge.objects.create(ofconsumption_id=ofconsumption_id,doughy=money, user_id=request.user.id)
        except Exception:
            response['status'] = False
            response['msg'] = '上传失败'
        return Response(response)