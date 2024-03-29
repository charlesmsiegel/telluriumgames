from collections import namedtuple

from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, View

from wod.models.items.mage import (
    Artifact,
    Charm,
    Grimoire,
    Talisman,
    Wonder,
    WonderResonanceRating,
)

EmptyRote = namedtuple("EmptyRote", ["name", "spheres"])
empty_rote = EmptyRote("", "")


class WonderDetailView(View):
    def get(self, request, *args, **kwargs):
        wonder = Wonder.objects.get(pk=kwargs["pk"])
        context = self.get_context(wonder)
        return render(request, "wod/items/mage/wonder/detail.html", context)

    def get_context(self, wonder):
        return {
            "object": wonder,
            "resonance": WonderResonanceRating.objects.filter(wonder=wonder).order_by(
                "resonance__name"
            ),
        }


class WonderCreateView(CreateView):
    model = Wonder
    fields = ["name", "rank", "background_cost", "quintessence_max", "description"]
    template_name = "wod/items/mage/wonder/form.html"


class WonderUpdateView(UpdateView):
    model = Wonder
    fields = ["name", "rank", "background_cost", "quintessence_max", "description"]
    template_name = "wod/items/mage/wonder/form.html"


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
            "abilities": "<br>".join(
                [x.replace("_", " ").title() for x in grimoire.abilities]
            ),
            "spheres": "<br>".join(
                [x.replace("_", " ").title() for x in grimoire.spheres]
            ),
            "effects": "<br>".join([str(x) for x in grimoire.effects.all()]),
            "date_written": grimoire.date_written,
            "faction": s,
        }
        context["paradigms"] = "<br>".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in grimoire.paradigms.all()
            ]
        )
        context["practices"] = "<br>".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in grimoire.practices.all()
            ]
        )
        context["instruments"] = "<br>".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in grimoire.instruments.all()
            ]
        )
        all_effects = list(context["object"].effects.all())
        row_length = 2
        all_effects = [
            all_effects[i : i + row_length]
            for i in range(0, len(all_effects), row_length)
        ]
        if len(all_effects) != 0:
            while len(all_effects[-1]) < row_length:
                all_effects[-1].append(empty_rote)
        context["effects"] = all_effects
        context["year"] = abs(grimoire.date_written)
        return context


class GrimoireCreateView(CreateView):
    model = Grimoire
    fields = "__all__"
    template_name = "wod/items/mage/grimoire/form.html"


class GrimoireUpdateView(UpdateView):
    model = Grimoire
    fields = "__all__"
    template_name = "wod/items/mage/grimoire/form.html"


class CharmDetailView(View):
    def get(self, request, *args, **kwargs):
        charm = Charm.objects.get(pk=kwargs["pk"])
        context = self.get_context(charm)
        return render(request, "wod/items/mage/charm/detail.html", context)

    def get_context(self, charm):
        return {
            "object": charm,
            "resonance": WonderResonanceRating.objects.filter(wonder=charm).order_by(
                "resonance__name"
            ),
        }


class CharmCreateView(CreateView):
    model = Charm
    fields = "__all__"
    template_name = "wod/items/mage/charm/form.html"


class CharmUpdateView(UpdateView):
    model = Charm
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
        "arete",
    ]
    template_name = "wod/items/mage/charm/form.html"


class ArtifactDetailView(View):
    def get(self, request, *args, **kwargs):
        artifact = Artifact.objects.get(pk=kwargs["pk"])
        context = self.get_context(artifact)
        return render(request, "wod/items/mage/artifact/detail.html", context)

    def get_context(self, artifact):
        return {
            "object": artifact,
            "resonance": WonderResonanceRating.objects.filter(wonder=artifact).order_by(
                "resonance__name"
            ),
        }


class ArtifactCreateView(CreateView):
    model = Artifact
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
    ]
    template_name = "wod/items/mage/artifact/form.html"


class ArtifactUpdateView(UpdateView):
    model = Artifact
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "power",
    ]
    template_name = "wod/items/mage/artifact/form.html"


class TalismanDetailView(View):
    def get(self, request, *args, **kwargs):
        talisman = Talisman.objects.get(pk=kwargs["pk"])
        context = self.get_context(talisman)
        return render(request, "wod/items/mage/talisman/detail.html", context)

    def get_context(self, talisman):
        return {
            "object": talisman,
            "resonance": WonderResonanceRating.objects.filter(wonder=talisman).order_by(
                "resonance__name"
            ),
        }


class TalismanCreateView(CreateView):
    model = Talisman
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "powers",
    ]
    template_name = "wod/items/mage/talisman/form.html"


class TalismanUpdateView(UpdateView):
    model = Talisman
    fields = [
        "name",
        "rank",
        "background_cost",
        "quintessence_max",
        "description",
        "powers",
    ]
    template_name = "wod/items/mage/talisman/form.html"
