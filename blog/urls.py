
from django.contrib import admin
from django.urls import path
from . import views
from .views import HomePageView , PostDetailView


urlpatterns = [
    path('admin/',admin.site.urls),
    #path('',view.index,name='index')
    path('', HomePageView.as_view(),name='home'),
    path('about/',views.AboutPageView,name='about'),
    path('contact/',views.ContactPageView,name='contact'),
    path('<slug:slug>/',PostDetailView.as_view(),name='post_detail'),

]