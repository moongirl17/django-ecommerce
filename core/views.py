from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from item.models import Category, Item

from .forms import SignupForm
from .forms import LogoutForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

class CustomLogoutView(auth_views.LogoutView):
    template_name = 'logout.html'
    next_page = '/login/'

    def get_form(self):
        return LogoutForm()