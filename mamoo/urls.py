from django.urls import include, path
from rest_framework import routers
from .views import MamooList

router = routers.DefaultRouter()

router.register('mamoo', MamooList)

urlpatterns = [
    path('', include(router.urls))
]
