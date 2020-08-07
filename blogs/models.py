from datetime import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Blog(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    main_photo = models.ImageField(upload_to='main_photos/%Y/%m/%d/', null=True, blank=True)
    slug = models.SlugField()
    categories = models.ManyToManyField(Category)
    publish_date_now = models.DateTimeField(default=datetime.now, blank=True)
    small_description = models.TextField()
    content = RichTextUploadingField()
    publish_date = datetime.now()
    min_read = models.IntegerField(null=True, blank=True)
    formatedDate = publish_date.strftime("%d %B %Y")
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title
