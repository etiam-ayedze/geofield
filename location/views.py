from django.shortcuts import render
from location.models import Region, Prefecture, Commune, Canton, Village, Quartier
from .forms import region_form
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

# def location_page(request):
#     return render(request, 'location/location.html')

def save_region(request):
    region = Region.objects.all()
    prefecture = Prefecture.objects.all()
    commune = Commune.objects.all()
    canton = Canton.objects.all()
    village = Village.objects.all()
    quartier = Quartier.objects.all()

    if request.method == 'POST':
        region_occur = region_form(request.POST or None)

        if region_occur.is_valid():
            region_occur.save()
            messages.add_message(request, messages.INFO, "Region enregistré avec succès")
        else:
            return redirect("save_region")
    return render(request, "location/location.html", locals())











