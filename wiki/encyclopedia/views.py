from django.shortcuts import render
import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    list_entries = util.list_entries()
    if entry not in list_entries:
        return render(request, "encyclopedia/error.html")
    
    else:
        content = util.get_entry(entry)
        return render(request, "encyclopedia/entry.html", {       
            "entry": entry,
            "content": content
        })
    
def search(request):
    query = request.GET.get('q')
    results = []

    if query
    
