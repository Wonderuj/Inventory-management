from django.urls import path,include
from api.views import inventoryView 
from rest_framework.routers import DefaultRouter

routes=DefaultRouter()
routes.register("", inventoryView, basename='inventoryView')
urlpatterns = [
    path("", include(routes.urls))
]
