from django.shortcuts import render

# Create your views here.


def acceuil(request):
    return render(request,'acceuil.html')



def pronostics(request):
    return render(request,'pronostics.html')


def abonnement(request):
    return render(request,'abonnement.html')





def archive(request):
    return render(request,'archive.html')



def contact(request):
    return render(request,'contact.html')                