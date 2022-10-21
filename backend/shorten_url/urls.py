from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from shorten_url import views

swagger_view = get_swagger_view(title='Swagger Help')

router = DefaultRouter()
router.register('shorturl', views.ShortURLViewSet, basename='shorturl')

urlpatterns = [
    path('', include(router.urls)),
    path('get-original-url/', views.get_specific_url),
    path('swagger/', swagger_view),
]
