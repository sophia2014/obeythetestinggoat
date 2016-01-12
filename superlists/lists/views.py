from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    new_list = List.objects.create()
    item = Item(text=request.POST['item_text'], list=new_list)

    try:
        item.full_clean()
        item.save()
    except ValidationError:
        new_list.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error})

    return redirect('/lists/%d/' %(new_list.id,))

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)

    # method == 'GET'
    return render(request, 'list.html', {'list': list_,})

def delete_item(request, list_id, item_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.filter(id=item_id).delete()
    return redirect('/lists/%d/' %(list_.id,))
