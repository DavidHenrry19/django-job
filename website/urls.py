from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto'),
    path('job-listing/', views.job_listing, name='job-listing'), 
    path('job-details/<int:pk>/', views.job_details, name='job-details')
]