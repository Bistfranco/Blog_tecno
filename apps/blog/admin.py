from django.contrib import admin
from . import models

admin.site.site_header = 'Administración del Blog'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Blog'


class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha', 'articulo', 'usuario', 'texto')
    list_display = ('articulo', 'usuario', 'fecha', 'texto')


admin.site.register(models.Comentario, ComentarioAdmin)
# admin.site.register(models.Comentario) # original


class AcercaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('descripcion', 'creacion')


admin.site.register(models.Acerca, AcercaAdmin)


class RedAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'url', 'icono')


admin.site.register(models.Red, RedAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')
    prepopulated_fields = {'slug': ('nombre', )}


admin.site.register(models.Categoria, CategoriaAdmin)


class EtiquetaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')


admin.site.register(models.Etiqueta, EtiquetaAdmin)


class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('titulo', 'categoria', 'publicado',
                    'autor', 'creacion', 'articuloEtiquetas')
    prepopulated_fields = {'slug': ('titulo', )}
    ordering = ('autor', '-creacion')
    search_fields = ('titulo', 'contenido',
                     'autor__username', 'categoria__nombre')
    list_filter = ('autor', 'categoria', 'etiquetas')

    def articuloEtiquetas(self, obj):
        return ' - '.join([etiqueta.nombre for etiqueta in obj.etiquetas.all().order_by('nombre')])

    articuloEtiquetas.short_description = 'Etiquetas'


admin.site.register(models.Articulo, ArticuloAdmin)
