"""
URL configuration for first_project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from first_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstpage/',views.firstpage),
    path('webpage/',views.webpage),
    path('colorpicker/',views.colorpicker),
    path('calculator/',views.calculator),
    path('clock/' ,views.clock),
    path('tool/',views.tool) ,
    path('slides/' , views.slides) ,
    path('slides/rgb/',views.rgb),
    path('slides/rgba/' , views.rgba) ,
    ]
