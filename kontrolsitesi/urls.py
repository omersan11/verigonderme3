"""
URL configuration for kontrolsitesi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from wifimodule import views  # wifimodule uygulamasındaki views dosyasını çağırıyoruz
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Formu gösterecek ana sayfa
    path('get_text/', views.get_text, name='get_text'),  # ESP'nin veri alacağı yol

    path('uzaklik_olcumu/', views.uzaklik_olcumu, name='uzaklik_olcumu'),
    path('add_distance_data/', views.add_distance_data, name='add_distance_data'),

    path('sicaklik_olcumu/', views.sicaklik_olcumu, name='sicaklik_olcumu'),
    path('add_temperature_data/', views.add_temperature_data, name='add_temperature_data'),
    path('nem_olcumu/', views.nem_olcumu, name='nem_olcumu'),
    path('add_humidity_data/', views.add_humidity_data, name='add_humidity_data'),


]