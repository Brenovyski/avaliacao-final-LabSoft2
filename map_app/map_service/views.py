from django.shortcuts import render
from rest_framework import viewsets
from .models import Seats
from .serializers import SeatsSerializer


# Create your views here.

def index(request):
    seats = Seats.objects.all()
    return render(request, 'map.html', {'seats': seats}	)

# API
class SeatsViewSet(viewsets.ModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer