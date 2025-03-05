from django.shortcuts import render
from .models import Course

def course_namesearch(request):
    search = request.GET.get('code', '')
    courses = Course.objects.filter(Course_name__icontains=search) if search else []
    return render(request, 'course_namesearch.html', {'courses': courses})
