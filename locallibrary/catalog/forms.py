import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Visitor
from .models import Donate
from .models import Blog
from .models import Comment
from .models import Interview
from .models import Predictor


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is allowed in the range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to alwayas to return the cleaned data
        return data


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields=["name", "phone_number", "email_id", "message"]


class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ["book", "author", "language", "copies", "edition", "price", "email", "phone", "donator_name", "donate_for_free"]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "slug", "author", "content", "status"]


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ["title", "slug", "author", "content", "status"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PredictorForm(forms.ModelForm):
    class Meta:
        model = Predictor
        fields = ('name', 'phone_number', 'email_id',
                  'tenth_marks', 'twelth_mark', 'tenth_year',
                  'twelth_year', 'tenth_board', 'twelth_board',
                  'gender', 'interest', 'subject_for_science',
                  'subject_for_arts', 'subject_for_commerce',
                  'scholarship_status', 'father_occupation',
                  'mother_occupation', 'income_status',
                  'extra_curriculum_activity',
                  'language_of_communication',
                  'do_you_take_interest_in_legal_matters',
                  'do_you_have_passion_about_creativity_and_innovations',
                  'do_you_have_curiosity_about_human_body',
                  'do_you_have_interest_in_financial_planning_and_control',
                  'do_you_take_interest_to_solve_family_and_society_problem',
                  'do_you_love_serving_animals',
                  'do_you_feel_comfortable_interacting_with_crowd',
                  'do_you_have_any_medical_experiences',
                  'do_you_believe_in_social_justice',
                  'do_you_have_capacity_to_influence_and_persuading_people',
                  'do_you_have_interest_in_marketing',
                  'do_you_have_curiosity_about_plants',
                  'do_you_have_emotional_intelligence',
                  'do_you_want_to_work_with_those_who_have_lost_their_direction',
                  'are_you_interested_in_agriculture',
                  'are_you_interested_to_work_with_different_culture_community_and_religions_across_the_country',
                  'do_you_have_deep_interest_in_Indian_constitution_IPC_CrPC_CPC_and_other_laws_of_India',
                  'do_you_want_to_work_with_business_people',
                  'do_you_have_interest_in_developing_sustainable_resources',
                  'you_want_to_be', 'do_you_follow_rules_and_regulations_in_every_aspects_of_life',
                  'do_you_take_interest_in_planning_and_organizing_activity_of_others',
                  'do_you_have_interest_in_indian_history_and_politics',
                  'how_many_hours_would_you_like_to_work_in_a_week'
)