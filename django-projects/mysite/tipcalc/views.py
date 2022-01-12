from django.shortcuts import render

# Create your views here.
def tip(request):
    return render(request, 'index.html')