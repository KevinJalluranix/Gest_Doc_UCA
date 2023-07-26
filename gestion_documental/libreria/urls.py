from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    #pagina principal
    path("", views.login, name="login"),
    path("inicio", views.inicio, name="inicio"),
    path("logout", views.logout, name="logout"),

    #pagina de documentos
    path("comision", views.comision, name="comision"),
    path("licencias", views.licencias, name="licencias"),
    path("justificaciones", views.justificaciones, name="justificaciones"),
    path("informes", views.informes, name="informes"),
    path("clasificar", views.clasificar, name="clasificar"),
    path("vacaciones", views.vacaciones, name="vacaciones"),

    #pagina de opciones
    path("libros", views.libros, name="libros"),
    path("iterador/<int:pos>", views.iterador, name="iterador"),
    path("libros/crear/<int:pos>", views.crear, name="crear"),
    path("ver_documento/<int:id>/<int:pos>", views.ver_documento, name="ver_documento"),
    path("eliminar/<int:id>/<int:pos>", views.eliminar, name="eliminar"),
    path("libros/editar/<int:id>/<int:pos>", views.editar, name="editar"),
    path("reporte", views.reporte, name="reporte"),

    #consultas
    path('obtener_datos_usuario/', views.obtener_datos_usuario, name='obtener_datos_usuario'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)