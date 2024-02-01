from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, get_object_or_404, redirect 

from .forms import AddCLientForm
from.models import Client 

from  team.models import Team 

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
            team = Team.objects.filter(created_by=request.user)[0]
                                                                
            client = form.save(commit=False)
            client.created_by = request.user
            client.team = team 
            client.save()

            messages.success(request, 'The client was created.')

            return redirect('client_list')
    else:
        form = AddCLientForm()

    return render(request, 'client/clients_add.html', {
        'form': form 
    })

@login_required
def clients_edit(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    if request.method =='POST':
        form = AddCLientForm(request.POST, instance=client)

        if form.is_valid():
            form.save() 

            messages.success(request, 'The lead was edited.')

            return redirect('clients_list')
    else:
        form = AddCLientForm(instance=client)

    return render(request, 'client/clients_edit.html', {
        'form': form 
    })

@login_required
def clients_delete(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()

    messages.success(request, 'The client was deleted.')

    return redirect('clients_list')