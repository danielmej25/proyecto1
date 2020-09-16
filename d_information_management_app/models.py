from django.db import models

# Create your models here.

# Clase que contiene la informacion basica de los Grupos de Investigacion
class grupoInvestigacion(object):

    # Se usara una abreviacion para las palabras GrupoInvestigacion como GI, AreaConocimiento como AC
    def __init__(self, parIdGI, parIdInstitucion, parIdAC, parIdDirector, parNombre, parAnyoFundacion, 
                parEmail, parCategoria):
        self.idGrupoInvestigacion = parIdGI
        self.idInstitucion = parIdInstitucion
        self.idAreaConocimiento = parIdAC
        self.idDirector = parIdDirector
        self.nombre = parNombre
        self.anyoFundacion = parAnyoFundacion
        self.email = parEmail
        self.categoria = parCategoria

# Metodo para la creacion de un objeto de la clase Grupo de Investigacion
def crearGrupoInvestigacion(request, parIdGI, parIdInstit, parIdAC, parIdDirector, parNombre, parAnyoFundac, 
                parEmail, parCategoria):
        
        # Aqui va el codigo para ingresar los datos en la base de datos
        # Tambien va el control de excepciones 
        # Y los condicionales para saber que retornar

        objGrupoInv1 = grupoInvestigacion(parIdGI, parIdInstit, parIdAC, parIdDirector, parNombre, parAnyoFundac, 
                parEmail, parCategoria)

        return HttpResponse(objGrupoInv1)