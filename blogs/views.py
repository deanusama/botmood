from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog, Category
from courses.models import Course
from hitcount.views import HitCountDetailView


def blog(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()[:5]


    paginator = Paginator(blogs, 2)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)



    context = {
        'blogs': paged_blog,
        'categories': categories,

    }
    return render(request, 'blogs/blog-list.html', context)



class PostDetailView(HitCountDetailView):
    model = Blog
    template_name = 'blogs/blog-detail.html'
    context_object_name = 'detail'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Blog.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
            'recent_posts': Blog.objects.order_by('-publish_date_now')[:10],
        })
        return context




# def detail(request, slug):
#     detail = Blog.objects.get(slug=slug)
#     top_course = Course.objects.all()[:3]
#
#     word_count = len(detail.content.split())
#     min_read = int(word_count) / 250
#     mint_read = round(min_read)
#
#     context = {
#         'detail': detail,
#         'top_course': top_course,
#         'mint_read': mint_read
#     }
#     return render(request, 'blogs/blog-detail.html', context)


def category_page(request, id):
    category_page = Blog.objects.filter(categories=id)
    category_name = Blog.objects.all
    category_page2 = Blog.objects.filter(categories=id)[:3]

    context = {
        'category_page': category_page,
        'category_page2': category_page2,
        'category_name': category_name
    }
    return render(request, 'blogs/category.html', context)

def search(request):
    query = request.GET['query']
    search_blog = Blog.objects.filter(title__icontains=query)
    post_count = search_blog.count()
    context = {
        'query': query,
        'search_blog': search_blog,
        'post_count': post_count

    }

    return render(request, 'blogs/search.html', context)

