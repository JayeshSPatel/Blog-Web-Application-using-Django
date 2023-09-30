from django.http import HttpResponse
from django.urls import path
from .views import homeapp,roomapp,createroom,deleteroom,updateroom,loginUser,logoutUser,registerUser

urlpatterns = [
    path('loginuser/',loginUser, name='login'),
    path('logoutuser/',logoutUser, name='logout'),
    path('registeruser/',registerUser, name='register'),
    path('',homeapp, name='home'),
    path('room_page/<str:pk>/',roomapp, name='room'),
    path('create-room/',createroom,name='create-room'),
    path('delete-room/<str:pk>/',deleteroom,name='delete-room'),
    path('update-room/<str:pk>/',updateroom,name='update-room'),
]
