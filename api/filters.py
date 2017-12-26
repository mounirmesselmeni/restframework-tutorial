import datetime
from dateutil.relativedelta import relativedelta
import django_filters
from django_filters import rest_framework as filters

from courses import models 

class TeacherFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Teacher
        fields = ['name']


class StudentFilter(filters.FilterSet):
    age = django_filters.NumberFilter(method='age_filter')

    def age_filter(self, queryset, name, value):
        today = datetime.date.today()
        age = (today - relativedelta(years=value)).year
        return queryset.filter(birth_date__year=age)

    class Meta:
        model = models.Student
        fields = ['age']
