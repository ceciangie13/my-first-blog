# Create your models here.
#Este es un lugar en el cual definiremos nuestra entrada del blog.

#Líneas from e import es para traer archivos desde ciertas capetas
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # class, para definir un objeto; Post, el nombre del modelo o molde para hacer galletas, models.Model significa que Post es un modelo de django
    #abajo se encuentran las propiedades que tendrá cada modelo
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #este es una relación (link) con otro modelo
    title = models.CharField(max_length=200) # así se define un texto con un número limitado de caracteres
    text = models.TextField() #Texto largo sin límite de carácteres. 
    created_date = models.DateTimeField( #este es fecha y hora
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
  #La identación, es decir, los espacios o sangrías hacia la derecha son muy IMPORTANTES en Python
    def publish(self): #Cuando empieza con def es para las acciones/métodos, en este caso de publish
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title