from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views
from .views import TicketViewSet

router = DefaultRouter()
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('purchase/', views.purchase_ticket, name='purchase_ticket'),
    path('api/', include(router.urls)),
]


