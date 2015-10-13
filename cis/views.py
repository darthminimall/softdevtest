from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Inventory, Computer

def index(request):
    context = {'inv_list': Inventory.objects.all(),
            'nav': (('Inventories',reverse('cis:index')),),
            'fmsg': '',
            'failure': False,
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
    context = {'inv_list': Inventory.objects.all(),
            'nav': (('Inventories',reverse('cis:index')),),
            'fmsg': '',
            'failure': False,
    }
    try:
        inv = Inventory(name=request.POST['name'])
        inv.save()
    except (KeyError):
        context['fmsg'] = 'No name given in POST data.'
        context['failure'] = True
        render(request, 'cis/index.html', context)
    else:
        return HttpResponseRedirect(reverse('cis:index'))

def inventory(request, inv_id):
    inv = get_object_or_404(Inventory, pk=inv_id);
    context = {'nav': ((inv.name, reverse('cis:inv',args=(inv.id,))),),
            'clist': inv.computer_set.all(),
            'iname': inv.name,
    }
    return render(request, 'cis/inventory.html', context)
