from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'modified_time']
    fields = ['title', 'body', 'category', 'tags', 'created_time']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Category)

