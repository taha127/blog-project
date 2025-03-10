from django.shortcuts import render
from .models import Post
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

def post_list_view(request):
    posts = Post.objects.filter(status='pub')
    return render(request, 'blog/posts_list.html',
                  {'posts_list': posts})
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # try:
    #     post = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     post = None
    #     print("Excepted")
    return render(request, 'blog/post_detail.html',
                  {'post': post})