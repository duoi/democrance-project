from django.core.management.base import BaseCommand
from policy.models import PolicyType

class Command(BaseCommand):
    help = 'Add default policy to database'

    def handle(self, *args, **options):
        obj, created = PolicyType.objects.get_or_create(name='personal-accident')
        if created:
            print(f'------ Created policy type: "{obj}"')
