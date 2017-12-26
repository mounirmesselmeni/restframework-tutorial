from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from . import serializers
from . import filters
from courses import models as courses_models


class TeacherViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = courses_models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    filter_class = filters.TeacherFilter


class StudentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = courses_models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_class = filters.StudentFilter


class CourseViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = courses_models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
