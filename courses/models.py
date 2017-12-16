from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=250)
    speciality = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=250)
    birth_date = models.DateField()
    current_level = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=250)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    level = models.PositiveIntegerField()
    students = models.ManyToManyField(Student)
    required_hours = models.PositiveIntegerField()

    def __str__(self):
        return '{} {}'.format(self.name, self.teacher)
