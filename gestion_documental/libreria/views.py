from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, HttpResponseRedirect, JsonResponse
from .models import Libro, Cargo, Login, Documento, dcomision, djustificaciones, dinformes, dvacacionesPEND, dvacacionesPROX, dlicenciasREM, dlicenciasSINREM, Tdocumento, personal, unidadCIP, usuario
from .forms import LibroForm, LoginForm, DocumentoForm, comisionForm, justificacionesForm, informesForm, vacacionespendForm, vacacionesproxForm, licenciasremForm, licenciassinremForm
from django.contrib import messages
from django.apps import apps
from django.urls import reverse
from datetime import timedelta

# Create your views here.

def inicio(request):

    datos = request.session.get('datos')
    user = usuario.objects.get(tipo_cargo = datos)

    datos_user = Cargo.objects.get(id=datos)

    return render(request, 'paginas/inicio.html', {'datos': datos_user, 'user':user})

def reporte(request):
    users = personal.objects.all()
    procedencia = unidadCIP.objects.all()

    return render(request, 'libros/reporte.html', {'users': users, 'procedencia':procedencia})

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all() #filter == get
    return render(request, 'libros/index.html', {'libros':libros})

def ver_documento(request, id, pos):

    if pos == 1:
        documento = dcomision.objects.get(id=id)
    if pos == 2:
        documento = djustificaciones.objects.get(id=id)
    if pos == 3:
        documento = dinformes.objects.get(id=id)
    if pos == 4:
        documento = dvacacionesPEND.objects.get(id=id)
    if pos == 5:
        documento = dvacacionesPROX.objects.get(id=id)
    if pos == 6:
        documento = dlicenciasREM.objects.get(id=id)
    if pos == 7:
        documento = dlicenciasSINREM.objects.get(id=id)

    file_path = documento.archivo.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)


def obtener_datos_usuario(request):
    selected_cargo_id = request.GET.get('selectedCargoId')
    users = usuario.objects.get(tipo_cargo=selected_cargo_id)
    
    data = {
        'nombres': users.nombres + " " + users.apellidos,
    }
    
    return JsonResponse(data)


def login(request):
    formulario = LoginForm(request.POST or None, request.FILES or None)
    cargos = Cargo.objects.all()


    if formulario.is_valid():
        username = request.POST.get('tipo_cargo')
        password = formulario.cleaned_data['contraseña']

        #obtener datos para validad
        users = Login.objects.filter(tipo_cargo=username, contraseña=password)
        
        if users:

            
            request.session['datos'] = username

            return redirect('inicio')

        else:
            messages.error(request,f'Usuario o contraseña inválido')
    
    return render(request, 'paginas/login.html', {'formulario':formulario, 'cargos':cargos})



def logout(request):
    messages.success(request,f'Saliste de la Sesión')
    return redirect('login')      


def iterador(request, pos):

    if pos == 1:
        return redirect('comision') 
    if pos == 2:
        return redirect('justificaciones') 
    if pos == 3:
        return redirect('informes')
    if pos == 4:
        url = reverse('vacaciones') + f'?op={1}'
        return HttpResponseRedirect(url)
    if pos == 5:
        url = reverse('vacaciones') + f'?op={2}'
        return HttpResponseRedirect(url)
    if pos == 6:
        url = reverse('licencias') + f'?op={1}'
        return HttpResponseRedirect(url)
    if pos == 7:
        url = reverse('licencias') + f'?op={2}'
        return HttpResponseRedirect(url)



def comision(request):
    pos = 1
    libros = dcomision.objects.all() #filter == get
    return render(request, 'libros/doc_comision.html', {'libros':libros, 'pos':pos})

def justificaciones(request):
    pos = 2
    libros = djustificaciones.objects.all() #filter == get
    return render(request, 'libros/doc_justificaciones.html', {'libros':libros, 'pos':pos})

def informes(request):
    pos = 3
    libros = dinformes.objects.all() #filter == get
    return render(request, 'libros/doc_informes.html', {'libros':libros, 'pos':pos})



def clasificar(request):

    libros1 = dcomision.objects.filter(registrado = False)   #filter (cumple) =! get (si o si) 
    libros2 = djustificaciones.objects.filter(registrado = False)
    libros3 = dinformes.objects.filter(registrado = False)

    libros4 = dvacacionesPEND.objects.filter(registrado = False) 
    libros5 = dvacacionesPROX.objects.filter(registrado = False)

    libros6 = dlicenciasREM.objects.filter(registrado = False) 
    libros7 = dlicenciasSINREM.objects.filter(registrado = False)

    libros = []

    for libro in libros4:
        libros.append({'libro': libro, 'pos': 4})

    for libro in libros5:
        libros.append({'libro': libro, 'pos': 5})

    for libro in libros6:
        libros.append({'libro': libro, 'pos': 6})

    for libro in libros7:
        libros.append({'libro': libro, 'pos': 7})
    
    for libro in libros2:
        libros.append({'libro': libro, 'pos': 2})

    for libro in libros3:
        libros.append({'libro': libro, 'pos': 3})

    for libro in libros1:
        libros.append({'libro': libro, 'pos': 1})




    libros = sorted(libros, key=lambda x: (
        -1 if x['pos'] in [4, 5, 6] else 0,  # Priorizar vacaciones y licencias
        x['libro'].fecha - timedelta(days=15) if x['pos'] == 1 else x['libro'].fecha
    ))



        
    return render(request, 'libros/doc_clasificados.html', {'libros':libros})

def vacaciones(request):
    
    op = request.GET.get('op')

    if op is None:
        op = 0

    if request.method == 'POST':
        opcion_seleccionada = request.POST.get('opcion')
       
       

        if opcion_seleccionada == 'opcion1':
            pos = 4
            libros = dvacacionesPEND.objects.all() 
            return render(request, 'libros/doc_vacacionesPEND.html', {'libros':libros, 'pos':pos})

        elif opcion_seleccionada == 'opcion2':
            pos = 5
            libros = dvacacionesPROX.objects.all()
            return render(request, 'libros/doc_vacacionesPROX.html', {'libros':libros, 'pos':pos})
    
    else:

        if op == '1':
            pos = 4
            libros = dvacacionesPEND.objects.all() 
            return render(request, 'libros/doc_vacacionesPEND.html', {'libros':libros, 'pos':pos})

        elif op == '2':
            pos = 5
            libros = dvacacionesPROX.objects.all()
            return render(request, 'libros/doc_vacacionesPROX.html', {'libros':libros, 'pos':pos})


def licencias(request):
    
    op = request.GET.get('op')

    if op is None:
        op = 0


    if request.method == 'POST':
        opcion_seleccionada = request.POST.get('opcion')
        
        if opcion_seleccionada == 'opcion1':
            pos = 6
            libros = dlicenciasREM.objects.all() 
            return render(request, 'libros/doc_licenciasREM.html', {'libros':libros, 'pos':pos})

        elif opcion_seleccionada == 'opcion2':
            pos = 7
            libros = dlicenciasSINREM.objects.all()
            return render(request, 'libros/doc_licenciasSINREM.html', {'libros':libros, 'pos':pos})

    else:

        if op == '1':
            pos = 6
            libros = dlicenciasREM.objects.all() 
            return render(request, 'libros/doc_licenciasREM.html', {'libros':libros, 'pos':pos})

        elif op == '2':
            pos = 7
            libros = dlicenciasSINREM.objects.all()
            return render(request, 'libros/doc_licenciasSINREM.html', {'libros':libros, 'pos':pos})



def crear(request, pos):
    
    op = 0

    if pos == 1:
        ubicacion = 'comision'
        form = 'comisionForm'
    if pos == 2:
        ubicacion = 'justificaciones'
        form = 'justificacionesForm'
    if pos == 3:
        ubicacion = 'informes'
        form = 'informesForm'
    if pos == 4:
        ubicacion = 'vacaciones'
        form = 'vacacionespendForm'
        op = 1
    if pos == 5:
        ubicacion = 'vacaciones'
        form = 'vacacionesproxForm'
        op = 2
    if pos == 6:
        ubicacion = 'licencias'
        form = 'licenciasremForm'
        op = 1
    if pos == 7:
        ubicacion = 'licencias'
        form = 'licenciassinremForm'
        op = 2
    

    formulario = globals()[form](request.POST or None, request.FILES or None)
    tipos_doc = Tdocumento.objects.all()
    users = personal.objects.all()
    procedencia = unidadCIP.objects.all()


    datos = request.session.get('datos')
    datos_user = Cargo.objects.get(id=datos)


    
    if formulario.is_valid():
        formulario.save()

        url = reverse(ubicacion) + f'?op={op}'
        return HttpResponseRedirect(url)

    return render(request, 'libros/crear.html', {'formulario':formulario, 'pos':pos, 'tipos_doc':tipos_doc, 'personal':users, 'procedencia':procedencia, 'datos': datos_user} )


def editar(request, id, pos):
    
    op = 0

    if pos == 1:
        ubicacion = 'comision'
    if pos == 2:
        ubicacion = 'justificaciones'
    if pos == 3:
        ubicacion = 'informes'
    if pos == 4:
        ubicacion = 'vacaciones'
        op = 1
    if pos == 5:
        ubicacion = 'vacaciones'
        op = 2
    if pos == 6:
        ubicacion = 'licencias'
        op = 1
    if pos == 7:
        ubicacion = 'licencias'
        op = 2

    if pos == 1:
        libro = dcomision.objects.get(id=id)
    if pos == 2:
        libro = djustificaciones.objects.get(id=id)
    if pos == 3:
        libro = dinformes.objects.get(id=id)
    if pos == 4:
        libro = dvacacionesPEND.objects.get(id=id)
    if pos == 5:
        libro = dvacacionesPROX.objects.get(id=id)
    if pos == 6:
        libro = dlicenciasREM.objects.get(id=id)
    if pos == 7:
        libro = dlicenciasSINREM.objects.get(id=id)

    formulario = comisionForm(request.POST or None, request.FILES or None, instance=libro)
    tipos_doc = Tdocumento.objects.all()
    users = personal.objects.all()
    procedencia = unidadCIP.objects.all()

    datos = request.session.get('datos')
    datos_user = Cargo.objects.get(id=datos)


    if formulario.is_valid() and request.POST:
        formulario.save()

        url = reverse(ubicacion) + f'?op={op}'
        return HttpResponseRedirect(url)

    return render(request, 'libros/editar.html', {'formulario':formulario, 'pos':pos, 'tipos_doc':tipos_doc, 'personal':users, 'procedencia':procedencia, 'datos': datos_user })



def eliminar(request, id, pos):

    op = 0

    if pos == 1:
        ubicacion = 'comision'
    if pos == 2:
        ubicacion = 'justificaciones'
    if pos == 3:
        ubicacion = 'informes'
    if pos == 4:
        ubicacion = 'vacaciones'
        op = 1
    if pos == 5:
        ubicacion = 'vacaciones'
        op = 2
    if pos == 6:
        ubicacion = 'licencias'
        op = 1
    if pos == 7:
        ubicacion = 'licencias'
        op = 2

    if pos == 1:
        libro = dcomision.objects.get(id=id)
    if pos == 2:
        libro = djustificaciones.objects.get(id=id)
    if pos == 3:
        libro = dinformes.objects.get(id=id)
    if pos == 4:
        libro = dvacacionesPEND.objects.get(id=id)
    if pos == 5:
        libro = dvacacionesPROX.objects.get(id=id)
    if pos == 6:
        libro = dlicenciasREM.objects.get(id=id)
    if pos == 7:
        libro = dlicenciasSINREM.objects.get(id=id)

    libro.delete()
    
    url = reverse(ubicacion) + f'?op={op}'
    return HttpResponseRedirect(url)