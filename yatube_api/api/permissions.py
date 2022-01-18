from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта,
    позволяющее только авторам объекта редактировать его.
    """

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        return (True if request.method in permissions.SAFE_METHODS else obj.author == request.user)
        # return obj.author == request.user
