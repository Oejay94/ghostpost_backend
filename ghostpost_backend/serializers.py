from rest_framework import serializers

from .models import BoastRoast

class BoastRoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoastRoast
        fields = [
            'title',
            'boast_or_roast',
            'body',
            'total_count',
            'created_on'
        ]