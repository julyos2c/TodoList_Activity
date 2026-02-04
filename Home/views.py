from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    posts = response.json()

    return render(request, 'Home/home.html', {'posts' : posts})

def about(request):
    return render(request, 'Home/about.html')

def contact(request):
    return render(request, 'Home/contact.html')
