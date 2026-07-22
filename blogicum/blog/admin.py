from django.contrib import admin
from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'is_published',
        'category',
        'pub_date',
        'location',

    )

    list_editable = (
        'is_published',
        'category',
    )
    search_fields = (
        'title',
    )

    list_filter = (
        'category',
    )

    list_display_links = (
        'title',
    )

    empty_value_display = 'Не задано'


class PostInLine(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInLine,
    )

    list_display = (
        'title',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)