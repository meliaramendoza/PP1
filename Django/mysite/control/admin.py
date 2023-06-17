from django.contrib import admin
from .models import Empleado, Jornada

# Registro del modelo Empleado en el panel de administrador
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'turno', 'dias_trabajo', 'horario_entrada', 'horario_salida')
    list_filter = ('nombre', 'turno')
    ordering = ('-turno',)

# Registro del modelo Jornada en el panel de administrador
@admin.register(Jornada)
class JornadaAdmin(admin.ModelAdmin):
    list_display = ('nombre_empleado', 'fecha', 'tipo_marcacion')
    list_filter = ('fecha',)
    ordering = ('-fecha',)

    def nombre_empleado(self, obj):
        return obj.empleado.nombre
    nombre_empleado.short_description = 'Nombre del Empleado'


admin.site.register(Jornada, JornadaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)