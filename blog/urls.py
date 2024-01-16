from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginViewSet, BlogViewSet

router = DefaultRouter()
router.register(r'', LoginViewSet, basename='login')
router.register(r'blogs',BlogViewSet, basename='blogs')

urlpatterns = [
    path('',include(router.urls))
]
