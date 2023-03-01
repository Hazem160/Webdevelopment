from django.contrib import admin
from .models import Listing,User,Bidd,Comments,In_Watchlist


admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bidd)
admin.site.register(Comments)
admin.site.register(In_Watchlist)
# Register your models here.
