from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Grandparents

def allgrandparents(request):
    gp_moments = Grandparents.objects
    return render(request, 'grandparents/grandparents.html', {'gp_moments':gp_moments})

def detail6(request, grandparents_id):
    detailgrandparents = get_object_or_404(Grandparents, pk=grandparents_id)
    return render(request, 'grandparents/detail6.html', {'grandparents':detailgrandparents})
