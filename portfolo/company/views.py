from django.shortcuts import render, redirect
from company.forms import ProfessionalForm
from company.models import Professional

# Create your views here.
# creating view for form
def pro_form(request):
    if request.method == "POST":
        form = ProfessionalForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('list_details')
            except:
                pass

    else:
        form = ProfessionalForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)

# creating a view to display a list of professional
def list_details(request):
    professionals = Professional.objects.all()

    context = {
        'professionals': professionals
    }

    return render(request, 'list_details.html', context)

# creating a view to edit the form
def edit_form(request, id):
    professional = Professional.objects.get(id=id)

    context = {
        'professional': professional
    }

    return render(request, 'update_edit.html', context)

# creating a view to update the form
def update_form(request, id):
    professional = Professional.objects.get(id=id)
    form = ProfessionalForm(request.POST, instance = professional)

    if form.is_valid():
        form.save()
        return redirect('list_details')

    context = {
       'professional': professional
    }


    return render(request, 'update_edit.html', context)

# deleting the professional from the database
def delete_form(request, id):
    professional = Professional.objects.get(id=id)

    professional.delete()

    return redirect('list_details')
