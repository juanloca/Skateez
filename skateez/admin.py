from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Tabla

admin.site.register(Tabla)

from .models import Ruedas

admin.site.register(Ruedas)

from .models import Ejes

admin.site.register(Ejes)

from .models import Rodamientos

admin.site.register(Rodamientos)

from .models import Pedidos

admin.site.register(Pedidos)

from .models import Cliente	

admin.site.register(Cliente)

# User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from skateez.models import Usuario

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)