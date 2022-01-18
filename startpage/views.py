from urllib import request
from django.shortcuts import render


def start_page(request):
        return render (request,
                'startpage/page.html')