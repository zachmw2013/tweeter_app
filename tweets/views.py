from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm

def tweet_list(request):
    return render(request, 'home.html', {'object_list': Tweet.objects.all()})

def tweet_new(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TweetForm

    return render(request, 'tweet_new.html', {'form': form })