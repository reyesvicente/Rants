
from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Rant
from .serializers import RantSerializer


class RantList(ListCreateAPIView):
    queryset = Rant.objects.all()
    serializer_class = RantSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RantSerializer(queryset, many=True)
        return Response(serializer.data)


class RantUpdate(UpdateAPIView):
    queryset = Rant.objects.all()
    serializer_class = RantSerializer


class RantDelete(DestroyAPIView):
    queryset = Rant.objects.all()
    serializer_class = RantSerializer


"""
class RantDetail(APIView):
    def get_object(self, pk):
        try:
            return Rant.objects.get(pk=pk)
        except Rant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rant = self.get_object(pk)
        serializer = RantSerializer(rant)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "rant": openapi.Schema(type=openapi.TYPE_STRING),
                "slug": openapi.Schema(type=openapi.TYPE_STRING),
                'categories': openapi.Schema(type=openapi.TYPE_STRING)
            }
        )
    )

    def put(self, request, pk, format=None):
        rant = self.get_object()
        serializer = RantSerializer(rant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rant = self.get_object(pk)
        rant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""