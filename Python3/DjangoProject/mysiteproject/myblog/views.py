from django.shortcuts import render
from .models import BlogArticles


def blog_title(request):
    mblogs = BlogArticles.objects.all()
    return render(request, "mblog/titles.html", {"mblogs": mblogs})


def blog_article(request, article_id):
    article = BlogArticles.objects.get(id=article_id)
    pub = article.publish
    return render(request, "mblog/content.html", {"article": article, "publish": pub})
# Create your views here.
