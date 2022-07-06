import csv
from django.db import models
from models import *

def exportcsv():
    songs = Song.objects.all()
    f = open('ml.csv', 'w',encoded="iso-8859-1")
    writer=csv.writer(f)
    writer.writerow(['album','id', 'lyrics'])
    studs = songs.values_list('album','id', 'lyrics')
    for std in studs:
        writer.writerow(std)
    