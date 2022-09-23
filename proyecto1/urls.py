"""proyecto1 URL Configuration

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
from Citas.views import crearCita, formularioCita, listarCita, editarCita, editarCliente, actualizarCita, actualizarCliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crearCita/',crearCita),
    path('formularioCita/',formularioCita, name='formularioCita'),
    path('listarCita/',listarCita, name='listarCita'),
    path('editarCita/<int:id>',editarCita, name='editarCita'),
     path('editarCliente/<int:id>',editarCliente, name='editarCliente'),
    path('actualizarCita/<int:id>',actualizarCita, name='actualizarCita'),
     path('actualizarCliente/<int:id>',actualizarCliente, name='actualizarCliente'),

]
