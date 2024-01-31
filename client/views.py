from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, get_object_or_404, redirect 

from .forms import AddCLientForm
from.models import Client 

@login_required

def client_list(request):
    clients = Client.objects.filter(created_by=request.user)

    return render(request, 'client/clients_list.html',{
        'clients': clients
    })

@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    return render(request, 'client/clients_detail.html',{
        'client': client
    })

@login_required
def clients_add(request):
    if request.method =='POST':
        form = AddCLientForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            messages.success(request, 'The client was created.')

            return redirect('client_list')
    else:
        form = AddCLientForm()

    return render(request, 'client/clients_add.html', {
        'form': form 
    })