from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from .models import Student
from .serializers import StudentAllSerializer, StudentSerializer
from grade_app.serializers import GradeSerializer

# Create your views here.


class All_students(APIView):
    def get(self, request):
        students = Student.objects.all()
        serialized_students = StudentAllSerializer(students, many=True)
        return Response(serialized_students.data)
    
    def post(self, request):
        new_student = StudentAllSerializer(data=request.data)
        if new_student.is_valid():
            new_student.save()
            return Response(new_student.data, status=HTTP_201_CREATED)
        return Response(new_student.errors, status=HTTP_400_BAD_REQUEST)



class A_student(APIView):
    def get_a_student(self, id):
        return get_object_or_404(Student, id=id)

    def get(self, request, id):
        return Response(StudentAllSerializer(self.get_a_student(id)).data)

    def put(self, request, id):
        student = self.get_a_student(id)
        updated_student = StudentAllSerializer(student, data=request.data, partial=True)
        if updated_student.is_valid():
            updated_student.save()
            return Response(updated_student.data)
        return Response(updated_student.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_a_student(id)
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
class A_student_grades(APIView):
    def get_a_students_grades(self, id):
        return get_object_or_404(Student, id=id).grades.all()
    
    def get(self,request, id):
        return Response(GradeSerializer(self.get_a_students_grades(id), many=True).data)
    

    
class A_student_grade(APIView):
    def get_a_students_grade(self, id, grade_id):
        return get_object_or_404(Student, id=id).grades.get(id = grade_id)
    
    def get(self,request, id, grade_id):
        return Response(GradeSerializer(self.get_a_students_grade(id, grade_id)).data)
    
    def put(self, request, id, grade_id):
        grade = self.get_a_students_grade(id, grade_id)
        updated_grade = GradeSerializer(grade, data=request.data, partial = True)
        if updated_grade.is_valid():
            updated_grade.save()
            return Response(updated_grade.data)
        return Response(updated_grade.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, grade_id):
        grade = self.get_a_students_grade(id, grade_id)
        grade.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    


