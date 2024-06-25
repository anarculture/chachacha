from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('<int:pk>/', views.report_detail, name='report_detail'),
    path('new/', views.report_create, name='report_create'),
    path('<int:pk>/edit/', views.report_update, name='report_update'),
    path('<int:pk>/delete/', views.report_delete, name='report_delete'),
]
