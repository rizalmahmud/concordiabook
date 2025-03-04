from django.db import models

# Create your models here.

from django.db import models

class Textbook(models.Model):
    CONDITION_CHOICES = [
        ('new', 'Like New'),
        ('written', 'Written'),
        ('old', 'Old'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=50, blank=True, null=True)
    course_code = models.CharField(max_length=20)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)  # ✅ ChoiceField
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"