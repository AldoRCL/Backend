from django.urls import path
from django.urls.conf import include
#Sirve para acceder a todas las variables definidas en el archivo settings
from django.conf import settings
#Sirve para cargar un grupo de rutas estaticas
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    #path('admin/', admin.site.urls),.
    path('cms/', include('cms.urls')),
    path('login',TokenObtainPairView.as_view())
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#El metodo static retornara una lista de URLPattern y se pasa dos parametros:
#1.la url (el prefijo) con el cual se accedera a esta ruta
#2.document_root => el contenido que se renderizara cuando se llame a esa ruta
#Esto se usa para renderizar archivos del backend

