"""classmates_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from tasks import views as task_views
from timetable import views as timetable_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', timetable_view.index, name="home"),  # TODO: Перенести в профильный URLs приложения
                  path('task', task_views.index, name="home"),
                  path('egg', timetable_view.easter_egg, name="EasterEgg")
                  # path('chat/<str:user>/', chatviews, name='chat'),
                  # path('', include('chat.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
