from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .models import Post
from .forms import PostForm


# def post_list_view(request):
#     posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html',
#                   {'posts_list': posts})

class PostListView(generic.ListView):
    # model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
    # try:
    #     post = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     post = None
    #     print("Excepted")
    # return render(request, 'blog/post_detail.html',
    #               {'post': post})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# def post_add_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')

#     else:
#         form = PostForm()

#     return render(request, 'blog/create_post.html',
#                   context = {'form': form})
    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #     user = User.objects.all()[0]
    #     Post.objects.create(title=post_title, text=post_text,
    #                         author=user, status='pub')
    # else:
    #     print('GET request')
    # return render(request, 'blog/create_post.html')


class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    form_class = PostForm

# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/create_post.html', context={'form': form})


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'

# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', context={'post': post})


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    # success_url = '/blog'
    # def get_success_url(self):
    #     return reverse('posts_list')
    success_url = reverse_lazy('posts_list')
