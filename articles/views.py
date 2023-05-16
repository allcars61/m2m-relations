# from django.shortcuts import render
#
# from articles.models import Article
#
#
# def articles_list(request):
#     template = 'articles/news.html'
#     context = {}
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     ordering = '-published_at'
#
#     return render(request, template, context)


from django.shortcuts import render
from django.utils import timezone
from .models import Article

def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'

    articles = Article.objects.filter(published_at__isnull=False, published_at__lte=timezone.now()).order_by(ordering)

    context = {'articles': articles}
    return render(request, template, context)