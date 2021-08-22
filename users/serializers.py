from projects.models import Project
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  # 메타 클래스로 클래스를 만들 수 있다
  class Meta:
    model = Project
    fields = ['id', 'name']