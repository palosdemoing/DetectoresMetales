from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Expedientes(models.Model):
    ID_expediente = models.AutoField(verbose_name='ID_Expediente', serialize=False, auto_created=True, primary_key=True)
    expediente = models.TextField(_('Expediente'), max_length=50, blank=True, null=True) # unique
    fecha_solicitud = models.DateTimeField(_('Fecha de Solicitud'))

    class Meta:
#        abstract = True
        verbose_name = _('Expediente')
        verbose_name_plural = _('Expedientes')
        ordering = ['ID_expediente']

    def __str__(self):
        return self.expediente

'''
python manage inspectdb ----------------------- (ya vere como)

CREATE TABLE `DETECTORES` (
  `Id` INTEGER NOT NULL AUTO_INCREMENT, 
  `SOLICITANTE` VARCHAR(50), 
  `DON` VARCHAR(50), 
  `DNI` VARCHAR(50), 
  `DOMICILIO` VARCHAR(50), 
  `LOCALIDAD` VARCHAR(50), 
  `PROVINCIA` VARCHAR(50), 
  `CP` VARCHAR(50), 
  `EXPEDIENTE` VARCHAR(50), 
  `ANIO` INTEGER DEFAULT 0, 
  `FECHA_SOLICITUD` DATETIME, 
  `FAVORABLES` TINYINT(1), 
  `DESFAVORABLES` TINYINT(1), 
  `FECHA_SUBSANACION` DATETIME, 
  `FECHA_CONST_SUBSANACION` DATETIME, 
  `FECHA_RESOLUCION` DATETIME, 
  `FECHA_ACUSE_RESOLUCION` DATETIME, 
  `NOTIFICACION_EN_MANO` TINYINT(1), 
  `NOTIFICACION_EMAIL_CON_ACUSE` TINYINT(1), 
  `SUBSANACION` TINYINT(1), 
  `VIGENCIA` DATETIME, 
  `ARCHIVADO` TINYINT(1), 
  `ENVIADO_A_FIRMA` TINYINT(1), 
  `TIEMPO` INTEGER DEFAULT 0, 
  `NO_CONFORMIDAD` TINYINT(1), 
  `FECHA_RECURSO_ALZADA` DATETIME, 
  `FECHA_REMISION_SGT` DATETIME, 
  `FAVORABLE_A_DT` TINYINT(1), 
  `INSATISFACCION` TINYINT(1), 
  `OBSERVACIONES` VARCHAR(100), 
  `ARCHIVADOR` VARCHAR(50), 
  `TOTAS_LAS_PLAYAS` TINYINT(1), 
  `FECHA_SOL1` DATETIME, 
  `ZF1` VARCHAR(50), 
  `ZF2` VARCHAR(50), 
  `ZF3` VARCHAR(50), 
  `ZF4` VARCHAR(50), 
  `ZF5` VARCHAR(50), 
  `ZF6` VARCHAR(50), 
  `ZF7` VARCHAR(50), 
  `ZF8` VARCHAR(50), 
  `ZF9` VARCHAR(50), 
  `ZF10` VARCHAR(50), 
  `ZF11` VARCHAR(50), 
  `ZF12` VARCHAR(50), 
  `ZF13` VARCHAR(50), 
  `ZF14` VARCHAR(50), 
  `ZF15` VARCHAR(50), 
  `ZF16` VARCHAR(50), 
  `ZF17` VARCHAR(50), 
  `ZF18` VARCHAR(50), 
  `ZD1` VARCHAR(50), 
  `ZD2` VARCHAR(50), 
  `ZD3` VARCHAR(50), 
  `ZD4` VARCHAR(50), 
  `ZD5` VARCHAR(50), 
  `ZD6` VARCHAR(50), 
  `ZD7` VARCHAR(50), 
  `ZD8` VARCHAR(50), 
  `ZD9` VARCHAR(50), 
  `ZD10` VARCHAR(50), 
  `ZD11` VARCHAR(50), 
  `ZD12` VARCHAR(50), 
  `ZD13` VARCHAR(50), 
  `ZD14` VARCHAR(50), 
  `ZD15` VARCHAR(50), 
  `ZD16` VARCHAR(50), 
  `ZD17` VARCHAR(50), 
  `ZD18` VARCHAR(50), 
  `ZD19` VARCHAR(50), 
  `ZD20` VARCHAR(50), 
  `ZD21` VARCHAR(50), 
  `IF1` VARCHAR(50), 
  `IF2` VARCHAR(50), 
  `IF3` VARCHAR(50), 
  `IF4` VARCHAR(50), 
  `IF5` VARCHAR(50), 
  `IF6` VARCHAR(50), 
  `IF7` VARCHAR(50), 
  `IF8` VARCHAR(50), 
  `IF9` VARCHAR(50), 
  `IF10` VARCHAR(50), 
  `IF11` VARCHAR(50), 
  `IF12` VARCHAR(50), 
  `IF13` VARCHAR(50), 
  `IF14` VARCHAR(50), 
  `IF15` VARCHAR(50), 
  `IF16` VARCHAR(50), 
  `IF17` VARCHAR(50), 
  `IF18` VARCHAR(50), 
  `FF1` VARCHAR(50), 
  `FF2` VARCHAR(50), 
  `FF3` VARCHAR(50), 
  `FF4` VARCHAR(50), 
  `FF5` VARCHAR(50), 
  `FF6` VARCHAR(50), 
  `FF7` VARCHAR(50), 
  `FF8` VARCHAR(50), 
  `FF9` VARCHAR(50), 
  `FF10` VARCHAR(50), 
  `FF11` VARCHAR(50), 
  `FF12` VARCHAR(50), 
  `FF13` VARCHAR(50), 
  `FF14` VARCHAR(50), 
  `FF15` VARCHAR(50), 
  `FF16` VARCHAR(50), 
  `FF17` VARCHAR(50), 
  `FF18` VARCHAR(50), 
  `LOC1` VARCHAR(50), 
  `LOC2` VARCHAR(50), 
  `LOC3` VARCHAR(50), 
  `LOC4` VARCHAR(50), 
  `LOC5` VARCHAR(50), 
  `LOC6` VARCHAR(50), 
  `LOC7` VARCHAR(50), 
  `LOC8` VARCHAR(50), 
  `LOC9` VARCHAR(50), 
  `LOC10` VARCHAR(50), 
  `LOC11` VARCHAR(50), 
  `LOC12` VARCHAR(50), 
  `LOC13` VARCHAR(50), 
  `LOC14` VARCHAR(50), 
  `LOC15` VARCHAR(50), 
  `LOC16` VARCHAR(50), 
  `LOC17` VARCHAR(50), 
  `LOC18` VARCHAR(50), 
  `ID1` VARCHAR(50), 
  `ID2` VARCHAR(50), 
  `ID3` VARCHAR(50), 
  `ID4` VARCHAR(50), 
  `ID5` VARCHAR(50), 
  `ID6` VARCHAR(50), 
  `ID7` VARCHAR(50), 
  `ID8` VARCHAR(50), 
  `ID9` VARCHAR(50), 
  `ID10` VARCHAR(50), 
  `ID11` VARCHAR(50), 
  `ID12` VARCHAR(50), 
  `ID13` VARCHAR(50), 
  `ID14` VARCHAR(50), 
  `ID15` VARCHAR(50), 
  `ID16` VARCHAR(50), 
  `ID17` VARCHAR(50), 
  `ID18` VARCHAR(50), 
  `ID19` VARCHAR(50), 
  `ID20` VARCHAR(50), 
  `FD1` VARCHAR(50), 
  `FD2` VARCHAR(50), 
  `FD3` VARCHAR(50), 
  `FD4` VARCHAR(50), 
  `FD5` VARCHAR(50), 
  `FD6` VARCHAR(50), 
  `FD7` VARCHAR(50), 
  `FD8` VARCHAR(50), 
  `FD9` VARCHAR(50), 
  `FD10` VARCHAR(50), 
  `FD11` VARCHAR(50), 
  `FD12` VARCHAR(50), 
  `FD13` VARCHAR(50), 
  `FD14` VARCHAR(50), 
  `FD15` VARCHAR(50), 
  `FD16` VARCHAR(50), 
  `FD17` VARCHAR(50), 
  `FD18` VARCHAR(50), 
  `FD19` VARCHAR(50), 
  `FD20` VARCHAR(50), 
  `BIC1` VARCHAR(50), 
  `BIC2` VARCHAR(50), 
  `BIC3` VARCHAR(50), 
  `BIC4` VARCHAR(50), 
  `BIC5` VARCHAR(50), 
  `BIC6` VARCHAR(50), 
  `BIC7` VARCHAR(50), 
  `BIC8` VARCHAR(50), 
  `BIC9` VARCHAR(50), 
  `BIC10` VARCHAR(50), 
  `BIC11` VARCHAR(50), 
  `BIC12` VARCHAR(50), 
  `BIC13` VARCHAR(50), 
  `BIC14` VARCHAR(50), 
  `BIC15` VARCHAR(50), 
  `BIC16` VARCHAR(50), 
  `BIC17` VARCHAR(50), 
  `BIC18` VARCHAR(50), 
  `BIC19` VARCHAR(50), 
  `BIC20` VARCHAR(50), 
  `BIC21` VARCHAR(50), 
  `ZSA1` VARCHAR(50), 
  `ZSA2` VARCHAR(50), 
  `ZSA3` VARCHAR(50), 
  `ZSA4` VARCHAR(50), 
  `ZSA5` VARCHAR(50), 
  `ZSA6` VARCHAR(50), 
  `ZSA7` VARCHAR(50), 
  `ZSA8` VARCHAR(50), 
  `ZSA9` VARCHAR(50), 
  `ZSA10` VARCHAR(50), 
  `ZSA11` VARCHAR(50), 
  `ZSA12` VARCHAR(50), 
  `ZSA13` VARCHAR(50), 
  `ZSA14` VARCHAR(50), 
  `ZSA15` VARCHAR(50), 
  `ZSA16` VARCHAR(50), 
  `ZSA17` VARCHAR(50), 
  `ZSA18` VARCHAR(50), 
  `ZSA19` VARCHAR(50), 
  `ZSA20` VARCHAR(50), 
  `ZSA21` VARCHAR(50), 
  `YAC1` VARCHAR(50), 
  `YAC2` VARCHAR(50), 
  `YAC3` VARCHAR(50), 
  `YAC4` VARCHAR(50), 
  `YAC5` VARCHAR(50), 
  `YAC6` VARCHAR(50), 
  `YAC7` VARCHAR(50), 
  `YAC8` VARCHAR(50), 
  `YAC9` VARCHAR(50), 
  `YAC10` VARCHAR(50), 
  `YAC11` VARCHAR(50), 
  `YAC12` VARCHAR(50), 
  `YAC13` VARCHAR(50), 
  `YAC14` VARCHAR(50), 
  `YAC15` VARCHAR(50), 
  `YAC16` VARCHAR(50), 
  `YAC17` VARCHAR(50), 
  `YAC18` VARCHAR(50), 
  `YAC19` VARCHAR(50), 
  `YAC20` VARCHAR(50), 
  `YAC21` VARCHAR(50), 
  `LD1` VARCHAR(50), 
  `LD2` VARCHAR(50), 
  `LD3` VARCHAR(50), 
  `LD4` VARCHAR(50), 
  `LD5` VARCHAR(50), 
  `LD6` VARCHAR(50), 
  `LD7` VARCHAR(50), 
  `LD8` VARCHAR(50), 
  `LD9` VARCHAR(50), 
  `LD10` VARCHAR(50), 
  `LD11` VARCHAR(50), 
  `LD12` VARCHAR(50), 
  `LD13` VARCHAR(50), 
  `LD14` VARCHAR(50), 
  `LD15` VARCHAR(50), 
  `LD16` VARCHAR(50), 
  `LD17` VARCHAR(50), 
  `LD18` VARCHAR(50), 
  `LD19` VARCHAR(50), 
  `LD20` VARCHAR(50), 
  `LD21` VARCHAR(50), 
  `NUMFAV` INTEGER DEFAULT 0, 
  `NUMDESF` INTEGER DEFAULT 0, 
  `TUTOR` VARCHAR(50), 
  `DNI_TUTOR` VARCHAR(50), 
  `MENOR` TINYINT(1), 
  UNIQUE (`EXPEDIENTE`), 
  INDEX (`Id`), 
  INDEX (`ID1`), 
  INDEX (`ID10`), 
  INDEX (`ID11`), 
  INDEX (`ID12`), 
  INDEX (`ID13`), 
  INDEX (`ID14`), 
  INDEX (`ID15`), 
  INDEX (`ID16`), 
  INDEX (`ID17`), 
  INDEX (`ID18`), 
  INDEX (`ID19`), 
  INDEX (`ID2`), 
  INDEX (`ID20`), 
  INDEX (`ID3`), 
  INDEX (`ID4`), 
  INDEX (`ID5`), 
  INDEX (`ID6`), 
  INDEX (`ID7`), 
  INDEX (`ID8`), 
  INDEX (`ID9`), 
  PRIMARY KEY (`Id`)
) ENGINE=innodb;
'''


'''
Los modelos sirven para comunicarnos con la Base de Datos: 
hacer consultas, crear objetos, modificarlos o borrarlos.

Los modelos son clases python (con algo de magia) que heredan 
de models.Model (from django.db import models), las cuales representan 
una tabla, y cada uno de sus atributos una columna:

    class User(models.Model):
        username = models.CharField(_('username'), max_length=30, unique=True)  # _('username') permitira traduccion
        first_name = models.CharField(_('first name'), max_length=30, blank=True)
        last_name = models.CharField(_('last name'), max_length=30, blank=True)
        email = models.EmailField(_('e-mail address'), blank=True)
        password = models.CharField(_('password'), max_length=128)
        ....


Pueden existir modelos que no tengan correspondencia con tablas, 
modelos abstractos. Estos lo que sirven es para no duplicar codigo. 
Imaginamos que tenemos por ejemplo noticias y eventos en nuestro 
portal los cuales queremos que sean tablas diferentes, pero sin 
embargo vemos que tienen campos y funcionalidad comun, pues podemos 
crear una clase base y agruparlos: 

    class BaseNews(models.Model):
        title = models.CharField(_('slug'), max_length=250)
        slug = models.CharField(_('title'), max_length=250, unique=True)

        class Meta:
            abstract = True

        def __str__(self):
            return self.title


    class NewsItem(BaseNews):

        publish_date = models.DateTimeField(verbose_name=_(u"Publish date"))
        owner = models.ForeignKey(User, verbose_name=_(u'Owner'))


    class Event(BaseNews):

        start_date = models.DateTimeField(verbose_name=_(u"Start date"))
        end_date = models.DateTimeField(verbose_name=_(u"End date"), null=True, blank=True)


Si quisieramos que en vez de ser dos tablas independientes 
fueran tres tablas, una con los datos comunes y dos con los 
especificos no pondriamos "abstract = True"

Los modelos se pueden relacionar por 3 tipo de relaciones:

     Campo OneToOneField: Uno a uno.
     
     Campo ForeignKey, uno a muchos.
     
     Campo ManyToManyField, muchos a muchos, realmente Django 
     introduce una tabla intermedia. Hay que tener cuidado ya 
     que al hacer un guardado o una actualizacion en la BD esta 
     se hace tras guardar el resto de campo del modelo.

Ademas de estas relaciones si un modelo esta conectado a otro, desde 
el segundo podemos acceder al primero por la relacion inversa, 
un atributo que Django nos aniade automaticamente al segundo modelo. 
Es decir si tenemos el anterior ejemplo, desde un usuario podremos 
acceder a todos sus noticias escribiendo el nombre del modelo seguido 
de un guion bajo y la palabra set, en el caso de que la relacion sea 
un OneToOneField seria sin "_set" :

    user = User.objects.get(username=XXXX)
    ....

    user.newsitem_set.all()


De igual manera seria si el campo fuera un M2M, en caso de que fuera un OneToOne seria:


    user = User.objects.get(username=XXXX)
    ....

    user.newsitem.get()
    

Este nombre se puede personalizar:

    owner = models.ForeignKey(User, verbose_name=_(u'Owner'), related_name="XXX")
    

Los modelos tienen un campo clean en el cual se pueden validar los datos. 







'''
