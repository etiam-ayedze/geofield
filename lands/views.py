from django.shortcuts import render, HttpResponse, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import proprio_form, typesuccession_form, typeparcelle_form, parcelle_form, historique_proprio_form
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from lands.models import Proprietaire, Typesuccession, Typeparcelle, Parcelle, HistoriqueProprio, Fichier
from location.models import Quartier, Village, Canton, Commune, Prefecture, Region
from django.contrib.gis.geos import Polygon
from djgeojson.views import GeoJSONLayerView
from django.core.serializers import serialize
# Create your views here.

#vue pour montrer la liste des propriétaires
@login_required
def voir_proprio(request):
    proprio = Proprietaire.objects.all()
    parcelle = Parcelle.objects.all()
    tparcelle = Typeparcelle.objects.all()
    tsuccession = Typesuccession.objects.all()
    quartier = Quartier.objects.all()
    historique = HistoriqueProprio.objects.all()

    return  render(request, 'lands/proprietaire.html', locals())



#vue pour enregistrer un nouveau propriétaire
@login_required
def save_proprio(request):
    update = False
    verifie_proprio = True
    proprio = Proprietaire.objects.all()
    parcelle = Parcelle.objects.all()
    tparcelle = Typeparcelle.objects.all()
    tsuccession = Typesuccession.objects.all()
    quartier = Quartier.objects.all()
    historique = HistoriqueProprio.objects.all()
    if request.method == 'POST':
        proprio_occur= proprio_form(request.POST or None)

        if proprio_occur.is_valid():
            proprio_occur.save()
            messages.add_message(request, messages.INFO, "Propriétaire enregistré avec succès")
        else:
            return HttpResponse(proprio_occur.errors.as_json())
            # return redirect(save_proprio)
    return render(request, 'lands/landsInfos.html', locals())



#vue pour modifier un propriétaire
@login_required
def modifier_proprio(request, id=None):
    inst = get_object_or_404(Proprietaire, id=id)
    proprietaire = Proprietaire.objects.all()
    if request.method == 'GET':
        update = True
        return render(request, 'lands/proprietaire.html', locals())
    else:
        form = proprio_form(request.POST or None, instance=inst)
        if form.is_valid():
            inst= form.save(commit=False)
            inst.save()
        return redirect(save_proprio)



#vue pour suppprimer un propriétaire
@login_required
def delete_proprio(request, id):
    obj = get_object_or_404(Proprietaire, id=id)
    obj.delete()
    return redirect(save_proprio)



#vue pour enregistrer un nouveau type de succession
@login_required
def save_typesuccession(request):
    update = False
    succession = Typesuccession.objects.all()
    if request.method == 'POST':
        succession_occur= typesuccession_form(request.POST or None)

        if succession_occur.is_valid():
            succession_occur.save()
            messages.add_message(request, messages.INFO, "Type de succession enregistré avec succès")
        else:
            #HttpResponse(succession_occur.errors.as_json())
            return redirect(save_typesuccession)
    return render(request, 'lands/type_succession.html', locals())




#vue pour modifier un type de succession
@login_required
def  modifier_typesuccession(request, id=None):
    inst = get_object_or_404(Typesuccession, id=id)
    typesuccession = Typesuccession.objects.all()
    if request.method =='GET':
        update = True
        return render(request, 'lands/type_succession.html', locals())
    else:
        form = typesuccession_form(request.POST or None, instance=inst)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.save()
        return redirect(save_typesuccession)



#vue pour supprimer un type de succession
@login_required
def delete_typesuccession(request, id):
    obj = get_object_or_404(Typesuccession, id=id)
    obj.delete()
    return redirect(save_typesuccession)



#vue pour enregistrer un type de parcelle
@login_required
def save_typeparcelle(request):
    update = False
    tparcelle = Typeparcelle.objects.all()
    if request.method == 'POST':
        tparcelle_occur = typeparcelle_form(request.POST or None)

        if tparcelle_occur.is_valid():
            tparcelle_occur.save()
            messages.add_message(request, messages.INFO, "Type de parcelle enregostré avec succès")
        else:
            HttpResponse(tparcelle_occur.errors.as_json())
            #return redirect(save_typeparcelle)
    return render(request,'lands/type_parcelle.html', locals())




#vue pour modifier un type de parcelle
@login_required
def modifier_typeparcelle(request, id:None):
    inst= get_object_or_404(Typeparcelle, id=id)
    t_parcelle = Typeparcelle.objects.all()
    if request.method=='GET':
        update = True
        return render(request, 'lands/type_parcelle.html', locals())
    else:
        form = typeparcelle_form(request.POST or None, instance=inst)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.save()
        return redirect(save_typeparcelle)



#vue pour supprimer un type de parcelle
@login_required
def delete_typeparcelle(request, id):
    obj = get_object_or_404(Typeparcelle, id=id)
    obj.delete()
    return redirect(save_typeparcelle)




#vue pour afficher  la page de datable des parcelles
@login_required
def save_parcelle(request):
    parcelle = Parcelle.objects.all()
    proprio = Proprietaire.objects.all()
    tparcelle = Typeparcelle.objects.all()
    tsuccession = Typesuccession.objects.all()
    quartier = Quartier.objects.all()
    return render(request, 'lands/parcelle.html', locals())



#vue pour afficher la page de landsInfos
@login_required
def save_lands_info(request):

    update = False
    verifie_proprio = False
    parcelle = Parcelle.objects.all()
    proprio = Proprietaire.objects.all()
    tparcelle = Typeparcelle.objects.all()
    tsuccession = Typesuccession.objects.all()
    quartier = Quartier.objects.all()
    historique = HistoriqueProprio.objects.all()
    file = Fichier.objects.all()

    if request.method == "POST" and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        # form_parc = parcelle_form(request.POST or None)
        # form_hist = historique_proprio_form(request.POST or None)

        numLot = request.POST.get('numLot')
        numTitreFoncier = request.POST.get('numTitreFoncier')
        numIdFiscal = request.POST.get('numIdFiscal')
        numApprobation = request.POST.get('numApprobation')
        dide = request.POST.get('dide')
        nomGeometre = request.POST.get('nomGeometre')
        surface = request.POST.get('surface')
        typeParcelle = request.POST.get('typeParcelle')
        quartier = request.POST.get('quartier')
        coordonee = request.POST.get('coordonee')


        parcelle_inst = Parcelle(numLot=numLot,
                                 numTitreFoncier=numTitreFoncier,
                                 numIdFiscal=numIdFiscal,
                                 numApprobation=numApprobation,
                                 dide=dide,
                                 nomGeometre=nomGeometre,
                                 surface=surface,
                                 typeParcelle=Typeparcelle.objects.get(id=typeParcelle),
                                 quartier=Quartier.objects.get(id=quartier),
                                 coordonee= Polygon(convert(coordonee)) )
        parcelle_inst.save()
        parc_cree = Parcelle.objects.get(numLot=numLot)
        # if form_hist.is_valid():

        proprietaire = request.POST.get('proprietaire')
        parcelle = request.POST.get('parcelle')
        # file = form_hist.cleaned_data['file']
        typeSuccession = request.POST.get('typeSuccession')
        dateDebutPossession = request.POST.get('dateDebutPossession')
        dateFinPossession = request.POST.get('dateFinPossession')


        hist_inst = HistoriqueProprio(proprietaire=Proprietaire.objects.get(id=proprietaire),
                                      parcelle=parcelle_inst,
                                      # file=file,
                                      typeSuccession=Typesuccession.objects.get(id=typeSuccession),
                                      dateDebutPossession=dateDebutPossession )
        hist_inst.save()

        file = request.POST.get('file')

        file_inst = Fichier(file=filename,
                            parcelle = parcelle_inst )

        file_inst.save()

        messages.add_message(request, messages.INFO, 'Enregistrement effectué avec succès!')


    return render(request, 'lands/landsInfos.html', locals())



#fonction pour convertir les coordonées géographiques en string
def convert(data):
    data = data.replace('[','')
    data = data.replace(']','')
    data = data.split(',')
    tab = []
    tab_finial = []
    tmp = []
    for i in data:
        try:
            item = float(i)
        except ValueError:
            pass
        else:
            tab.append(item)

    for i in range(0,len(tab),2):
        z = tab[i:i+2]
        tab_finial.append(z[::-1])
    return tab_finial



#vue pour modifier une parcelle
def modifier_parcelle(request, id=None):
    pass



#fonction pour supprimer une parcelle
def delete_parcelle(request, id):
    obj = get_object_or_404(Parcelle, id=id)
    obj.delete()
    return redirect(save_parcelle)



#vue pour afficher les détails d'une parcelle
@login_required
def detailParcelle(request, id):
    proprio = Proprietaire.objects.all()
    parcelle= Parcelle.objects.get(pk=id)
    tparcelle = Typeparcelle.objects.all()
    tsuccession = Typesuccession.objects.all()
    historique = HistoriqueProprio.objects.get(parcelle=id)
    quartier = Quartier.objects.all()
    village = Village.objects.all()
    canton = Canton.objects.all()
    commune = Commune.objects.all()
    prefecture = Prefecture.objects.all()
    region = Region.objects.all()
    file = Fichier.objects.get(parcelle=id)

    return render(request, 'lands/detailsParcelle.html', locals())



# Vue pour afficher une seule parcelle sur la map
@login_required
def parcelleDetailvue(request, id):
    parcelle = Parcelle.objects.get(id=id)
    p = serialize('geojson', [parcelle],
                  geometry_field='coordonee',
                  fields=('numLot',))
    return HttpResponse(p, content_type='application/json')



#Vue pour afficher la liste des parcelles détenue par un propriétaire
@login_required
def liste_propriete(request, id):
    proprietaire = Proprietaire.objects.get(pk=id)
    historique = HistoriqueProprio.objects.filter(proprietaire=id)
    parcelle = Parcelle.objects.all()

    return render(request, 'lands/liste_possession_proprio.html', locals())



#Vue pour afficher stat1
@login_required
def statFile1(request):
    parelle = Parcelle.objects.all()
    # annee = HistoriqueProprio.objects.values('dateDebutPossession')

    annee = HistoriqueProprio.objects.all().only('dateDebutPossession').order_by('-dateDebutPossession').distinct('dateDebutPossession')

    return render(request, 'lands/statFile1.html', locals())



#Vue ppur filtrer le nombre de parcelle par mois
@login_required
def parcelleParMois(request):
    annee = request.POST.get('annee')
    parelle = Parcelle.objects.all()
    historique = HistoriqueProprio.objects.all()
    parcHistorJan = HistoriqueProprio.objects.filter(dateDebutPossession__year= str(annee), dateDebutPossession__month='01').count()
    parcHistorFev = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='02').count()
    parcHistorMar = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='03').count()
    parcHistorAvr = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='04').count
    parcHistorMai = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='05').count()
    parcHistorJuin = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='06').count()
    parcHistorJuil = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='07').count()
    parcHistorAout = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='08').count()
    parcHistorSept = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='09').count()
    parcHistorOct = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='10').count()
    parcHistorNov = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='11').count()
    parcHistorDec = HistoriqueProprio.objects.filter(dateDebutPossession__year=annee, dateDebutPossession__month='12').count()

    return render(request, 'lands/statFile1.html', locals())

