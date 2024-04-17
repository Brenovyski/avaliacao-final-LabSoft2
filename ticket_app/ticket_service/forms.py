from django import forms

class SeatSelectionForm(forms.Form):
    seat_number = forms.CharField(label="Escolha seu assento")
