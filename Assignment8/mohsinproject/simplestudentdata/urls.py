from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentDataViewSet

router = DefaultRouter()
router.register(r'student', StudentDataViewSet, basename = 'student')

urlpatterns = [
    path('', include(router.urls)),
]