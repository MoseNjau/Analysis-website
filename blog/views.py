from django.utils.text import slugify
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import AddPostForm

def post_list(request):
    posts = Post.objects.filter(status = "P")
    blogs = [post for post in posts]
    context = {
        "posts" : posts,
        "blogs" : blogs,
        }
    
    return render(request, "blog/post_list.html", context)

def post_detail(request, post_slug, year, month, day):
    post = get_object_or_404(Post, slug=post_slug, created__year=year, created__month=month, created__day=day)
    context = {
        "post": post,
        }
    
    return render(request,"blog/post_detail.html", context)

class PostList(ListView):
    template_name = "blog/post_list.html"
    queryset = Post.objects.filter(status = "P")

class PostDetail(DetailView):
    template_name = "blog/post_detail.html"
    queryset = Post.objects.filter(status = "P")
    
    def get_object(self):
        return get_object_or_404(
            Post,
            slug=self.kwargs.get("post_slug"),
            created__year=self.kwargs.get("year"),
            created__month=self.kwargs.get("month"), 
            created__day=self.kwargs.get("day"))
    
    def post(self, request,post_slug, year, month, day):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.author = request.user
            new_comment.post=get_object_or_404(Post, 
                                               slug=post_slug, 
                                               created__year=year, 
                                               created__month=month, 
                                               created__day=day)
            new_comment.save()
            
        return redirect(reverse("blog:post_detail", args = [post_slug, year, month, day]))
    
                                
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "form": CommentForm(),
            "post": self.get_object(),
        }
        return context
class MyPosts(LoginRequiredMixin, View):
    template_name = "blog/my_posts.html"
    
    def get(self, request, status=None):
        posts = Post.objects.filter(author=request.user)
        if status:
            posts = posts.filter(status=status[0].upper())
        context = {
            "posts":posts,
        }
        return render (request, self.template_name, context)
    
class AddPosts(LoginRequiredMixin, View):
    template_name = "blog/add_post.html"
    
    def get(self, request):
        form = AddPostForm()
        context = {
            "form":form,
        }
        return render (request, self.template_name, context)
        
    def post(self, request, slug, year, month, day):
        form = AddPostForm(data=request.POST)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = slugify(form.cleaned_data.get("title"))
            if form.cleaned_data.get("status") == 'D':
                new_post.published = None
            new_post.save()
        return redirect(reverse("blog:my_posts"))
    
class EditPost(LoginRequiredMixin, View):
    template_name = "blog/edit_post.html"
    
    def get(self, request, slug, year, month, day):
        post = get_object_or_404(Post, slug=slug,
                                 created__year=year,
                                 created__month=month,
                                 created__day=day)
        data = {
            "title" : post.title,
            "status" : post.status,
            "body" : post.body,
        }
        form = AddPostForm(data=data)
        context = {
            "form":form,
        }
        return render (request, self.template_name, context)
        
    def post(self, request, slug, year, month, day):
        post = get_object_or_404(
                            Post, slug=slug,
                            created__year=year,
                            created__month=month,
                            created__day=day)
        form = AddPostForm(data=request.POST)
        
        if form.is_valid():
            form.save(commit=False)
        return redirect(reverse("blog:my_posts"))

class PostView(View):
    def get(self, request):
        posts = PostView.objects.all()  # Replace YourPostModel with your actual model name
        context = {'posts': posts}
        return render(request, 'blog/post_view.html', context)