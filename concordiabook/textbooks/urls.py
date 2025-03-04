from django.urls import path
from .views import textbook_list, homepage  # ✅ Ensure homepage is imported

urlpatterns = [
    path('', homepage, name='homepage'),  # ✅ Default homepage
    path('textbooks/<str:course_code>/', textbook_list, name='textbook_list'),
]