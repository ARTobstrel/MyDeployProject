from django.contrib import auth
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, get_object_or_404
from article.models import Article

#My Views
def index(request):
    """Основная страница"""
    return render_to_response('index.html')

def articles(request, page_number=1):
    """Список всех статей"""
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    return render_to_response('articles.html', {'articles':current_page.page(page_number),
                                                'username':auth.get_user(request).username,
                                                }
                              )

def article(request, art_id=1):
    """Выбранная статья"""
    args = {}
    args['article'] = get_object_or_404(Article, id=art_id)
    return render_to_response('article.html', args)