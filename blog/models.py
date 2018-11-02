from django.db import models

from django.utils import timezone
from stdimage.models import StdImageField

import uuid
import os
from datetime import datetime

# Create your models here.
def get_image_upload_path(self, filename):
  n = datetime.now()
  prefix = "upload/"
  ymd='/'.join([n.strftime('%Y'), n.strftime('%m'), n.strftime('%d'), ""]) + "/"
  directory=str(self.author.id) + "/"
  name=str(uuid.uuid4()).replace("-", "")
  extension=os.path.splitext(filename)[-1]

  print(''.join([prefix, directory, ymd, name, extension]))

  return ''.join([prefix, directory, ymd, name, extension])


class Post(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  image = StdImageField(upload_to=get_image_upload_path, blank=True, null=True, variations={
    'large': (600, 400),
    'thumbnail': (100, 100, True),
    'medium': (300, 200),
    })
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title


class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.text


class Like(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)

class CommentLike(models.Model):
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)
