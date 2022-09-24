from rest_framework import serializers

from Story.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('uid',
                  'username',
                  'text',
                  'time')