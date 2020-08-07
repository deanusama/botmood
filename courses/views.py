from django.shortcuts import render, get_object_or_404
from courses.models import Course, Author


def courses(request, ):
    courses = Course.objects.all()
    featured = Course.objects.filter(is_featured=True)
    post_count = courses.count()

    context = {
        'courses': courses,
        'featured': featured,
        'post_count': post_count,

    }
    return render(request, 'course/course.html', context)


def course_detail(request, slug):
    detail_page = get_object_or_404(Course, slug=slug)

    context = {
        'detail_page': detail_page,
    }
    return render(request, 'course/course_detail.html', context)


def instructor(request):
    instructors = Author.objects.all()

    context = {
        'instructors': instructors
    }
    return render(request, 'course/instructor.html', context)


def instructor_detail(request, id):
    instructors = Author.objects.all()
    instructor_detail = Author.objects.get(pk=id)
    courses1 = Course.objects.filter(author=id)
    context = {
        'instructor_detail': instructor_detail,
        'courses1': courses1,
        'instructors': instructors
    }
    return render(request, 'course/instructor_detail.html', context)
