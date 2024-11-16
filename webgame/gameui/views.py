from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.urls import reverse
from django.db import IntegrityError, models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import User, Pet, Egg
from .util import parsePet, randomPet, combinePets, starterPets, hatch, get_settings, set_settings
import json

# Create your views here.

@csrf_exempt
def settings_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        quality = data.get('quality')
        set_settings(request.user,quality=int(quality))
        print(f"Quality setting received: {quality}")
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

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
        next = request.GET.get('next') if request.GET.get('next') else ''
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
def pets(request:HttpRequest):
    pets = Pet.objects.filter(master=request.user)
    parsedPets = []
    for pet in pets:
        parsedPets.append((parsedPet := parsePet(pet)))
    
    return render(request, 'pets.html', {
        'title':'My Pets',
        'pets':parsedPets,
        'settings':get_settings(request.user)
    })

@login_required(login_url='login')
def addPet(request:HttpRequest):
    if request.user.is_superuser:
        randPet = randomPet(request.user)
        randPet.save()
        return HttpResponseRedirect(reverse('my-pets'))
    else:
        return HttpResponseForbidden()
    
@login_required(login_url='login')
def aBreed(request:HttpRequest):
    if request.method == 'GET': #and request.user.is_superuser:
        try:
            pet1 = Pet.objects.get(id=int(request.GET.get('p1')))
            pet2 = Pet.objects.get(id=int(request.GET.get('p2')))
        except KeyError:
            pet1 = Pet.objects.get(id=0)
            pet2 = Pet.objects.get(id=1)
        except ValueError:
            pet1 = Pet.objects.get(letterId=request.GET.get('p1'))
            pet2 = Pet.objects.get(letterId=request.GET.get('p2'))
        child = combinePets(pet1, pet2,request.user)
        child.save()

        return HttpResponseRedirect(reverse('my-pets'))
    else:
        return HttpResponseForbidden()
    
@login_required(login_url='login')
def hatcher(request:HttpRequest):
    eggs = Egg.objects.filter(master=request.user)
    return render(request, 'hatchery.html', {"eggs":eggs})

@login_required(login_url='login')
def settings(request: HttpRequest):
    print(get_settings(request.user))
    return render(request, 'settings.html', {'settings':get_settings(request.user)})