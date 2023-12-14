from django.contrib import admin
from django.urls import path, include
from polesapp import views


app_name = 'polesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.details, name='details'),
    path("<int:question_id>/results/", views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
