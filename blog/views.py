from django.shortcuts import render, get_object_or_404, redirect

from django.utils import timezone
from .models import Post, Comment, Like, CommentLike
from .forms import PostForm, CommentForm

from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
  posts = Post.objects.all().order_by('-created_date')

  return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):

  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm()
  return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):

  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm(instance=post)

  return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
  
  post = get_object_or_404(Post, pk=pk)
  # delete image
  post.image.delete()
  post.delete()
  return redirect('post_list')

def add_comment_to_post(request, pk):

  post = get_object_or_404(Post, pk=pk)

  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = post
      comment.save()
      return redirect('post_detail', pk=post.pk)

  else:
     form = CommentForm(initial={
       'author' : request.user,
     })

  return render(request, 'blog/add_comment_to_post.html', {'form': form})

def remove_comment(request, pk):

  comment = get_object_or_404(Comment, pk=pk)
  comment.delete()
  return redirect('post_detail', pk=comment.post.pk)

def like_post(request, pk):

  post = get_object_or_404(Post, pk=pk)
  qset = Like.objects.filter(post=post).filter(author=request.user)
  if qset.count() > 0:
    for like in qset:
      like.delete()
  else:
    like = Like()
    like.post = post
    like.author = request.user
    like.save()
  return redirect('post_detail', pk=pk)

def like_comment(request, pk):

  comment = get_object_or_404(Comment, pk=pk)
  qset = CommentLike.objects.filter(comment=comment).filter(author=request.user)
  if qset.count() > 0:
    for like in qset:
      like.delete()
  else:
    like = CommentLike()
    like.comment = comment
    like.author = request.user
    like.save()
  return redirect('post_detail', pk=comment.post.pk)


