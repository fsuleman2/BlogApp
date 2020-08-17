from django.urls import path
from .views import PostAPIVIEW,PostAPIDetailView

urlpatterns=[
    path('',PostAPIDetailView.as_view(),name='api_detail'),
    path('<int:pk>',PostAPIVIEW.as_view(),name='list')
]