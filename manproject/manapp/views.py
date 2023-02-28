from django.http import HttpResponse
from django.shortcuts import render
from .models import Persn
from .models import choose


# Create your views here.
def mod(request):
    obj = Persn.objects.all()
    objc = choose.objects.all()
    return render(request, "index.html", {'result': obj, 'results': objc})

