from django.shortcuts import render
from showroom.models import Wine
from django.http import JsonResponse
from .countries import COUNTRY

# Create your views here.
def index(request):
    return render(request, 'index.html')

def catalog(request):
    if request.is_ajax and request.method == "GET":
        query = Wine.objects.all()
        name = request.GET.get('name', None)
        year = request.GET.get('year', None)
        grape = request.GET.get('grapes', None)
        country = request.GET.get('country', None)
        
        if name is not None and name != '':
            query = query.filter(name__icontains=name)
        if year is not None and year !='':
            query = query.filter(year__exact=int(year))
        if country is not None and country !='':
            country = country.split(';')
            query = query.filter(country__in=country)
        if grape is not None and grape !='':
            query = query.filter(grapes__icontains=grape)
        
        data = list(query.values('name', 'year', 'grapes', 'country', 'region', 'description', 'image'))

        return JsonResponse(data, status=200, safe=False)
    else:
        return JsonResponse({}, status=400)

def countrylist(request):
    if request.is_ajax and request.method == "GET":
        query = Wine.objects.all()
        rawData = list(query.values_list('country', flat=True))
        rawData = list(dict.fromkeys(rawData))
        data = []
        for i in range(len(rawData)):
            data.append({'id': i, 'text': rawData[i]})
        data = {'results': data}

        return JsonResponse(data, status=200, safe=False)
    else:
        return JsonResponse({}, status=400)