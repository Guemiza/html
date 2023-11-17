from django.contrib import admin
from catalog.models import Author, Genre, Book, Language, BookInstance
from django.contrib import admin

class LanguageAdmin(admin.ModelAdmin):
    pass
class GenreAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name','date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

def display_genre(self):
    return ','.join(Genre.name for genre in self.genre.all()[:3])

display_genre.Short_description = 'Genre'  
#inlines = [BookInstanceInline] 

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',  'genre')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields' :('book', 'imprint','id')
        }),
        (
            'Availability', {
                'fields':('status', 'due_back')

            }),
        )

class BookInstanceInline(admin.TabularInline):
    
   model = BookInstance

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    inlines = [BookInstanceInline]

admin.site.register(Language, LanguageAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
