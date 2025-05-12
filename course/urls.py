from django.urls import path

from rest_framework import routers

from .views import (
    CourseViewset, ModuleViewset
)

app_name = 'course'
router = routers.SimpleRouter()
router.register('course',CourseViewset)
router.register('module',ModuleViewset)

urlpatterns = router.urls

