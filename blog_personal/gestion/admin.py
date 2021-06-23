from django.contrib import admin
from .models import LibroModel, UsuarioModel, PrestamoModel


class LibroAdmin(admin.ModelAdmin):
    #modifica la vista del modelo
    list_display = ['libroNombre','libroAutor','libroCantidad']
    #agrega un buscador al modelo, y ademas hay que indicar a que columnas se realizara la busqueda cuando se tenga una 
    search_fields =['libroNombre','libroEdicion']
    #Agrega campo de busqueda rapida para listar una busqueda mas generica, se recomienda utilizar campos en los cuales no contengan muchos valores
    list_filter =['libroAutor'] 
    #indica si se desea ver algun campo que el ususario no puede manipular (solo lectura)
    #los campos de solo lectura, se coloran al final , despues de los campos de escritura
    readonly_fields = ['libroId']


class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['usuario','libro']


admin.site.register(LibroModel,LibroAdmin)
admin.site.register(UsuarioModel)
admin.site.register(PrestamoModel,PrestamoAdmin)
