from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Textbook

@admin.register(Textbook)  # Alternative: admin.site.register(Textbook)
class TextbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'edition', 'condition', 'course_code', 'availability')
    list_filter = ('condition', 'availability', 'course_code')
    search_fields = ('title', 'author', 'course_code')