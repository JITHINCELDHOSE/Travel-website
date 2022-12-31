from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def travel_destination(request):
    return render(request, 'travel_destination.html')


def destination_details(request):
    return render(request, 'destination_details.html')


def elements(request):
    return render(request, 'elements.html')


def contact(request):
    return render(request, 'contact.html')


def switzerland(request):
    return render(request, 'switzerland.html')


def indonesia(request):
    return render(request, 'indonesia.html')


def australia(request):
    return render(request, 'australia.html')