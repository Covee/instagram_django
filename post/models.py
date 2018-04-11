from django.conf import settings
from django.db import models


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	photo = models.ImageField(upload_to='post')
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return f'Post (PK: {self.pk}, Author: {self.author.username})'

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.TextField(max_length=1000)

	def __str__(self):
		return f'Comment (PK: {self.pk}, Author:{self.author.username})'