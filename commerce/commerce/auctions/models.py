from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    message = models.CharField(max_length=500,blank=True, null=True)
    
    

class Listing(models.Model):

    item = models.CharField(max_length=100)
    cost = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    image = models.ImageField(upload_to="commerce_pict/", null=True, blank=True)
    description = models.CharField(max_length=1000, blank=True, null=True, default="")
    category = models.CharField(max_length=20, default="No category")
    name = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, related_name="lister")

    def __str__(self):
        return f"{self.name} : {self.item}, ({self.cost})"

class In_Watchlist(models.Model):

    in_Watchlist = models.BooleanField(default="False")
    name = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, 
    related_name="in_Watchlist")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, 
    related_name="listing_auction")
    
    def __str__(self):
        return f"In_Watchlist : {self.name},{self.listing.pk},{self.listing.item}, ({self.in_Watchlist})"



class Comments (models.Model):
    comments = models.CharField(max_length=1000, default="")
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE,blank=True, null=True,related_name="comments")


class Bidd (models.Model):

    offer = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    #item = models.ForeignKey(Listing,on_delete=models.CASCADE, related_name="auction")
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE,blank=True, null=True,related_name="auction")
    name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True, related_name="bidder")

    def __str__(self):
        return f"{self.name} : {self.listing.item},({self.offer})"

