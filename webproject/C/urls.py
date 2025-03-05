from django.urls import path
from .views import course_namesearch

urlpatterns = [
    path('name_search/', course_namesearch, name='search_name'),
]
