"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views, hod_views, staff_views, students_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),
    path('base/', views.BASE, name='base'),
    path('doLogout',views.doLogout,name='logout'),
    path('Hod/Home', hod_views.HOME, name='hod_home'),
    path('Hod/Student/Add', hod_views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',hod_views.VIEW_STUDENT,name='view_student'),
    path('Hod/Staff/Add', hod_views.ADD_STAFF,name='add_staff'),
    path('Hod/Course/Add',hod_views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',hod_views.VIEW_COURSE,name='view_course'),
    path('Hod/send_Staff_Notification/Add', hod_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('Staff/Home', staff_views.HOME, name='staff_home'),
    path('take-attendance/', staff_views.take_attendance, name='take_attendance'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
