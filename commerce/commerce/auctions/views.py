from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django import forms
from django.db.models import Max
from .models import User, Listing, Bidd, Comments,In_Watchlist

class NewListing(forms.Form):
    item = forms.CharField(label="Name of the item", widget=forms.TextInput(attrs={'class':'form-control width'}))
    cost = forms.FloatField(label="Initial bid",widget=forms.NumberInput(attrs={'class':'form-control'}))
    description = forms.CharField(label="Describe the object", widget=forms.Textarea(attrs={'class':'form-control','rows':3, 'cols':5}))
    category = forms.CharField(label="category", widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField(label="upload an image of item", widget=forms.FileInput(attrs={'class':'form-control-file'}))

   
class Comments_form(forms.Form):
     comment = forms.CharField(label="Comment here", 
     widget=forms.Textarea(attrs={'class':'form-control','rows':3, 'cols':5}))


@login_required(login_url="/login")
def index(request):
    user = User.objects.get(pk=request.user.id)
    return render(request, "auctions/index.html",
    {"user": user,
     "user_listing": Listing.objects.all()})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


# path to create a new listing
@login_required(login_url="/login")
def listing(request):
    if request.method == "POST":
        form = NewListing(request.POST,request.FILES)
        if form.is_valid():
            item = form.cleaned_data["item"]
            cost = form.cleaned_data["cost"]
            image = form.cleaned_data["image"]
            description = form.cleaned_data["description"]
            category = form.cleaned_data["category"]
            name = User.objects.get(pk=int(request.user.id))
            listing = Listing(name=name,item=item, cost=cost, 
            image=image,description=description, category=category)
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request,"auctions/listing.html",{
            "form":form
        })
    return render(request,"auctions/listing.html",{
        "form":NewListing()
    })
# Once user clicks on a auction listing, it will display to them the item with
# button to add it to watchlist and if it is the same person who created the listing,
# to remove it. A user can also add comments to it if they want.
@login_required(login_url="/login")
def active_listing(request,listing_id):

    this_listing = Listing.objects.get(id=listing_id)
    user = request.user
    
    try:
        this_watchlist = In_Watchlist.objects.filter(name=request.user).get(listing=this_listing)
    except In_Watchlist.DoesNotExist:
        this_watchlist= None
    try:
        bid = Bidd.objects.filter(listing=this_listing)
        
    except Bidd.DoesNotExist:
        bid=None
    if request.method == "POST":
        # Saves the current listing into watchlist if user clicks button 
        # in acitve_listing.html 
        if "in_Watchlist" in request.POST:
            state = str(request.POST["in_Watchlist"])
            if state == "False":
                if not this_watchlist:
                    state_False = In_Watchlist(in_Watchlist=state,name=user,listing=this_listing)
                    state_False.save()
                else:
                    this_watchlist.in_Watchlist = state
                    this_watchlist.save()
            elif state == "True":
                if not this_watchlist:
                    state_True = In_Watchlist(in_Watchlist=state,name=user,listing=this_listing)
                    state_True.save()
                else:
                    this_watchlist.in_Watchlist = state
                    this_watchlist.save()

        #Saves a comment if user decides to comment
        if "comment" in request.POST:
            comment = Comments_form(request.POST)
            if comment.is_valid():
                comment = comment.cleaned_data["comment"]
                something = Comments(comments=comment, auction=this_listing)
                something.save()
            else:
                current_state = In_Watchlist.objects.filter(name=user).get(listing=this_listing)
                return render(request, "auctions/active_listing.html",{
                    "listing": this_listing,
                    "comments": this_listing.comments.all(),
                    "user": request.user,
                    "comment_input": comment,
                    "state" : current_state,
                    "highest_bidd": bid.aggregate(Max("offer"))
                })
            # handles the bid input from an user. It asks for bid to be at least bigger than
            #previous bid
        if "bidd" in request.POST:
            input_bid = request.POST["bidd"]
            Max_offer = bid.aggregate(Max("offer"))
            if Max_offer["offer__max"] == None:
                Max_offer["offer__max"] = this_listing.cost 
            if int(input_bid) < Max_offer["offer__max"]:
                return HttpResponse("Bid must be greater than cost or current offer")
            else:
                current_bid = Bidd(name=request.user,listing=this_listing,offer=int(input_bid))
                current_bid.save()
                return HttpResponseRedirect(reverse('index'))
        # Handles the behaviour for sending message to the winner of auction 
        # after it is removed by the person who listed the auction item
        if "state" in request.POST:
            if request.POST["state"]:
                max_offer = bid.aggregate(Max("offer"))
                winning_auction = bid.get(offer = max_offer["offer__max"])
                winning_auction.name.message = "You have won the auction!"
                winning_auction.name.save()
                this_listing.delete()
                return HttpResponseRedirect(reverse('index'))
        return HttpResponseRedirect(reverse('watchlist'))

    current_state = In_Watchlist.objects.filter(name=user).filter(listing=this_listing)
    dict_template = {
            "listing": this_listing,
            "comments": this_listing.comments.all(),
            "user": request.user,
            "comment_input": Comments_form(),
            "state" : current_state,
            "highest_bidd": bid.aggregate(Max("offer"))
        }
    if current_state:
        return render(request, "auctions/active_listing.html", dict_template)
    else:
        current_state = False
        return render(request, "auctions/active_listing.html", dict_template)

@login_required(login_url="/login")
def watchlist(request):

    listings = In_Watchlist.objects.filter(name=request.user).filter(in_Watchlist="True")
    return render(request,"auctions/watchlist.html",{
        "watchlist": listings
    })

@login_required(login_url="/login")
def messages(request):
    return render(request,"auctions/messages.html",{
        "user": User.objects.get(username=request.user)
    })