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
        return 'Article %d: %s' % (self.id, self.article_title)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)


class Mainpage(models.Model):
    """Данная модель отвечает за главную страницу блога"""

    class Meta:
        db_table = 'mainpage'

    page_title = models.CharField(max_length=200)
    start_text = RichTextUploadingField()

    def __str__(self):
        return 'Main page'
