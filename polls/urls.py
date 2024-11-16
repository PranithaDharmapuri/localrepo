from django.urls import path
from . import views

app_name="polls"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.details, name='details'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('add_question/', views.add_question, name='add_question'),
    path('<int:question_id>/delete/', views.delete_question, name='delete_question'),
    path('name_form/',views.get_name,name='name_form'),
    path('thanks/', views.thanks,name='thanks')
]