from django.db import models


class BaseModelMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        if hasattr(self, "name"):
            return f"{self.__class__.__name__} <id: {self.pk} {self.name}>"
        else:
            return "%s object (%s)" % (self.__class__.__name__, self.pk)

    class Meta:
        abstract = True


class SoftDeleteMixin:
    """
        Soft delete a model instance.
    """

    def perform_destroy(self, instance):
        if hasattr(instance, "is_active"):
            instance.is_active = False
            instance.save()
        else:
            instance.delete()
