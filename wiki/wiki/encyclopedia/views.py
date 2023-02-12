from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.urls import reverse
import markdown2
from random import randint
from . import util


class NewForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))
    
class AddPageForm(forms.Form):
    title = forms.CharField(label="Name of web page")
    textArea = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':5}))

# It handles search bar of wiki homepage. If request is "post", it ultimately redirects
# to "link" path where it will be rendered a page with all the results from the search. 

def index(request):

    if "entries" not in request.session:
        request.session["entries"] = []

    if request.method == "POST":
        request.session["entries"].clear()
        form = NewForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            list = [x.lower() for x in util.list_entries() if search.lower() in x.lower()]
            if len(list) != 0:
                request.session["entries"] += list
                #page = util.get_entry("search")
                return HttpResponseRedirect(reverse("wiki:links"))
               
            else:
                return render(request,"encyclopedia/index.html")
        else:
            return render(request,"encyclopedia/index.html",{
                "form":form
            })
            
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries() , "form": NewForm()
    })

# It is responsible to convert markdown file format into html when user access wiki page

def entry(request,entry):
    
    if util.get_entry(entry) == None:
        return HttpResponseRedirect(reverse("wiki:index"))
   
    return render(request,"encyclopedia/pages.html",{
        "entry": markdown2.Markdown().convert(util.get_entry(entry)),
        "title": entry  
    })

def links(request):
    return render(request,"encyclopedia/search.html",{
                    "entry": request.session["entries"]
                   })


# It is path dedicated to creating a new wiki page when an user clicks "create new page"
# from homepage.

def newPage(request):
    if request.method == "POST":
        form = AddPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            textArea = form.cleaned_data["textArea"]

            if title in util.list_entries():
                return HttpResponse("Error, multiple files with same name") 
            util.save_entry(title,textArea)
            #request.session["entries"] += [title]
            return HttpResponseRedirect(reverse('wiki:entry', args=(title,)))

        return render(request,"encyclopedia/newPage.html",{
            "form": form})
    return render(request,"encyclopedia/newPage.html", {
        "form": AddPageForm()})

# Below every page, an user can press a link that allows them to edit it. It sets by default
# a textarea value that is the previous page's content and as hidden value the name of the page.
 
def edit(request,title):
    if request.method == "POST":
        form = AddPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            textArea = form.cleaned_data["textArea"]
            util.save_entry(title,textArea)
            return HttpResponseRedirect(reverse("wiki:entry",args=(title,)))
        else:
            return render(request,"encyclopedia/edit.html",{
                "form":form, "title":title, 
            })
    new_form = AddPageForm()
    new_form.fields["textArea"].initial = util.get_entry(title)
    new_form.fields["textArea"].label = ""
    new_form.fields["title"].initial = title
    new_form.fields["title"].widget = new_form.fields["title"].hidden_widget()
      
    return render(request,"encyclopedia/edit.html",{
        "title":title,
        "form":new_form 
    })

# Returns random existing wiki page.

def random(request):
    length = util.list_entries()
    range = len(length)
    rand_index = randint(0,range)
    return HttpResponseRedirect(reverse("wiki:entry",args=(length[rand_index],)))




    


