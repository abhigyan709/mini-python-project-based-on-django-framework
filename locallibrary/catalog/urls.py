from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'index'),
    path('patient', views.PatientListView.as_view(), name='patient'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
    path('doctor/<int:pk>', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('signup/', views.SignUp.as_view(), name='signup'),

]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
]
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
urlpatterns += [
    #path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    #path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
urlpatterns += [
    path('doctor/create/', views.DoctorCreate.as_view(), name="doctor_create"),
    path('doctor', views.DoctorListView.as_view(), name="doctor_list"),
    path('doctor/<int:pk>', views.DoctorDetailView.as_view(), name="doctor-detail"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
