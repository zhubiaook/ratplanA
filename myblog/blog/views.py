from django.db.models import Q
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Article, Category, Tag
from django.views.generic import ListView, DeleteView
from pure_pagination import PaginationMixin
from django.contrib import messages


class IndexView(PaginationMixin, ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = 10


class ArchiveView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(
            created_time__year=year, created_time__month=month)


class CategoryView(IndexView):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        cate = get_object_or_404(Category, pk=pk)
        return super(CategoryView, self).get_queryset().filter(
            category=cate
        )


class TagView(IndexView):
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        tags = get_object_or_404(Tag, pk=pk)
        return super(TagView, self).get_queryset().filter(
            tags=tags
        )


class DetailView(DeleteView):
    pass


def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    article.increase_views()
    return render(request, 'blog/single.html', context={'article': article})


def search(request):
    q = request.GET.get('q')
    if q:
        article_list = Article.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
        return render(request, 'blog/index.html', {'article_list': article_list})
    else:
        error_message = '请输入搜索词'
        messages.add_message(request, messages.ERROR, error_message, extra_tags='danger')
    return redirect(reverse('blog:index'))
