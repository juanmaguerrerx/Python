from django.contrib import admin
from django.urls import path
from club import views
from django.views.generic import RedirectView


urlpatterns = [
    # path('/', views.welcome),
    path('admin/', admin.site.urls),
    path('members/', views.member_All, name='member_All'),
    path('members/new/', views.member_New, name='member_New'),
    path('members/edit/<int:member_id>/', views.member_Edit, name='member_Edit'),
    path('members/delete/<int:member_id>/', views.member_Delete, name='member_Delete'),
    path('courts/', views.court_All, name='court_All'),
    path('courts/new/', views.court_New, name='court_New'),
    path('courts/edit/<int:court_id>/', views.court_Edit, name='court_Edit'),
    path('courts/delete/<int:court_id>/', views.court_Delete, name='court_Delete'),
    path('books/', views.book_All, name='book_All'),
    path('books/new/', views.book_New, name='book_New'),
    path('books/edit/<int:book_id>/', views.book_Edit, name='book_Edit'),
    path('books/delete/<int:book_id>/', views.book_Delete, name='book_Delete'),
]