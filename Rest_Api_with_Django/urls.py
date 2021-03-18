

from django.contrib import admin
from django.urls import path,include
from rest_api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_app/',include('rest_api.urls'))
]
