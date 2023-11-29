from rest_framework import serializers
from .models import Grade
from subject_app.serializers import SubjectSerializer
from student_app.serializers import StudentAllSerializer

class GradeSerializer(serializers.ModelSerializer):
    a_subject = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()

    class Meta:
        model = Grade
        fields = ['id','grade', 'a_subject', 'student']

    def get_a_subject(self, obj):
        # Customize the representation of the related Subject
        if obj.a_subject:
            return {"id": obj.a_subject.id, "name":obj.a_subject.subject_name}
        return None

    def get_student(self, obj):
        # Customize the representation of the related Student
        if obj.student:
            return {"id":obj.student.id,"name":obj.student.name}
        return None
