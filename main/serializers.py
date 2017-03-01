from django.contrib.auth.models import User, Group
from erp.models import Customer,Role
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class CustSerializer(serializers.HyperlinkedModelSerializer):
    #import pdb; pdb.set_trace()
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
    #user = serializers.ReadOnlyField(source='user.username')
    role = serializers.HyperlinkedRelatedField(view_name='role-detail', queryset=Role.objects.all())
    class Meta:
        model = Customer
        fields = ('url', 'name', 'phone', 'user','role')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('url', 'name')
