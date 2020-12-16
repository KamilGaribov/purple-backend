from django.urls import path
from .routers import router
from .views import Test
app_name = 'api'


urlpatterns = [
    path('test/', Test.as_view(), name='test')
]

urlpatterns += router.urls