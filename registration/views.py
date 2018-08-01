from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User


def usr(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    users = User.objects.all()
    return render(request, "show.html", {'users': users})
