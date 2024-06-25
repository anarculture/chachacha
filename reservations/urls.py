from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('new/', views.reservation_create, name='reservation_create'),
    path('<int:pk>/edit/', views.reservation_update, name='reservation_update'),
    path('<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
    path('guests/', views.guest_list, name='guest_list'),
    path('guests/<int:pk>/', views.guest_detail, name='guest_detail'),
    # Comment out the following lines if they use GuestForm
    # path('guests/new/', views.guest_create, name='guest_create'),
    # path('guests/<int:pk>/edit/', views.guest_update, name='guest_update'),
    # path('guests/<int:pk>/delete/', views.guest_delete, name='guest_delete'),
]
