from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from testapi.models import KeyWordData
from testapi.serializers import KeyWordDataSerializer
from testapi.decorators import authorization


@csrf_exempt
@authorization
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
@authorization
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
@authorization
def video_results(request, pk):
    try:
        current_record = KeyWordData.objects.get(id=pk)
    except KeyWordData.DoesNotExist:
        return HttpResponse(status=404)
    return JsonResponse({
        "key_word": current_record.key_word,
        "id": pk,
        "urls": [url[0] for url in list(current_record.videos.values_list("url"))]
    }, status=200)
