from django import forms
from .models import Member, Court, Book

class MemberForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Member.CATEGORY_CHOICES)
    class Meta:
        model = Member
        fields = ['full_name', 'phone', 'birth_date', 'category']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ['descr', 'ten_pad']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['member', 'court', 'date_time']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
