from django.contrib import admin
from .models import Perfil

#admin.site.register(Perfil)

@admin.register(Perfil)
#paso por medio del decorador la clase y como quiere que se vea en el admmon
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nombre','puesto','descripccion']
            