from django.urls import path
from .views import All_students, A_student, A_student_grades, A_student_grade

urlpatterns = [
    path("", All_students.as_view(), name='all_students'),
    path("<int:id>/", A_student.as_view(), name="a_student"),
    path("<int:id>/grades/", A_student_grades.as_view(), name='students_grades'),
    path("<int:id>/grades/<int:grade_id>/", A_student_grade.as_view(), name="student_grade"),
    # path("<int:id>/grades/<int:grade_id>/subject/<str:subject_name>/", Create_a_grade.as_view(), name="create_grade")
]
