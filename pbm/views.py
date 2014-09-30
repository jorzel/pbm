from django.shortcuts import render_to_response
from .models import Research, News


def about(request):
    return render_to_response("about.html")


def news(request):
    news = News.objects.all().order_by('-date')
    print news
    return render_to_response("news.html", {'news': news})


def contact(request):
    return render_to_response("contact.html")


def events(request):
    return render_to_response("events.html")


def research(request):
    return render_to_response("research.html")


def equipment(request):
    return render_to_response("equipment.html")
