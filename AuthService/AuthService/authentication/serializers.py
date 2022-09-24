from rest_framework import serializers

from authentication.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name',
                  'phone_number',
                  'email',
                  'address',
                  'username',
                  'password',)