from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def about(request):
    return render(request, 'basic_app/about.html')

def discuss(request):
    return render(request, 'basic_app/discuss.html')

def contact(request):
    return render(request, 'basic_app/contact.html')

def articles(request):
    return render(request, 'basic_app/articles.html')

def meditation(request):
    return render(request, 'basic_app/meditation.html')

def discuss(request):
    return render(request, 'basic_app/discuss.html')

def quiz(request):
    return render(request, 'basic_app/quiz.html')

def kidsarticle(request):
    return render(request, 'basic_app/kidsarticle.html')

def teenagearticle(request):
    return render(request, 'basic_app/teenagearticle.html')

def adultarticle(request):
    return render(request, 'basic_app/adultarticle.html')
