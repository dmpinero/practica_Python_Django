from datetime import datetime, timezone
from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Define si un usuario puede ejecutar el método o acceder a la vista/controlador que quiere acceder
        :param request:
        :param view:
        :return:
        """
        if view.action in ('create', 'retrieve', 'update', 'destroy'):
            return True

    def has_object_permission(self, request, view, obj):
        """
        Define si un usuario puede realizar la operación que quiere sobre el objeto 'obj'
        :param request:
        :param view:
        :param obj:
        :return:
        """
        if view.action == 'create':
            return True
        else:
            return request.user.is_superuser or request.user == obj  # Usuario administrador o es el mismo usuario

class UserPostPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si un usuario puede ejecutar el método o acceder a la vista/controlador que quiere acceder
        :param request:
        :param view:
        :return:
        """
        if view.action in ('create', 'retrieve', 'update', 'destroy', 'list'):
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si un usuario puede realizar la operación que quiere sobre el objeto 'obj'
        :param request:
        :param view:
        :param obj:
        :return:
        """
        # En el detalle de un post hay que comprobar los permisos si el post no es público (fecha de publicación
        # es mayor que la fecha actual
        if view.action == 'create':
            tiene_permisos = request.user.is_authenticated
        else:
            tiene_permisos = request.user.is_superuser or request.user == obj  # Usuario administrador o es el mismo usuario

        if view.action == 'retrieve':
            if obj.published_at.astimezone(timezone.utc).replace(tzinfo=None) > datetime.now():
                return tiene_permisos
            else:
                return False
        else:
            return tiene_permisos