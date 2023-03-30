from django.db import models


class Article(models.Model):
    # мы не описываем поле id, которое обычно является первичным ключом.
    # В models.Model оно уже описано, и нам не нужно это делать дополнительно.
    # Но мы его можем переопределить.
    name = models.CharField(max_length=200) # название статьи
    body = models.TextField() # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)
