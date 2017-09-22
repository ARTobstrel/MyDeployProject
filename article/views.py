from django.contrib import auth
from django.core.paginator import Paginator
from django.shortcuts import render_to_response
from article.models import Article

#My Views
def articles(request, page_number=1):
    """Основная страница"""
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 9)
    return render_to_response('articles.html', {'articles':current_page.page(page_number),
                                                'username':auth.get_user(request).username,
                                                }
                              )