from django.contrib.auth.models import User
from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    teaching_skill = models.CharField(max_length=50, null=True, blank=True)
    profile = models.ImageField(upload_to='profile/%Y/%m/%d/')
    description = models.TextField()
    fb = models.URLField()
    insta = models.URLField()

    def __str__(self):
        return self.name

    def short_description(self):
        return self.description[:150]

class TopAuthor(models.Model):

    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profiles/%Y/%m/%d/')

    def __str__(self):
        return self.name

class Course(models.Model):

    topauthor = models.ForeignKey(TopAuthor, on_delete=models.CASCADE, null=True, blank=True)
    more_instructor = models.IntegerField(default=0, null=True, blank=True)
    author = models.ManyToManyField(Author)
    images = models.ImageField(upload_to='images/%Y/%m/%d/')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    Content = models.TextField()
    total_hours = models.IntegerField(default=0)
    lectures = models.IntegerField(default=0)
    week = models.IntegerField()
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    ##################  INCLUDE  ###################
    experience_level = models.CharField(max_length=60)
    # FOR THOSE WHO WANT TO LEARN #

    who_want_to = models.CharField(max_length=255)
    who_want_to2 = models.CharField(max_length=255)
    who_want_to3 = models.CharField(max_length=255)

    ############ Daily Qoute #############

    quote_author = models.CharField(max_length=255)
    qoute = models.CharField(max_length=500)




    ############# SKILLS #################

    skill = models.CharField(max_length=40, null=True, blank=True)
    skill2 = models.CharField(max_length=40, null=True, blank=True)
    skill3 = models.CharField(max_length=40, null=True, blank=True)
    skill4 = models.CharField(max_length=40, null=True, blank=True)
    skill5 = models.CharField(max_length=40, null=True, blank=True)
    skill6 = models.CharField(max_length=40, null=True, blank=True)
    skill7 = models.CharField(max_length=40, null=True, blank=True)
    skill8 = models.CharField(max_length=40, null=True, blank=True)
    skill9 = models.CharField(max_length=40, null=True, blank=True)
    skill10 = models.CharField(max_length=40, null=True, blank=True)



    ######################   CONTENT   ########################

    learning_content_heading = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail = models.TextField(null=True, blank=True)

    learning_content_heading2 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail2 = models.TextField(null=True, blank=True)

    learning_content_heading3 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail3 = models.TextField(null=True, blank=True)

    learning_content_heading4 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail4 = models.TextField(null=True, blank=True)

    learning_content_heading5 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail5 = models.TextField(null=True, blank=True)

    learning_content_heading6 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail6 = models.TextField(null=True, blank=True)

    learning_content_heading7 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail7 = models.TextField(null=True, blank=True)

    learning_content_heading8 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail8 = models.TextField(null=True, blank=True)

    learning_content_heading9 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail9 = models.TextField(null=True, blank=True)

    learning_content_heading10 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail10 = models.TextField(null=True, blank=True)

    learning_content_heading11 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail11 = models.TextField(null=True, blank=True)

    learning_content_heading12 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail12 = models.TextField(null=True, blank=True)

    learning_content_heading13 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail13 = models.TextField(null=True, blank=True)

    learning_content_heading14 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail14 = models.TextField(null=True, blank=True)

    learning_content_heading15 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail15 = models.TextField(null=True, blank=True)

    learning_content_heading16 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail16 = models.TextField(null=True, blank=True)

    learning_content_heading17 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail17 = models.TextField(null=True, blank=True)

    learning_content_heading18 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail18 = models.TextField(null=True, blank=True)

    learning_content_heading19 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail19 = models.TextField(null=True, blank=True)

    learning_content_heading20 = models.CharField(max_length=255, null=True, blank=True)
    learning_content_detail20 = models.TextField(null=True, blank=True)


            # Frequently Ask Questions #

    Faq_Question = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer = models.TextField(null=True, blank=True)

    Faq_Question2 = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer2 = models.TextField(null=True, blank=True)

    Faq_Question3 = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer3 = models.TextField(null=True, blank=True)

    Faq_Question4 = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer4 = models.TextField(null=True, blank=True)

    Faq_Question5 = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer5 = models.TextField(null=True, blank=True)

    Faq_Question6 = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer6 = models.TextField(null=True, blank=True)

    Faq_Question7 = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer7 = models.TextField(null=True, blank=True)

    Faq_Question8 = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer8 = models.TextField(null=True, blank=True)

    Faq_Question9 = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer9 = models.TextField(null=True, blank=True)

    Faq_Question10 = models.CharField(max_length=255, null=True, blank=True)
    Faq_Answer10 = models.TextField(null=True, blank=True)

    is_featured = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title

    def short_description(self):
        return self.description[:120]

    def to_short_description(self):
        return self.description[:80]
