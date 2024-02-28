from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=50)  # object_id is provided with a character field
    content_object = GenericForeignKey('content_type', 'object_id')
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    home_page = models.URLField(blank=True, null=True)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.created_at}'

