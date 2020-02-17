from django.contrib import admin
# from .models import BookInstance
from .models import Patient, Disease, Doctor, Department

#class BooksInstanceInline(admin.TabularInline):
 #   model = BookInstance


#@admin.register(Book)
#class BookAdmin(admin.ModelAdmin):
   # list_display = ('title', 'author', 'display_genre')
   # inlines = [BooksInstanceInline]

# register the admin classes for BookInstance using the decorator
""""@admin.register(BookInstance)
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
    )"""

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Disease)
admin.site.register(Department)



