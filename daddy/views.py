from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Daddy

def alldaddy(request):
    dad_moments = Daddy.objects
    return render(request, 'daddy/daddy.html', {'dad_moments':dad_moments})

def detail4(request, daddy_id):
    detaildaddy = get_object_or_404(Daddy, pk=daddy_id)
    return render(request, 'daddy/detail4.html', {'daddy':detaildaddy})