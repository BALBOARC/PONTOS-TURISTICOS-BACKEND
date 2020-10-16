from django.contrib import admin
from .models import Comentario
from .actions import aprova_comentarios, reprova_comentarios

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions = [reprova_comentarios, aprova_comentarios]

admin.site.register(Comentario, ComentarioAdmin)