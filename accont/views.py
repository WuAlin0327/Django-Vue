from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from accont import models
from accont.utils.token import get_token_code


class LoginView(APIView):

    def post(self, request):

        res = {
            'alert': True,
            'token': '账号或者密码错误',

        }
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.UserInfo.objects.filter(username=username, password=password).first()
        if user:
            token = get_token_code(user.username)
            token_obj = models.Token.objects.filter(user_id=user.id).first()
            if token_obj:
                token_obj.token = token
                token_obj.save()
            else:
                models.Token.objects.create(user_id=user.id, token=token)
            res['user'] = user.username
            res['alert'] = False
            res['token'] = token

        return Response(res)
