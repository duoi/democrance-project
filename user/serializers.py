from django.contrib.auth import get_user_model
from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    """
    The customer serializer has the required fields `first_name`,
    `last_name` and `dob`, and on success returns the User model.

    However, those fields are set to `write_only` and the API
    should just return the user PK.
    """
    id = serializers.IntegerField(
        read_only=True,
        required=False,
        help_text="The customer's primary key"
    )
    first_name = serializers.CharField(
        write_only=True,
        required=True,
        help_text="The customer's first name"
    )
    last_name = serializers.CharField(
        write_only=True,
        required=True,
        help_text="The customer's last name"
    )
    dob = serializers.DateField(
        write_only=True,
        required=True,
        source="date_of_birth",
        input_formats=['%d-%m-%Y', 'iso-8601'],
        help_text="The customer's date of birth"
    )

    def create(self, validated_data):
        user = get_user_model().objects.create(
            is_customer=True,
            **validated_data
        )
        return user
