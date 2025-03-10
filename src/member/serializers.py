from rest_framework import serializers
from .models import Member

# Serializers define the API representation.
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


#==MemberType serializers======
class MembershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

