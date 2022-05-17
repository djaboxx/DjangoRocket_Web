from django.views import View
from django.http import HttpResponse

class Main(View):
    def get(self, request):
        return HttpResponse(200)

    def post(self, request):
        pass