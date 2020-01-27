from django.db import models
from django.utils.timezone import now


class ModelWithTimestamp(models.Model):
    """
    Adds fields to record creation and update dates of models.

    Should replace default subclassing of `model.Model` on new model creation.
    """
    date_created = models.DateTimeField(
        help_text='The date that this model was created',
        default=now,
    )
    date_updated = models.DateTimeField(
        help_text='The date that this model was updated',
        default=None,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.date_created = now()
        self.date_updated = now()

        super().save(*args, **kwargs)

    class Meta:
        abstract = True
