from django.shortcuts import render

# Create your views here.
def katherine_index(request):
    return render(request, 'katherine_index.html')
