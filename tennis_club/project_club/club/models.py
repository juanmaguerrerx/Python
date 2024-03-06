# En el archivo models.py de la aplicación 'club'

from django.db import models

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    birth_date = models.DateField()
    CATEGORY_CHOICES = [
        ('Infant', 'Infant'),
        ('Junior', 'Junior'),
        ('Adult', 'Adult'),
        ('Senior', 'Senior'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.full_name

class Court(models.Model):
    court_id = models.AutoField(primary_key=True)
    descr = models.CharField(max_length=50)
    TEN_PAD_CHOICES = [
        ('t', 'Tennis'),
        ('p', 'Paddle'),
    ]
    ten_pad = models.CharField(max_length=1, choices=TEN_PAD_CHOICES)

    def __str__(self):
        return self.descr

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.member} - {self.court} - {self.date_time}"

