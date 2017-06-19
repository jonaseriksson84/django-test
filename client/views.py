from django.shortcuts import render


# Create your views here.
def index(request, path=''):
    """
    Renders the Angular2 SPA
    """
    return render(request, 'client/index.html')
