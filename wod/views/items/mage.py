from collections import namedtuple

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, View

from wod.models.items.mage import Grimoire, Library, Wonder

EmptyRote = namedtuple("EmptyRote", ["name", "spheres"])
empty_rote = EmptyRote("", "")


class WonderDetailView(DetailView):
    model = Wonder
    template_name = "wod/items/mage/wonder/detail.html"


class WonderCreateView(CreateView):
    model = Wonder
    fields = "__all__"
    template_name = "wod/items/mage/wonder/create.html"


class WonderUpdateView(UpdateView):
    model = Wonder
    fields = "__all__"
    template_name = "wod/items/mage/wonder/update.html"


class GrimoireDetailView(View):
    def get(self, request, *args, **kwargs):
        grimoire = Grimoire.objects.get(pk=kwargs["pk"])
        context = self.get_context(grimoire)
        return render(request, "wod/items/mage/grimoire/detail.html", context)

    def get_context(self, grimoire):
        if grimoire.faction is not None:
            if grimoire.faction.parent is not None:
                if grimoire.faction.parent.parent is not None:
                    s = f"{grimoire.faction.parent} ({grimoire.faction})"
                else:
                    s = f"{grimoire.faction}"
            else:
                s = ""
        else:
            s = ""
        context = {
            "object": grimoire,
            "paradigms": "<br>".join([str(x) for x in grimoire.paradigms.all()]),
            "practices": "<br>".join([str(x) for x in grimoire.practices.all()]),
            "instruments": "<br>".join([str(x) for x in grimoire.instruments.all()]),
            "abilities": "<br>".join(
                [x.replace("_", " ").title() for x in grimoire.abilities]
            ),
            "spheres": "<br>".join(
                [x.replace("_", " ").title() for x in grimoire.spheres]
            ),
            "rotes": "<br>".join([str(x) for x in grimoire.rotes.all()]),
            "date_written": grimoire.date_written,
            "faction": s,
        }
        all_rotes = list(context["object"].rotes.all())
        row_length = 2
        all_rotes = [
            all_rotes[i : i + row_length] for i in range(0, len(all_rotes), row_length)
        ]
        if len(all_rotes) != 0:
            while len(all_rotes[-1]) < row_length:
                all_rotes[-1].append(empty_rote)
        context["rotes"] = all_rotes
        context["year"] = abs(grimoire.date_written)
        return context


class GrimoireCreateView(CreateView):
    model = Grimoire
    fields = "__all__"
    template_name = "wod/items/mage/grimoire/create.html"


class GrimoireUpdateView(UpdateView):
    model = Grimoire
    fields = "__all__"
    template_name = "wod/items/mage/grimoire/update.html"


class LibraryDetailView(DetailView):
    model = Library
    template_name = "wod/items/mage/library/detail.html"


class LibraryCreateView(CreateView):
    model = Library
    fields = "__all__"
    template_name = "wod/items/mage/library/create.html"


class LibraryUpdateView(UpdateView):
    model = Library
    fields = "__all__"
    template_name = "wod/items/mage/library/update.html"
