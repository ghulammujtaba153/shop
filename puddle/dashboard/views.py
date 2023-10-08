from django.shortcuts import render, get_object_or_404

from item.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def index(req):
    items=Item.objects.filter(created_by=req.user)

    return render(req, 'dashboard/index.html', {
        'items' :items,
    })

