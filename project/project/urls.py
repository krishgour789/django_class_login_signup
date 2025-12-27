"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landingpage',views.landingpage,name='landingpage'),
    path('',views.register,name='register'),
    path('registerdata',views.registerdata,name='registerdata'),
    path('login',views.login,name='login'),
    path('logindata',views.logindata,name='logindata'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dynamic_url/<str:name>/<int:age>/<slug:qual>',views.dynamic_url),
    path('dashboard/query/<int:pk>/', views.query, name='query'),
    path('query_data/<int:pk>/', views.query_data, name='query_data'),
    path('dashboard/show_query/<int:pk>/', views.show_query, name='show_query'),
    path('dashboard/query/delete/<int:pk>/', views.delete, name='delete'),
    path('dashboard/query/edit/<int:pk>/', views.edit, name='edit'),
    path('dashboard/query/updatedata/<int:pk>/', views.updatedata, name='updatedata'),
    path('forgetpassword', views.forgetpassword, name='forgetpassword'),
    path('forgetdata', views.forgetdata, name='forgetdata'),
    path('resetpassword', views.resetpassword, name='resetpassword'),
    path('resetdata', views.resetdata, name='resetdata'),

    
   
]
