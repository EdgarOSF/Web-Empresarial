from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories') # Muestra la informacion del modelo por las colunmas indicadas en la tupla
    ordering = ('author', 'published') # ordenacion: aqui primero se ordena por author y despues los ordena por fecha de publicado
    search_fields = ('title', 'content', 'author__username', 'categories__name') # Campos por los que se buscara un dato
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name') # Muestra una lista de opciones de busqueda directa de los datos las columnas indicadas

    # creamos una columna nueva de un dato que es manytomany y le cambiamos un nombre.
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
