from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from .models import Comment

# Create your tests here.
class CommentModelTest(TestCase):
    # Create object ContentType and User
    def setUp(self):
        self.content_type = ContentType.objects.create(model='post')
        self.user = User.objects.create_user(username='testuser', password='testpass')

    # Create object Comment
    def test_comment_creation(self):
        comment = Comment.objects.create(
            content_type=self.content_type,
            object_id=1,
            user_name='Koss Lip',
            email='koss@koss.com',
            text='This is a test comment.'
        )

        # Checking whether the Comment object was created correctly
        self.assertEqual(comment.user_name, 'Koss Lip')
        self.assertEqual(comment.email, 'koss@koss.com')
        self.assertEqual(comment.text, 'This is a test comment.')
        self.assertEqual(comment.content_type, self.content_type)
        self.assertEqual(comment.object_id, 1)


    def test_comment_str_method(self):
        comment = Comment.objects.create(
            content_type=self.content_type,
            object_id=1,
            user_name='Koss Lip',
            email='koss@koss.com',
            text='Another test comment.'
        )

        # Checking that the __str__ method returns the expected value
        expected_str = 'Koss Lip - ' + str(comment.created_at)
        self.assertEqual(str(comment), expected_str)

