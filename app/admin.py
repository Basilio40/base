from django.contrib import admin
from .models import Obras, Imagem


@admin.register(Obras)
class ObrasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'logradouro', 'data_inicio', 'data_prevista')
    list_editable = ('data_inicio', 'data_prevista')
    list_filter = ('nome',)


admin.site.register(Imagem)
