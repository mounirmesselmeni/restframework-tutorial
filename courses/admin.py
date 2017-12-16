from django.contrib import admin

from . import models


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'speciality',
    ]
    search_fields = ['name']


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'birth_date',
        'current_level',
    ]
    search_fields = ['name']


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'teacher',
        'level',
        'required_hours',
    ]
    search_fields = ['name', 'teacher__name']
    list_filter = ['teacher', 'level']
