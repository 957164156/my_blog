from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from article.models import Article
from comments.forms import CommentFrom

# Create your views here.

def blog_index(request):

    return HttpResponse('Hello,World')


def home(request):

    return HttpResponse('Hello , Django')


def detail(request, pk):


    article = get_object_or_404(Article, pk = pk)

    #取出所有的评论
    form = CommentFrom()
    comment_list = article.comment_set.all()
    #创建context
    context = {
        'article':article,
        'form':form,
        'comment_list':comment_list
    }

    return render(request, 'blog/detail.html', context=context)

def index(request):

    articles = Article.objects.all()
    recent_article = articles[:5]
    contentInfo = {
        'articles_list':articles,
        'content':'django test content',
        'recent_articles':recent_article
    }

    return render(request, 'blog/index.html', context=contentInfo)


