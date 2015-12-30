import uuid
from django.utils import timezone
from django.db import models

# Create your models here.

class Tag(models.Model):
    tagID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    beschreibung = models.TextField()

class Reise(models.Model):
    reiseID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    autor = models.ForeignKey('auth.User')
    titel = models.CharField(max_length=256)
    einleitung = models.TextField()
    tage = models.ManyToManyField(Tag, through='Reisetage')
    reiselink = models.URLField()
    datum_erzeugung = models.DateTimeField(default=timezone.now)
    datum_veroeffentlichung = models.DateTimeField(blank=True, null=True)
    datum_beginn = models.DateField(blank=True, null=True)
    datum_ende = models.DateField(blank=True, null=True)

    def publish(self):
        self.datum_veroeffentlichung = timezone.now()
        self.save()

    def __str__(self):
        return self.titel

class Reisetage(models.Model):
    reise = models.ForeignKey(Reise, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    tagnummer = models.IntegerField()
