
from django.http import HttpResponse
from django.template import loader
from django.http import Http404	
from .models import Cliente
from .models import Tabla
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# --- Vistas Genericas ---

class IndexView(generic.ListView):
    template_name = 'skateez/index.html'

    def get_queryset(self):

        return Tabla.objects.all()

   

class DetailView(generic.DetailView):
    model = Tabla
    template_name = 'skateez/detail.html'

class ResultsView(generic.DetailView):
    model = Tabla
    template_name = 'skateez/results.html'


    
# --- Listas ---

class ListaTabla(ListView):
	model = Tabla

"""	
	template_name = 'skateez/tabla_list.html'
		def get_context_data(self, **kwargs):
			context = super(ListaTabla, self).get_context_data(**kwargs)
			context['tabla_list'] = Tabla.objects.all()
			return context
"""


# --- Vistas genericas de creación, actualización y borrado --- 


class Create(CreateView):
    model = Tabla
    fields = ['name']

class Update(UpdateView):
    model = Tabla
    fields = ['name']

class Delete(DeleteView):
    model = Tabla
    success_url = reverse_lazy('author-list')

class Create(LoginRequiredMixin, CreateView):
    model = Tabla
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

# --- Formulario ---

from skateez.forms import ContactForm
from django.views.generic.edit import FormView

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)




# --- USERSignup ---

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registration/signup.html", {'form': form})


# --- UserLogin ---

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

def login_view(request):
    # Creamos el formulario de autenticación vacío
        form = AuthenticationForm()
        if request.method == "POST":
            # Añadimos los datos recibidos al formulario
            form = AuthenticationForm(data=request.POST)
            # Si el formulario es válido...
            if form.is_valid():
                # Recuperamos las credenciales validadas
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # Verificamos las credenciales del usuario
                user = authenticate(username=username, password=password)

                # Si existe un usuario con ese nombre y contraseña
                if user is not None:
                    # Hacemos el login manualmente
                    do_login(request, user)
                    # Y le redireccionamos a la portada
                    return redirect('/')

        # Si llegamos al final renderizamos el formulario
        return render(request, "registration/login.html", {'form': form})
        
# --- UserLogout ---
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/skateez/welcome')


# --- Welcome ---

def welcome(request):
    # Si estamos identificados devolvemos la portada
        if request.user.is_authenticated:
            return render(request, "registration/index.html")
        # En otro caso redireccionamos al login
        return redirect('/skateez/login')