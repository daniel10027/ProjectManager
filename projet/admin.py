from django.contrib import admin
from .models import (Categorie, Projet, DevisProjet, ElementDevis, Equipe)


# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    search_fields = ["nom",]
    list_display = ('nom', 'active', 'created', 'date_update', )


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    search_fields = ["nom", "categorie__nom", "proprietaire__user__nom",
                     "proprietaire__user__prenoms", "localite"]
    list_display = ('nom', 'categorie', 'proprietaire', 'localite',
                    'cout_estimatif', 'active', 'created', 'date_update', )


@admin.register(DevisProjet)
class DevisProjetAdmin(admin.ModelAdmin):
    search_fields = ["projet__nom", "projet__categorie__nom", "projet__proprietaire__user__nom",
                     "projet__proprietaire__user__prenoms", "projet__localite"]
    list_display = ('projet', 'active', 'created', 'date_update', )


@admin.register(ElementDevis)
class ElementDevisAdmin(admin.ModelAdmin):
    search_fields = ["devis__projet__nom", "devis__projet__categorie__nom", "devis__projet__proprietaire__user__nom",
                     "devis__projet__proprietaire__user__prenoms", "devis__projet__localite"]
    list_display = ('devis', 'titre', 'cout', 'active',
                    'created', 'date_update', )


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    search_fields = ["projet__nom", "projet__categorie__nom", "projet__proprietaire__user__nom",
                     "projet__proprietaire__user__prenoms", "projet__localite", "responsable__user__nom", "responsable__user__prenoms"]
    list_display = ('projet', 'activite', 'responsable',
                    'active', 'created', 'date_update', )
