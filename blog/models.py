from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    status = models.CharField(choices=(("P", "published"), ("D", "draft")), max_length=1)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)
    published = models.DateTimeField(default=timezone.now, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    slug = models.SlugField(db_index=True)
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args = [self.slug, self.created.year, self.created.month, self.created.day])
    
    def __str__(self):
        return (self.title)
    
    def __repr__(self):
        return (self.title)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)
    comment = models.TextField()
    
    def __str__(self):
        return (f"{self.post}'s comment")
        