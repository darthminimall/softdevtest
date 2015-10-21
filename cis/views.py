from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Inventory, Computer
from .forms import addInvForm, AddCompForm, EditCompForm

def index(request):
    context = {'inv_list': Inventory.objects.all(),
            'nav': (('Inventories',reverse('cis:index')),),
            'fmsg': '',
            'failure': False,
            'form': addInvForm(),
    }
    return render(request, 'cis/index.html', context)

def delete_inventory(request, inv_id):
    context = {'inv_list': Inventory.objects.all(),
            'nav': (('Inventories', reverse('cis:index')),),
            'fmsg' : '',
            'failure' : False,
    }
    inv = get_object_or_404(Inventory, pk=inv_id)
    inv.delete()
    return HttpResponseRedirect(reverse('cis:index'))

def add_inventory(request):
    if request.method == 'POST':
        form = addInvForm(request.POST)
        if form.is_valid():
            i = Inventory(name=form.cleaned_data['name'])
            i.save()
            return HttpResponseRedirect(reverse('cis:index'))
    else:
        form = addInvForm()
    context = {
            'nav':(('Inventories', reverse('cis:index')),
                ('Add Inventory', reverse('cis:add_inv'))),
            'form': form,
    }
    return render(request, 'cis/add_inventory.html', context)

def inventory(request, inv_id):
    inv = get_object_or_404(Inventory, pk=inv_id);
    context = {'nav': (('Inventories',reverse('cis:index')),
        (inv.name, reverse('cis:inv',args=(inv.id,))),),
            'clist': inv.computer_set.all(),
            'inv': inv,
    }
    return render(request, 'cis/inventory.html', context)

def add_computer(request,inv_id):
    def_inv = get_object_or_404(Inventory, pk=inv_id)
    if request.method == 'POST':
        form = AddCompForm(request.POST);
        if form.is_valid():
            comp = Computer(sn=form.cleaned_data['sn'],
                    manufacturer=form.cleaned_data['manufacturer'],
                    comments=form.cleaned_data['comments'],
                    inv=def_inv)
            comp.save()
            return HttpResponseRedirect(reverse('cis:inv',args=(def_inv.id,)))
    else:
        form = AddCompForm()
    context = {
            'nav': (
                ('Inventories',reverse('cis:index')),
                (def_inv.name, reverse('cis:inv',args=(def_inv.id,))),
                ('Add Computer',reverse('cis:add_cmp',args=(def_inv.id,))),
                ),
            'form': form,
            }
    return render(request, 'cis/add_computer.html', context)

def computer(request,inv_id,cmp_id):
    inv = get_object_or_404(Inventory,pk=inv_id)
    comp = get_object_or_404(Computer, pk=cmp_id)
    context = {
            'nav': (
                ('Inventories',reverse('cis:index')),
                (inv.name, reverse('cis:inv',args=(inv_id,))),
                (" ".join((comp.manufacturer,comp.sn)),
                    reverse('cis:cmp',args=(inv_id,cmp_id,))),
                ),
            'comp': comp,
            'inv': inv,
            }
    return render(request,'cis/computer.html',context);

def edit_computer(request,inv_id,cmp_id):
    inv = get_object_or_404(Inventory,pk=inv_id)
    comp = get_object_or_404(Computer,pk=cmp_id)
    if request.method == 'POST':
        form = EditCompForm(request.POST)
        if form.is_valid():
            comp.manufacturer = form.cleaned_data['manufacturer']
            comp.sn = form.cleaned_data['sn']
            comp.comments = form.cleaned_data['comments']
            comp.inv = form.cleaned_data['inventory']
            comp.save()
            return HttpResponseRedirect(reverse('cis:cmp',args=(inv_id,cmp_id)))
    else:
        form = EditCompForm({'manufacturer':comp.manufacturer,
            'sn': comp.sn,
            'comments': comp.comments,
            'inventory': comp.inv.id})
    context = {
            'nav': (
                ('Inventories', reverse('cis:index')),
                (inv.name, reverse('cis:inv',args=(inv.id,))),
                (" ".join((comp.manufacturer,comp.sn)),
                    reverse('cis:cmp',args=(inv_id,cmp_id))),
                ("Edit Computer",
                    reverse('cis:edit_cmp',args=(inv_id,cmp_id))),
                ),
            'inv': inv,
            'comp': comp,
            'form': form,
            }

    return render(request,'cis/edit_computer.html',context)

def delete_computer(self,inv_id,cmp_id):
    computer = get_object_or_404(Computer,pk=cmp_id)
    cpmputer.delete()
    return HttpResponseRedirect(reverse('cis:inventory',args=(inv_id,)))

