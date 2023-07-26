from django.contrib import admin
from .models import Libro, Cargo, Login, Documento, dcomision, djustificaciones, dinformes, dvacacionesPEND, dvacacionesPROX, dlicenciasREM, dlicenciasSINREM, personal, usuario, unidadCIP, Tdocumento

# Register your models here.
admin.site.register(Libro)
admin.site.register(Cargo)
admin.site.register(Login)
admin.site.register(Documento)


admin.site.register(dcomision)
admin.site.register(djustificaciones)
admin.site.register(dinformes)
admin.site.register(dvacacionesPEND)
admin.site.register(dvacacionesPROX)
admin.site.register(dlicenciasREM)
admin.site.register(dlicenciasSINREM)

admin.site.register(personal)
admin.site.register(usuario)
admin.site.register(unidadCIP)
admin.site.register(Tdocumento)