from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('api/schedule/', include('schedule_app.urls')),
    path('api/teachers/', include('teachers_app.urls')),   # ← ДОЛЖНО БЫТЬ!
    path('api/events/', include('events_app.urls')),
]
