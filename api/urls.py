from django.urls import path
from .routers import router
app_name = 'api'


urlpatterns = [
]

urlpatterns += router.urls