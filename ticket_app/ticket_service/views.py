from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SeatSelectionForm
from .models import Ticket
from .serializers import TicketSerializer
import requests


# Create your views here.

def index(request):

    response = requests.get('http://127.0.0.1:8001/api/seats/')
    seats_data = response.json()
    
    # Filter for seats that are not occupied
    available_seats = [seat for seat in seats_data if not seat['is_occupied']]

    # Pass the available seats to your template
    return render(request, 'ticket.html', {'seats': available_seats})

def purchase_ticket(request):
    if request.method == 'POST':
        form = SeatSelectionForm(request.POST)
        if form.is_valid():
            seat_number = form.cleaned_data['seat_number']
            # Assume the API accepts PATCH to update the seat
            patch_url = f'http://127.0.0.1:8001/api/seats/{seat_number}/'
            patch_data = {'is_occupied': True}
            patch_response = requests.patch(patch_url, json=patch_data)

            if patch_response.status_code == 200:
                # Redirect to a success page or back to form
                return redirect('/')
            else:
                return redirect('/')

            return HttpResponseRedirect('/')
        else:
            print(form.errors)
            return redirect('/')
    return HttpResponseRedirect('/')
# API
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer