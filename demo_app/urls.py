from django.urls import path
from . import views

urlpatterns = [
    path('sample_msg/', views.sample_msg, name='sample_msg'),
    path('index/', views.new_page, name='indx'),
]
