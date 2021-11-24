from django.shortcuts import render

# Create your views here.
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})


def blog_article(requst, article_id):
    article = BlogArticles.objects.get(id=article_id)
    pub = article.publish
    return render(requst, "blog/content.html", {"article": article, "publish": pub})
