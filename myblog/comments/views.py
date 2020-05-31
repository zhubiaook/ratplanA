from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from blog.models import Article
from .forms import CommentForm


@require_POST
def comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        cmt = form.save(commit=False)
        cmt.article = article
        cmt.save()
        messages.add_message(request, messages.SUCCESS, '评论发表成功!', extra_tags='success')
        return redirect(reverse('blog:detail', args=[pk]))
    context = {
        'form': form,
        'article': article
    }
    messages.add_message(request, messages.ERROR, '评论发表失败，请参考表单错误提示修改，重新提交', extra_tags='danger')
    return render(request, 'comments/inclusions/_form.html', context=context)