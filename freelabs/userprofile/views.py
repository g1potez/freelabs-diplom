from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TracksForm, UsernameEditForm, MailEditForm, AvatarsForm
from .models import Tracks, Avatars
from django.contrib.auth.models import User
from django.contrib import messages

def clear_messages(request):
    storage = messages.get_messages(request)
    storage.used = True

def profile(request):
    message = ''
    message_error = ''

    if request.method == 'POST':
        form = TracksForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.user)
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            message = 'Успешно!'
        else:
            message_error = 'Некорректный формат, пожалуйста, используйте .mp3 или .wav'

    form = TracksForm()
    tracks = Tracks.objects.filter(user=request.user)
    image = Avatars.objects.filter(user=request.user)
    return render(request, 'userprofile/profile.html', context={'form': form, 'message': message, 'message_error': message_error, 'tracks': tracks, 'image': image})


def edit(request):
    if request.method == 'POST':
        form_img = AvatarsForm(request.POST, request.FILES)
        form_username = UsernameEditForm(request.POST, instance=request.user)
        form_mail = MailEditForm(request.POST, instance=request.user)
        form_username.actual_user = request.user

        if form_img.is_valid():
            Avatars.objects.all().delete()
            print(request.user)
            obj = form_img.save(commit=False)
            obj.user = request.user
            obj.save()

        if form_username.is_valid():
            username = form_username.cleaned_data.get('username')
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Данное имя уже занято')
            else:
                form_username.save()
                clear_messages(request)
                for field in form_username.errors:
                    for error in form_username[field].errors:
                        messages.error(request, error)

        if form_mail.is_valid():
            email = form_mail.cleaned_data.get('email')
            if User.objects.filter(email = email).exists():
                messages.error(request, 'Данный email уже занят')
            else:
                form_mail.save()
                clear_messages(request)
                for field in form_mail.errors:
                    for error in form_mail[field].errors:
                        messages.error(request, error)
        else:
            clear_messages(request)

    form_username = UsernameEditForm()
    form_mail = MailEditForm()
    form_img = AvatarsForm()
    image = Avatars.objects.filter(user=request.user)
    return render(request, 'userprofile/edit.html', context={'form_username': form_username, 'form_mail': form_mail, 'form_img': form_img, 'image': image})
