from django import template
from ..models import Article, Category, Tag
from django.db.models.aggregates import Count


register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_articles(context, num=5):
    return {
        'recent_article_list': Article.objects.all()[:num]
    }


@register.inclusion_tag('blog/inclusions/_archive_list.html', takes_context=True)
def show_archives(context):
    return {
        'archive_list': Article.objects.dates('created_time', 'month', 'DESC')
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.annotate(num_article=Count('article')).filter(num_article__gt=0)
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.annotate(num_article=Count('article')).filter(num_article__gt=0)
    }