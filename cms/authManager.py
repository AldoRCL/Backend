from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    """Clase que sirve para modificar el comportamiento del modelo auth_user de django"""


    def create_user(self, email, nombre, apellido, tipo, password=None):
        """Creacion de un usuario comun"""
        if not email:
            raise ValueError("El usuario debe tener obligatoriamente un correo")
        #Normalizo el correo que a parte de validar si hay un 0 o in . lo lleva a lowercase(minusculas) y quita espacios al inicio y al final si esque hubiese

        email = self.normalize_email(email)
        #Creo mi objeto de usuario PERO aun no se guarda en la bd
        nuevoUsuario = self.model(usuarioCorreo = email, usuarioNombre = nombre, usuarioApellido = apellido, usuarioTipo = tipo)

        #Ahora encripto la contrasena
        nuevoUsuario.set_password(password)
        #Guardo en la bd
        #Sirve para referencias a la bd en el caso que nossotros tengamos varias conexionesen nuestro proyecto de django
        nuevoUsuario.save(using=self._db)
        return nuevoUsuario

    def create_superuser(self,usuarioCorreo, usuarioNombre, usuarioApellido, usuarioTipo, password):
        """Creacion de un nuevo super usuario para que pueda acceder al panel administrativo y al;gunas opciones adicionales"""
        usuario = self.create_user(
            usuarioCorreo, usuarioNombre, usuarioApellido, usuarioTipo, password)
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        