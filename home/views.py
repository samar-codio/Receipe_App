from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login/')
def receipe_form(request):
    if request.method == "POST":
        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        if receipe_name and receipe_description and receipe_image:
            receipe.objects.create(
                receipe_name=receipe_name,
                receipe_image=receipe_image,
                receipe_description=receipe_description,
            )
            return redirect('receipe_form')
    vals = receipe.objects.all()
    context = {'receipe_data': vals}

    if request.GET.get('search'):
        queryset = vals.filter(
            receipe_name__icontains=request.GET.get('search'))
        context = {'receipe_data': queryset}
    return render(request, 'receipe_form.html', context)


def delete_receipe(request, id):
    queryset = receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipe/")


def update_receipe(request, id):
    queryset = receipe.objects.get(id=id)
    context = {'up_receipe': queryset}
    if request.method == "POST":

        data = request.POST

        receipe_name = request.POST.get("receipe_name")
        receipe_description = request.POST.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipe/')

    return render(request, "update_receipe.html", context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username):
            messages.warning(request, 'Invalid Username')
            return (redirect('/login'))

        user = authenticate(username=username, password=password)

        if user == None:
            messages.warning(request, 'Invalid Credentials')
            return (redirect('/login'))
        else:
            login(request, user)
            return (redirect('/receipe/'))

    return (render(request, 'login_page.html'))


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.warning(request, 'Username already exists')
            return (redirect('/register'))

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,

        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Account Successfully Created !')
        return (redirect('/login'))

    return (render(request, 'register.html'))


def logout_page(request):
    logout(request)
    return redirect('/login/')
