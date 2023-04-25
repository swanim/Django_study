from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world")

def some_url(request):
    return HttpResponse("Some_url을 구현해 봤습니다")