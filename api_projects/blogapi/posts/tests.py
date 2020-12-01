from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):
	@classmethod

	def setUpTestData(cls):
		testuser1 = User.objects.create_user(
			username = 'testuser1',password = '1234'
		)
		testuser1.save()

		test_post = Post.objects.create(
			author = testuser1,
			title = 'Blog Title',
			body = 'Body content...'
		)
		test_post.save()

	def test_blog_content(self):
		post = Post.objects.get(id = 1)
		author = f'{post.author}'
		title = f'{post.title}'
		body = f'{post.body}'
		self.assertEqual(author, 'testuser1')
		self.assertEqual(title, 'Blog Title')
		self.assertEqual(body, 'Body content...')
def get_queryset(self):
	        """
	        This view should return a list of all the purchases
	        for the currently authenticated user.
	        """
	        user = self.request.user
	        return Post.objects.filter(author=user)

