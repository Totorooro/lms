from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, GroupViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'lessons', LessonViewSet, basename='lesson')

urlpatterns = [
    path('', include(router.urls)),
]