from rest_framework import serializers
from .models import Members  , MembershipType

# Serializers define the API representation.
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'


#==MemberType serializers======
class MembershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipType
        fields = '__all__'

