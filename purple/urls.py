from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls', namespace='api')),
    path('ordered/', MakeOrder)
    # path(r'^', NextAppView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)