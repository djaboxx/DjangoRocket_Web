from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect

class Main(View):
    def get(self, request):
        return render(request, "homepage.html")

    def post(self, request):
        pass