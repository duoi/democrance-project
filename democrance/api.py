from django.urls import include, path
from rest_framework import routers

from user.viewsets import CustomerViewset
from policy.viewsets import PolicyViewset

router = routers.SimpleRouter()
router.register(r'create_policy', PolicyViewset)
router.register(r'create_customer', CustomerViewset)

urlpatterns = [
    path(r'api/v1/', include((router.urls, 'router'), namespace='v1'))
]
