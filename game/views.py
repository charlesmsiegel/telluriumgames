from django.shortcuts import render
from django.views.generic import DetailView

from game.models import Chronicle


# Create your views here.
class ChronicleDetailView(DetailView):
    model = Chronicle
    template_name = "game/chronicle/detail.html"
