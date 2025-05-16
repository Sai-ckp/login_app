
from django.urls import path
from . import views



urlpatterns = [
   path('store/', views.store_list, name='store_list'),  # Display store
   path('store/add/', views.store_add, name='store_add'),  # Add store
   path('store/edit/<int:pk>/', views.store_edit, name='store_edit'),  # Edit store
   path('store/delete/<int:pk>/', views.store_delete, name='store_delete'),  # Delete store
     # Add this for viewing details
   path('store/view/<int:pk>/', views.store_view, name='store_view'),  # View Details   

]
