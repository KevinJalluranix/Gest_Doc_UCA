from django import forms

from .models import Libro, Cargo, Login, Documento, dcomision, djustificaciones, dinformes, dvacacionesPEND, dvacacionesPROX, dlicenciasREM, dlicenciasSINREM


class LibroForm(forms.ModelForm):
    
    class Meta:
        model = Libro
        fields = '__all__'

class DocumentoForm(forms.ModelForm):
    
    class Meta:
        model = Documento
        fields = '__all__'


class comisionForm(forms.ModelForm):


    class Meta:
        model = dcomision
        fields = '__all__'


    
class justificacionesForm(forms.ModelForm):
    
    class Meta:
        model = djustificaciones
        fields = '__all__'

class informesForm(forms.ModelForm):
    
    class Meta:
        model = dinformes
        fields = '__all__'

class vacacionespendForm(forms.ModelForm):
    
    class Meta:
        model = dvacacionesPEND
        fields = '__all__'

class vacacionesproxForm(forms.ModelForm):
    
    class Meta:
        model = dvacacionesPROX
        fields = '__all__'

class licenciasremForm(forms.ModelForm):
    
    class Meta:
        model = dlicenciasREM
        fields = '__all__'

class licenciassinremForm(forms.ModelForm):
    
    class Meta:
        model = dlicenciasSINREM
        fields = '__all__'



class LoginForm(forms.ModelForm):
    
    class Meta:
        model = Login
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        #cargos = Cargo.objects.all()
        #choices = [(cargo.id, cargo.cargo) for cargo in cargos]
        #self.fields['tipo_cargo'].widget = forms.Select(choices=choices)

        self.fields['contraseña'].widget = forms.PasswordInput()

