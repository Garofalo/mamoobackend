from django.urls import include, path
from rest_framework import routers
from mamoo.views import MamooList, UserList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin

router = routers.DefaultRouter()

router.register('mamoo', MamooList)
# router.register('profile', ProfileList)
router.register('user', UserList)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
]
