from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.student, ),
    path('vw/', views.view_details, ),
    path('delt(?P<pk>)\w+',views.delete_row,name='delt1'),
    path('updt(?P<pk>)\w+',views.update_row,name='updt1')

   
]
