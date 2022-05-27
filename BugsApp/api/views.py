from html5lib import serialize
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from BugsApp.api.serializers import BugsSerializers
from BugsApp.models import Bugs

class report_view(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BugsSerializers(data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Reported'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class my_reports_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            myBugs = Bugs.objects.filter(reporter=pk)
        except:
            return Response({}, status=status.HTTP_200_OK)

        serializer = BugsSerializers(myBugs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class show_all_view(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        try:
            allBugs = Bugs.objects.all()
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        serializer = BugsSerializers(allBugs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class get_bug_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            bugDetails = Bugs.objects.get(pk=pk)
        except:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        serializer = BugsSerializers(bugDetails)
        return Response(serializer.data, status=status.HTTP_200_OK)
        


        
