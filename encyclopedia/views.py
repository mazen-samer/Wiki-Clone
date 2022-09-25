from cgitb import text
from unicodedata import name
from django.shortcuts import render
import markdown
from . import util
import random


def Random(request):
    x = random.randrange(len(util.list_entries()))
    name = util.list_entries()[x]
    return render(request, "encyclopedia/random.html",{
        "name": name,
        "content": markdown.markdown(util.get_entry(name))          
    })




def edit(request, title):
    if request.method == 'POST':
        text = request.POST['text']
        util.save_entry(title, text)
        return render(request, "encyclopedia/display.html",{
            "name": title,
            "content": markdown.markdown(util.get_entry(title))          
    })
        
    return render(request, "encyclopedia/edit.html",{
        "title": title,
        "content": util.get_entry(title)
    })



def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        if title in util.list_entries():
            return render(request, "encyclopedia/page exists.html")
        util.save_entry(title, text)
        return render(request, "encyclopedia/display.html",{
            "name": title,
            "content": markdown.markdown(util.get_entry(title))          
    })
    return render(request, "encyclopedia/create.html")



def search(request):
    if request.method == 'POST':
        searched = request.POST['q']
        if searched in util.list_entries():
            return render(request, "encyclopedia/display.html",{
            "name": searched,
            "content": markdown.markdown(util.get_entry(searched))          
    })
        
        else: 
            return render(request, "encyclopedia/search.html",{
                "searched": list(filter(lambda k: searched in k, util.list_entries()))
            })
    else:
        return render(request, "encyclopedia/search.html",{
            "entries": util.list_entries()
        })


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request, name):
    return render(request, "encyclopedia/display.html",{
        "name": name,
        "content": markdown.markdown(util.get_entry(name))          
    })

 