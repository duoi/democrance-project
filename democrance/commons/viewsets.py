from rest_framework import mixins, viewsets


class BaseViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    An inheritable "base" view set. This doesn't make much sense now
    but if we were to implement a more complex API that also lists,
    updates and/or deletes and we have a complex permissions system
    it makes more sense to centralise and generalize the code to make
    building new APIs quicker and more reliable, and for issues to
    become more obvious.
    """
    serializer_class = None
