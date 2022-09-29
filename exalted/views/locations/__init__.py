from django.shortcuts import redirect, render
from django.views.generic import View

from core.utils import level_name, tree_sort
from exalted.models.locations.mortals import ExLocation

from . import mortals


class LocationIndexView(View):
    def get(self, request):
        context = self.get_context()
        return render(request, "exalted/locations/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "exalted/locations/index.html", context)

    def get_context(self):
        locations = ExLocation.objects.all().order_by("name")
        context = {}
        context["locations"] = locations
        L1 = []
        L2 = []
        for x in ExLocation.objects.filter(parent=None).order_by("name"):
            L1.extend([level_name(y) for y in tree_sort(x)])
            L2.extend(tree_sort(x))

        context["names_dict"] = dict(zip(L1, L2))
        return context


class GenericLocationDetailView(View):
    views = {
        "location": mortals.ExLocationDetailView,
    }

    def get(self, request, *args, **kwargs):
        loc = ExLocation.objects.get(pk=kwargs["pk"])
        if loc.type in self.views:
            return self.views[loc.type].as_view()(request, *args, **kwargs)
        return redirect("exalted:locations:index")
