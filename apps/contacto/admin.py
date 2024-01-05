from django.contrib import admin
from . import models

# Register your models here.


class ContactoAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'nombre_apellido', 'asunto', 'mensaje')
    list_display = ('id', 'nombre_apellido', 'email',
                    'asunto', 'mensaje', 'fecha')


admin.site.register(models.Contacto, ContactoAdmin)
