from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import auth
from authapp.models import ShopUser
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm


def login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                # return HttpResponseRedirect('/')
                return HttpResponseRedirect(reverse('main:index'))
    else:
        # render empty form
        form = ShopUserLoginForm()
    
    context = {
        'page_title': 'Log in',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        # render empty form
        form = ShopUserRegisterForm()
    
    context = {
        'page_title': 'Sign up',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'error: activation error of user {e.args}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user: {e:args}')
        return HttpResponseRedirect(reverse('main'))