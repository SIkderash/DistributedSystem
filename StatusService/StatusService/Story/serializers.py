from rest_framework import serializers

from Story.models import EncodedImages, Stories

class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ('uid',
                  'username',
                  'time')

class EncodedImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncodedImages
        fields = ('uid')