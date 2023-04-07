from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# from django.http import HttpResponse
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm
from django.contrib import messages


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/article.html', context={
            'article': article,
        })


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        messages.get_messages(request)
        return render(request, 'article/index.html', context={
            'articles': articles,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        messages.get_messages(request)
        return render(request, 'article/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, 'Article was added successfully')
            return redirect('articles') # Редирект на указанный маршрут
        messages.error(request, 'Failed to add article')
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'article/create.html', {'form': form})


# class CommentArticleView(View):
#
#     def get(self, request, *args, **kwargs):
#         form = CommentArticleForm(request.POST) # Создаем экземпляр нашей формы
#         if form.is_valid():
#             comment = Comment(
#                 name - form.cleaned_data['content']
#             )
#
#         return render(request, 'comment.html', {'form': form}) # Передаем форму в контексте
