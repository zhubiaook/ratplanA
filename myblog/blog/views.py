import re
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import Article, Category, Tag
from markdown import Markdown
from markdown.extensions.toc import TocExtension


def index(request):
    article_list = Article.objects.all()
    return render(request, 'blog/index.html', context={'article_list': article_list})


def archive(request, year, month):
    article_list = Article.objects.filter(
        created_time__year=year,
        created_time__month=month
    )
    return render(request, 'blog/index.html', context={'article_list': article_list})


def category(request, pk):
    article_list = Article.objects.filter(
        category=Category.objects.get(pk=pk)
    )
    return render(request, 'blog/index.html', context={'article_list': article_list})


def tag(request, pk):
    article_list = Article.objects.filter(
        tags=Tag.objects.get(pk=pk)
    )
    return render(request, 'blog/index.html', context={'article_list': article_list})


def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    md = Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify)
    ])
    article.body = md.convert(article.body)
    result = re.search(r'<ul>(.*)</ul>', md.toc, re.S)
    if result.group(1):
        article.toc = md.toc
    else:
        article.toc = None
    return render(request, 'blog/single.html', context={'article': article})
