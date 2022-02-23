from django.contrib import admin

from .models import Pacientes
from .models import Medicos
from .models import Consultas

# Register your models here.
admin.site.register(Pacientes)
admin.site.register(Medicos)
admin.site.register(Consultas)
