from pathlib import PurePath
from django.utils.text import slugify
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Organisation(models.Model):
    name = models.TextField()
    members = models.ManyToManyField(
        User,
        blank=True,
        related_name='%(app_label)s_organisations',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def organisation_image_path(self, filename):
        """Provide a nice path and filename for uploads: vN_organisations/N-name.EXT."""

        # Assumes __main__ = 'mhep.v1.models.organisation'
        version = __name__.split(".")[1]
        id = self.id
        name = slugify(self.name)
        extension = PurePath(filename).suffix

        return f"{version}_organisations/{id}-{name}{extension}"

    logo = models.FileField(upload_to=organisation_image_path, null=True, blank=True)

    def __str__(self):
        return self.name
