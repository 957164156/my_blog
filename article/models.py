from django.db import models
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    '''wen zhang de fenlei'''
    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name

class Tag(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):

        return self.name


class Article(models.Model):

    title = models.CharField(max_length=100)  #

    #fenlei
    category = models.CharField(max_length=50, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    '''wenzhang  neirong '''
    content = models.TextField(blank=True, null=True)
    '''forginer Key'''
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    #author = models.ForeignKey(User,default='')
    def __str__(self):

        return self.title

    class Meta:
        ordering = ['-create_time']

    def get_absolute_url(self):

        return reverse('article:detail', kwargs={'pk': self.pk})

