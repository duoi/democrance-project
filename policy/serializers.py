from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from policy.models import (
    PolicyType,
    Policy
)


class PolicySerializer(serializers.Serializer):
    """
    Typically I'd use generic serializers rather than model serializers to:
    1. Avoid abstracting away crucial model creation and updating code
    2. Help the serializers be self-documenting
    3. Allow for snakeCase inputs, for example:

       someField = serializers.BooleanField(
            source=some_field,
            help_text="I am officially `some_field` but inputted with snakeCase"
       )
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Because you're supposed to pass choices inline, everything
        # catches on fire if you don't have a table already there i.e
        # prior to your first migration. So we override it and catch
        # it on execution to update the types instead.
        self.fields['type'].choices = PolicyType.objects.all()

    id = serializers.IntegerField(
        read_only=True,
        required=False,
        help_text="The policy's primary key"
    )
    customer = serializers.IntegerField(
        help_text='The user that this policy belongs to',
        write_only=True,
        required=True,
    )
    type = serializers.ChoiceField(
        write_only=True,
        required=True,
        help_text="The type of coverage that this policy is for",
        choices=[]
    )
    premium = serializers.IntegerField(
        write_only=True,
        required=True,
        help_text="The premium that this policy will command"
    )
    cover = serializers.IntegerField(
        write_only=True,
        required=True,
        help_text="The financial amount that this policy will seek to cover"
    )

    def validate(self, attrs):
        # Run the standard validations first before getting to the custom ones
        super().validate(attrs)

        try:
            customer_obj = get_user_model().objects.get(
                id=attrs['customer'],
                is_customer=True
            )
        except get_user_model().DoesNotExist:
            raise ValidationError({"customer": {"Invalid user": f"Customer with ID {attrs['customer']} doesn't exist."}})

        attrs['customer'] = customer_obj
        return attrs

    def create(self, validated_data):
        """
        Example return:

        {
            'id': 1
        }
        """
        policy = Policy.objects.create(**validated_data)
        return policy
