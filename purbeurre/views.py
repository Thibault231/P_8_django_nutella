from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError
from .models import *
from .python.api import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


### Ask for first page: GET ###
# display index template
@transaction.non_atomic_requests
def index(request):
    #Db_implementation()
    return render(request, 'purbeurre/index.html')

@transaction.non_atomic_requests
def result(request):
    item_name = (request.POST['item_name']).lower()
    food_item = (get_list_or_404(FoodItem, name__icontains=item_name))[0]
    category_item = food_item.linked_cat.all()
    substitute_list = list(category_item[0].fooditem_set.filter(nutriscore__lte=food_item.nutriscore).order_by('nutriscore'))
    substitute_list.remove(food_item)
    context = {
    'substitute_list': substitute_list,
    'item_name':food_item,
    'connected': True
    }
    return render(request, 'purbeurre/result.html', context)

@transaction.non_atomic_requests
def item(request, item_id):
    food_item = get_object_or_404(FoodItem, id=item_id)
    context = {
        'food_item': food_item
    }
    return render(request, 'purbeurre/item.html', context)

@login_required
def save(request, item_id):
    food_item = get_object_or_404(FoodItem, id=item_id)
    account = Account.objects.get(user=request.user)
    old_history = account.history.all()
    if food_item not in old_history:
        account.history.add(food_item)
        message = "Le produit a bien été ajouté à vos favoris" 
    else:
        message = "Le produit est déjà dans vos favoris" 
    context = {
        'message' : message
    }
    return render(request, 'purbeurre/save.html', context)

@login_required
def history(request):
    account = Account.objects.get(user=request.user)
    substitute_list = account.history.all()

    context = {
    'substitute_list': substitute_list,
    }
    return render(request, 'purbeurre/history.html', context)

def legal(request):
    return render(request, 'purbeurre/legal.html')