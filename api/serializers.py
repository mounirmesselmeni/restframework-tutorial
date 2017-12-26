import datetime
from rest_framework import serializers

from courses.models import Teacher, Student, Course


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'id',
            'name',
            'speciality',
        ]


class StudentSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        today = datetime.date.today()
        return (
            today.year - obj.birth_date.year - ((today.month, today.day) < (obj.birth_date.month,
                                                                            obj.birth_date.day))
        )
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'birth_date',
            'current_level',
            'age',
        ]


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'teacher',
            'level',
            'students',
        ]
