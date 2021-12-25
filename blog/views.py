from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    params = {
        "title": "Django ITエンジニア『さだや』公式サイト",
        "msg": "welcome to sadaya_blog!!",
        "goto": "test",
    }
    return render(request, "blog/index.html", params)   #☆☆☆

def test(request):
    params = {
        "title": "Django ITエンジニア『さだや』公式サイト",
        "msg": "変わったかな？",
        "goto": "index",
    }
    return render(request, "blog/index.html", params)   #☆☆☆