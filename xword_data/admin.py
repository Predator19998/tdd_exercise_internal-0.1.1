from django.contrib import admin
from .models import Puzzle, Entry, Clue

# Register your models here.
@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'byline', 'publisher')
    search_fields = ('title', 'byline', 'publisher')
    list_filter = ('date', 'publisher')

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_text',)
    search_fields = ('entry_text',)

@admin.register(Clue)
class ClueAdmin(admin.ModelAdmin):
    list_display = ('clue_text', 'entry', 'puzzle', 'theme')
    search_fields = ('clue_text', 'entry__entry_text', 'puzzle__title')
    list_filter = ('theme', 'puzzle')