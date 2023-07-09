from typing import Any, Dict
from django.views.generic import DetailView
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from .models import Post, Hero, Contact, Comment


class BlogPageView(TemplateView):
    template_name = 'blog/post_list.html'
    paginate_by = 10
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve all posts and order them
        posts = Post.objects.order_by(self.ordering)

        # Paginate the posts
        paginator = Paginator(posts, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['posts'] = page_obj
        context['hero'] = Hero.objects.all()
        context['contact_data'] = Contact.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        content = request.POST['content']
        comment = Comment.objects.create(
            post=post, content=content, author=request.user)
        # You may add additional logic here, such as redirecting to the post detail page
        return redirect('blog:post-detail', pk=pk)
