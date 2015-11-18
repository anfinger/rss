from django.shortcuts import render
from django.utils import timezone
#from django.http import HttpResponse

from .models import Aktuelles

def index(request):
    aktuelles = Aktuelles.objects.filter(published_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'home/index.html', {'aktuelles': aktuelles})
