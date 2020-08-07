from django.contrib import admin
from .models import Author, Course, TopAuthor


admin.site.register(Author)
admin.site.register(TopAuthor)
admin.site.register(Course)

