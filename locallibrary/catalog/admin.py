from django.contrib import admin
from catalog.models import Author, Book
from catalog.models import Genre, Language
from catalog.models import BookInstance
from catalog.models import Visitor, Donate
from catalog.models import Blog, Comment
from catalog.models import Interview
from catalog.models import Exam, Question


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


class DonateInline(admin.TabularInline):
    model = Donate


class DonateAdmin(admin.ModelAdmin):
    list_display = ('book', 'author', "language", 'copies', 'edition', 'price', 'email', 'phone', 'donator_name', 'donate_for_free')
    fields = ['book', 'author', 'language', 'copies', 'edition', 'price', 'email', 'phone', 'donator_name', 'donate_for_free']


admin.site.register(Donate, DonateAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Genre)
admin.site.register(Language)


class BlogInline(admin.TabularInline):
    model = Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)


class CommentInline(admin.TabularInline):
    model = Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)


class InterviewInline(admin.TabularInline):
    model = Interview


class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Interview, InterviewAdmin)

admin.site.register(Exam)
admin.site.register(Question)


