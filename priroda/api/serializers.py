from rest_framework import serializers
from priroda.models import Priroda

class PrirodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Priroda
        fields = ('id','title', 'content')