from django.db import models

# Create your models here.
class Comment(models.Model):
    '''评论标题'''
    title = models.CharField(max_length=100)
    ''''''
    content = models.TextField(null=True)
    '''时间'''
    create_time = models.DateTimeField(auto_now_add=True)
    '''评论的用户信息'''
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=255)
    user_url = models.URLField(blank=True)

    '''评论对应的文章'''
    article = models.ForeignKey('article.Article')

    def __str__(self):

        return self.title[:20]