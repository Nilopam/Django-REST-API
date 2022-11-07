from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    
    path('emp/',views.EmpListView.as_view()),
    path('emp/<int:pk>',views.EmpDetailsView.as_view()),
    path('project/',views.EmpProjectListView.as_view()),
    path('project/<int:pk>',views.EmpProjectDetailsView.as_view()),
    
]