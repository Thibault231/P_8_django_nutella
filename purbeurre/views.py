from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError
from .models import *
from .python.api import *
from .forms import SubstituteForm


### Ask for first page: GET ###
# display index template
@transaction.non_atomic_requests
def index(request):
    #Db_implementation()
    if request.method == 'POST':
        item_name = request.POST.get('item_name').encode('utf8')
        food_item = FoodItem.objects.get(name=item_name)
        context = {
        'name': food_item.name,
        'nutriscore': food_item.nutriscore
        }
        return render(request, 'purbeurre/result.html', context)
    return render(request, 'purbeurre/index.html')

@transaction.non_atomic_requests
def result(request):
    context = {
        'name': 'ok',
        'nutriscore': 'ok'
    }
    return render(request, 'purbeurre/result.html', context)

### Ask for a subsitute: GET ###
# testing connection with DB
# if connection ok:
    # get dats

    # if food name correct
        # find a substitute
        # if substitute exists
            #send datas and template
        # if substitute doesn't exists
            # error not found
    # else:
        # error 404
# if not:
    #error 500


### Ask for a food item: GET###
# testing connection with DB
# if connection ok
    # if food name correct

    
            #send datas and template
    # else:
        # error 404
# if not:
    #error 500


### Ask for the history: POST ###
# testing connection with DB
# if connection ok:
    # found client count
    # if count exists
        # if history empty
            #empty template response
        # else:
            #send datas and template
    # else:
        # error 404
# if not:
    #error 500

### Connecting to an account: GET ###
# testing connection with DB
# if connection ok:
    #get datas
    # if datas corrects
        # get clients informations from DB
        # send response and template
    # else
        # error 404
# if not:
    #error 500


### Creating an account: GET ###
# testing connection with DB
# if connection ok:
    #get datas
    # if datas corrects
        # check unexisting client
        # if count doesn't exist
            #create account
            # send response and template
        # else:
            # error response
    # else
        # error 404
# if not:
    #error 500


### See my account: POST ###
# testing connection with DB
# if connection ok:
    # get connection's datas
    # if datas corrects
        # found client count
        # if count exists
            # get client datas in db
            # send response and template
        # else:
            # create account page
    # else:
        # connection page
# if not:
    #error 500


### save my search: POST ###
# testing connection with DB
# if connection ok:
    # get connection's datas
    # if datas corrects
        # found client count
        # if count exists
            # get datas
            # save datas in db
            # send response and template
        # else:
            # error 404
    # else:
        # connection page
# if not:
    #error 500
