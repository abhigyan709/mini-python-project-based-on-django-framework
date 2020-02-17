import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description os the book')
    isbn = models.CharField('ISBN',max_length=13,help_text='13 Character ISBN number. International Standard Book Number.')

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


GENDER = (
    ('Male', "Male"), ('Female', "Female"), ('Transgender', "Transgender")
)
DISEASE_TYPE = (
    ('inf', "Infectious"), ('def', "Deficiency"), ('her', "Hereditary"),
    ('phy', "Physiological"), ('non', "None"), ('ud', "Under Diagnosis")
)


class Patient(models.Model):
    first_Name = models.CharField(max_length=200, default=None)
    last_Name = models.CharField(max_length=200, default=None)
    gender = models.CharField(
        max_length=20, choices=GENDER, blank=False, default='Male'
    )
    birth_Date = models.DateField(null=False, blank=False)
    aadhar_ID = models.CharField(max_length=12, primary_key=True, editable=True, default=None)
    phone_Number = models.CharField(max_length=12, default=None, editable=True, unique=True)
    treatment_Under = models.ForeignKey('doctor', on_delete=models.CASCADE, null=True)
    disease_Type = models.ForeignKey('disease', on_delete=models.SET_NULL, null=True)
    short_Detail_of_Problem = models.CharField(max_length=500, blank=False, default=None)

    class Meta:
        ordering = ['first_Name', 'last_Name']

    def __str__(self):
        return f'{self.first_Name} {self.last_Name}'

    def get_absolute_url(self):
        return reverse('patient-detail', args=[str(self.aadhar_ID)])


class Department(models.Model):
    name = models.CharField(max_length=100, default=None, null=False)

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
    license_Number = models.CharField(max_length=25, primary_key=True, default=None, editable=True)

    class Meta:
        ordering = ['first_Name', 'last_Name']

    def __str__(self):
        return f'{self.first_Name} {self.last_Name}'

    def get_absolute_url(self):
        return reverse('doctor-detail', args=[str(self.license_Number)])


class Disease(models.Model):
    name = models.CharField(max_length=200, default=None)
    type = models.CharField(
        max_length=20,
        choices=DISEASE_TYPE,
        blank=False,
        default='non'
    )
    description = models.TextField(max_length=300, default=None)

    def __str__(self):
        return self.name

