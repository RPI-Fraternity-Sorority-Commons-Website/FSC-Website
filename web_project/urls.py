"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from IFC import views  # Import your views from the IFC app

urlpatterns = [
    path("", include("IFC.urls")),
    path('admin/', admin.site.urls),
    path('create-accounts/', views.create_user_accounts, name='create_accounts'),  # Add this line to link the create accounts view
    # Lines below are used to create a login/logout page for NORMAL USERS
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Default login view
    #path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),  # Logout view"""
]