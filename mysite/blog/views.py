from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from accounts.models import User
from taggit.models import Tag
from .models import Post
from .forms import Comment_form

def post_list(request,category_slug=None,tag_slug=None):
    posts=Post.objects.all()
    template='blog/posts.html'
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        posts=posts.filter(tags=tag)
    elif category_slug:
        posts = posts.filter(category=category_slug)
    else:
        template='blog/index.html'
    
    return render(request,template,{'posts':posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    tags=post.tags.all()
    comments = post.postcomments.filter(active=True)
    if request.method == "POST":
        comment_form=Comment_form(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        comment_form=Comment_form()
    return render(
        request,
        "blog/detail.html",
        {"post": post,'comments':comments,'comment_form':comment_form,'tags':tags})

    
        








