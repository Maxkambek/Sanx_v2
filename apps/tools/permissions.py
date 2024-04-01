from rest_framework import permissions


class IsDriverUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Driver'


class IsClientUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Client'


class IsCompanyUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Company'


class IsAdministratorUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Administrator'


class IsSuperAdministratorUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'SuperAdmin'
