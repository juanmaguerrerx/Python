from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, Court, Book
from .forms import MemberForm, CourtForm, BookForm


def member_All(request):
    members = Member.objects.all()
    return render(request, 'member/member_all.html', {'members': members})

def member_New(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_All')
    else:
        form = MemberForm()
    return render(request, 'form_template.html', {'form': form, 'form_title': 'New Member'})


def member_Edit(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_All')
    else:
        form = MemberForm(instance=member)
    return render(request, 'form_template.html', {'form': form, 'form_title': 'Edit Member'})

def member_Delete(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    member.delete()
    return redirect('member_All')

def court_All(request):
    courts = Court.objects.all()
    return render(request, 'court/court_all.html', {'courts': courts})

def court_New(request):
    if request.method == 'POST':
        form = CourtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('court_All')
    else:
        form = CourtForm()
    return render(request, 'form_template.html', {'form': form, 'form_title': 'New Court'})

def court_Edit(request, court_id):
    court = get_object_or_404(Court, pk=court_id)
    if request.method == 'POST':
        form = CourtForm(request.POST, instance=court)
        if form.is_valid():
            form.save()
            return redirect('court_All')
    else:
        form = CourtForm(instance=court)
    return render(request, 'form_template.html', {'form': form, 'form_title': 'Edit Court'})

def court_Delete(request, court_id):
    court = get_object_or_404(Court, pk=court_id)
    court.delete()
    return redirect('court_All')

def book_All(request):
    books = Book.objects.all()
    return render(request, 'book/book_all.html', {'books': books})

def book_New(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_All')
    else:
        form = BookForm()
    return render(request, 'form_template.html', {'form': form, 'form_title': 'New Book'})

def book_Edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_All')
    else:
        form = BookForm(instance=book)
    return render(request, 'form_template.html', {'form': form, 'form_title': 'Edit Book'})

def book_Delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('book_All')

def welcome(request):
    return render(request, 'welcome.html')