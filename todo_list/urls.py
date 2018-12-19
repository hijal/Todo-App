from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('delete/<list_id>', views.delete, name = 'delete'),
    path('cross_line/<list_id>', views.cross_line, name = 'cross_line'),
    path('uncross_line/<list_id>', views.uncross_line, name = 'uncross_line'),
    path('edit/<list_id>/', views.edit, name = 'edit'),
]