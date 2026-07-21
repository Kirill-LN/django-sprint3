from django.urls import path, include

urlpatterns = [
    path(
        '',
        include('blog.urls', namespace='blog')
    ),

    path(
        'pages/',
        include('pages.urls', namespace='pages')
    )
]
