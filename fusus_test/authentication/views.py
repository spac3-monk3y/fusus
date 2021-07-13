from .serializers import GroupSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

# NOTE: this ask is a bit confusing as is not specified if should return all 
# the groups available, or only the ones relevant to the authenticated user.
# I personally assumed the latter.
class UserGroupsView(ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.groups.all()
