from democrance.commons.viewsets import BaseViewSet
from policy.models import Policy
from policy.serializers import PolicySerializer


class PolicyViewset(BaseViewSet):
    serializer_class = PolicySerializer
    queryset = Policy.objects.all()
