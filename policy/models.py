from django.db import models

from democrance.commons.mixins import ModelWithTimestamp


class PolicyType(ModelWithTimestamp):
    """
    This is being done like this in order to standardise the policy types.

    "Why not use a enumeration" - these make changes complicated and will
    require database migrations, and also require programmatic insertion.
    """
    name = models.TextField(
        help_text="The name of this policy type"
    )

    def __str__(self):
        return f"{self.name}"


class Policy(ModelWithTimestamp):
    """
    The insurance policy model used for Democrance
    """
    customer = models.ForeignKey(
        to='user.User',
        on_delete=models.DO_NOTHING,
        related_name="policies",
        help_text="The customer that this policy belongs to"
    )
    type = models.ForeignKey(
        PolicyType,
        on_delete=models.DO_NOTHING,
        help_text="The type of policy associated with this cover"
    )
    premium = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        help_text="The premium to be paid for this cover"
    )
    cover = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        help_text="The amount that this policy seeks to cover"
    )

    def __str__(self):
        return f"{self.pk} {self.customer}"
