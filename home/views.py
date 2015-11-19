from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import AktuellesForm

#from django.http import HttpResponse

from .models import Aktuelles

def aktuelles(request):
    aktuelles = Aktuelles.objects.filter(published_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'home/aktuelles.html', {'aktuelles': aktuelles})

def aktuell_detail(request, pk):
    aktuell = get_object_or_404(Aktuelles, pk=pk)
    return render(request, 'home/aktuell_detail.html', {'aktuell': aktuell})

def aktuell_neu(request):
    if request.method == "POST":
        form = AktuellesForm(request.POST)
        if form.is_valid():
            aktuell = form.save(commit=False)
            aktuell.author = request.user
            aktuell.published_date = timezone.now()
            aktuell.save()
            return redirect('home.views.aktuell_detail', pk=aktuell.pk)
    else:
        form = AktuellesForm()
    return render(request, 'home/aktuell_edit.html', {'form': form})

def aktuell_edit(request, pk):
    aktuell = get_object_or_404(Aktuelles, pk=pk)
    if request.method == "POST":
        form = AktuellesForm(request.POST, instance=aktuell)
        if form.is_valid():
            aktuell = form.save(commit=False)
            aktuell.author = request.user
            aktuell.published_date = timezone.now()
            aktuell.save()
            return redirect('home.views.aktuell_detail', pk=aktuell.pk)
    else:
        form = AktuellesForm(instance=aktuell)
    return render(request, 'home/aktuell_edit.html', {'form': form})
