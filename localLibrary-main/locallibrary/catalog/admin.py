from django.contrib import admin
from .models import Genre, Book, Author, BookInstance,Publisher

# admin.site.register(Genre)
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)

# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', "author", "display_genre")

# Register the Admin classes for BookInstance using the decorator

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuhorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

