from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        #Authenticated users only can see list view

        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        #Read permissions are allowed to any request so we'll always
        #allow GET, HEAD, or OPTIONS REquest 
        if request.method in permissions.SAFE_METHODS:
            return True
        
            #Write permissions are only to the author of a post request so we
        return obj.author == request.user