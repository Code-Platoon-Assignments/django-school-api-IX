from django.shortcuts import render, get_object_or_404
from .serializers import Subject, SubjectSerializer, SubjectOnlySerializer
from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.response import Response

# Create your views here.

class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects.data)
    
    def post(self, request):
        new_subject = SubjectOnlySerializer(data=request.data)
        if new_subject.is_valid():
            new_subject.save()
            return Response(new_subject.data, status=HTTP_201_CREATED)
        return Response(new_subject.errors, status=HTTP_400_BAD_REQUEST)
    
class A_subject(APIView):

    def get_a_subject(self, subject):
        return get_object_or_404(Subject, subject_name = subject.title())
    
    def get(self, request, subject):
        return Response(SubjectSerializer(self.get_a_subject(subject)).data)
    
    def put(self, request, subject):
        subject = self.get_a_subject(subject)
        updated_subject = SubjectSerializer(subject, data=request.data, partial=True)
        if updated_subject.is_valid():
            updated_subject.save()
            return Response(updated_subject.data)
        return Response(updated_subject.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, subject):
        subject = self.get_a_subject(subject)
        subject.delete()
        return Response(status=HTTP_204_NO_CONTENT)
        
