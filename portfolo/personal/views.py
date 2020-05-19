from django.shortcuts import render

# Create your views here.
def personal_index(request):
    return render(request, 'personal_index.html')
