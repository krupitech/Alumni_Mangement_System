
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import alumni_views, views, Hod_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name ='base'),

    #Login Path
    path('login/', views.LOGIN, name ='login'),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

