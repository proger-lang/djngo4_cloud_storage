from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appmain/', include('shop1.urls', namespace="shop1")),
  ]
