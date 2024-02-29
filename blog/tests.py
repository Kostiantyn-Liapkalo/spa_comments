from django.test import TestCase
from .models import Blog

# Create your tests here.
class BlogModelTest(TestCase):

    # Create object Blog
    def test_blog_creation(self):

        blog = Blog.objects.create(
            title='Test Blog Title',
            content='This is a test blog content.'
        )

        # Checking whether the Blog object was created correctly
        self.assertEqual(blog.title, 'Test Blog Title')
        self.assertEqual(blog.content, 'This is a test blog content.')

    def test_blog_str_method(self):

        blog = Blog.objects.create(
            title='Another Test Blog',
            content='This is another test blog content.'
        )

        # Checking that the __str__ method returns the expected value
        expected_str = 'Another Test Blog'
        self.assertEqual(str(blog), expected_str)
