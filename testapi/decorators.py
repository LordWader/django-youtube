import json

from django.http import HttpResponse


def authorization(f):
    def wrapped_f(request):
        if not request.headers.get("authorization"):
            return HttpResponse(json.dumps({"error": "Only authorized persons with token"}), status=500)
        return f(request)

    return wrapped_f
