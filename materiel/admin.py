from django.contrib import admin
from .models import Categorie, Materiel, Mouvement
# Register your models here.


# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    search_fields = ["nom",]
    list_display = ('nom', 'active', 'created', 'date_update', )


# Register your models here.
@admin.register(Materiel)
class MaterielAdmin(admin.ModelAdmin):
    search_fields = ["nom",'categorie__nom', 'prix_unitaire', 'quantite',]
    list_display = ('nom', 'categorie', 'prix_unitaire', 'quantite', 'active', 'created', 'date_update', )


# Register your models here.
@admin.register(Mouvement)
class MouvementAdmin(admin.ModelAdmin):
    search_fields = ['materiel__nom', 'effectue_pa__user__nom', 'projet__nom', 'type_mouvement']
    list_display = ('materiel', 'effectue_par', 'projet', 'type_mouvement', 'quantite', 'active', 'created', 'date_update', )