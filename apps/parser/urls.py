from django.urls import path, include

from rest_framework import routers

from . import views as views

router = routers.SimpleRouter()

router.register(r'all', views.AllCompanyNewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
    path('<str:path_name>/', views.CompanyNewsViewSet.as_view({'get': 'list'})),
]