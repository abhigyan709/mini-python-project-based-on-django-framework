from django.contrib import admin
from .models import Author, Book
from .models import Genre, Language
from .models import BookInstance
from .models import Visitor
from .models import Patient, Disease, Doctor


class VisitorInline(admin.TabularInline):
    model = Visitor


class BooksInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_id', 'message')
    fields = ['name', 'phone_number', 'email_id', 'message']


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# register the admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Disease)



