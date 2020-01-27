import uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone

from democrance.commons.mixins import ModelWithTimestamp


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a full User model.

    """

    class Meta:
        db_table = 'auth_user'
        managed = True

    username = models.CharField(
        default=uuid.uuid4,
        unique=True,
        db_index=True,
        max_length=36
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Email Address',
        db_index=True,
    )
    first_name = models.TextField(
        null=True,
        blank=True,
        default=None
    )
    last_name = models.TextField(
        null=True,
        blank=True,
        default=None
    )
    date_of_birth = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
        help_text="The date of birth of this user"
    )
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_customer = models.BooleanField(
        default=True,
        help_text="Whether or not this user is a Democrance customer"
    )
    is_active = models.BooleanField(
        db_index=True,
        default=True
    )
    is_superuser = models.BooleanField(
        default=False,
        help_text='Designates whether the user is a superuser.',
    )
    date_joined = models.DateTimeField(
        default=timezone.now
    )

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.

        :return:
        """
        return '%s %s' % (self.first_name, self.last_name or '')

    def get_short_name(self):
        """
        Returns the short name for the user

        :return:
        """
        return self.first_name or self.username


    # Alternative implementation: rather than adding an `is_customer` boolean just add
    # the user to a `customer` group.
    #
    # def _add_to_group(self):
    #     """
    #     Add user to customer group.
    #
    #     :return:
    #     """
    #     group = Group.objects.get_or_create(name="CUSTOMERS")
    #     group.user_set.add(self)
    #
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self._add_to_group()
    #
    #     return self
