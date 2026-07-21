from django.shortcuts import render
from django.http import HttpResponseNotFound


def index(request):
    template = 'blog/index.html'
    sorted_posts = sorted(posts, key=lambda d: -d['id'])
    context = {'posts': sorted_posts}
    return render(request, template, context)


def post_detail(request, id: int):
    template = 'blog/detail.html'
    try:
        context = {'post': posts[id]}
    except IndexError:
        return HttpResponseNotFound(render(request, 'error/404.html'))
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    filter_post_for_category = [
        post for post in posts if post['category'] == category_slug
    ]

    sorted_filter_post_for_category = sorted(
        filter_post_for_category,
        key=lambda b: -b['id']
    )
    context = {
        'category': category_slug,
        'post_for_category': sorted_filter_post_for_category
    }

    return render(request, template, context)
