# NOTE: THIS PROJECT FOLLOWS PEP8(Python Enhancement Proposal Guidelines)
import datetime
from django.shortcuts import render, get_object_or_404
from catalog.models import Book, Author, BookInstance, Genre, Language, About, Blog
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.forms import RenewBookForm
from django.contrib.auth.forms import UserCreationForm
from .forms import VisitorForm, DonateForm


# views created here, new views have to append like user owned library, donate books, lend own books
def index(request):                                             # Generate Counts For Some Highlight Object to Show Data
    num_books = Book.objects.all().count()                      # View function for Home Page
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()    # Available books (status = 'a')
    num_authors = Author.objects.count()                                            # The 'all()' is implied by default.
    num_languages = Language.objects.count()
    num_genres = Genre.objects.count()
    num_visits = request.session.get('num_visits', 0)                                   # Number of visits to this view,
    request.session['num_visits'] = num_visits+1                                    # as counted in the session variable
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
        'num_languages': num_languages,
        'num_genres': num_genres
    }
    return render(request, 'index.html', context=context)                # Rendering the HTML Request Page To index.html


class GenreListView(generic.ListView):                                                                # Genres List View
    model = Genre
    paginate_by = 10


class BookListView(generic.ListView):                                                                   # Book List View
    model = Book
    paginate_by = 10


class LanguageListView(generic.ListView):                                                           # Language List View
    model = Language
    paginate_by = 10
    template_name = 'language_list.html'


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 10
    template_name = 'blog_list.html'


class AboutPageView(generic.ListView):                                                                 # About Page View
    model = About
    paginate_by = 10


class BookDetailView(generic.DetailView):                                         # Detailed view of the available books
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorListView(generic.ListView):                           # Generic class-based list view for a list of authors.
    model= Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):                             # Generic class-based detail view for an author.
    model = Author

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'author': author})


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):               # list view for Loaned book by user
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to user with can_mark_returned permission."""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # if this is POST request then process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}
    permission_required = 'catalog.can_mark_returned'


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    permission_required = 'catalog.can_mark_returned'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_mark_returned'


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class VisitorClass(generic.CreateView):
    form_class = VisitorForm
    success_url = reverse_lazy('index')
    template_name = 'catalog/visitor_form.html'


class DonateClass(LoginRequiredMixin, generic.CreateView):
    form_class = DonateForm
    success_url = reverse_lazy('index')
    template_name = 'catalog/donate_form.html'


