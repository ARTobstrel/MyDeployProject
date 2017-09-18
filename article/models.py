from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta():
        """описывает название таблицы"""
        db_table = "article"

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()

class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)