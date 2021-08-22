from projects.models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
  # 메타 클래스로 클래스를 만들 수 있다
  class Meta:
    model = Project
    fields = '__all__'
    # all로 하면 모든 필드가 serialized됨
    # fields = ['title'] 등과 같이 model의 일부만 설정할 수도 있음