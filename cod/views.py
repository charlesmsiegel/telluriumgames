from collections import namedtuple

from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, View

from cod.models.characters.mage import (
    Legacy,
    Mage,
    Order,
    Path,
    Proximi,
    ProximiFamily,
    Rote,
)
from cod.models.characters.mortal import (
    Condition,
    Merit,
    MeritRating,
    Mortal,
    Specialty,
)

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


class MortalCreateView(CreateView):
    model = Mortal
    fields = "__all__"
    template_name = "cod/characters/mortal/create.html"


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


class ProximiCreateView(CreateView):
    model = Proximi
    fields = "__all__"
    template_name = "cod/characters/proximi/create.html"


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


class MageCreateView(CreateView):
    model = Mage
    fields = "__all__"
    template_name = "cod/characters/mage/create.html"


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
            name=request.POST["char_name"], player=request.user
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

        all_blessings = list(
            context["object"].possible_blessings.all().order_by("arcanum")
        )
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


class ProximiFamilyCreateView(CreateView):
    model = ProximiFamily
    fields = "__all__"
    template_name = "cod/characters/proximifamily/create.html"


class ConditionDetailView(DetailView):
    model = Condition
    template_name = "cod/characters/condition/detail.html"


class LegacyDetailView(DetailView):
    model = Legacy
    template_name = "cod/characters/legacy/detail.html"


class MeritDetailView(DetailView):
    model = Merit
    template_name = "cod/characters/merit/detail.html"


class OrderDetailView(DetailView):
    model = Order
    template_name = "cod/characters/order/detail.html"


class PathDetailView(DetailView):
    model = Path
    template_name = "cod/characters/path/detail.html"


class RoteDetailView(DetailView):
    model = Rote
    template_name = "cod/characters/rote/detail.html"


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "cod/characters/specialty/detail.html"
