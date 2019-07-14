from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
import json

from rest_framework.renderers import JSONRenderer

from testapi.models import KeyWordData
from testapi.serializers import KeyWordDataSerializer
from testapi.tasks import search_func


@csrf_exempt
@permission_classes((AllowAny,))
def items_list(request):
    if request.method == "GET":
        data = KeyWordData.objects.all()
        serializer = KeyWordDataSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        io = request.body.decode('utf-8').replace("'", "")
        data = json.loads(io)
        serializer = KeyWordDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def item_detail(request, pk):
    try:
        current_record = KeyWordData.objects.get(id=pk)
    except KeyWordData.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "DELETE":
        current_record.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=500)


@csrf_exempt
def video_results(request, pk):
    search_func()
    try:
        current_record = KeyWordData.objects.get(id=pk)
    except KeyWordData.DoesNotExist:
        return HttpResponse(status=404)
    return JsonResponse({
        "key_word": current_record.key_word,
        "id": pk,
        "urls": [url[0] for url in list(current_record.videos.values_list("url"))]
    }, status=200)
