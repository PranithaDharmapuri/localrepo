from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('results/', views.results, name='results'),
     path('<int:question_id>/votes/', views.votes, name='votes'),
]