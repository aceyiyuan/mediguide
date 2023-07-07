from django.shortcuts import render
from django.db.models import Q
from .models import MedicationInfo

def index(request):
    medications = MedicationInfo.objects.all()
    letters = [chr(letter) for letter in range(65, 91)]  # A-Z

    context = {
        'medications': medications,
        'letters': letters,
    }

    return render(request, 'core/index.html', context)


def search(request):
    query = request.GET.get('query')
    medications = MedicationInfo.objects.all()
   
    letters = [chr(letter) for letter in range(65, 91)]  # A-Z

    if query and query.strip():
    
        medications = medications.filter(
            Q(name__icontains=query) | Q(active_ingredient__icontains=query),
            
        )  

    context = {
        'medications': medications,
        'letters': letters,
        'active_letter': query[0].upper() if query else None,
        'search_query': query,
    }

    return render(request, 'core/index.html', context)




