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


class Interview(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
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
        return reverse('interview', )


class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


GENDER = (
        (0, "Male"),
        (1, "Female")
    )
INTEREST = (
    ('s', "Science"),
    ('m', "Math"),
    ('c', "commerce" )
)
SUBJECT_SCIENCE = (
    ('pcm', "PCM"),
    ('pcb', "PCB"),
    ('pcmb', "PCMB"),
    ('no', "NONE")
)
SUBJECT_ARTS = (
    ('history', "HISTORY"),
    ('journalism', "JOURNALISM"),
    ('english', "ENGLISH"),
    ('politicalScience', "POLITICAL SCIENCE"),
    ('geography', "GEOGRAPHY"),
    ('no', "NONE")
)
SUBJECT_COMMERCE = (
    ('economics', "ECONOMICS"),
    ('bussiness', "BUSSINESS STUDIES"),
    ('accountancy', "ACCOUNTANCY"),
    ('no', "NONE")
)
SCHOLARSHIP = (
    ('yes', "YES"),
    ('nope', "NO")
)
FATHER_OCCUPATION = (
    ('govtService', "GOVERNMENT SERVICE"),
    ('privateService', "PRIVATE SERVICE"),
    ('agriculture', "AGRICULTURE"),
    ('bussiness', "BUSSINESS"),
    ('other', "OTHER")
)

MOTHER_OCCUPATION = (
    ('govtService', "GOVERNMENT SERVICE"),
    ('housewife', "HOUSEWIFE"),
    ('privateService', "PRIVATE SERVICE"),
    ('agriculture', "AGRICULTURE"),
    ('bussiness', "BUSSINESS"),
    ('other', "OTHER")
)

INCOME_STATUS = (
    ('high', "HIGH(>1000000)"),
    ('medium', "MEDIUM(500000-1000000)"),
    ('low', "LOW(<500000)")
)
LOGICAL_THINKING = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
LEGAL_INTEREST = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
CFREATIVITY = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
CURIOSITY_INTEREST = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
FINANCIAL_PLANNING = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
FAMILY_PLANNING = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
LOVE_ANIMALS = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
CROWD_INTERACTION = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
MEDICAL_EXPERIENCE = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
SOCIAL_JUSTICE = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
INFLUENCE_PEOPLE = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
MARKETING = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
PLANT_INTEREST = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
EMOTIONAL_INTELLIGENCE = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
LOST_DIRECTION = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
AGRICULTURE = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
RELIGION = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
CONSTITUTION = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
BUSSINESS = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
SUSTAINABLE = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
GOALS = (
    ('entrepreneur', "An Entrepreneur"),
    ('mnc', "An Employee of a Multi National Company"),
    ('govt', "A Government Servant"),
    ('social', "Social Worker")
)
RULES = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
ORGANIZING = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
POLITICS = (
    ('yes', "YES"),
    ('no', "NO"),
    ('notMuch', "NOT MUCH")
)
WORKING = (
    ('work1', "Not more than 40 hours."),
    ('work2', "Not more than 48 hours."),
    ('work3', "Not more than 32 hours."),
    ('work4', "Number of hours required according to work requirement.")
)


class Predictor(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    email_id = models.EmailField()
    tenth_marks = models.DecimalField(max_digits=4, decimal_places=2)
    twelth_mark = models.DecimalField(max_digits=4, decimal_places=2)
    tenth_year = models.DateField(null=True, blank=False)
    twelth_year = models.DateField(null=True, blank=False)
    tenth_board = models.CharField(max_length=20, help_text="Enter your Board name", default = "CBSE")
    twelth_board = models.CharField(max_length=20, help_text="Enter your 12th board Name", default="CBSE")
    gender = models.IntegerField(
        max_length=20,
        choices=GENDER,
        blank=False,
        default='Male',
        help_text="What's your Gender",
    )
    interest = models.CharField(
        max_length=20,
        choices=INTEREST,
        blank=False,
        default='s',
        help_text='In which stream you are Interested',
    )
    subject_for_science = models.CharField(
        max_length=20,
        choices=SUBJECT_SCIENCE,
        blank=True,
        default='no',
        help_text="Select the subject combination"
    )
    subject_for_arts = models.CharField(
        max_length=20,
        choices=SUBJECT_ARTS,
        blank=True,
        default='no',
        help_text="Select the subject for Arts"
    )
    subject_for_commerce = models.CharField(
        max_length=20,
        choices=SUBJECT_COMMERCE,
        blank=True,
        default='no',
        help_text="Select the subject for Commerce"
    )
    scholarship_status = models.CharField(
        max_length=20,
        choices=SCHOLARSHIP,
        blank=False,
        default='nope',
        help_text="Do have any Scholarship"
    )
    father_occupation = models.CharField(
        max_length=25,
        choices=FATHER_OCCUPATION,
        blank=False,
        default='other',
        help_text = "What is your Father's Occupation"
    )
    mother_occupation = models.CharField(
        max_length=25,
        choices=MOTHER_OCCUPATION,
        blank=False,
        default='housewife',
        help_text = "What is your Father's Occupation"
    )
    income_status = models.CharField(
        max_length=25,
        choices=INCOME_STATUS,
        blank=False,
        default='low',
        help_text = "What is your Family's Income"
    )
    extra_curriculum_activity = models.TextField(max_length=5000, default="Mention, if you have any other extra curriculum activity.")
    language_of_communication = models.CharField(max_length=50, default="Hindi")
    do_you_enjoy_logical_thinking_and_reasoning = models.CharField(
        max_length=25,
        choices=LOGICAL_THINKING,
        blank=False,
        default='notMuch',
        help_text = "Are you interested in Logical Thinking and Reasoning"
    )
    do_you_take_interest_in_legal_matters = models.CharField(
        max_length=25,
        choices=LEGAL_INTEREST,
        blank=False,
        default='notMuch',
        help_text= "Are you intersted in Legal Matters?"
    )
    do_you_have_passion_about_creativity_and_innovations = models.CharField(
        max_length=25,
        choices=CFREATIVITY,
        blank=False,
        default='notMuch',
        help_text= "Do you take interest in Creativity and Innovations"
    )
    do_you_have_curiosity_about_human_body = models.CharField(
        max_length=25,
        choices=CURIOSITY_INTEREST,
        blank=False,
        default='notMuch',
        help_text= "Do you have curiosity about human body ?"
    )
    do_you_have_interest_in_financial_planning_and_control = models.CharField(
        max_length=25,
        choices=FINANCIAL_PLANNING,
        blank=False,
        default='notMuch',
        help_text = "Do you have interest in financial planning and control ?"
    )
    do_you_take_interest_to_solve_family_and_society_problem = models.CharField(
        max_length=25,
        choices=FAMILY_PLANNING,
        blank=False,
        default='notMuch',
        help_text = "Do you take interest to solve family and society problem ?"
    )
    do_you_love_serving_animals = models.CharField(
        max_length=25,
        choices=LOVE_ANIMALS,
        blank=False,
        default='notMuch',
        help_text = "Do you love serving animals ?"
    )
    do_you_feel_comfortable_interacting_with_crowd = models.CharField(
        max_length=25,
        choices=CROWD_INTERACTION,
        blank=False,
        default='notMuch',
        help_text = "Do you feel comfortable interacting with crowd ?"
    )
    do_you_have_any_medical_experiences = models.CharField(
        max_length=25,
        choices=MEDICAL_EXPERIENCE,
        blank=False,
        default='notMuch',
        help_text = "Do you have any medical experiences ?"
    )
    do_you_believe_in_social_justice = models.CharField(
        max_length=25,
        choices=SOCIAL_JUSTICE,
        blank=False,
        default='notMuch',
        help_text = "Do you believe in Social Justice ?"
    )
    do_you_have_capacity_to_influence_and_persuading_people = models.CharField(
        max_length=25,
        choices=INFLUENCE_PEOPLE,
        blank=False,
        default='notMuch',
        help_text = "Do you have capacity to influence and persuading people ?"
    )
    do_you_have_interest_in_marketing = models.CharField(
        max_length=25,
        choices=MARKETING,
        blank=False,
        default='notMuch',
        help_text = "Do you have interest in marketing ?"
    )
    do_you_have_curiosity_about_plants = models.CharField(
        max_length=25,
        choices=PLANT_INTEREST,
        blank=False,
        default='notMuch',
        help_text = "Do you have curiosity about plants ?"
    )
    do_you_have_emotional_intelligence = models.CharField(
        max_length=25,
        choices=EMOTIONAL_INTELLIGENCE,
        blank=False,
        default='notMuch',
        help_text = "Do you have emotional intelligence ?"
    )
    do_you_want_to_work_with_those_who_have_lost_their_direction = models.CharField(
        max_length=25,
        choices=LOST_DIRECTION,
        blank=False,
        default='notMuch',
        help_text = "Do you want to work with those who have lost their direction ?"
    )
    are_you_interested_in_agriculture = models.CharField(
        max_length=25,
        choices=AGRICULTURE,
        blank=False,
        default='notMuch',
        help_text = "Are you interested in agriculture ?"
    )
    are_you_interested_to_work_with_different_culture_community_and_religions_across_the_country = models.CharField(
        max_length=25,
        choices=RELIGION,
        blank=False,
        default='notMuch',
        help_text = "Are you interested to work with different culture,community & religions across the country ?"
    )
    do_you_have_deep_interest_in_Indian_constitution_IPC_CrPC_CPC_and_other_laws_of_India = models.CharField(
        max_length=25,
        choices=CONSTITUTION,
        blank=False,
        default='notMuch',
        help_text = "Do you have deep interest in Indian constitution,IPC, CrPC,CPC & other laws of India ?"
    )
    do_you_want_to_work_with_business_people = models.CharField(
        max_length=25,
        choices=BUSSINESS,
        blank=False,
        default="notMuch",
        help_text = "Do you want to work with business people ?"
    )
    do_you_have_interest_in_developing_sustainable_resources = models.CharField(
        max_length=25,
        choices=SUSTAINABLE,
        blank=False,
        default="notMuch",
        help_text = "Do you have interest in developing sustainable resources ?"
    )
    you_want_to_be = models.CharField(
        max_length=25,
        choices=GOALS,
        blank=False,
        default='mnc',
        help_text = "You want to be _________."
    )
    do_you_follow_rules_and_regulations_in_every_aspects_of_life = models.CharField(
        max_length=25,
        choices=RULES,
        blank=False,
        default="notMuch",
        help_text = "Do you follow rules and regulations in every aspects of life ?"
    )
    do_you_take_interest_in_planning_and_organizing_activity_of_others = models.CharField(
        max_length=25,
        choices=ORGANIZING,
        blank=False,
        default="notMuch",
        help_text = "Do you take interest in planning and organizing activity of others ?"
    )
    do_you_have_interest_in_indian_history_and_politics = models.CharField(
        max_length=25,
        choices=POLITICS,
        blank=False,
        default="notMuch",
        help_text = "Do you have interest in indian history and politics ?"
    )
    how_many_hours_would_you_like_to_work_in_a_week = models.CharField(
        max_length=25,
        choices=WORKING,
        blank=False,
        default="work1",
        help_text = "How many hours would you like to work in a week ?"
    )