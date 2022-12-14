from django.contrib import admin
from .models import Game, Category

class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'release_date',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Game, GameAdmin) 
admin.site.register(Category, CategoryAdmin)
