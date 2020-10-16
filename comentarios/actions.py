def reprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=False)

def aprova_comentarios(modeladmin, request, queryset):
    queryset.update(aprovado=True)

reprova_comentarios.short_description = 'Reprovar comentarios'
aprova_comentarios.short_description = 'Aprovar comentarios'