from cod.models import MeritRating, Mortal
from django.shortcuts import redirect, render
from django.views.generic import DetailView, View


# Create your views here.
class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "cod/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        # character_class_dict = {
        #     # "vampire": Vampire,
        #     # "werewolf": Werewolf,
        #     "mage": Mage,
        #     # "wraith": Wraith,
        #     # "changeling": Changeling,
        # }
        # if request.POST["character_type"] in character_class_dict:
        #     char_cl = character_class_dict[request.POST["character_type"]]
        #     character = char_cl.objects.create(
        #         name=request.POST["character_name"], player=request.user
        #     )
        #     return redirect(character.get_absolute_url())
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
            "specialties": char.specialties.all().order_by("specialty"),
        }
        return render(request, "cod/characters/mortal/detail.html", context,)


class CharacterDetailView(View):
    """Class that manages Views for characters"""

    create_views = {
        "mortal": MortalDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Mortal.objects.get(pk=kwargs["pk"])
        if char.type in self.create_views:
            return self.create_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("cod:characters_index")
