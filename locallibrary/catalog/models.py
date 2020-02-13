import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g Science Fiction)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre',)


class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('language',)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description os the book')
    isbn = models.CharField('ISBN',max_length=13,help_text='13 Character ISBN number. International Standard Book Number.')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this Boook')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this Book across whole Library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r','Reserved')
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"), )

    def __str__(self):
        """String for representing the model object."""
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Visitor(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    email_id = models.EmailField()
    message = models.CharField(max_length=1000)


GENDER = (
    ('m', "Male"), ('f', "Female"), ('t', "Transgender")
)
DISEASE_TYPE = (
    ('inf', "Infectious"), ('def', "Deficiency"), ('her', "Hereditary"),
    ('phy', "Physiological"), ('non', "None"), ('ud', "Under Diagnosis")
)


class Patient(models.Model):
    first_Name = models.CharField(max_length=200, default=None)
    last_Name = models.CharField(max_length=200, default=None)
    gender = models.CharField(
        max_length=20,
        choices=GENDER,
        blank=False,
        default='m'
    )
    aadhar_ID = models.CharField(max_length=12, primary_key=True, editable=True, default=None)
    phone_Number = models.CharField(max_length=12, default=None, editable=True, unique=True)
    treatment_Under = models.ForeignKey('doctor', on_delete=models.SET_NULL, null=True)
    disease_Type = models.ForeignKey('disease', on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['first_Name', 'last_Name']

    def __str__(self):
        return f'{self.first_Name} {self.last_Name}'

DEPARTMENTS = (
    ('Cardiologist', "Cardiologist"), ('Neurologist', "Neurologist"), ('Pediatrics', "Pediatrics"),
    ('Surgeon', "Surgeon"), ('Physician', "Physician"), ('Gaenocologist', "Gaenocologist"),
    ('Dermatologist', "Dermatologist"),
    ('Dentist', "Dentist")

)


class Department(models.Model):
    name = models.CharField(
        max_length=20,
        choices=DEPARTMENTS,
        blank=False,
        default='Physician',
        unique=True
    )

    def __str__(self):
        return f'{self.name}'

class Doctor(models.Model):
    first_Name = models.CharField(max_length=200, default=None)
    last_Name = models.CharField(max_length=200, default=None)
    department = models.ManyToManyField(Department, default=None)
    gender = models.CharField(
        max_length=20,
        choices=GENDER,
        blank=False,
        default='m'
    )
    license_Number = models.CharField(max_length=25, default=None, unique=True)



    class Meta:
        ordering = ['first_Name', 'last_Name']

    def __str__(self):
        return f'{self.first_Name} {self.last_Name}'


class Disease(models.Model):
    name = models.CharField(max_length=200, default=None)
    type = models.CharField(
        max_length=20,
        choices=DISEASE_TYPE,
        blank=False,
        default='non'
    )

    def __str__(self):
        return self.name
