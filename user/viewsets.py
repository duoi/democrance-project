from democrance.commons.viewsets import BaseViewSet
from user.models import User
from user.serializers import CustomerSerializer


class CustomerViewset(BaseViewSet):
    serializer_class = CustomerSerializer
    queryset = User.objects.filter(is_customer=True)
