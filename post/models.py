from django.conf import settings
from django.db import models


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	photo = models.ImageField(upload_to='post')
	# filtered_image = models.ImageField(upload_to'post/filtered')
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	passed_time = models.TimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return f'Post (PK: {self.pk}, Author: {self.author.username})'

	def delete(self, post_pk):
		self.photo.delete()
		super(Post, self).delete(post_pk)

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.TextField(max_length=1000)

	def __str__(self):
		return f'Comment (PK: {self.pk}, Author:{self.author.username})'