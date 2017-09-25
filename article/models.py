from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Article(models.Model):
    class Meta():
        """описывает название таблицы"""
        db_table = "article"

    article_title = models.CharField(max_length=200)
    article_text = RichTextUploadingField()
    article_date = models.DateTimeField()

    def __str__(self):
        """Возвращает строковое представление модели, а именно название статьи"""
        return self.article_title

class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)