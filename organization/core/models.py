import uuid

from django.db import models


def string_uuid():
    return str(uuid.uuid4())


class BaseModel(models.Model):
    id = models.CharField(primary_key=True, default=string_uuid, editable=False, max_length=36)
    last_modified_at = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        abstract = True
