from RelationApp.models import Relation
from rest_framework import serializers

class RelationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = '__all__'
