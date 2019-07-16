from django.urls import path,include
from .views import StudentViewSet
from rest_framework import routers
from .views import TeacherViewSet
from .views import CourseViewSet
router=routers.DefaultRouter()
router.register("students",StudentViewSet)
router.register("teachers",TeacherViewSet)
router.register("courses",CourseViewSet)

urlpatterns=[
path("",include(router.urls)),
]

urlpatterns=[
path("",include(router.urls)),
]


urlpatterns=[
path("",include(router.urls)),
]