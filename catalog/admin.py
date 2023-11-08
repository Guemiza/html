from django.contrib import admin
from django.contrib.admin import ModelAdmin

from catalog.models import Author,Genre,Book,Language,BookInstance


# Register your models here.
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)


#admin.site.register(Author,AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


