from rest_framework import serializers
from it.models import It

# It Serializers
class ItSerializer(serializers.ModelSerializer):
    class Meta:
        model = It
        fields = "__all__"