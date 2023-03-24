from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class ArticleView(View):

    def get(self, request, tags, article_id):
        return render(
            request,
            'article/article.html',
            context={'article_id': article_id, 'tags': tags}
        )

def index(request):
    return render(
        request,
        'article/index.html',
        context={'title': 'article_app'}
    )