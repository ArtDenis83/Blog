from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

def index(request):
    blogposts = BlogPost.objects.order_by('-date_added')
    context = {"blogposts": blogposts}
    return render(request, 'blogs/index.html', context)


@login_required
def add_new(request):

    # New form
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return redirect ("blogs:index")

    # Show empty or invalid form
    context = {"form":form}
    return render (request, 'blogs/add_new.html', context)


@login_required
def edit_entry(request, entry_id):
    # edit current entry
    entry = BlogPost.objects.get(id=entry_id)
    entry_id = entry.id
    # check owner
    if entry.owner != request.user:
        return redirect("blogs:index")

    if request.method != 'POST':
        form = BlogForm(instance=entry)
    else:
        # Send data with POST-method, process data
        form = BlogForm(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    # Show empty or invalid form
    context = {"entry":entry,"form": form}
    return render (request, 'blogs/edit_entry.html', context)



