# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from accounts.forms import CustomUSerCreationForm
from core.models import CharacterModel, ItemModel, LocationModel
from game.models import Chronicle, Scene


# Create your views here.
class SignUp(CreateView):
    """View for the Sign Up Page"""

    form_class = CustomUSerCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class ProfileView(View):
    """View for User Profiles"""

    def get(self, request):
        if request.user.is_authenticated:
            context = self.get_context(request.user)
            return render(request, "accounts/index.html", context,)
        return redirect("/accounts/login/")

    def post(self, request):
        context = self.get_context(request.user)
        if any(x.startswith("XP for") for x in request.POST.keys()):
            to_remove = [x for x in request.POST.keys() if x.startswith("XP for")][0]
            new_dict = {
                k: v
                for k, v in request.POST.items()
                if k not in [to_remove, "csrfmiddlewaretoken"]
            }
            scene_name = [x for x in request.POST.keys() if x.startswith("XP for")][
                0
            ].split("XP for ")[-1]
            scene = Scene.objects.get(name=scene_name)
            for char in scene.characters.all():
                if char.name in new_dict.keys():
                    char.xp += int(new_dict[char.name])
                    char.save()
            scene.xp_given = True
            scene.save()
        else:
            char = [x for x in context["to_approve"] if x.name in request.POST.keys()][
                0
            ]
            char.status = "App"
            char.save()
        context = self.get_context(request.user)
        return render(request, "accounts/index.html", context,)

    def get_context(self, user):
        to_approve = CharacterModel.objects.filter(status__in=["Un", "Sub"])
        chronicles_sted = [
            x for x in Chronicle.objects.all() if user in x.storytellers.all()
        ]
        to_approve = [x for x in to_approve if x.chronicle in chronicles_sted]

        xp_requests = Scene.objects.filter(
            story__chronicle__in=chronicles_sted, finished=True, xp_given=False
        )

        return {
            "user": user,
            "username": user.username,
            "to_approve": to_approve,
            "xp_requests": xp_requests,
            "characters": CharacterModel.objects.filter(owner=user).order_by("name"),
            "locations": LocationModel.objects.filter(owner=user).order_by("name"),
            "items": ItemModel.objects.filter(owner=user).order_by("name"),
        }
