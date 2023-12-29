from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status='published')

    options = (('draft', 'Draft'),
               ('published', 'Published'),)
    # category = models.ForeignKey(Category, 
    #                             on_delete=models.PROTECT, 
    #                              default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               default='published')
    status = models.CharField(max_length=10,choices=options,
                              default='published')

    objects = models.Manager()
    postobjects = PostObjects()

    tags = TaggableManager()
    def get_absolute_url(self):
        return reverse("blog:post_single", args=[self.slug])
    
    class Meta:
        ordering = ('-published',)
    def __str__(self) -> str:
        return self.title

    