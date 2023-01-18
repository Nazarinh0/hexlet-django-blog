from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'article/article.html',
            context={'app_name': 'ARTICLE OR ARCTIC?'}
        )
