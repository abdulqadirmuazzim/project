from django.shortcuts import render


def home(req):
    return render(req, 'home.html')


def pro(req):
    return render(req, 'products.html')


def about(req):
    return render(req, 'about.html')


def con(req):
    return render(req, 'contact.html')


def api(req):
    return render(req, 'contact.html')
