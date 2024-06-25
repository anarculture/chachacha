import os

# Set project directory
project_dir = '/home/anarculture/code/anarculture/chachacha/hotel_pms'
os.chdir(project_dir)

# Define URL patterns content for each app
urls_content = {
    'users/urls.py': """\
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:pk>/', views.user_detail, name='user_detail'),
    path('new/', views.user_create, name='user_create'),
    path('<int:pk>/edit/', views.user_update, name='user_update'),
    path('<int:pk>/delete/', views.user_delete, name='user_delete'),
]
""",
    'reservations/urls.py': """\
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('new/', views.reservation_create, name='reservation_create'),
    path('<int:pk>/edit/', views.reservation_update, name='reservation_update'),
    path('<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
]
""",
    'billing/urls.py': """\
from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('new/', views.invoice_create, name='invoice_create'),
    path('<int:pk>/edit/', views.invoice_update, name='invoice_update'),
    path('<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),
]
""",
    'reporting/urls.py': """\
from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('<int:pk>/', views.report_detail, name='report_detail'),
    path('new/', views.report_create, name='report_create'),
    path('<int:pk>/edit/', views.report_update, name='report_update'),
    path('<int:pk>/delete/', views.report_delete, name='report_delete'),
]
"""
}

# Create directories and files for URLs
for path, content in urls_content.items():
    full_path = os.path.join(project_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)

print("URL patterns for each app have been created.")
