from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views
from .views import SeatsViewSet

router = DefaultRouter()
router.register(r'seats', SeatsViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]

