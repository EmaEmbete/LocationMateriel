from django.contrib import admin
from django.urls import path
from app.views import home




urlpatterns = [
    path('',home.index, name='home'),


    path('clients/',clients.index, name='clients_index'),
    path('clients/create',clients.create, name='clients_create'),
    path('clients/store', clients.store, name='clients_store'),
    path('clients/edit/<int:id>', clients.edit, name='clients_edit'),
    path('clients/delete/<int:id>',clients.delete, name='clients_delete'),




]