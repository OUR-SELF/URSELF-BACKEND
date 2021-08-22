# 데이터 처리
from users.serializers import UserSerializer
from users.models import Consumer_Users

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# user 목록 보여주는 역할
class UserList(APIView):
    # 프로젝트 list를 보여줄 때 (GET)
    def get(self, request):
        consumers = Consumer_Users.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = UserSerializer(consumers, many=True)
        return Response(serializer.data)