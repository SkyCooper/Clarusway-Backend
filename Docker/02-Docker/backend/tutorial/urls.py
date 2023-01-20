from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TutorialMVS
# from .views import tutorial_detail, tutorial_list

router = DefaultRouter()
router.register(r'tutorials', TutorialMVS)

urlpatterns = router.urls