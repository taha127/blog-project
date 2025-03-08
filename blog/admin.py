from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'datetime_created', 'status')
    ordering = ('-status',)
    # list_filter = ('status', 'datetime_created', 'author')
    # search_fields = ('title', 'text')
    # prepopulated_fields = {'slug': ('title',)}
    # date_hierarchy = 'datetime_created'
    # ordering = ['status', 'datetime_created']
    # fields = ('title', 'text', 'author', 'status', 'slug')
    # readonly_fields = ('datetime_created', 'datetime_modified')


# admin.site.register(Post, PostAdmin) //old way of registering models
