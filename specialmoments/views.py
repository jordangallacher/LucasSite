from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Specialmoments

def allmoments(request):
    moments = Specialmoments.objects
    return render(request, 'specialmoments/specialmoments.html', {'moments':moments})

def detail2(request, specialmoments_id):
    detailmoments = get_object_or_404(Specialmoments, pk=specialmoments_id)
    return render(request, 'specialmoments/detail2.html', {'specialmoments':detailmoments})
