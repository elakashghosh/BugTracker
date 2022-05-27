from BugsApp.models import Bugs
from rest_framework import serializers

class BugsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bugs
        fields = '__all__'
