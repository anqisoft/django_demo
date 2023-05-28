from django.http import HttpResponse
from django.shortcuts import render

from .models import MyModel

def hello(request):
    return HttpResponse("Hello, world from bard demo1!")
def index(request):
    # models = MyModel.objects.all()
    #
    # Render the index template with the models.
    return render(request, 'index.html', {'models': MyModel.objects.all()})
