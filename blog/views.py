from django.shortcuts import render

posts = [
    {
        'author': 'Denis',
        'title': 'Od Sokrata do Freuda',
        'date_posted': 'August 27, 2021',
        'content': 'Lorem ipsum'
    },
    {
        'author': 'Dejan',
        'title': 'Od Golfa do Ferarija',
        'date_posted': 'August 28, 2021',
        'content': 'Lorem ipsum 2'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def test(name: str):
    return name + "da"


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})