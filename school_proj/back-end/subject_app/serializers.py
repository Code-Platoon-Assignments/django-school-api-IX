from .models import Subject
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    grade_average = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ["subject_name", "professor", "students", "grade_average"]

    def get_students(self, obj):
        if obj.students:
            return obj.students.count()
        return 0
    
    def get_grade_average(self, obj):
        grades = obj.grades.all()
        if len(grades):
            return round(sum([x.grade for x in grades])/len(grades),2)
        return 0
    
class SubjectOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

