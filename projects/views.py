from django.shortcuts import render

# 데이터 처리
from projects.models import Project
from projects.serializers import ProjectSerializer

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# 프로젝트 목록을 보여주는 역할
class ProjectList(APIView):
    # 프로젝트 list를 보여줄 때 (GET)
    def get(self, request):
        projects = Project.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    # 새로운 프로젝트를 작성할 때 (POST)
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(): # 유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 프로젝트 detail을 보여주는 역할
class ProjectDetail(APIView):
    # Project 객체 가져오기
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
    
    # Project detail 보기 (GET)
    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    # Project 수정하기 (PUT)
    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Project 삭제하기 (DELETE)
    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      
    