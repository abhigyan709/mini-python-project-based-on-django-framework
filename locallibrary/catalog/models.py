import uuid                      # required for unique book instance
from django.db import models
from django.urls import reverse  # used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date


class Genre(models.Model):

    """Model Representing a Book Genre"""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g Science Fiction)')

    def __str__(self):

        """String for representing the Model Object."""
        return self.name

    def get_absolute_url(self):
        return reverse('genre',)


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    def get_absolute_url(self):
        return reverse('language',)


class Book(models.Model):
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have only one author but can have multiple books
    # Author as a string Rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description os the book')
    isbn = models.CharField('ISBN',
                            max_length=13,
                            help_text='13 Character ISBN number. International Standard Book Number.')

    # ManyToManyField used because genre can contain many books. Books can cover many genre.
    # genre class has already been defined so we can specify the above object
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this Boook')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Str for generating the Model Object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
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
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Return the url to access a particular author instance"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the model Object."""
        return f'{self.last_name}, {self.first_name}'


class Visitor(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    email_id = models.EmailField()
    message = models.CharField(max_length=1000)


class Donate(models.Model):
    book = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    language = models.CharField(max_length=100, default="English")
    copies = models.IntegerField(default=1)
    edition = models.CharField(max_length=100)
    price = models.DecimalField(max_digits= 7, decimal_places=2)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    donator_name = models.CharField(max_length=100, default="Your Name")
    donate_for_free = models.CharField(max_length=5, default="Yes")


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
    

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(default="yes")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', )