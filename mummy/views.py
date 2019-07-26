from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Mummy

def allmummy(request):
    mum_moments = Mummy.objects
    return render(request, 'mummy/mummy.html', {'mum_moments':mum_moments})

def detail3(request, mummy_id):
    detailmummy = get_object_or_404(Mummy, pk=mummy_id)
    return render(request, 'mummy/detail3.html', {'mummy':detailmummy})