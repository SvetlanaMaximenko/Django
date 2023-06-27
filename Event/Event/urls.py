"""
URL configuration for Event project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from Events.views import UserReg, Home, UserList, EventsList, EventsEdit, EventsListMy, register_user
from rest_framework import urls
from djoser import views

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class TokenPairView(TokenObtainPairView):
    pass


class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Hello, World!'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    # path('api/users/registration', UserReg.as_view(), name="reg"),
    # path('api/login', AuthToken.as_view(), name="login"),
    path('api/users/registration', register_user, name="reg"),
    path('api/users', UserList.as_view(), name="list"),
    path('api/events', EventsList.as_view(), name="list_events"),
    path('api/events/my', EventsListMy.as_view()),
    path('api/event/<int:event_id>', EventsEdit.as_view()),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/auth/', include("djoser.urls")),
    path('api/token/', TokenPairView.as_view(), name='token_obtain_pair'),
    path('api/protected/', ProtectedView.as_view(), name='protected'),
]
