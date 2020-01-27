from django.contrib import admin

from policy.models import (
    Policy,
    PolicyType
)


admin.site.register(Policy)
admin.site.register(PolicyType)
