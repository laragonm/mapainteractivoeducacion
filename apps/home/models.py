import os
import uuid
from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import model_to_dict
from solo.models import SingletonModel
from django_currentuser.middleware import get_current_authenticated_user

from apps.core.models import Base

ESTADO = (
    (1, 'ACTIVO'),
    (0, 'INACTIVO')
)
TIPO = (
    (1, 'CENTRO TECNOLÓGICO - INATEC'),
    (2, 'CENTRO TECNOLÓGICO ACREDITADO - INATEC'),
    (3, 'CENTRO ESCOLAR - PUBLICO'),
    (4, 'ESCUELA NORMAL - PUBLICA'),
    (5, 'UNIVERSIDAD LEGALMENTE CONSTITUIDA'),
    (6, 'UNIVERSIDAD MIEMBRO'),
    (7, 'CENTRO ESCOLAR - PRIVADO'),
    (8, 'ESCUELA NORMAL - PRIVADA')
)

SECTORES_INATEC = (
    ('2', 'Agropecuario y Forestal'),
    ('3', 'Industria y Construccion'),
    ('4', 'Comercio y Servicio')
)


def imagenNoticia_path(instance, filename):
    if instance.pk:
        event = Noticia.objects.get(pk=instance.pk)
        event.imagen.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'noticias/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenEvento_path(instance, filename):
    if instance.pk:
        event = Evento.objects.get(pk=instance.pk)
        event.imagen.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'eventos/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenDepartamento_path(instance, filename):
    if instance.pk:
        event = Departamento.objects.get(pk=instance.pk)
        event.portada.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'departamentos/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenInstituciones_path(instance, filename):
    if instance.pk:
        event = Institucion.objects.get(pk=instance.pk)
        event.foto.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'instituciones/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenSubsistema_path(instance, filename):
    if instance.pk:
        event = Subsistema.objects.get(pk=instance.pk)
        event.portada.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'subsistemas/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenSubsistema2_path(instance, filename):
    if instance.pk:
        event = Subsistema.objects.get(pk=instance.pk)
        event.imagen.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'subsistemas/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenSubsistema3_path(instance, filename):
    if instance.pk:
        event = Subsistema.objects.get(pk=instance.pk)
        event.imagen_cp.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'subsistemas/{0}.{1}'.format(uuid.uuid4(), extension)


def Video_path(instance, filename):
    if instance.pk:
        event = Videohome.objects.get(pk=instance.pk)
        event.file.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'video/{0}.{1}'.format(uuid.uuid4(), extension)


def Video2_path(instance, filename):
    if instance.pk:
        event = Videohome.objects.get(pk=instance.pk)
        event.file2.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'video/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenLogo_path(instance, filename):
    if instance.pk:
        event = Logo.objects.get(pk=instance.pk)
        event.logo_actual.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'logo/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenPatrimonio_path(instance, filename):
    if instance.pk:
        event = PatrimonioUnesco.objects.get(pk=instance.pk)
        event.banner.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'patrimonios/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenPatrimonio2_path(instance, filename):
    if instance.pk:
        event = PatrimonioUnesco.objects.get(pk=instance.pk)
        event.imagen.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'patrimonios/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenbannerPatrimonio_path(instance, filename):
    if instance.pk:
        event = PatrimonioUnesco.objects.get(pk=instance.pk)
        event.banner_patrimonio.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'patrimonios/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenbannerPlataforma_path(instance, filename):
    if instance.pk:
        event = BannerPlataforma.objects.get(pk=instance.pk)
        event.banner_plataforma.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'plataforma/{0}.{1}'.format(uuid.uuid4(), extension)


def imagenPlataforma_path(instance, filename):
    if instance.pk:
        event = PlataformaVirtual.objects.get(pk=instance.pk)
        event.imagen.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'plataforma/{0}.{1}'.format(uuid.uuid4(), extension)


def bannerPlataforma_path(instance, filename):
    if instance.pk:
        event = PlataformaVirtual.objects.get(pk=instance.pk)
        event.banner.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'plataforma/{0}.{1}'.format(uuid.uuid4(), extension)


def Pdf_path(instance, filename):
    if instance.pk:
        event = Subsistema.objects.get(pk=instance.pk)
        event.pdf.delete()
    extension = os.path.splitext(filename)[1][1:]
    return 'video/{0}.{1}'.format(uuid.uuid4(), extension)


class BannerPatrimonio(SingletonModel):
    banner_patrimonio = models.ImageField(blank=True, null=False, upload_to=imagenbannerPatrimonio_path,
                                          verbose_name='Banner Principal Patrimonio')

    class Meta:
        verbose_name = 'Banner Principal Patrimonio'

    def __str__(self):
        return self.banner_patrimonio.name


class BannerPlataforma(SingletonModel):
    banner_plataforma = models.ImageField(blank=True, null=False, upload_to=imagenbannerPlataforma_path,
                                          verbose_name='Banner Principal Plataformas')

    class Meta:
        verbose_name = 'Banner Principal Plataforma'

    def __str__(self):
        return self.banner_plataforma.name


class Videohome(SingletonModel):
    file = models.FileField(upload_to=Video_path, null=True, verbose_name="Video Presentacion Inicio")
    file2 = models.FileField(upload_to=Video2_path, null=True, verbose_name="Video Presentacion Inicio para movil")

    class Meta:
        verbose_name = 'Video Presentacion Inicio'

    def __str__(self):
        return self.file.name


class VideoNosotros(SingletonModel):
    video = models.URLField(max_length=512, blank=True, null=True, verbose_name="Video Presentacion Nosotros")

    class Meta:
        verbose_name = 'Video Presentacion Nosotros'

    def __str__(self):
        return self.video


class Logo(SingletonModel):
    logo_actual = models.ImageField(blank=True, null=False, upload_to=imagenLogo_path,
                                    verbose_name='Imagen Logo Actual')

    class Meta:
        verbose_name = 'Logo Gobierno'

    def __str__(self):
        return self.logo_actual.name


class Departamento(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    orden = models.PositiveSmallIntegerField(verbose_name='orden', unique=True)
    portada = models.ImageField(blank=True, null=False, upload_to=imagenDepartamento_path,
                                verbose_name='Imagen de portada')
    latitud = models.CharField(blank=True, null=False, max_length=50, verbose_name='Latitud (Georeferencia)')
    longitud = models.CharField(blank=True, null=False, max_length=50, verbose_name='Longitud (Georeferencia)')
    latitud_2 = models.CharField(blank=True, null=False, max_length=50, verbose_name='Latitud (Georeferencia)')
    longitud_2 = models.CharField(blank=True, null=False, max_length=50, verbose_name='Longitud (Georeferencia)')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Departamentos'
        ordering = ['orden']

    def __str__(self):
        return self.nombre

    def to_json(self):
        return model_to_dict(self)


class Subsistema(Base):
    is_cleaned = False
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    web = models.URLField(max_length=512, blank=True, null=True, verbose_name='Sitio web')
    imagen = models.ImageField(null=True, blank=True, upload_to=imagenSubsistema2_path,
                               verbose_name='Imagen Default Tarjeta')
    imagen_cp = models.ImageField(null=True, blank=True, upload_to=imagenSubsistema3_path,
                                  verbose_name='Imagen Default Tarjeta - Centro Pivado/INATEC')
    portada = models.ImageField(null=True, blank=True, upload_to=imagenSubsistema_path, verbose_name='Imagen Portada')
    pdf = models.FileField(upload_to=Pdf_path, null=True, verbose_name="PDF de las ofertas")
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Subsistemas'

    def __str__(self):
        return self.nombre

    def clean(self):
        self.is_cleaned = True
        user = get_current_authenticated_user()

        find = Subsistema.objects.filter(pk=self.pk).first()  # busca el objeto a modificar
        nombre = find.nombre
        if user.groups.filter(pk=self.pk).exists():  # verifica que posea permisos al subsistema
            exist = user.groups.filter(
                pk=find.pk).exists()  # verifica los permisos del usuario segun objeto a modificar
        else:
            exist = False
        if not exist and not user.is_superuser:
            raise ValidationError(f'Usted no tiene permisos al susbsistema {nombre}')
        super(Subsistema, self).clean()

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()
        super(Subsistema, self).save(*args, **kwargs)


class Noticia(Base):
    is_cleaned = False
    id_subsistema = models.ForeignKey(Subsistema, on_delete=models.PROTECT, verbose_name='Subsistema perteneciente')
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    titulo = models.CharField(max_length=128)
    fecha = models.DateField(verbose_name='Fecha de Noticia')
    descripcion = RichTextField(verbose_name='Descripción', max_length=200)
    link = models.URLField(blank=False, null=False, max_length=512, verbose_name='link del Noticia')
    imagen = models.ImageField(blank=False, null=False, upload_to=imagenNoticia_path, verbose_name='Imagen de noticia')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Noticias'
        ordering = ['-fecha']

    def __str__(self):
        return self.id_subsistema.nombre

    def clean(self):
        self.is_cleaned = True
        user = get_current_authenticated_user()
        if not self.pk:  # verifica que si es un objeto nuevo
            exist = user.groups.filter(pk=self.id_subsistema.pk).exists()  # verifica los permisos del usuario
            nombre = self.id_subsistema.nombre
        else:
            find = Noticia.objects.filter(pk=self.pk).first()  # busca el objeto a modificar
            nombre = find.id_subsistema.nombre
            if user.groups.filter(pk=self.id_subsistema.pk).exists():  # verifica que posea permisos al subsistema
                exist = user.groups.filter(
                    pk=find.id_subsistema.pk).exists()  # verifica los permisos del usuario segun objeto a modificar
            else:
                exist = False
        if not exist and not user.is_superuser:
            raise ValidationError(f'Usted no tiene permisos al susbsistema {nombre}')
        super(Noticia, self).clean()

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()
        super(Noticia, self).save(*args, **kwargs)


class Evento(Base):
    is_cleaned = False
    id_subsistema = models.ForeignKey(Subsistema, on_delete=models.PROTECT, verbose_name='Subsistema perteneciente')
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    titulo = models.CharField(max_length=128)
    fecha = models.DateField(verbose_name='Fecha de Evento')
    descripcion = RichTextField(verbose_name='Descripción', max_length=200)
    link = models.URLField(blank=False, null=False, max_length=512, verbose_name='link del Evento')
    imagen = models.ImageField(blank=False, null=False, upload_to=imagenEvento_path, verbose_name='Imagen de evento')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Eventos'
        ordering = ['-fecha']

    def __str__(self):
        return self.id_subsistema.nombre

    def clean(self):
        self.is_cleaned = True
        user = get_current_authenticated_user()
        if not self.pk:  # verifica que si es un objeto nuevo
            exist = user.groups.filter(pk=self.id_subsistema.pk).exists()  # verifica los permisos del usuario
            nombre = self.id_subsistema.nombre
        else:
            find = Evento.objects.filter(pk=self.pk).first()  # busca el objeto a modificar
            nombre = find.id_subsistema.nombre
            if user.groups.filter(pk=self.id_subsistema.pk).exists():  # verifica que posea permisos al subsistema
                exist = user.groups.filter(
                    pk=find.id_subsistema.pk).exists()  # verifica los permisos del usuario segun objeto a modificar
            else:
                exist = False
        if not exist and not user.is_superuser:
            raise ValidationError(f'Usted no tiene permisos al susbsistema {nombre}')
        super(Evento, self).clean()

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()
        super(Evento, self).save(*args, **kwargs)


class Municipio(Base):
    slug = AutoSlugField(populate_from='nombre', editable=True)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    latitud = models.CharField(blank=True, null=False, max_length=50, verbose_name='Latitud (Georeferencia)')
    longitud = models.CharField(blank=True, null=False, max_length=50, verbose_name='Longitud (Georeferencia)')
    latitud_2 = models.CharField(blank=True, null=False, max_length=50, verbose_name='Latitud (Georeferencia)')
    longitud_2 = models.CharField(blank=True, null=False, max_length=50, verbose_name='Longitud (Georeferencia)')
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    distrito = models.PositiveSmallIntegerField(blank=True, null=False, verbose_name='Distrito (Managua)')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.nombre

    def serialize(self):
        return self.__dict__


class Dashboard(Base):
    is_cleaned = False
    id_subsistema = models.ForeignKey(Subsistema, on_delete=models.PROTECT, verbose_name='Subsistema perteneciente')
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, verbose_name='Departamento')
    anio = models.PositiveSmallIntegerField(default=2022, verbose_name='Año')
    estudiantes_h = models.PositiveIntegerField(verbose_name='Cantidad de estudiantes de sexo Masculino')
    estudiantes_m = models.PositiveIntegerField(verbose_name='Cantidad de estudiantes de sexo femenino')
    estudiante_r = models.PositiveIntegerField(verbose_name='Cantidad de estudiantes de la zona Rural')
    estudiante_u = models.PositiveIntegerField(verbose_name='Cantidad de estudiantes de la zona Urbana')
    estudiantes_i = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                verbose_name='Cantidad de estudiantes Inicial /Mined')
    estudiantes_e = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                verbose_name='Cantidad de estudiantes Especial /Mined')
    estudiantes_p = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                verbose_name='Cantidad de estudiantes Primaria /Mined')
    estudiantes_s = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                verbose_name='Cantidad de estudiantes Secundaria /Mined')
    estudiantes_alf = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                  verbose_name='Cantidad de estudiantes Alfabetizados /Mined')
    estudiantes_f = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                verbose_name='Cantidad de estudiantes Formacion Docente /Mined')
    estudiantes_t = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                verbose_name='Cantidad de estudiantes Bachiller Técnico /Inatec')
    estudiantes_tg = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                 verbose_name='Cantidad de estudiantes Técnico General /Inatec')
    estudiantes_te = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                 verbose_name='Cantidad de estudiantes Técnico Especialista /Inatec')
    estudiantes_ts = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                 verbose_name='Cantidad de estudiantes Técnico Superior /Inatec')
    estudiantes_c = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                verbose_name='Cantidad de estudiantes Capacitacion /Inatec')
    estudiantes_omo = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                  verbose_name='Cantidad de estudiantes Escuela Municipal de Oficio /Inatec')
    estudiantes_fd = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                 verbose_name='Cantidad de estudiantes Formacion Docente /Inatec')
    estudiantes_cap_idioma = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                         verbose_name='Cantidad de estudiantes Idiomas /Inatec')
    estudiantes_tec = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                  verbose_name='Cantidad de estudiantes Educación Tecnica en Campo /Inatec')
    estudiante_rcp = models.PositiveIntegerField(blank=True, default=0, null=False,
                                                 verbose_name='Cantidad de estudiantes Reconocimiento de Competencia Profesionales /Inatec')
    estudiante_af = models.PositiveIntegerField(blank=True, default=0, null=False,
                                                verbose_name='Cantidad de estudiantes sector  Agropecuario y Forestal /Inatec')
    estudiante_ic = models.PositiveIntegerField(blank=True, default=0, null=False,
                                                verbose_name='Cantidad de estudiantes sector industria y Comercial /Inatec')
    estudiante_cs = models.PositiveIntegerField(blank=True, default=0, null=False,
                                                verbose_name='Cantidad de estudiantes sector Comercio y Servicio /Inatec')
    estudiante_fp = models.PositiveIntegerField(blank=True, default=0, null=False,
                                                verbose_name='Cantidad de estudiantes  Forma presencial /Inatec')
    estudiante_fv = models.PositiveIntegerField(blank=True, default=0, null=False,
                                                verbose_name='Cantidad de estudiantes  Forma virtual /Inatec')
    estudiante_d = models.PositiveIntegerField(blank=True, default=0, null=False,
                                               verbose_name='Cantidad de estudiantes  Doctor /CNU')
    estudiante_em = models.PositiveIntegerField(blank=True, default=0, null=False,
                                                verbose_name='Cantidad de estudiantes  Especialista Medico /CNU')
    estudiante_m = models.PositiveIntegerField(blank=True, default=0, null=False,
                                               verbose_name='Cantidad de estudiantes  Master /CNU')
    estudiante_es = models.PositiveIntegerField(blank=True, default=0, null=False,
                                                verbose_name='Cantidad de estudiantes  Especialista /CNU')
    estudiante_l = models.PositiveIntegerField(blank=True, default=0, null=False,
                                               verbose_name='Cantidad de estudiantes  Licenciado o Equivalente /CNU')
    estudiante_tes = models.PositiveIntegerField(blank=True, default=0, null=False,
                                                 verbose_name='Cantidad de estudiantes  Técnico Superios /CNU')
    docente_h = models.PositiveIntegerField(verbose_name='Cantidad de docentes de sexo Masculino')
    docente_m = models.PositiveIntegerField(verbose_name='Cantidad de docentes de sexo femenino')
    egresado_h = models.PositiveIntegerField(verbose_name='Cantidad de estudiantes egresados de sexo Masculino')
    egresado_m = models.PositiveIntegerField(verbose_name='Cantidad de estudiantes egresados de sexo femenino')
    egresado_r = models.PositiveIntegerField(verbose_name='Cantidad de estudiantes egresados de la zona Rural')
    egresado_u = models.PositiveIntegerField(verbose_name='Cantidad de estudiantes egresados de la zona Urbana')
    egresado_t = models.PositiveIntegerField(blank=True, null=False, default=0,
                                             verbose_name='Cantidad de estudiantes Egresado Bachiller Técnico /Inatec')
    egresado_tg = models.PositiveIntegerField(blank=True, null=False, default=0,
                                              verbose_name='Cantidad de estudiantes Egresado Técnico General /Inatec')
    egresado_te = models.PositiveIntegerField(blank=True, null=False, default=0,
                                              verbose_name='Cantidad de estudiantes Egresado  Técnico Especialista /Inatec')
    egresado_ts = models.PositiveIntegerField(blank=True, null=False, default=0,
                                              verbose_name='Cantidad de estudiantes Egresado Técnico Superior /Inatec')
    egresado_c = models.PositiveIntegerField(blank=True, null=False, default=0,
                                             verbose_name='Cantidad de estudiantes Egresado Capacitacion /Inatec')
    egresado_omo = models.PositiveIntegerField(blank=True, null=False, default=0,
                                               verbose_name='Cantidad de estudiantes Egresado Escuela Municipal de Oficio /Inatec')
    egresado_fd = models.PositiveIntegerField(blank=True, null=False, default=0,
                                              verbose_name='Cantidad de estudiantes Egresado Formacion Docente /Inatec')
    egresado_cap_idioma = models.PositiveIntegerField(blank=True, null=False, default=0,
                                                      verbose_name='Cantidad de estudiantes Egresado Idiomas /Inatec')
    egresado_tec = models.PositiveIntegerField(blank=True, null=False, default=0,
                                               verbose_name='Cantidad de estudiantes Egresado Educación Tecnica en Campo /Inatec')
    egresado_rcp = models.PositiveIntegerField(blank=True, default=0, null=False,
                                               verbose_name='Cantidad de estudiantes Egresado Reconocimiento de Competencia Profesionales /Inatec')
    egresado_p = models.PositiveIntegerField(blank=True, default=0, null=False,
                                             verbose_name='Cantidad de estudiantes Egresado  Posgrado /CNU')
    egresado_l = models.PositiveIntegerField(blank=True, default=0, null=False,
                                             verbose_name='Cantidad de estudiantes Egresado  Licenciado o Equivalente /CNU')
    egresado_tes = models.PositiveIntegerField(blank=True, default=0, null=False,
                                               verbose_name='Cantidad de estudiantes Egresado Técnico Superios /CNU')
    becas_e = models.PositiveIntegerField(blank=True, default=0, null=False,
                                          verbose_name='Cantidad de estudiantes Becas Especiales /CNU')
    becas_a = models.PositiveIntegerField(blank=True, default=0, null=False,
                                          verbose_name='Cantidad de estudiantes Becas Aranceles /CNU')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        ordering = ['id_subsistema']
        verbose_name_plural = 'Dashboard Subsistema'

    def __str__(self):
        return self.id_subsistema.nombre

    def clean(self):
        self.is_cleaned = True
        user = get_current_authenticated_user()

        save = True
        mensaje = 'Usted no tiene permisos al susbsistema '
        # total = self.estudiantes_h + self.estudiantes_m
        # total_rango = self.edad_3a5 + self.edad_6a11 + self.edad_12a18 + self.edad_18
        # total_zona = self.estudiante_r + self.estudiante_u
        #
        # if total == total_rango:
        #     if total != total_zona:
        #         mensaje = 'La suma total por zona es diferente al total de estudiantes (Femenino + Masculino) '
        #         save = False
        # else:
        #     mensaje = 'La suma total por rango de edad es diferente al total de estudiantes (Femenino + Masculino) '
        #     save = False

        if not self.pk:  # verifica que si es un objeto nuevo
            exist = user.groups.filter(pk=self.id_subsistema.pk).exists()  # verifica los permisos del usuario
            nombre = self.id_subsistema.nombre
        else:
            find = Dashboard.objects.filter(pk=self.pk).first()  # busca el objeto a modificar
            nombre = find.id_subsistema.nombre
            if user.groups.filter(pk=self.id_subsistema.pk).exists():  # verifica que posea permisos al subsistema
                exist = user.groups.filter(
                    pk=find.id_subsistema.pk).exists()  # verifica los permisos del usuario segun objeto a modificar
            else:
                exist = False

        if not save:  # Verifica si los datos estan correctos
            raise ValidationError(f'{mensaje}')
        else:
            if not exist and not user.is_superuser:  # Verifica permisos
                raise ValidationError(f'{mensaje} {nombre}')
        super(Dashboard, self).clean()

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()
        super(Dashboard, self).save(*args, **kwargs)


class Oferta(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    tipo = models.IntegerField(choices=TIPO, default=1, verbose_name='Tipo Institucion')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        return self.nombre


class Modalidad(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return self.nombre


class Institucion(Base):
    is_cleaned = False
    id_subsistema = models.ForeignKey(Subsistema, on_delete=models.PROTECT, verbose_name='Subsistema perteneciente')
    id_municipo = models.ForeignKey(Municipio, on_delete=models.PROTECT, verbose_name='Municipio')
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    direccion = RichTextField(verbose_name='Dirección', max_length=256)
    telefono = models.CharField(max_length=60, verbose_name='Teléfono')
    web = models.URLField(max_length=512, blank=True, null=True, verbose_name='Sitio web')
    latitud = models.CharField(blank=True, null=False, max_length=50, verbose_name='Latitud (Georeferencia)')
    longitud = models.CharField(blank=True, null=False, max_length=50, verbose_name='Longitud (Georeferencia)')
    tipo = models.IntegerField(choices=TIPO, default=1, verbose_name='Tipo Institucion')
    sector = models.CharField(choices=SECTORES_INATEC, blank=True, null=False, max_length=10,
                              verbose_name='Sector - Inatec')
    foto = models.ImageField(blank=True, null=False, upload_to=imagenInstituciones_path,
                             verbose_name='Imagen de la Institucion o Centro')
    id_oferta = models.ManyToManyField(Oferta, blank=True, verbose_name='Ofertas que posee la institucion')
    id_modalidad = models.ManyToManyField(Modalidad, blank=True, verbose_name='Modalidades')
    codigoestablecimiento = models.CharField(blank=True, null=False, max_length=10,
                                             verbose_name='Codigo Establecimiento/ MINED')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Instituciones'

    def __str__(self):
        return self.nombre

    def clean(self):
        self.is_cleaned = True
        user = get_current_authenticated_user()
        if not self.pk:  # verifica que si es un objeto nuevo
            exist = user.groups.filter(pk=self.id_subsistema.pk).exists()  # verifica los permisos del usuario
            nombre = self.id_subsistema.nombre
        else:
            find = Institucion.objects.filter(pk=self.pk).first()  # busca el objeto a modificar
            nombre = find.id_subsistema.nombre
            if user.groups.filter(pk=self.id_subsistema.pk).exists():  # verifica que posea permisos al subsistema
                exist = user.groups.filter(
                    pk=find.id_subsistema.pk).exists()  # verifica los permisos del usuario segun objeto a modificar
            else:
                exist = False
        if not exist and not user.is_superuser:
            raise ValidationError(f'Usted no tiene permisos al susbsistema {nombre}')
        super(Institucion, self).clean()

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()
        super(Institucion, self).save(*args, **kwargs)


class ClasificacionUnesco(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Clasificación Unesco'

    def __str__(self):
        return self.nombre


class PatrimonioUnesco(Base):
    id_clasificacion = models.ForeignKey(ClasificacionUnesco, on_delete=models.PROTECT, verbose_name='Clasificacion')
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    descripcion = RichTextField(verbose_name='Descripción')
    latitud = models.CharField(blank=True, null=False, max_length=50, verbose_name='Latitud (Georeferencia)')
    longitud = models.CharField(blank=True, null=False, max_length=50, verbose_name='Longitud (Georeferencia)')
    latitud_2 = models.CharField(blank=True, null=False, max_length=50, verbose_name='Latitud 2(Georeferencia)')
    longitud_2 = models.CharField(blank=True, null=False, max_length=50, verbose_name='Longitud 2(Georeferencia)')
    id_municipio = models.ManyToManyField(Municipio, blank=True, verbose_name='Municipios que l@ conforman')
    url_unesco = models.URLField(max_length=512, blank=True, null=True, verbose_name='URL Unesco')
    link_2 = models.URLField(max_length=512, blank=True, null=True, verbose_name='Link fuente 2')
    link_3 = models.URLField(max_length=512, blank=True, null=True, verbose_name='Link fuente 3')
    banner = models.ImageField(null=True, blank=True, upload_to=imagenPatrimonio_path,
                               verbose_name='Banner del Patrimonio')
    imagen = models.ImageField(null=True, blank=True, upload_to=imagenPatrimonio2_path,
                               verbose_name='Imagen Tarjeta')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Patrimonios Unesco'

    def __str__(self):
        return self.nombre


class PlataformaVirtual(Base):
    nombre = models.CharField(max_length=128, verbose_name='Nombre')
    descripcion = RichTextField(verbose_name='Descripción')
    url = models.URLField(max_length=512, blank=True, null=True, verbose_name='URL')
    imagen = models.ImageField(null=True, blank=True, upload_to=imagenPlataforma_path, verbose_name='Imagen Tarjeta')
    banner = models.ImageField(null=True, blank=True, upload_to=bannerPlataforma_path, verbose_name='Banner Principal')
    orden = models.IntegerField(blank=True, null=True, default=0, verbose_name='Orden')
    estado = models.IntegerField(choices=ESTADO, default=1, verbose_name='Estado')

    class Meta:
        verbose_name_plural = 'Plataformas virtuales'

    def __str__(self):
        return self.nombre
