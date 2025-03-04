from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Textbook

def homepage(request):
    return render(request, 'textbooks/home.html')  # Make sure home.html exists

def textbook_list(request, course_code):
    textbooks = Textbook.objects.filter(course_code=course_code, availability=True)

    return render(request, 'textbooks/list.html', {
        'course_code': course_code,
        'textbooks': textbooks
    })