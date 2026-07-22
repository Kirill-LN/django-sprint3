from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Post, Category

def index(request):
    template = 'blog/index.html'
    posts = Post.objects.select_related(
        'location',
        'author',
    ).filter(is_published=True)

    context = {
        'post_list': posts
    }
    return render(request, template, context)


def post_detail(request, id: int):
    template = 'blog/detail.html'

    post = get_object_or_404(
        Post.objects.select_related(
            'location',
            'author',
        ).filter(is_published=True),
        pk=id
    )
    context = {
        'post': post
    }

    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    category = get_object_or_404(Category, slug=category_slug)

    posts = Post.objects.select_related(
        'category',
        'author',
        'location',
    ).filter(
        is_published=True,
        category__is_published=True,
        category__slug=category_slug,
    ).order_by('category')

    context = {
        'post_list': posts,
        'category': category,
    }

    return render(request, template, context)