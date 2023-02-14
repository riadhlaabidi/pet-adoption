from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PetList, PetDetail

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', PetList.as_view(), name='pet-list'),
    path('<int:pk>/', PetDetail.as_view(), name='pet-detail'),
])
