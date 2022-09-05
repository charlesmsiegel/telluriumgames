from django.shortcuts import render
from django.views.generic import DetailView, View

from core.models import Language, Material, Medium, NewsItem


# Create your views here.
class HomeView(View):
    """This View controls the main landing page for the site"""

    def get(self, request):
        context = {"user": request.user}
        context["news"] = NewsItem.objects.order_by("-date")
        return render(request, "core/index.html", context=context)


class LanguageDetailView(DetailView):
    model = Language
    template_name = "core/language/detail.html"


class MediumDetailView(DetailView):
    model = Medium
    template_name = "core/medium/detail.html"


class MaterialDetailView(DetailView):
    model = Material
    template_name = "core/material/detail.html"
