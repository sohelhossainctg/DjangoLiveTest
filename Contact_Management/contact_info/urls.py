from django.urls import path
from . import views

urlpatterns = [
    path('add_contact/', views.add_contact, name='add_contact'), 
    path('edit_contact/', views.home, name='edit_contact'), 
    path('update_contact/<int:id>/', views.update_contact, name='update_contact'), 
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'), 
    path('view_profile/<int:id>/', views.view_profile, name='view_profile'), 
]