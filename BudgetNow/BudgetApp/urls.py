from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('edit_expense/', views.edit_expense, name='edit_expense'),
    path('delete_expense/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('view_expenses/<int:pk>/', views.view_expenses, name='view_expenses'),
    path('search_expenses/', views.search_expenses, name='search_expenses'),
    
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
    path('view_category/<int:pk>/', views.view_category, name='view_category'),
    

    path('insert_budget/', views.insert_budget, name='insert_budget'),
    path('update_budget/<int:pk>/', views.update_budget, name = 'update_budget'),
    path('check_budget/<int:pk>/', views.check_budget, name='check_budget'),
    
]
