from rest_framework import serializers

from Story.models import Stories

class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ('uid',
                  'username',
                  'time')