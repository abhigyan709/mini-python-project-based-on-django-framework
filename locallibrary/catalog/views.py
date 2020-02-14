import datetime
from django.shortcuts import render, get_object_or_404, redirect
from . models import Book, Author, BookInstance, Genre, Language, Patient, Doctor
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . forms import RenewBookForm
from django.contrib.auth.forms import UserCreationForm
from . forms import VisitorForm, PatientForm



@permission_required('catalog.USER')
def index(request):
    context = {}
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PatientForm
    context['form'] = form
    return render(request, 'index.html', context=context)


class PatientListView(generic.ListView):
    model = Patient
    paginate_by = 25


class PatientDetailView(generic.DetailView):
    model = Patient

    def patient_detail_view(request, primary_key):
        patient = get_object_or_404(Patient, pk=primary_key)
        return render(request, 'catalog/patient_detail.html', context={'patient': patient})


class DoctorListView(generic.ListView):
    model = Doctor
    paginate_by = 10


class DoctorDetailView(generic.DetailView):
    model = Doctor

    def doctor_detail_view(request, primary_key):
        doctor = get_object_or_404(Doctor, pk=primary_key)
        return render(request, 'catalog/doctor_detail.html', context={'doctor' : doctor})


class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 10


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class LanguageListView(generic.ListView):
    model = Language
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorListView(generic.ListView):
    model= Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'author': author})


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            return HttpResponseRedirect(reverse('all-borrowed') )

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


class DoctorCreate(PermissionRequiredMixin, CreateView):
    model = Doctor
    fields = '__all__'
    permission_required = 'catalog.USER'


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


class VisitorClass(generic.CreateView, LoginRequiredMixin):
    form_class = VisitorForm
    success_url = reverse_lazy('index')
    template_name = 'catalog/visitor_form.html'







