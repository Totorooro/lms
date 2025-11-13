from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('api/schedule/', include('schedule_app.urls')),
    path('api/event/', include('events_app.urls')),
    path('api/homework/', include('Homework_app.urls')),
    path('api/journal/', include('journal_app.urls')),
    path('api/teachers/', include('teachers_app.urls')),
    path('api/exams/', include('exams_app.urls')),
]
