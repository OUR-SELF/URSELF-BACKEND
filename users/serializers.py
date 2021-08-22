from users.models import Consumer_Users
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  # 메타 클래스로 클래스를 만들 수 있다
  class Meta:
    model = Consumer_Users
    fields = ['id', 'name', 'profile_img']