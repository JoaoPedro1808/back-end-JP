from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ContentViewSet
from . import views

router = DefaultRouter()
router.register(r'contents', ContentViewSet)

urlpatterns = router.urls + [
    path('api/sample-data/', views.sample_data, name='sample_data'),
]