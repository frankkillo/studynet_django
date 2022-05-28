from versatileimagefield.fields import VersatileImageField
from django.conf import settings
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Course(models.Model):
    categories = models.ManyToManyField(Category, related_name="courses")
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    image = VersatileImageField(upload_to='course_image', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Lesson(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    ARTICLE = 'article'
    QUIZ = 'quiz'
    VIDEO = 'video'

    CHOICES_TYPE = (
        (ARTICLE, 'Article'),
        (QUIZ, 'Quiz'),
        (VIDEO, 'Video')
    )

    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=CHOICES_STATUS, default=PUBLISHED)
    type = models.CharField(max_length=15, choices=CHOICES_TYPE, default=ARTICLE)
    youtube_id = models.CharField(max_length=20, blank=True, null=True)


class Comment(models.Model):
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]


class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="quizzes", on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=50)
    ops_1 = models.CharField(max_length=50)
    ops_2 = models.CharField(max_length=50)
    ops_3 = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Quizzes"