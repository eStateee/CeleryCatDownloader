
from django.http import HttpResponse
from cats_app.tasks import get_cats

def cat_view(request):
    if request.method == "GET":
        get_cats.delay()
        return HttpResponse('Downloading cats')
    else:
        return HttpResponse(f'Error in request method, {request.method}')
