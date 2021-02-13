from django.urls import path
from .routers import router
from .views import Test
app_name = 'api'


urlpatterns = [
    path('test/', Test.as_view(), name='test'),
    # path('ff/', SocialMediaApi, name='social'),
    # path('fi/', SocialMediaApi, name='social'),
    # path('tf/', SocialMediaApi, name='social'),
    # path('ti/', SocialMediaApi, name='social'),
    # path('fo/', SocialMediaApi, name='social'),
]

urlpatterns += router.urls