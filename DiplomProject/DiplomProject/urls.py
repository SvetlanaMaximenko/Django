"""
URL configuration for DiplomProject project.

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
from django.contrib import admin
from django.urls import path, include

from DiplomProject import settings
from user import user_views
from events import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_views.UserLogin.as_view(), name="login"),
    path('logout/', user_views.UserLogout.as_view(), name="logout"),
    path('', views.EventList.as_view(), name="home"),
    path('accounts/', include("user.urls")),
    path('login/registration', user_views.UserReg.as_view(), name="registration"),
    path('my_events/', views.EventMyList.as_view(), name="my_events"),
    path('photo_album/', views.FotoAlbum.as_view(), name="album"),
    path('my_events/<int:event_id>/', views.FotoVisit.as_view(), name="foto_visit"),
    path('event/', include("events.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
