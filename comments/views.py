from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentFrom
from article.models import Article
from django.http import HttpResponse

# Create your views here.

def article_comment(request, article_pk):
    '''文章评论提交函数'''
    #return HttpResponse(article_pk)
    #获取到文章
    article = get_object_or_404(Article, pk = article_pk)


    if  request.method == 'POST':
        #只有当是post请求
        form = CommentFrom(request.POST)
        if form.is_valid():

            #
            comment = form.save(commit=False)

            comment.article = article

            comment.save()


            return redirect(article)
        else:

            comment_list = article.comment_set.all()

            context = {'post': article,
                   'form': form,
                   'comment_list': comment_list
                   }
            return render(request, 'blog/detail.html', context=context)

    return redirect(article)