from django.conf import settings
from django.urls import path, re_path
from .views import HomePageView, MunicipioPageView, DepartamentoPageView, SubsistemaCNUPageView, getMunicipios, \
    getCentroPorMunicpio, SubsistemaINATECPageView, SubsistemaMINEDPageView, getLocationInstitucion, \
    getOfertasPorInstitucion, getLocationInstitucionPorDepartamentoMunicpio, getLocationDepartamentos, \
    getLocationMunicipios, NosotrosPageView, PatrimoniosDetallesPageView, getMunicipiosPatrimonio, PatrimoniosPageView, \
    PlataformasPageView, PlataformasDetallesPageView
from django.views.static import serve
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('municipio/<slug:slug>', MunicipioPageView.as_view(), name='municipio'),
    path('departamento/<int:pk>', DepartamentoPageView.as_view(), name='departamento'),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    path('subsistema/inatec', SubsistemaINATECPageView.as_view(), name='subsistema_inatec'),
    path('subsistema/mined', SubsistemaMINEDPageView.as_view(), name='subsistema_mined'),
    path('subsistema/cnu', SubsistemaCNUPageView.as_view(), name='subsistema_cnu'),
    path('municipios/data', getMunicipios, name='municipios_json'),
    path('instituciones/data', getCentroPorMunicpio, name='instituciones_json'),
    path('ofertas/institucion/data', getOfertasPorInstitucion, name='oferta_institucion_json'),
    path('instituciones/data/especifico', getLocationInstitucion, name='instituciones_especifico_json'),
    path('instituciones/data/general', getLocationInstitucionPorDepartamentoMunicpio,
         name='instituciones_general_json'),
    path('departamento/data/especifico', getLocationDepartamentos, name='departamento_data'),
    path('municipio/data/especifico', getLocationMunicipios, name='municipio_data'),
    path('nosotros/', NosotrosPageView.as_view(), name='nosotros'),
    path('patrimonios/', PatrimoniosPageView.as_view(), name='patrimonios'),
    path('plataformas/', PlataformasPageView.as_view(), name='plataformas'),
    path('plataformas-detalles/<int:pk>', PlataformasDetallesPageView.as_view(),
         name='plataformas_detalles'),
    path('patrimonios-detalles/<int:pk>', PatrimoniosDetallesPageView.as_view(),
         name='patrimonios_detalles'),
    path('municipios/data/general', getMunicipiosPatrimonio,
         name='municipios_general_json'),
]
