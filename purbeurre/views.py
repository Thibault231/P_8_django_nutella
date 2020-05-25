# coding: utf-8
"""Run the views for Purbeurre APP.
Views:
-index:@transaction.non_atomic_requests
-result:@transaction.non_atomic_requests
-item:@transaction.non_atomic_requests
-save:@login_required
-history:@login_required
-legal(request)
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db import transaction
from .models import FoodItem, Account


def index(request):
    """Front page of web site.
    @transaction.non_atomic_requests
    Arguments:
    -request {GET}
    Returns:
    -template -- index.html
    """
    return render(request, 'purbeurre/index.html')


def result(request):
    """Manage the research of substitute.
    @transaction.non_atomic_requests
    Arguments:
    -request {POST}
    Returns:
    -template -- result.html
    """
    try: 
        item_name = (request.POST['item_name']).lower()
        if  item_name == "":
            return render(request, '404.html')
        food_item = (get_list_or_404(FoodItem, name__icontains=item_name))[0]
        category_item = food_item.linked_cat.all()
        substitute_list = list(category_item[0].fooditem_set.filter(
            nutriscore__lte=food_item.nutriscore).order_by('nutriscore'))
        substitute_list.remove(food_item)
        context = {
            'substitute_list': substitute_list,
            'item_name': food_item,
            'connected': True
        }
        return render(request, 'purbeurre/result.html', context)
    except ValueError:
        return render(request, '404.html')        
    else:
        return render(request, '404.html')


def item(request, item_id):
    """Display details on a selected fooditem.
    @transaction.non_atomic_requests
    Arguments:
    -request {GET}
    Returns:
    -template -- item.html
    """
    food_item = get_object_or_404(FoodItem, id=item_id)
    context = {
        'food_item': food_item
    }
    return render(request, 'purbeurre/item.html', context)


@login_required
def save(request, item_id):
    """Rule the saving of a substitute
    on an account.
    @login_required
    Arguments:
    -request {GET}
    Returns:
    -template -- save.html
    """
    food_item = get_object_or_404(FoodItem, id=item_id)
    account = Account.objects.get(user=request.user)
    old_history = account.history.all()
    if food_item not in old_history:
        account.history.add(food_item)
        message = "Le produit a bien été ajouté à vos favoris"
    else:
        message = "Le produit est déjà dans vos favoris"
    context = {
        'message': message
    }
    return render(request, 'purbeurre/save.html', context)


@login_required
def history(request):
    """Display the substitutes
    saved in an account.
    @login_required
    Arguments:
    -request {GET}
    Returns:
    -template -- history.html
    """
    account = Account.objects.get(user=request.user)
    substitute_list = account.history.all()

    context = {
        'substitute_list': substitute_list,
    }
    return render(request, 'purbeurre/history.html', context)


def legal(request):
    """Rule the legal notice of the website;
    Arguments:
    -request {GET}
    Returns:
    -template -- legal.html
    """
    return render(request, 'purbeurre/legal.html')
