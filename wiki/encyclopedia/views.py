from django.shortcuts import render, redirect
import markdown2
import os
import random
from . import util

entries_dir = 'entries'

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    list_entries = util.list_entries()
    if entry not in list_entries:
        error_message = "This page doesn't exist"
        return render(request, "encyclopedia/error.html", { 'error_message': error_message})
    
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
        for filename in os.listdir(entries_dir):
            if filename.endswith('.md'):
                with open(os.path.join(entries_dir, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    if query.lower() in content.lower():
                        results.append(filename)

    return render(request, "encyclopedia/search_results.html", {'results': results, 'query': query})

def create(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            content_raw = request.POST.get('content')
            content = markdown2.markdown(content_raw)
            list_entries = util.list_entries()
            if title.lower() in [entry.lower() for entry in list_entries]:
                error_message = "Error - This page already exists"
                return render(request, "encyclopedia/error.html", {'error_message': error_message})
            if not title:
                error_message = "Error - Please add a title"
                return render(request, "encyclopedia/error.html", {'error_message': error_message})
            util.save_entry(title, content)
            return redirect('entry', entry=title)
        return render(request, "encyclopedia/create.html")

def edit(request, entry):
    list_entries = util.list_entries()
    if request.method == 'GET':
        content = util.get_entry(entry)
        return render(request, "encyclopedia/edit.html", {       
            "entry": entry,
            "content": content
        })
    elif request.method == 'POST':
            content_raw = request.POST.get('content')
            content = markdown2.markdown(content_raw)
            util.save_entry(entry, content)
            return redirect ('entry', entry=entry)
        
    elif entry not in list_entries:
        error_message = "Error - This page doesn't exist"
        return render(request, "encyclopedia/error.html", { 'error_message': error_message})
    
def rand_entry(request):
    list_entries = util.list_entries()
    random_entry = random.choice(list_entries)
    content = util.get_entry(random_entry)
    return render(request, "encyclopedia/entry.html", {       
            "entry": random_entry,
            "content": content
        })