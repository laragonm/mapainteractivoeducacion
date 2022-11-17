from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from solo.admin import SingletonModelAdmin
from apps.home.forms import LogoForm
from apps.home.models import Dashboard, Noticia, Subsistema, Departamento, Municipio, Oferta, Institucion, Evento, \
    Modalidad, Videohome, VideoNosotros, Logo, ClasificacionUnesco, PatrimonioUnesco, BannerPatrimonio, \
    BannerPlataforma, PlataformaVirtual


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    search_fields = ['id_subsistema']
    list_display = ['id_subsistema', 'id_departamento', 'anio', 'fecha_grabacion', 'fecha_modificacion']
    list_filter = ['anio', 'id_subsistema', 'id_departamento']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    search_fields = ['id_subsistema', 'titulo', 'fecha']
    list_display = ['id_subsistema', 'titulo', 'fecha', 'fecha_grabacion', 'fecha_modificacion']
    list_filter = ['id_subsistema', 'fecha']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(Subsistema)
class SubsistemaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado', 'fecha_grabacion', 'fecha_modificacion']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'fecha_grabacion', 'fecha_modificacion']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_filter = ['id_departamento']
    list_display = ['nombre', 'estado', 'fecha_grabacion', 'fecha_modificacion']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'tipo']
    list_filter = ['tipo', 'estado']
    list_display = ['nombre', 'tipo', 'estado', 'fecha_grabacion', 'fecha_modificacion']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'tipo', 'id_municipo', 'estado', 'fecha_grabacion', 'fecha_modificacion']
    filter_horizontal = ('id_modalidad', 'id_oferta')
    list_filter = ['id_subsistema', 'tipo', ('id_municipo__id_departamento', RelatedOnlyFieldListFilter), 'id_municipo']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    search_fields = ['id_subsistema', 'titulo', 'fecha']
    list_display = ['id_subsistema', 'titulo', 'fecha', 'fecha_grabacion', 'fecha_modificacion']
    list_filter = ['id_subsistema', 'fecha']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(Modalidad)
class ModalidadAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'estado', 'fecha_grabacion', 'fecha_modificacion']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(ClasificacionUnesco)
class ClasificacionUnescoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'estado', 'fecha_grabacion', 'fecha_modificacion']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(PatrimonioUnesco)
class PatrimonioUnescoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'estado', 'fecha_grabacion', 'fecha_modificacion']
    filter_horizontal = ['id_municipio']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(PlataformaVirtual)
class PlataformaVirtualAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'estado', 'fecha_grabacion', 'fecha_modificacion']
    exclude = ('usuario_grabacion', 'usuario_modificacion')


@admin.register(Logo)
class SectionAdmin(SingletonModelAdmin):
    form = LogoForm


admin.site.register(Videohome, SingletonModelAdmin)
admin.site.register(VideoNosotros, SingletonModelAdmin)
admin.site.register(BannerPatrimonio, SingletonModelAdmin)
admin.site.register(BannerPlataforma, SingletonModelAdmin)
