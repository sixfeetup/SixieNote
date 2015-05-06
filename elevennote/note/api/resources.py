from django.contrib.auth.models import User

from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization

from .authorization import UserObjectsOnlyAuthorization
from ..models import Note


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get']
        resource_name = 'user'
        authentication = BasicAuthentication()
        authorization = Authorization()
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }


class NoteResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')

    class Meta:
        queryset = Note.objects.all()
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {
            'owner': ALL_WITH_RELATIONS,
            'pub_date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
