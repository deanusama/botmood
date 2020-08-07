from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class About(models.Model):
    about = RichTextUploadingField()

