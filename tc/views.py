from django.shortcuts import redirect, render
from django.views.generic import View

from tc.models.characters.aberrant import Aberrant, MegaEdgeRating, PowerRating
from tc.models.characters.human import EdgeRating, Human, PathRating
from tc.models.characters.talent import Talent


# Create your views here.
class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "tc/characters/index.html", context)

    def get_context(self):
        chars = Human.objects.all().order_by("name")
        context = {}
        context["chars"] = chars
        return context


class HumanDetailView(View):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/human/detail.html", context)

    def get_context(self, pk):
        char = Human.objects.get(id=pk)
        context = {"character": char}
        context["origin_path"] = PathRating.objects.filter(
            character=char, path__type="origin"
        ).first()
        context["role_path"] = PathRating.objects.filter(
            character=char, path__type="role"
        ).first()
        context["society_path"] = PathRating.objects.filter(
            character=char, path__type="society"
        ).first()
        context["additional_paths"] = [
            x
            for x in PathRating.objects.filter(character=char)
            if x
            not in [
                context["origin_path"],
                context["role_path"],
                context["society_path"],
            ]
        ]
        for skill in char.get_skills():
            context[skill + "_spec"] = ", ".join(
                [x.name for x in char.specialties.filter(skill=skill)]
            )
        context["edges"] = EdgeRating.objects.filter(character=char)
        return context


class TalentDetailView(HumanDetailView):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/talent/detail.html", context)

    def get_context(self, pk):
        context = super().get_context(pk=pk)
        return context


class AberrantDetailView(HumanDetailView):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/aberrant/detail.html", context)

    def get_context(self, pk):
        context = super().get_context(pk=pk)
        context["mega_edges"] = MegaEdgeRating.objects.filter(character=context['character'])
        context["powers"] = PowerRating.objects.filter(character=context['character'])
        return context


class CharacterDetailView(View):
    detail_views = {
        "human": HumanDetailView,
        "talent": TalentDetailView,
        "aberrant": AberrantDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Human.objects.get(pk=kwargs["pk"])
        if char.type in self.detail_views:
            return self.detail_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("tc:characters_index")


class RandomCharacterView(View):
    chars = {
        "human": Human,
        "talent": Talent,
        "aberrant": Aberrant,
    }

    def post(self, request, *args, **kwargs):
        char = self.chars[request.POST["char_type"]].objects.create(
            name=request.POST["char_name"], player=request.user.tc_profile
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
