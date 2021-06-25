from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (PlatosController, ArchivosController)


urlpatterns = [
    path('platos',PlatosController.as_view()),
    path('subirImagen', ArchivosController.as_view())
]
