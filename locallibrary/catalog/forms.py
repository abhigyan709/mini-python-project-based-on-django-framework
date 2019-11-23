import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Visitor
from .models import Donate
from .models import Blog
from .models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')