from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Idc
from .serializers import IdcSerializer


def idc_list(request, *args, **kwargs):
    if request.method == "GET":
        querySet = Idc.objects.all()
        serialiserQ = IdcSerializer(querySet, many=True)
        context = JSONRenderer().render(serialiserQ.data)
        return HttpResponse(context, content_type="application/json")

    elif request.method == "POST":
        JSONParser().parse(request)

    return HttpResponse(">>>")


#############################Use the rest_framework -> ApiView#########
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class IdcList(APIView):
    def get(self, request, format=None):
        querySet = Idc.objects.all()
        serializer = IdcSerializer(querySet, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IdcSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class IdcDetail(APIView):



    def get_object(self, pk):
        try:
            return Idc.objects.get(pk=pk)
        except Idc.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        idcObj = self.get_object(pk)

        serializer = IdcSerializer(idcObj)

        return Response(serializer.data)


    def put(self, request, pk, format=None):
        idcObj = self.get_object(pk)
        serializer = IdcSerializer(idcObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk, format=None):
        idc = self.get_object(pk)
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


####################ViewSet_v1##################################
from rest_framework import viewsets
class IdcViewset_v1(viewsets.ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


