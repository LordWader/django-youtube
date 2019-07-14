from rest_framework import serializers
from testapi.models import KeyWordData, YouTubeVideo


class KeyWordDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWordData
        fields = ('id', 'key_word')
