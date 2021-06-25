from django import db
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import BooleanField
from .authManager import UsuarioManager

class PlatoModel(models.Model):
    platoId = models.AutoField(
        primary_key=True,
        null=False,
        db_column='id',
        unique=True
    )
    platoNombre = models.CharField(
        max_length=45,
        null=False,
        db_column='nombre',
        unique=True
    )
    platoPrecio = models.DecimalField(
        db_column='precio',
        null=False,
        max_digits=5,
        decimal_places=2
    )

    platoFoto = models.ImageField(
        upload_to ='platos/',
        db_column='foto',
        null=True
    )
    platoCantidad = models.IntegerField(
        db_column='cantidad',
        default=0,
    )
    updateAt = models.DateTimeField(
        auto_now=True,
        db_column='updated_at'
    )
    class Meta: 
        db_table ='platos'
        ordering = ['platoNombre']

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    """ Modificar el modelo auth_user de la base de datos"""

    TIPO_PERSONAL = [
        (1,'ADMINISTRADOR'),
        (2,'CAJERO'),
        (3,'MOZO')
    ]

    usuarioId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='id'
    )

    usuarioNombre = models.CharField(
        max_length=20,
        null=False,
        db_column='nombre',
        verbose_name='Nombre del usuario'
    )

    usuarioApellido = models.CharField(
        max_length=20,
        null=False,
        db_column='apellido',
        verbose_name='Apellido del usuario'
    )

    usuarioCorreo = models.EmailField(
        db_column='correo',
        null=False,
        unique=True,
        verbose_name='Correo del usuario'
    )
    usuarioTipo = models.IntegerField(
        choices = TIPO_PERSONAL,
        db_column='tipo',
        verbose_name='Tipo del usuario'
    )
    
    usuarioTelefono = models.CharField(
        max_length=10,
        db_column='telefono'
    )

    password = models.TextField()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UsuarioManager()
    #aHORA DEFINO QUE COLUMNA SERA LA ENCARGADA DE VALIDAR QUE EL USUARIO SEA UNICO
    USERNAME_FIELD = 'usuarioCorreo'

    REQUIRED_FIELDS = ['usuarioNombre', 'usuarioApellido','usuarioTipo']

    updateAt = models.DateTimeField(
        auto_now=True,
        db_column='updated_at'
    )

    class Meta:
        db_table = 'usuarios'

class MesaModel(models.Model):
    mesaId = models.AutoField(
        primary_key=True,
        unique = True,
        null = False,
        db_column='id',
    )

    mesaDescripcion = models.CharField(
        max_length=10,
        null = False,
        db_column='descripcion',
    )

    mesaCapaciodad = models.IntegerField(
        db_column='capacidad',
        null = False
    )
    
    updateAt = models.DateTimeField(
        auto_now=True,
        db_column='updated_at'
    )

    class Meta:
        db_table = 'mesas'

class PedidoModel(models.Model):
    pedidoId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='id'
    )        

    pedidoFecha = models.DateTimeField(
        auto_now=True,
        db_column='fecha'
    )
    pedidoTotal = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        db_column='total'
    )

    pedidoNombreCliente = models.CharField(
        max_length=45,
        db_column='nombre_cliente'
    )

    pedidoDocumentoCliente = models.CharField(
        max_length=12,
        db_column='documento_cliente',
    )

    usuario = models.ForeignKey(
        to=UsuarioModel,
        on_delete=models.PROTECT,
        related_name='usuarioPedidos',
        db_column='usuario_Id'
    )

    mesa = models.ForeignKey(
        to=MesaModel,
        on_delete=models.PROTECT,
        related_name='mesaPedidos',
        db_column='mesa_Id'
    )
    class Meta:
        db_table = 'pedidos'
        ordering = ['-pedidoFecha'] 

class DetalleModel(models.Model):
    detalleId = models.AutoField(
        primary_key=True,
        db_column='id',
        unique=True,
        null=False
    )

    detalleCantidad = models.IntegerField(
        db_column='cantidad',
        null=False,
    )

    detalleSubTotal = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        db_column='sub_total'
    )

    pedido = models.ForeignKey(
        to=PedidoModel,
        db_column='pedido_id',
        on_delete=models.PROTECT,
        related_name='pedidoDetalles'
    )

    plato = models.ForeignKey(
        to=PlatoModel,
        db_column='plato_id',
        on_delete=models.PROTECT,
        related_name='platoDetalles'
    )
    class Meta:
        db_table = 'detalles'