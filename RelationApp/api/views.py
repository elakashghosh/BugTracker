from html5lib import serialize
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from uritemplate import partial
from RelationApp.api.serializers import RelationSerializers
from BugsApp.models import Bugs
from RelationApp.models import Relation

class AssignAV(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = RelationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Done'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# To fetch work assigned to a particular developer(will be fetched by the developer himself)
class myWorkAV(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, myId):
        try:
            myWork = Relation.objects.filter(assignedTo=myId)
        except:
            return Response({}, status=status.HTTP_200_OK)
        
        serializer = RelationSerializers(myWork, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# fetch all the work that has been assigned by admin(will be fetched by admin only)
class allAssignedWorkAV(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        try:
            allWork = Relation.objects.all()
        except:
            return Response({}, status=status.HTTP_200_OK)
        
        serializer = RelationSerializers(allWork, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# update status of a bug
class UpdateBugStatusAV(APIView):
    def get_object(self, pk):
        return Relation.objects.get(pk=pk)
    
    def patch(self, request, pk):
        relationObject = self.get_object(pk)
        serializer = RelationSerializers(relationObject, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


