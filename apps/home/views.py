import datetime
import json
from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from apps.home.models import Videohome
from .models import Noticia, Subsistema, Evento, Departamento, Municipio, Institucion, Dashboard, Oferta, VideoNosotros, \
    Modalidad, Logo, PatrimonioUnesco, BannerPatrimonio, PlataformaVirtual, BannerPlataforma


# Se define variables globales
def global_(self, **kwargs):
    data = []
    logo = Logo.objects.first()
    video = Videohome.objects.filter().first()
    for a in Departamento.objects.filter(estado=1).all():
        obj = {}
        obj["nombre"] = a.nombre
        obj["url"] = reverse_lazy('home:departamento', kwargs={'pk': a.pk})
        data.append(obj)

    return {'departamentos': data, 'logo': logo, 'video': video}


class HomePageView(TemplateView):
    template_name = 'home/home.html'
    model = Municipio, Dashboard, Institucion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inicio'] = True  # variable para mostrar u ocultar dasboard Costa caribe
        context.update({
            'inatec': Noticia.objects.filter(id_subsistema=1).filter(estado=1).order_by('fecha').first(),
            'mined': Noticia.objects.filter(id_subsistema=2).filter(estado=1).order_by('fecha').first(),
            'cnu': Noticia.objects.filter(id_subsistema=3).filter(estado=1).order_by('fecha').first(),
        })

        context.update({
            'subsistem': Subsistema.objects.filter(estado=1).all().order_by('pk'),
            'inatece': Evento.objects.filter(id_subsistema=1).filter(estado=1).order_by('fecha').all(),
            'minede': Evento.objects.filter(id_subsistema=2).filter(estado=1).order_by('fecha').all(),
            'cnue': Evento.objects.filter(id_subsistema=3).filter(estado=1).order_by('fecha').all(),
        })

        context.update({
            'dashboardInatec': Dashboard.objects.filter(id_subsistema=1, estado=1, anio=2021).order_by('anio').all(),
            'dashboardMined': Dashboard.objects.filter(id_subsistema=2, estado=1, anio=2021).order_by('anio').all(),
            'dashboardCnu': Dashboard.objects.filter(id_subsistema=3, estado=1, anio=2021).order_by('anio').all(),
            'cantCentrosInatecAgro': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=1, sector=2).count(),
            'cantCentrosInatecIndus': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=1, sector=3).count(),
            'cantCentrosInatecComer': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=1, sector=4).count(),
            'cantCentrosInatecAgroAcre': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=2,
                                                                    sector=2).count(),
            'cantCentrosInatecIndusAcre': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=2,
                                                                     sector=3).count(),
            'cantCentrosInatecComerAcre': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=2,
                                                                     sector=4).count(),
            'cantCentrosMined': Institucion.objects.filter(id_subsistema=2, estado=1, tipo__in=(3, 4)).count(),
            'cantCentrosMinedPrivado': Institucion.objects.filter(id_subsistema=2, estado=1, tipo__in=(7, 8)).count(),
            'cantCentrosCnu': Institucion.objects.filter(id_subsistema=3, estado=1, tipo=6).count(),
            'cantCentrosCnulegal': Institucion.objects.filter(id_subsistema=3, estado=1, tipo=5).count(),
            'dashboardInateccc': Dashboard.objects.filter(id_subsistema=1, estado=1, anio=2021,
                                                          id_departamento__in=(91, 93)).order_by('anio').all(),
            'dashboardMinedcc': Dashboard.objects.filter(id_subsistema=2, estado=1, anio=2021,
                                                         id_departamento__in=(91, 93)).order_by('anio').all(),
            'dashboardCnucc': Dashboard.objects.filter(id_subsistema=3, estado=1, anio=2021,
                                                       id_departamento__in=(91, 93)).order_by('anio').all(),
            'cantCentrosInatecAgrocc': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=1, sector=2,
                                                                  id_municipo__in=(Municipio.objects.filter(estado=1,
                                                                                                            id_departamento__in=(
                                                                                                                91,
                                                                                                                93)).all())).count(),
            'cantCentrosInatecInduscc': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=1, sector=3,
                                                                   id_municipo__in=(Municipio.objects.filter(estado=1,
                                                                                                             id_departamento__in=(
                                                                                                                 91,
                                                                                                                 93)).all())).count(),
            'cantCentrosInatecComercc': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=1, sector=4,
                                                                   id_municipo__in=(Municipio.objects.filter(estado=1,
                                                                                                             id_departamento__in=(
                                                                                                                 91,
                                                                                                                 93)).all())).count(),
            'cantCentrosInatecAgroAcrecc': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=2, sector=2,
                                                                      id_municipo__in=(
                                                                          Municipio.objects.filter(estado=1,
                                                                                                   id_departamento__in=(
                                                                                                       91,
                                                                                                       93)).all())).count(),
            'cantCentrosInatecIndusAcrecc': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=2, sector=3,
                                                                       id_municipo__in=(
                                                                           Municipio.objects.filter(estado=1,
                                                                                                    id_departamento__in=(
                                                                                                        91,
                                                                                                        93)).all())).count(),
            'cantCentrosInatecComerAcrecc': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=2, sector=4,
                                                                       id_municipo__in=(
                                                                           Municipio.objects.filter(estado=1,
                                                                                                    id_departamento__in=(
                                                                                                        91,
                                                                                                        93)).all())).count(),
            'cantCentrosMinedcc': Institucion.objects.filter(id_subsistema=2, estado=1, tipo__in=(3, 4),
                                                             id_municipo__in=(Municipio.objects.filter(estado=1,
                                                                                                       id_departamento__in=(
                                                                                                           91,
                                                                                                           93)).all())).count(),
            'cantCentrosMinedPrivadocc': Institucion.objects.filter(id_subsistema=2, estado=1, tipo__in=(7, 8),
                                                                    id_municipo__in=(Municipio.objects.filter(estado=1,
                                                                                                              id_departamento__in=(
                                                                                                                  91,
                                                                                                                  93)).all())).count(),
            'cantCentrosCnucc': Institucion.objects.filter(id_subsistema=3, estado=1, tipo=6,
                                                           id_municipo__in=(Municipio.objects.filter(estado=1,
                                                                                                     id_departamento__in=(
                                                                                                         91,
                                                                                                         93)).all())).count(),
            'cantCentrosCnulegalcc': Institucion.objects.filter(id_subsistema=3, estado=1, tipo=5,
                                                                id_municipo__in=(Municipio.objects.filter(estado=1,
                                                                                                          id_departamento__in=(
                                                                                                              91,
                                                                                                              93)).all())).count(),
        })

        return context


class MunicipioPageView(TemplateView):
    template_name = 'municipio/municipio.html'
    model = Municipio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        municipio = Municipio.objects.filter(slug=kwargs['slug']).get()
        # context['depto'] = Municipio.objects.filter(visible=True, nombre=self.object.id)
        context['municipio'] = municipio
        context.update({
            'inatec': Noticia.objects.filter(id_subsistema=1).filter(estado=1).filter(
                id_departamento=municipio.id_departamento).order_by('fecha').first(),
            'mined': Noticia.objects.filter(id_subsistema=2).filter(estado=1).filter(
                id_departamento=municipio.id_departamento).order_by('fecha').first(),
            'cnu': Noticia.objects.filter(id_subsistema=3).filter(estado=1).filter(
                id_departamento=municipio.id_departamento).order_by('fecha').first(),
        })

        context.update({
            'inatece': Evento.objects.filter(id_subsistema=1).filter(estado=1).filter(
                id_departamento=municipio.id_departamento).order_by('fecha').all(),
            'minede': Evento.objects.filter(id_subsistema=2).filter(estado=1).filter(
                id_departamento=municipio.id_departamento).order_by('fecha').all(),
            'cnue': Evento.objects.filter(id_subsistema=3).filter(estado=1).filter(
                id_departamento=municipio.id_departamento).order_by('fecha').all(),
        })

        subsistema = Subsistema.objects.all().order_by('id')
        context['subsistema'] = subsistema

        return context


class DepartamentoPageView(TemplateView):
    template_name = 'departamento/departamento.html'
    model = Departamento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        # LEE EL AÑO ACTUAL
        fechaActual = datetime.datetime.now()
        fecha = fechaActual.date()
        anioActual = fecha.strftime("%Y")

        context.update({
            'dashboardInatec': Dashboard.objects.filter(id_subsistema=1, estado=1, anio=2021,
                                                        id_departamento=pk).order_by('anio').all(),
            'dashboardMined': Dashboard.objects.filter(id_subsistema=2, estado=1, anio=2021,
                                                       id_departamento=pk).order_by('anio').all(),
            'dashboardCnu': Dashboard.objects.filter(id_subsistema=3, estado=1, anio=2021, id_departamento=pk).order_by(
                'anio').all(),
            'cantCentrosInatecAgro': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=1, sector=2,
                                                                id_municipo__in=(Municipio.objects.filter(
                                                                    id_departamento=pk).all())).count(),
            'cantCentrosInatecIndus': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=1, sector=3,
                                                                 id_municipo__in=(Municipio.objects.filter(
                                                                     id_departamento=pk).all())).count(),
            'cantCentrosInatecComer': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=1, sector=4,
                                                                 id_municipo__in=(Municipio.objects.filter(
                                                                     id_departamento=pk).all())).count(),
            'cantCentrosInatecAgroAcre': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=2, id_municipo__in=(
                Municipio.objects.filter(id_departamento=pk).all()),
                                                                    sector=2).count(),
            'cantCentrosInatecIndusAcre': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=2,
                                                                     id_municipo__in=(Municipio.objects.filter(
                                                                         id_departamento=pk).all()),
                                                                     sector=3).count(),
            'cantCentrosInatecComerAcre': Institucion.objects.filter(id_subsistema=1, estado=1, tipo=2,
                                                                     id_municipo__in=(Municipio.objects.filter(
                                                                         id_departamento=pk).all()),
                                                                     sector=4).count(),
            'cantCentrosMined': Institucion.objects.filter(id_subsistema=2, estado=1, tipo__in=(3, 4), id_municipo__in=(
                Municipio.objects.filter(id_departamento=pk).all())).count(),
            'cantCentrosMinedPrivado': Institucion.objects.filter(id_subsistema=2, estado=1, tipo__in=(7, 8),
                                                                  id_municipo__in=(Municipio.objects.filter(
                                                                      id_departamento=pk).all())).count(),
            'cantCentrosCnu': Institucion.objects.filter(id_subsistema=3, estado=1, tipo=6, id_municipo__in=(
                Municipio.objects.filter(id_departamento=pk).all())).count(),
            'cantCentrosCnulegal': Institucion.objects.filter(id_subsistema=3, estado=1, tipo=5, id_municipo__in=(
                Municipio.objects.filter(id_departamento=pk).all())).count(),
        })
        context['subsistem'] = Subsistema.objects.filter(estado=1).all().order_by('pk'),
        context['inicio'] = False  # variable para mostrar u ocultar dasboard Costa caribe
        context['departamento'] = Departamento.objects.filter(pk=pk).first()
        data = Municipio.objects.all().filter(estado=1)
        data = serializers.serialize('json', data, fields=("pk", "slug", "nombre"))
        context['municipios'] = data
        return context


class SubsistemaCNUPageView(TemplateView):
    template_name = 'subsistema/susbsistema.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departamentos = Departamento.objects.all()
        portada = Subsistema.objects.filter(id=3).first()
        context['departamento'] = departamentos
        context['titulo'] = 'CNU'
        context['subsistema'] = 3
        context['bcolor'] = '#043284'
        context['modalidad'] = 'Estudios y programas:'
        estrategias = (
            (1, 'Todos'),
            (2, 'Licenciatura'),
            (3, 'Ingenería'),
            (4, 'Técnico'),
            (5, 'Doctorado'),
            (6, 'Maestría'),
            (7, 'Diplomado'),
        )
        context['estrategias'] = estrategias
        context['portada'] = portada.portada
        return context


class SubsistemaINATECPageView(TemplateView):
    template_name = 'subsistema/susbsistema.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departamentos = Departamento.objects.all()
        portada = Subsistema.objects.filter(id=1).first()
        context['departamento'] = departamentos
        context['titulo'] = 'INATEC'
        context['subsistema'] = 1
        context['inatec'] = Noticia.objects.filter(id_subsistema=1).filter(estado=1).order_by('id').first()
        context['bcolor'] = '#e3007e'
        context['modalidad'] = 'Programas/Estrategias:'
        estrategias = (
            (1, 'Todos'),
            (2, 'Educación Técnica'),
            (3, 'Capacitación'),
            (4, 'Campo'),
            (5, 'Oficio'),
        )
        context['estrategias'] = estrategias
        context['portada'] = portada.portada
        return context


class SubsistemaMINEDPageView(TemplateView):
    template_name = 'subsistema/susbsistema.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departamentos = Departamento.objects.all()
        portada = Subsistema.objects.filter(id=2).first()
        context['departamento'] = departamentos
        context['titulo'] = 'MINED'
        context['subsistema'] = 2
        context['bcolor'] = '#00aeef'
        context['modalidad'] = 'Niveles de formación:'
        estrategias = (
            (1, 'Todos'),
            (2, 'Primaria'),
            (3, 'Secundaria'),
            (4, 'Eduación Especial'),
        )
        context['estrategias'] = estrategias
        context['portada'] = portada.portada
        return context


def getMunicipios(request):
    data = []
    mun = Municipio.objects.filter(id_departamento=request.POST.get('id_departamento'))
    for d in mun:
        obj = {
            'id_municipio': d.id,
            'nombre': d.nombre
        }
        data.append(obj)
    return JsonResponse(data, safe=False)


def getCentroPorMunicpio(request):
    data = []
    inst = Institucion.objects.filter(id_municipo=request.POST.get('id_municipio'),
                                      id_subsistema=request.POST.get('subsistema'),
                                      tipo=request.POST.get('tipo'))
    for i in inst:
        obj = {
            'id_institucion': i.id,
            'nombre': i.nombre
        }
        data.append(obj)
    return JsonResponse(data, safe=False)


def getLocationInstitucion(request):
    inst = Institucion.objects.filter(id=request.POST.get('id_institucion')).first()
    if inst.foto:
        fotodef = json.dumps(inst.foto.url)
    else:
        fotodef = json.dumps(inst.id_subsistema.imagen.url)
    obj = {
        'id_institucion': inst.id,
        'nombre': inst.nombre,
        'direccion': inst.direccion,
        'telefono': inst.telefono,
        'latitud': inst.latitud,
        'longitud': inst.longitud,
        'web': inst.web,
        'foto': fotodef
    }
    return JsonResponse(obj, safe=False)


def getOfertasPorInstitucion(request):
    data = []

    id_subsistema = request.POST.get('id_subsistema')

    if id_subsistema == '2':
        ofertas = Modalidad.objects.filter(institucion=request.POST.get('id_institucion'), estado=1)
    else:
        ofertas = Oferta.objects.filter(institucion=request.POST.get('id_institucion'), estado=1)

    inst = Institucion.objects.filter(id=request.POST.get('id_institucion')).first()

    if ofertas:
        for o in ofertas:
            obj = {
                'id_oferta': o.id,
                'nombre': o.nombre,
                'nombre_institucion': inst.nombre

            }
            data.append(obj)
    else:
        obj = {
            'id_oferta': '',
            'nombre': '',
            'nombre_institucion': inst.nombre

        }
        data.append(obj)

    return JsonResponse(data, safe=False)


def getLocationInstitucionPorDepartamentoMunicpio(request):
    data = []
    parametro = request.POST.get('parametro')
    id_parametro = request.POST.get('id')
    id_subsistema = request.POST.get('idsubsistema')
    tipo = request.POST.get('tipo')

    if parametro == '1':
        inst = Institucion.objects.filter(id_municipo__id_departamento=id_parametro, id_subsistema=id_subsistema)
    elif parametro == '2':
        inst = Institucion.objects.filter(id_municipo=id_parametro, id_subsistema=id_subsistema)
    elif parametro == '3':
        inst = Institucion.objects.filter(id_subsistema=id_subsistema)
    else:
        inst = Institucion.objects.filter(id_municipo=id_parametro, id_subsistema=id_subsistema, tipo=tipo)

    for i in inst:
        if i.foto:
            fotodef = json.dumps(i.foto.url)
        else:
            fotodef = json.dumps(i.id_subsistema.imagen.url)

        obj = {
            'id_institucion': i.id,
            'nombre': i.nombre,
            'direccion': i.direccion,
            'telefono': i.telefono,
            'latitud': i.latitud,
            'longitud': i.longitud,
            'web': i.web,
            'foto': fotodef
        }
        data.append(obj)
    return JsonResponse(data, safe=False)


def getLocationDepartamentos(request):
    dep = Departamento.objects.filter(id=request.POST.get('id_departamento')).first()
    obj = {
        'id_departamento': dep.id,
        'nombre': dep.nombre,
        'latitud': dep.latitud,
        'longitud': dep.longitud,
        'longitud_2': dep.longitud_2,
        'latitud_2': dep.latitud_2,
    }
    return JsonResponse(obj, safe=False)


def getLocationMunicipios(request):
    mun = Municipio.objects.filter(id=request.POST.get('id_municipio')).first()
    obj = {
        'id_municipio': mun.id,
        'nombre': mun.nombre,
        'latitud': mun.latitud,
        'longitud': mun.longitud,
        'latitud_2': mun.latitud_2,
        'longitud_2': mun.longitud_2,
    }
    return JsonResponse(obj, safe=False)


class NosotrosPageView(TemplateView):
    template_name = 'nosotros/nosotros.html'
    model = Subsistema

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videoNosotros'] = VideoNosotros.objects.filter().first()

        return context


class PatrimoniosPageView(TemplateView):
    template_name = 'patrimonios/patrimonio_home.html'
    model = PatrimonioUnesco

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patrimonios'] = PatrimonioUnesco.objects.filter(estado=1).all().order_by('pk')
        context['bannerPat'] = BannerPatrimonio.objects.filter().first()
        return context


class PlataformasPageView(TemplateView):
    template_name = 'plataformas/plataforma_home.html'
    model = PlataformaVirtual

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plataformas'] = PlataformaVirtual.objects.filter(estado=1).all().order_by('orden')
        context['bannerPlat'] = BannerPlataforma.objects.filter().first()
        return context


class PlataformasDetallesPageView(TemplateView):
    template_name = 'plataformas/plataformas_detalles.html'
    model = PlataformaVirtual

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['plataformas'] = PlataformaVirtual.objects.filter(pk=pk).first()
        context['bannerPlat'] = BannerPlataforma.objects.filter().first()
        return context


class PatrimoniosDetallesPageView(TemplateView):
    template_name = 'patrimonios/patrimoniosDetalles.html'
    model = PatrimonioUnesco

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['patrimonio'] = PatrimonioUnesco.objects.filter(pk=pk).first()
        return context


def getMunicipiosPatrimonio(request):
    data = []

    id_patrimonio = request.POST.get('id_patrimonio')
    patrimonio = PatrimonioUnesco.objects.filter(pk=id_patrimonio).first()
    mun = Municipio.objects.filter(pk__in=patrimonio.id_municipio.all(), estado=1).all()

    for o in mun:
        obj = {
            'latitud': o.latitud,
            'longitud': o.longitud,

        }
        data.append(obj)

    data.append(obj)
    return JsonResponse(data, safe=False)
