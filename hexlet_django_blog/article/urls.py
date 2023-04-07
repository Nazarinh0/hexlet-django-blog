from django.urls import path
from hexlet_django_blog.article import views
# from django.views.generic.base import TemplateView


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<int:id>/', views.ArticleView.as_view(), name='article'),
    path('create/', views.ArticleFormCreateView.as_view(), name='article_create')
]