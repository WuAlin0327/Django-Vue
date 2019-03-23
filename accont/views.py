from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from accont import models
from accont.utils.token import get_token_code

class LoginView(APIView):


    def post(self,request):

        res = {
            'alert':True,
            'token':'账号或者密码错误'
        }
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.UserInfo.objects.filter(username=username,password=password).first()
        if user:
            res['alert'] = False
            res['token'] = get_token_code(user.username)

        return Response(res)