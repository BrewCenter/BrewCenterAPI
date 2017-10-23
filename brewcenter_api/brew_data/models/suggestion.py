from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from accounts.models import Token


class Suggestion(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    replace_object_id = models.PositiveIntegerField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    submitted_by_user = models.ForeignKey(User)
    submitted_with_token = models.ForeignKey(Token, null=True, blank=True)
    submitted_timestamp = models.DateTimeField(auto_now_add=True)
