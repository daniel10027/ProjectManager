from django.contrib import admin
from .models import (User, Profile, Domaine)
# Register your models here.

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ["nom",
                     "prenoms", ]
    list_display = ('nom', 'prenoms', 'email', 'active', 'created', 'date_update', 'is_client', 'is_ouvrier', 'is_responsable', 'is_admin', )

@admin.register(Domaine)
class DomaineAdmin(admin.ModelAdmin):
    search_fields = ["nom",]
    list_display = ('nom', 'active', 'created', 'date_update', )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ["user__nom","user__prenoms",]
    list_display = ('user', 'telephone', 'lieu_de_residence', 'sexe', 'cout_journalier', 'domaine', 'active', 'created', 'date_update', )

