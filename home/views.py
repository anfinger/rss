from django.shortcuts import render, get_object_or_404
from django.utils import timezone
#from django.http import HttpResponse

from .models import Aktuelles

def aktuelles(request):
    aktuelles = Aktuelles.objects.filter(published_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'home/aktuelles.html', {'aktuelles': aktuelles})

def aktuell_detail(request, pk):
    aktuell = get_object_or_404(Aktuelles, pk=pk)
    return render(request, 'home/aktuell_detail.html', {'aktuell': aktuell})
