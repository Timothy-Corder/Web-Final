from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.db import IntegrityError, models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Pet, Egg
from .util import parsePet, randomPet, combinePets, starterPets

# Create your views here.


@login_required(login_url='login')
def homepage(request:HttpRequest):
    return render(request, 'home.html', {
        'title':'Homepage'
    })


def toHome(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    else:
        return redirect(reverse('login'))
    
def login_view(request:HttpRequest):
    print(request.content_params)
    if request.method == 'POST':

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        next = request.POST['next'].strip('/')
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if not next:
                next = 'home'
            return HttpResponseRedirect(reverse(next))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        next = request.GET.get('next')
        return render(request, 'login.html', {'next':next})

def register_view(request:HttpRequest):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        for pet in starterPets(user):
            pet.save()
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, 'register.html')
    
@login_required(login_url='login')
def logout_view(request:HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

@login_required(login_url='login')
def farm(request:HttpRequest):
    # randPet = randomPet(request.user)
    # randPet.save()
    pets = Pet.objects.filter(master=request.user)
    parsedPets = []
    for pet in pets:
        parsedPets.append((parsedPet := parsePet(pet)))
        print(parsedPet)
    # combinePets(pets[19], pets[5], request.user)
    
    return render(request, 'farm.html', {
        'title':'My Farm',
        'pets':parsedPets
    })

@login_required(login_url='login')
def addPet(request:HttpRequest):
    if request.user.is_superuser:
        randPet = randomPet(request.user)
        randPet.save()
        return HttpResponseRedirect(reverse('my-pets'))
    else:
        return HttpResponseForbidden()