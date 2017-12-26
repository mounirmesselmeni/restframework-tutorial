from django.conf.urls import url, include
from rest_framework_extensions.routers import ExtendedDefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = ExtendedDefaultRouter()
router.register(r'teachers', views.TeacherViewSet).register(
    r'courses', views.CourseViewSet, base_name='courses', parents_query_lookups=['teacher'],
)
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token),
]
