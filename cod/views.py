from collections import namedtuple

from django.shortcuts import redirect, render
from django.views.generic import DetailView, View

from cod.models.characters.mage import Mage, Proximi, ProximiFamily
from cod.models.characters.mortal import MeritRating, Mortal

# Create your views here.
EmptyRote = namedtuple("EmptyRote", ["name", "arcana", "level"])
empty_rote = EmptyRote("", "", "")


class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "cod/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "cod/characters/index.html", context)

    def get_context(self):
        chars = Mortal.objects.all().order_by("name")
        context = {}
        context["chars"] = chars
        return context


class MortalDetailView(View):
    def get(self, request, *args, **kwargs):
        char = Mortal.objects.get(pk=kwargs["pk"])
        context = {
            "object": char,
            "merits": MeritRating.objects.filter(character=char).order_by(
                "merit__name"
            ),
            "specialties": char.specialties.all().order_by("name"),
        }
        return render(request, "cod/characters/mortal/detail.html", context,)


class ProximiDetailView(View):
    def get(self, request, *args, **kwargs):
        char = Proximi.objects.get(pk=kwargs["pk"])
        context = {
            "object": char,
            "merits": MeritRating.objects.filter(character=char).order_by(
                "merit__name"
            ),
            "specialties": char.specialties.all().order_by("name"),
        }

        all_blessings = list(context["object"].blessings.all())
        row_length = 2
        all_blessings = [
            all_blessings[i : i + row_length]
            for i in range(0, len(all_blessings), row_length)
        ]
        if len(all_blessings) != 0:
            while len(all_blessings[-1]) < row_length:
                all_blessings[-1].append(empty_rote)
        context["blessings"] = all_blessings
        return render(request, "cod/characters/proximi/detail.html", context,)


class MageDetailView(View):
    def get(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        context = {
            "object": char,
            "merits": MeritRating.objects.filter(character=char).order_by(
                "merit__name"
            ),
            "specialties": char.specialties.all().order_by("name"),
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

        return render(request, "cod/characters/mage/detail.html", context,)


class CharacterDetailView(View):
    """Class that manages Views for characters"""

    create_views = {
        "mortal": MortalDetailView,
        "mage": MageDetailView,
        "proximi": ProximiDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Mortal.objects.get(pk=kwargs["pk"])
        if char.type in self.create_views:
            return self.create_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("cod:characters_index")


class RandomCharacterView(View):
    chars = {
        "mortal": Mortal,
        "mage": Mage,
        "proximi": Proximi,
    }

    def post(self, request, *args, **kwargs):
        char = self.chars[request.POST["char_type"]].objects.create(
            name=request.POST["char_name"], player=request.user.cod_profile
        )
        try:
            xp = int(request.POST["xp"])
        except ValueError:
            xp = 0
        xp = max(xp, 0)
        char.random(xp=xp)
        char.save()
        return redirect(char.get_absolute_url())

    def get(self, request):
        return redirect("cod:characters_index")


class ProximiFamilyDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        fam = ProximiFamily.objects.get(pk=kwargs["pk"])
        context = {
            "object": fam,
        }
        context["arcana"] = ", ".join(
            [x.title() for x in fam.path.ruling_arcana + [fam.blessing_arcana]]
        )

        all_blessings = list(context["object"].possible_blessings.all())
        row_length = 2
        all_blessings = [
            all_blessings[i : i + row_length]
            for i in range(0, len(all_blessings), row_length)
        ]
        if len(all_blessings) != 0:
            while len(all_blessings[-1]) < row_length:
                all_blessings[-1].append(empty_rote)
        context["blessings"] = all_blessings
        return render(request, "cod/characters/proximifamily/detail.html", context,)
