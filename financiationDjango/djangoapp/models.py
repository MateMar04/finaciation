# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asesorados(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    cuil = models.BigIntegerField(db_column='CUIL', blank=False, null=False)
    nombre = models.CharField(db_column='NOMBRE', max_length=70, blank=False, null=False)
    apellido = models.CharField(db_column='APELLIDO', max_length=70, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'asesorados'


class Convenios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenios'


class DepartamentosCiudad(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=70, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos_ciudad'


class DepartamentosDelMinisterio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos_del_ministerio'


class Direcciones(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    calle = models.CharField(db_column='CALLE', max_length=70, blank=False, null=False)
    altura = models.IntegerField(db_column='ALTURA', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'direcciones'


class EmailsReferentesContactados(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    mail = models.CharField(db_column='MAIL', max_length=100, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'emails_referentes_contactados'


class EmailsUsuarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    mail = models.CharField(db_column='MAIL', max_length=100, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'emails_usuarios'


class EstadosDeUsuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_de_usuario'


class EstadosDeVerificacionDeUsuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_de_verificacion_de_usuario'


class EstadosDeVisita(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estados_de_visita'


class Faqs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    pregunta = models.TextField(db_column='PREGUNTA', blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'faqs'


class Intendentes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=70, blank=False, null=False)
    apellido = models.CharField(db_column='APELLIDO', max_length=70, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'intendentes'


class Localidades(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=70, blank=False, null=False)
    id_departamento = models.ForeignKey(DepartamentosCiudad, models.DO_NOTHING, db_column='ID_DEPARTAMENTO',
                                        blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'localidades'


class Logos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logos'


class MarcasDeVehiculos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'marcas_de_vehiculos'


class ModelosDeVehiculos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=False, null=False)
    id_marca = models.ForeignKey(MarcasDeVehiculos, models.DO_NOTHING, db_column='ID_MARCA', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'modelos_de_vehiculos'


class PartidosPoliticos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partidos_politicos'


class PatentesDeVehiculos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    patente = models.CharField(db_column='PATENTE', max_length=7, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'patentes_de_vehiculos'


class Roles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class TelefonosReferentesContactados(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    telefono = models.BigIntegerField(db_column='TELEFONO', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'telefonos_referentes_contactados'


class ReferentesContactados(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=70, blank=False, null=False)
    apellido = models.CharField(db_column='APELLIDO', max_length=70, blank=False,
                                null=False)

    class Meta:
        managed = False
        db_table = 'referentes_contactados'


class Usuarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre_de_usuario = models.CharField(db_column='NOMBRE_DE_USUARIO', max_length=30, blank=False, null=False)
    cuil = models.BigIntegerField(db_column='CUIL', blank=False, null=False)
    contrasenia = models.TextField(db_column='CONTRASENIA', blank=False, null=False)
    foto_de_perfil = models.TextField(db_column='FOTO_DE_PERFIL', blank=True, null=True)
    id_email = models.ManyToManyField(EmailsUsuarios, db_column='ID_EMAIL')
    id_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='ID_ROL', blank=False, null=False)
    id_estado_de_verificacion = models.ForeignKey(EstadosDeVerificacionDeUsuario, models.DO_NOTHING,
                                                  db_column='ID_ESTADO_DE_VERIFICACION', blank=False, null=False)
    id_estado_de_usuario = models.ForeignKey(EstadosDeUsuario, models.DO_NOTHING, db_column='ID_ESTADO_DE_USUARIO',
                                             blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Grupos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=70, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'grupos'


class Vehiculos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    id_patente = models.ForeignKey(PatentesDeVehiculos, models.DO_NOTHING, db_column='ID_PATENTE', blank=False,
                                   null=False)
    id_marca = models.ForeignKey(MarcasDeVehiculos, models.DO_NOTHING, db_column='ID_MARCA', blank=False, null=False)
    id_modelo = models.ForeignKey(ModelosDeVehiculos, models.DO_NOTHING, db_column='ID_MODELO', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'vehiculos'


class Visitas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    flyer = models.IntegerField(db_column='FLYER', blank=False, null=False)
    distancia = models.IntegerField(db_column='DISTANCIA', blank=False, null=False)
    tiempo_de_viaje = models.IntegerField(db_column='TIEMPO_DE_VIAJE', blank=False, null=False)
    fecha_de_visita = models.DateField(db_column='FECHA_DE_VISITA', blank=False, null=False)
    registro_civil = models.IntegerField(db_column='REGISTRO_CIVIL', blank=False, null=False)
    hospedaje = models.IntegerField(db_column='HOSPEDAJE', blank=False, null=False)
    fondo_de_modernizacion = models.IntegerField(db_column='FONDO_DE_MODERNIZACION', blank=False, null=False)
    horario_inicio = models.DateTimeField(db_column='HORARIO_INICIO', blank=False, null=False)
    horario_finalizacion = models.DateTimeField(db_column='HORARIO_FINALIZACION', blank=False, null=False)
    nombre_lugar = models.CharField(db_column='NOMBRE_LUGAR', max_length=70, blank=False, null=False)
    id_localidad = models.ForeignKey(Localidades, models.DO_NOTHING, db_column='ID_LOCALIDAD', blank=False, null=False)
    id_grupo = models.ForeignKey(Grupos, models.DO_NOTHING, db_column='ID_GRUPO', blank=False, null=False)
    id_estado_de_visita = models.ForeignKey(EstadosDeVisita, models.DO_NOTHING, db_column='ID_ESTADO_DE_VISITA',
                                            blank=False, null=False)
    id_convenio_firmado = models.ManyToManyField(Convenios, db_column='ID_CONVENIO_FIRMADO')
    id_referente_contactado = models.ForeignKey(ReferentesContactados, models.DO_NOTHING,
                                                db_column='ID_REFERENTE_CONTACTADO', blank=False, null=False)
    id_direccion = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='ID_DIRECCION', blank=False, null=False)
    id_logo = models.ManyToManyField(Logos, db_column='ID_LOGO')

    class Meta:
        managed = False
        db_table = 'visitas'


class EstadoDeConsulta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=False, null=False)
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_de_consulta'


class Consultas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_visita = models.ForeignKey('Visitas', models.DO_NOTHING, db_column='ID_VISITA', blank=False, null=False)
    id_asesorado = models.ForeignKey(Asesorados, models.DO_NOTHING, db_column='ID_ASESORADO', blank=False, null=False)
    id_asesor = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ID_ASESOR', blank=False, null=False)
    id_departamento_ministerio = models.ForeignKey('DepartamentosDelMinisterio', models.DO_NOTHING,
                                                   db_column='ID_DEPARTAMENTO_MINISTERIO', blank=False, null=False)
    id_faq = models.ForeignKey('Faqs', models.DO_NOTHING, db_column='ID_FAQ', blank=False, null=False)
    id_estado = models.ForeignKey('EstadoDeConsulta', models.DO_NOTHING, db_column='ID_ESTADO', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'consultas'


class Coordinadores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    id_usuario = models.OneToOneField('Usuarios', models.DO_NOTHING, db_column='ID_USUARIO', blank=False, null=False)
    id_grupo = models.ForeignKey('Grupos', models.DO_NOTHING, db_column='ID_GRUPO', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'coordinadores'


class Asesores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ID_USUARIO', blank=False, null=False)
    id_grupo = models.ForeignKey('Grupos', models.DO_NOTHING, db_column='ID_GRUPO', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'asesores'
        unique_together = (('id_usuario', 'id_grupo'),)


class EmailsIntendentes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    mail = models.CharField(db_column='MAIL', max_length=100, blank=False, null=False)
    id_intendente = models.ForeignKey('Intendentes', models.DO_NOTHING, db_column='ID_INTENDENTE', blank=False,
                                      null=False)

    class Meta:
        managed = False
        db_table = 'emails_intendentes'


class EmailsReferentesContactados(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    mail = models.CharField(db_column='MAIL', max_length=100, blank=False, null=False)
    id_referente = models.ForeignKey('ReferentesContactados', models.DO_NOTHING, db_column='ID_REFERENTE', blank=False,
                                     null=False)

    class Meta:
        managed = False
        db_table = 'emails_referentes_contactados'


class EmailsUsuarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    mail = models.CharField(db_column='MAIL', max_length=100, blank=False, null=False)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='ID_USUARIO', blank=False,
                                   null=False)

    class Meta:
        managed = False
        db_table = 'emails_usuarios'


class TelefonosIntendentes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    telefono = models.BigIntegerField(db_column='TELEFONO', blank=False, null=False)
    id_intendente = models.ForeignKey(Intendentes, models.DO_NOTHING, db_column='ID_INTENDENTE', blank=False,
                                      null=False)

    class Meta:
        managed = False
        db_table = 'telefonos_intendentes'


class TelefonosReferentesContactados(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    telefono = models.BigIntegerField(db_column='TELEFONO', blank=False, null=False)
    id_referente = models.ForeignKey(ReferentesContactados, models.DO_NOTHING, db_column='ID_REFERENTE', blank=False,
                                     null=False)

    class Meta:
        managed = False
        db_table = 'telefonos_referentes_contactados'
