
from django.http import HttpResponse
from django.template import loader
from django.http import Http404	
from .models import Cliente
from .models import Tabla
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from skateez.models import Author
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

# !!CAMBIAR!!

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from skateez.models import Usuario

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Usuario'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


    
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
    model = Author
    fields = ['name']

class Update(UpdateView):
    model = Author
    fields = ['name']

class Delete(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')

class Create(LoginRequiredMixin, CreateView):
    model = Author
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'skateez/signup.html', {'form': form})


# --- UserLogin ---

from django.contrib.auth import authenticate, login

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
        
    else:
        return 
        
# --- UserLogout ---
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('index')