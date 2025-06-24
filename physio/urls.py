"""
URL configuration for physio project.

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
from exercise import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main Pages
    path('', views.login, name='login'),  # Default page
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Patient Functionalities
    path('appointments/', views.appointment_dashboard, name='appointments'),
    path('feedback/', views.submit_feedback, name='feedback'),
    path('consultation/', views.consultation_request, name='consultation_request'),

    # Admin/Doctor Functionalities
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/consultation/', views.admin_consultation, name='admin_consultation'),
    path('dashboard/appointments/', views.admin_appointments, name='admin_appointments'),
    path('dashboard/feedback/', views.admin_feedback, name='admin_feedback'),
    path('pay/', views.simulated_payment, name='simulated_payment'),
    path('chatbot/', views.chatbot_response, name='chatbot'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),


]

# Media file support (uploads)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
