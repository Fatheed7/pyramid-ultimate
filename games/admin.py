from django.contrib import admin
from .models import Game, Category, PrimaryChallenge, SecondaryChallenge, Developer

class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'release_date',
        'steam_link'
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'despaced',
    )

    ordering = ('name',)

class PrimaryChallengeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'game',
    )

    ordering = ('name',)

class SecondaryChallengeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'game',
    )

    ordering = ('name',)

class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'website',
    )

    ordering = ('name',)

admin.site.register(Game, GameAdmin) 
admin.site.register(Category, CategoryAdmin)
admin.site.register(PrimaryChallenge, PrimaryChallengeAdmin)
admin.site.register(SecondaryChallenge, SecondaryChallengeAdmin)
admin.site.register(Developer, DeveloperAdmin)

