from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import Article


class AllArticlesRssFeed(Feed):
    title = "Slynxes-Blog"
    link = "/"
    description = 'Slynxes All Blog'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return '%s'.format(item.title)

    def item_link(self, item):
        return reverse('blog:detail', kwargs={'pk': item.id})

    def item_description(self, item):
        return item.body_html