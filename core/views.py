from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Olá, Django!",
        "status": "ok"
    })
