from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, IntegrityError
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from purbeurre.models import *



@login_required
def myaccount(request):
    user = request.user
    account = Account.objects.get(user=user)
    substitute_list = list(account.history.all())
    latest_substitute = substitute_list[-1]
    context = {
    'user': user,
    'latest_substitute': latest_substitute
    }
    return render(request, 'purbeurre/myaccount.html', context)

def count_creation(request):
    error_password = False
    error_username = False
    error_email = False
    if request.method == "POST":
        form = CountCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if password1==password2:
                user_control = User.objects.filter(username=username)
                if not user_control:
                    useremail_control = User.objects.filter(email=email)
                    if not  useremail_control:
                        user = User.objects.create_user(
                            username, email, password1)  
                        user.first_name = first_name
                        user.last_name = last_name
                        user.save()
                        account = Account.objects.create(user=user)    
                        login(request, user)
                        return render(request, 'purbeurre/myaccount.html')
                    else:
                        error_email = True
                else:
                   error_username = True
            else:
                error_password = True
    else:
        form = CountCreationForm()
    return render(request, 'purbeurre/count_creation.html', locals())

def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'purbeurre/connexion.html', locals())

@login_required
def deconnexion(request):
    logout(request)
    return render(request, 'purbeurre/index.html')

