from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class resourcecliente(resources.ModelResource):
    class Meta:
        model = cliente

class admincliente(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name_cliente']
    list_display = ['Dpi','Edad','sexo']
    resource_class = resourcecliente
admin.site.register(cliente,admincliente)



class resourceservicio(resources.ModelResource):
    class Meta:
        model = servicio

class adminservicio(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['chequeo_medico']
    list_display = ['precio']
    resource_class = resourceservicio

admin.site.register(servicio, adminservicio)

class resourcecita(resources.ModelResource):
    class Meta:
        model = cita

class admincita(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['fecha_y_hora']
    resource_class = resourcecita

admin.site.register(cita, admincita)


class resourcemedico(resources.ModelResource):
    class Meta:
        model = medico

class adminmedico(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name_medico']
    list_display = ['especialidad','turno']
    resource_class = resourcemedico

admin.site.register(medico, adminmedico)