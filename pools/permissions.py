from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' and hasattr(request.data, 'user'):
            if request.user.is_authenticated and int(request.data['user']) == request.user.id:
                return True

        # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Read permissions allowed to any request so this allows GET, HEAD or OPTIONS

        if request.method in permissions.SAFE_METHODS or not hasattr(obj, "user"):
            return True
                
        
        # Write permissions only allowed to owner
        return obj.user == request.user