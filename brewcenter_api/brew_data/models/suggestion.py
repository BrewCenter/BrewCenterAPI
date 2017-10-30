from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from accounts.models import Token


class Suggestion(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    suggested_object_id = models.PositiveIntegerField()
    suggested_object = GenericForeignKey('content_type', 'suggested_object_id')
    replaced_object_id = models.PositiveIntegerField(null=True, blank=True)
    replaced_object = GenericForeignKey('content_type', 'replaced_object_id')

    submitted_by_user = models.ForeignKey(User, null=True, blank=True)
    submitted_with_token = models.ForeignKey(Token, null=True, blank=True)
    submitted_timestamp = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
