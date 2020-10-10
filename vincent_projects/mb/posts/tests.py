from django.test import TestCase
from .models import Post
from django.urls import reverse #new
# Create your tests here.

class PostModelTest(TestCase):#The TestCase module lets us create a sample database and our Post model.
	
	def setUp(self):
		Post.objects.create(text='just a test')

	def test_text_content(self):
		post = Post.objects.get(id = 1)
		expected_object_name = f'{post.text}'
		self.assertEqual(expected_object_name,'just a test')

#does it actually exist and return a HTTP 200 response?
#does it use HomePageView as the view?
#does it use home.html as the template?

class HomePageViewTest(TestCase):

	def setUp(self):
		Post.objects.create(text='this is another test')

	def test_view_url_exists_at_proper_location(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code,200)

	def test_view_url_by_name(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code,200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code,200)
		self.assertTemplateUsed(resp,'posts/home.html')