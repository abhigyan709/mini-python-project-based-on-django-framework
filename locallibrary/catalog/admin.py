from django.contrib import admin
from .models import Author, Book
from .models import Genre, Language
from .models import BookInstance
from .models import Visitor
from .models import Predictor


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


class PredictorInline(admin.TabularInline):
    model = Predictor

class PredictorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_id', 'tenth_marks', 'twelth_mark', 'tenth_year',
                    'twelth_year', 'tenth_board', 'twelth_board', 'gender', 'interest', 'subject_for_science',
                    'subject_for_arts', 'subject_for_commerce', 'scholarship_status',
                    'father_occupation', 'mother_occupation', 'income_status', 'extra_curriculum_activity',
                    'language_of_communication', 'do_you_take_interest_in_legal_matters',
                    'do_you_have_passion_about_creativity_and_innovations', 'do_you_have_curiosity_about_human_body',
                    'do_you_have_interest_in_financial_planning_and_control',
                    'do_you_take_interest_to_solve_family_and_society_problem', 'do_you_love_serving_animals',
                    'do_you_feel_comfortable_interacting_with_crowd', 'do_you_have_any_medical_experiences',
                    'do_you_believe_in_social_justice', 'do_you_have_capacity_to_influence_and_persuading_people',
                    'do_you_have_interest_in_marketing', 'do_you_have_curiosity_about_plants',
                    'do_you_have_emotional_intelligence', 'do_you_want_to_work_with_those_who_have_lost_their_direction',
                    'are_you_interested_in_agriculture',
                    'are_you_interested_to_work_with_different_culture_community_and_religions_across_the_country',
                    'do_you_have_deep_interest_in_Indian_constitution_IPC_CrPC_CPC_and_other_laws_of_India',
                    'do_you_want_to_work_with_business_people', 'do_you_have_interest_in_developing_sustainable_resources',
                    'you_want_to_be', 'do_you_follow_rules_and_regulations_in_every_aspects_of_life',
                    'do_you_take_interest_in_planning_and_organizing_activity_of_others',
                    'do_you_have_interest_in_indian_history_and_politics',
                    'how_many_hours_would_you_like_to_work_in_a_week'
                    )
    list_filter = ('name', 'phone_number', 'email_id',
                   'interest', 'subject_for_science',
                   'subject_for_arts', 'subject_for_commerce',
                   )
    search_fields = ['name', 'phone_number', 'email_id',
                   'interest', 'subject_for_science',
                   'subject_for_arts', 'subject_for_commerce']

admin.site.register(Predictor, PredictorAdmin)



