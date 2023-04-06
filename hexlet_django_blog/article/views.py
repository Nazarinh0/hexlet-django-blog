from django.shortcuts import render, get_object_or_404
from django.views import View
# from django.http import HttpResponse
from hexlet_django_blog.article.models import Article
from .forms import CommentArticleForm

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/article.html', context={
            'article': article,
        })


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles,
        })

class CommentArticleView(View):

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST) # Создаем экземпляр нашей формы
        if form.is_valid():
            comment = Comment(
                name - form.cleaned_data['content']
            )

        return render(request, 'comment.html', {'form': form}) # Передаем форму в контексте
