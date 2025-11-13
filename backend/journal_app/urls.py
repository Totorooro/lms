from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GradeViewSet
from .views import JournalSummaryView

router = DefaultRouter()
router.register(r'grades', GradeViewSet, basename='grade')

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', JournalSummaryView.as_view(), name='journal-summary'),
]