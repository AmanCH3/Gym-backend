from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Members, MembershipType
from .serializers import MemberSerializer, MembershipTypeSerializer

class MemberViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Members model.
    """
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific member.
        """
        member = get_object_or_404(Members, pk=pk)
        serializer = MemberSerializer(member)
        return Response({
            "data": serializer.data,
            "statusCode": 200,
            "message": "Data retrieved successfully!"
        })

    def destroy(self, request, pk=None):
        """
        Delete a specific member.
        """
        member = get_object_or_404(Members, pk=pk)
        member.delete()
        return Response({
            "data": "ok",
            "statusCode": 200,
            "message": "Data deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        """
        Update a specific member.
        """
        member = get_object_or_404(Members, pk=pk)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": "updated data",
                "statusCode": 200,
                "message": "Data updated successfully!"
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """
        Create a new member.
        """
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": "ok",
                "statusCode": 200,
                "message": "Member saved successfully!"
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        List all members.
        """
        members = Members.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response({
            "data": serializer.data,
            "statusCode": 200,
            "message": "Data retrieved successfully!"
        })

    @action(detail=False, methods=['get'], url_path='count/(?P<type_name>[^/.]+)')
    def count_by_type(self, request, type_name=None):
        """
        Custom action to count members by membership type.
        """
        count = Members.objects.filter(membership_type__type_name=type_name).count()
        return Response({
            "data": count,
            "statusCode": 200,
            "message": "Count retrieved successfully!"
        })

class MembershipTypeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for MembershipType model.
    """
    queryset = MembershipType.objects.all()
    serializer_class = MembershipTypeSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific membership type.
        """
        membership_type = get_object_or_404(MembershipType, pk=pk)
        serializer = MembershipTypeSerializer(membership_type)
        return Response({
            "data": serializer.data,
            "statusCode": 200,
            "message": "Data retrieved successfully!"
        })

    def destroy(self, request, pk=None):
        """
        Delete a specific membership type.
        """
        membership_type = get_object_or_404(MembershipType, pk=pk)
        membership_type.delete()
        return Response({
            "data": "ok",
            "statusCode": 200,
            "message": "Membership type deleted successfully!"
        }, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None):
        """
        Update a specific membership type.
        """
        membership_type = get_object_or_404(MembershipType, pk=pk)
        serializer = MembershipTypeSerializer(membership_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": "updated data",
                "statusCode": 200,
                "message": "Data updated successfully!"
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        """
        Create a new membership type.
        """
        serializer = MembershipTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": "ok",
                "statusCode": 200,
                "message": "Membership type saved successfully!"
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        List all membership types.
        """
        membership_types = MembershipType.objects.all()
        serializer = MembershipTypeSerializer(membership_types, many=True)
        return Response({
            "data": serializer.data,
            "statusCode": 200,
            "message": "Data retrieved successfully!"
        })