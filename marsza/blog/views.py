from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm, EditForm, CommentForm, EditCommentForm
from django.urls import reverse_lazy, reverse
from django.db.models import Count

class Homepage(ListView):
    paginate_by = 10
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-created']
    queryset = Post.objects.annotate(likes_count=Count('likes'))

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Homepage, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryPage(request, cat):
    category_posts = Post.objects.filter(category=cat.replace('-', ' '))
    return render(request, 'blog/category.html', {'cat':cat.title().replace('-', ' '), 'category_posts':category_posts})

class PostDetails(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetails, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        comments_count = Comment.objects.filter(post=self.kwargs['pk']).count()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['comments_count'] = comments_count
        context["cat_menu"] = cat_menu
        context["liked"] = liked
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategory(CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategory, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/edit_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(EditPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def Like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog:post_details', args=[str(pk)]))

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class EditComment(UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'blog/edit_comment.html'

class DeleteComment(DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'
    success_url = reverse_lazy('blog:home')   