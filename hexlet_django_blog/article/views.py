from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from hexlet_django_blog.article.models import Article


class ArticleView(View):

    def get(self, request, tags, article_id):
        return render(
            request,
            'article/article.html',
            context={'article_id': article_id, 'tags': tags}
        )


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })
