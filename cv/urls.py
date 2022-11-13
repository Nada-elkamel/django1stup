from django.urls import path
from .import views

urlpatterns =[
    path('',views.index,name='index'),
    path('competence',views.index1,name='index1'),
    path('diplome-formation',views.index2),
    path('experience-stage',views.index3),
      
      
]