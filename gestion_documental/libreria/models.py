from django.db import models
from .choices import OPCIONES_MESES

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripcion", null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion 
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


# Create your models here.
class Tdocumento(models.Model):
    id = models.AutoField(primary_key = True)
    tipo_documento = models.CharField(max_length=100, verbose_name="tipo_documento")

    def __str__(self):
        fila = "tipo documento: " + self.tipo_documento
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()



class unidadCIP(models.Model):
    id = models.AutoField(primary_key = True)
    unidad_cip = models.CharField(max_length=100, verbose_name="unidad_cip")

    def __str__(self):
        fila = "Unidad CIP: " + self.unidad_cip
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

#---------------------------------

class Cargo(models.Model):
    id = models.AutoField(primary_key = True)
    cargo = models.CharField(max_length=45, verbose_name="cargo")

    def __str__(self):
        fila = "cargo: " + self.cargo 
        return fila

class Login(models.Model):
    id = models.AutoField(primary_key = True)
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="Cargo", verbose_name="Cargo")
    contraseña = models.CharField(max_length=45, verbose_name="contraseña")

    def __str__(self):
        fila = "Cargo: " + str(self.tipo_cargo) + " - " + "Contraseña: " + self.contraseña 
        return fila



class personal(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length=45, verbose_name="Nombre")
    apellidos = models.CharField(max_length=45, verbose_name="Apellidos")
    Correo = models.EmailField(max_length=45, verbose_name="Correo")
    DNI = models.CharField(max_length=8, verbose_name="DNI")
    Telefono = models.IntegerField(verbose_name="Telefono")
    codigo_uca = models.IntegerField(verbose_name="Codigo_UCA")
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="Personal", verbose_name="Cargo")
    unidad_cip = models.ForeignKey(unidadCIP, on_delete=models.CASCADE, related_name="unidadCIP", verbose_name="unidadCIP")

    def __str__(self):
        fila = "Nombres: " + self.nombres + " - " + "Cargo: " + str(self.tipo_cargo) + " - " + "unidad_cip: " + str(self.unidad_cip)
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


class usuario(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField(max_length=45, verbose_name="Nombre")
    apellidos = models.CharField(max_length=45, verbose_name="Apellidos")
    Correo = models.EmailField(max_length=45, verbose_name="Correo")
    DNI = models.CharField(max_length=8, verbose_name="DNI")
    Telefono = models.IntegerField(verbose_name="Telefono")
    codigo_uca = models.IntegerField(verbose_name="Codigo_UCA")
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="Usuarios", verbose_name="Cargo")


    def __str__(self):
        fila = "Nombres: " + self.nombres + " - " + "Cargo: " + str(self.tipo_cargo)
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()



#tablas de documentos

class Documento(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    numero = models.CharField(max_length=50, verbose_name="Numero")
    personal_procedencia = models.CharField(max_length=50, verbose_name="Personal/Procedencia")
    archivo = models.FileField(upload_to='documentos/', verbose_name="Documento", null=True)
    descripcion = models.TextField(verbose_name="Descripcion", null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion 
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.archivo.storage.delete(self.archivo.name)
        super().delete()

class Rfecha(models.Model):
    id = models.AutoField(primary_key = True)
    fecha = models.CharField(max_length=100, verbose_name="fecha")

    def __str__(self):
        fila = "fecha: " + self.fecha
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class dcomision(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.TextField(verbose_name="Descripcion", default=None)
    tipo_documento = models.ForeignKey(Tdocumento, on_delete=models.CASCADE, related_name="Documentos", verbose_name="Tipo de documento", default=None)
    numero = models.CharField(max_length=50, verbose_name="Numero", default=None)
    procedencia = models.ForeignKey(unidadCIP, on_delete=models.CASCADE, related_name="pro_comision", verbose_name="procedencia", default=None,  blank=True, null=True)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE, related_name="per_comision", verbose_name="personal", default=None,  blank=True, null=True)
    fecha = models.DateField(default=None, verbose_name="Fecha de Recepcion")
    mes = models.CharField(max_length=20, choices=OPCIONES_MESES, default=1, verbose_name="Mes Correspondiente")
    archivo = models.FileField(upload_to='documentos/', verbose_name="Documento", default=None)
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="com_usuarios", verbose_name="Cargo", default=None, blank=True, null=True)
    registrado = models.BooleanField(default=False, verbose_name="¿Registrado?")


    def __str__(self):
        fila = "Descripcion: " + self.descripcion + " - " + "tipo: " + str(self.tipo_documento)
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.archivo.storage.delete(self.archivo.name)
        super().delete()


class djustificaciones(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.TextField(verbose_name="Descripcion", default=None)
    tipo_documento = models.ForeignKey(Tdocumento, on_delete=models.CASCADE, related_name="jus_documentos", verbose_name="Tipo de documento", default=None)
    numero = models.CharField(max_length=50, verbose_name="Numero", default=None)
    procedencia = models.ForeignKey(unidadCIP, on_delete=models.CASCADE, related_name="jus_procedencia", verbose_name="procedencia", default=None,  blank=True, null=True)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE, related_name="jus_personal", verbose_name="personal", default=None,  blank=True, null=True)
    fecha = models.DateField(default=None, verbose_name="Fecha de Recepcion")
    mes = models.CharField(max_length=20, choices=OPCIONES_MESES, default=1, verbose_name="Mes Correspondiente")
    archivo = models.FileField(upload_to='documentos/', verbose_name="Documento", default=None)
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="jus_usuarios", verbose_name="Cargo", default=None, blank=True, null=True)
    registrado = models.BooleanField(default=False, verbose_name="¿Registrado?")


    def __str__(self):
        fila = "Descripcion: " + self.descripcion + " - " + "tipo: " + str(self.tipo_documento)
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.archivo.storage.delete(self.archivo.name)
        super().delete()


class dinformes(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.TextField(verbose_name="Descripcion", default=None)
    tipo_documento = models.ForeignKey(Tdocumento, on_delete=models.CASCADE, related_name="inf_documentos", verbose_name="Tipo de documento", default=None)
    numero = models.CharField(max_length=50, verbose_name="Numero", default=None)
    procedencia = models.ForeignKey(unidadCIP, on_delete=models.CASCADE, related_name="inf_procedencia", verbose_name="procedencia", default=None,  blank=True, null=True)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE, related_name="inf_personal", verbose_name="personal", default=None,  blank=True, null=True)
    fecha = models.DateField(default=None, verbose_name="Fecha de Recepcion")
    mes = models.CharField(max_length=20, choices=OPCIONES_MESES, default=1, verbose_name="Mes Correspondiente")
    archivo = models.FileField(upload_to='documentos/', verbose_name="Documento", default=None)
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="inf_usuarios", verbose_name="Cargo", default=None, blank=True, null=True)
    registrado = models.BooleanField(default=False, verbose_name="¿Registrado?")


    def __str__(self):
        fila = "Descripcion: " + self.descripcion + " - " + "tipo: " + str(self.tipo_documento)
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.archivo.storage.delete(self.archivo.name)
        super().delete()


class dvacacionesPEND(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.TextField(verbose_name="Descripcion", default=None)
    tipo_documento = models.ForeignKey(Tdocumento, on_delete=models.CASCADE, related_name="pend_documentos", verbose_name="Tipo de documento", default=None)
    numero = models.CharField(max_length=50, verbose_name="Numero", default=None)
    procedencia = models.ForeignKey(unidadCIP, on_delete=models.CASCADE, related_name="pend_procedencia", verbose_name="procedencia", default=None,  blank=True, null=True)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE, related_name="pend_personal", verbose_name="personal", default=None,  blank=True, null=True)
    fecha = models.DateField(default=None, verbose_name="Fecha de Recepcion")
    mes = models.CharField(max_length=20, choices=OPCIONES_MESES, default=1, verbose_name="Mes Correspondiente")
    archivo = models.FileField(upload_to='documentos/', verbose_name="Documento", default=None)
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="pend_usuarios", verbose_name="Cargo", default=None, blank=True, null=True)
    registrado = models.BooleanField(default=False, verbose_name="¿Registrado?")


    def __str__(self):
        fila = "Descripcion: " + self.descripcion + " - " + "tipo: " + str(self.tipo_documento)
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.archivo.storage.delete(self.archivo.name)
        super().delete()


class dvacacionesPROX(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.TextField(verbose_name="Descripcion", default=None)
    tipo_documento = models.ForeignKey(Tdocumento, on_delete=models.CASCADE, related_name="prox_documentos", verbose_name="Tipo de documento", default=None)
    numero = models.CharField(max_length=50, verbose_name="Numero", default=None)
    procedencia = models.ForeignKey(unidadCIP, on_delete=models.CASCADE, related_name="prox_procedencia", verbose_name="procedencia", default=None,  blank=True, null=True)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE, related_name="prox_personal", verbose_name="personal", default=None,  blank=True, null=True)
    fecha = models.DateField(default=None, verbose_name="Fecha de Recepcion")
    mes = models.CharField(max_length=20, choices=OPCIONES_MESES, default=1, verbose_name="Mes Correspondiente")
    archivo = models.FileField(upload_to='documentos/', verbose_name="Documento", default=None)
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="prox_usuarios", verbose_name="Cargo", default=None, blank=True, null=True)
    registrado = models.BooleanField(default=False, verbose_name="¿Registrado?")


    def __str__(self):
        fila = "Descripcion: " + self.descripcion + " - " + "tipo: " + str(self.tipo_documento)
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.archivo.storage.delete(self.archivo.name)
        super().delete()


class dlicenciasREM(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.TextField(verbose_name="Descripcion", default=None)
    tipo_documento = models.ForeignKey(Tdocumento, on_delete=models.CASCADE, related_name="rem_documentos", verbose_name="Tipo de documento", default=None)
    numero = models.CharField(max_length=50, verbose_name="Numero", default=None)
    procedencia = models.ForeignKey(unidadCIP, on_delete=models.CASCADE, related_name="rem_procedencia", verbose_name="procedencia", default=None,  blank=True, null=True)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE, related_name="rem_personal", verbose_name="personal", default=None,  blank=True, null=True)
    fecha = models.DateField(default=None, verbose_name="Fecha de Recepcion")
    mes = models.CharField(max_length=20, choices=OPCIONES_MESES, default=1, verbose_name="Mes Correspondiente")
    archivo = models.FileField(upload_to='documentos/', verbose_name="Documento", default=None)
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="rem_usuarios", verbose_name="Cargo", default=None, blank=True, null=True)
    registrado = models.BooleanField(default=False, verbose_name="¿Registrado?")


    def __str__(self):
        fila = "Descripcion: " + self.descripcion + " - " + "tipo: " + str(self.tipo_documento)
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.archivo.storage.delete(self.archivo.name)
        super().delete()


class dlicenciasSINREM(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.TextField(verbose_name="Descripcion", default=None)
    tipo_documento = models.ForeignKey(Tdocumento, on_delete=models.CASCADE, related_name="sinr_documentos", verbose_name="Tipo de documento", default=None)
    numero = models.CharField(max_length=50, verbose_name="Numero", default=None)
    procedencia = models.ForeignKey(unidadCIP, on_delete=models.CASCADE, related_name="sinr_procedencia", verbose_name="procedencia", default=None,  blank=True, null=True)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE, related_name="sinr_personal", verbose_name="personal", default=None,  blank=True, null=True)
    fecha = models.DateField(default=None, verbose_name="Fecha de Recepcion")
    mes = models.CharField(max_length=20, choices=OPCIONES_MESES, default=1, verbose_name="Mes Correspondiente")
    archivo = models.FileField(upload_to='documentos/', verbose_name="Documento", default=None)
    tipo_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name="sinr_usuarios", verbose_name="Cargo", default=None, blank=True, null=True)
    registrado = models.BooleanField(default=False, verbose_name="¿Registrado?")


    def __str__(self):
        fila = "Descripcion: " + self.descripcion + " - " + "tipo: " + str(self.tipo_documento)
        return fila
    
    def delete(self, using=None, Keep_parents=False):
        self.archivo.storage.delete(self.archivo.name)
        super().delete()
