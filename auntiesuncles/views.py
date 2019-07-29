from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Auntiesuncles

def allauntiesuncles(request):
    auntuncle_moments = Auntiesuncles.objects
    return render(request, 'auntiesuncles/auntiesuncles.html', {'auntuncle_moments':auntuncle_moments})

def detail5(request, auntiesuncles_id):
    detailauntiesuncles = get_object_or_404(Auntiesuncles, pk=auntiesuncles_id)
    return render(request, 'auntiesuncles/detail5.html', {'auntiesuncles':detailauntiesuncles})
