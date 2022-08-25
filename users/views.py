from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register (request):
    #Register new user
    if request.method != "POST":
        form = UserCreationForm()
    else:
    # Processing of the completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # logging in and redirection to homepage
            login(request, new_user)
            return redirect ('blogs:index')

    # Show empty or invalid form
    context = {"form":form}
    return render (request, 'registration/register.html', context)


