from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()

router.register(r'vitrin', VitrinApi)
router.register(r'marsipan', MarsipanApi)
router.register(r'flower', FlowerApi)
router.register(r'xonca', XoncaApi)
router.register(r'cafe', CafeApi)
router.register(r'contact', ContactApi)
router.register(r'homepageproductcount', HomePageProductCountApi)
router.register(r'homepageproduct', HomePageProductApi, basename='HomePageProduct')
# router.register(r'payment', Payment, basename='payment')