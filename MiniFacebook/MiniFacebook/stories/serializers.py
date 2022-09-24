from rest_framework import serializers

from stories.models import Status, Stories

class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ('uid',
                  'username',
                  'time')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('uid',
                  'username',
                  'text',
                  'time')