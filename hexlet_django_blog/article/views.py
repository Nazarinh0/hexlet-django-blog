from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request, tags, article_id):
        return render(
            request,
            'article/article.html',
            context={'article_id': article_id, 'tags': tags}
        )
