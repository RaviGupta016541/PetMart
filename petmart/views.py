from django.http import HttpResponse


def index(request):
    return HttpResponse('<script>window.location="/shop";</script>')