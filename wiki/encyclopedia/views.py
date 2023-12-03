from django.shortcuts import render
import os
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

    if query:
        entries_dir = 'entries'
        for filename in os.listdir(entries_dir):
            if filename.endswith('.md'):
                with open(os.path.join(entries_dir, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    if query.lower() in content.lower():
                        results.append(filename)

    return render(request, "encyclopedia/search_results.html", {'results': results, 'query': query})

def create(request):
    return render(request, "encyclopedia/create.html")
    
