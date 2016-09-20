from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from rest_framework.viewsets import ViewSet

from users.permissions import UserPermission
from users.serializers import UserSerializer

class UserViewSet(ViewSet):

    """
    Endpoint de listado de usuarios
    """
    permission_classes = (UserPermission,)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)