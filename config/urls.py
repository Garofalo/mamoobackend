from django.urls import include, path
from rest_framework import routers
from mamoo.views import MamooList, UserList, current_user
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()

router.register('mamoo', MamooList)
# router.register('profile', ProfileList)
# router.register('user', UserList)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('token-auth/', TokenObtainPairView.as_view()),
    # path('refresh-token/', TokenRefreshView.as_view()),
    path('user/', UserList.as_view()),
    path('current_user/', current_user),
    path('token-auth/', obtain_jwt_token)
]
