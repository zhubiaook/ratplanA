import os
import pathlib
import random
import sys
from datetime import timedelta

import django
import faker
from django.utils import timezone


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogproject.settings")
    django.setup()

    from blog.models import Category, Article, Tag
    from comments.models import Comment
    from django.contrib.auth.models import User
    print('clean database')
    Article.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    User.objects.all().delete()

    print('create a blog user')
    user = User.objects.create_superuser('admin', 'admin@zhubiaook.com', 'admin')
    category_list = ['Python学习笔记', '开源项目', '工具资源', '程序员生活感悟', 'test category']
    tag_list = ['django', 'Python', 'Pipenv', 'Docker', 'Nginx', 'Elasticsearch', 'Gunicorn', 'Supervisor', 'test tag']
    a_year_ago = timezone.now() - timedelta(days=365)

    print('create categories and tags')
    for cate in category_list:
        Category.objects.create(name=cate)

    for tag in tag_list:
        Tag.objects.create(name=tag)

    print('create a markdown sample article')
    Article.objects.create(
        title='Markdown',
        body=pathlib.Path(BASE_DIR).joinpath('scripts', 'md.sample').read_text(encoding='utf-8'),
        category=Category.objects.create(name='Markdown-Test'),
        author=user,
    )

    print('create some faked posts published within the past year')
    fake = faker.Faker('zh_CN')
    for _ in range(100):
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by('?').first()
        created_time = fake.date_time_between(start_date='-1y',
                                              end_date='now',
                                              tzinfo=timezone.get_current_timezone())

        article = Article.objects.create(
            title=fake.sentence().rstrip('.'),
            body='\n\n'.join(fake.paragraphs(10)),
            created_time=created_time,
            category=cate,
            author=user,
        )

        article.tags.add(tag1, tag2)
        article.save()

    print('create some comments')
    for article in Article.objects.all()[:20]:
        article_created_time = article.created_time
        delta_in_days = '-' + str((timezone.now() - article_created_time).days) + 'd'
        for _ in range(random.randrange(3, 15)):
            Comment.objects.create(
                name=fake.name(),
                email=fake.email(),
                url=fake.uri(),
                text=fake.paragraph(),
                created_time=fake.date_time_between(
                    start_date=delta_in_days,
                    end_date="now",
                    tzinfo=timezone.get_current_timezone()),
                article=article,
            )

    print('done!')
