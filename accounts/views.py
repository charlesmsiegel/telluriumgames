from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from accounts.models import CoDProfile, TCProfile, WoDProfile
from cod.models.characters.mortal import Mortal

# from tc.models import Aberrant
# from wod.models.characters import Character

# from characters.models import Character


# Create your views here.
class SignUp(CreateView):
    """View for the Sign Up Page"""

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class ProfileView(View):
    """View for User Profiles"""

    def get(self, request):
        if request.user.is_authenticated:
            cod_profile = CoDProfile.objects.get(user=request.user)
            # wod_profile = WoDProfile.objects.get(user=request.user)
            # tc_profile = TCProfile.objects.get(user=request.user)
            to_approve = []
            xp_requests = []
            characters = []
            characters.extend(Mortal.objects.filter(player=cod_profile))
            # characters.extend(Character.objects.filter(player=wod_profile))
            # characters.extend(Aberrant.objects.filter(player=tc_profile))
            # characters.sort(key=lambda x: x.name)
            if cod_profile.storyteller:
                to_approve.extend(Mortal.objects.filter(status__in=["Un", "Sub"]))
            # if wod_profile.storyteller:
            #     to_approve.extend(Character.objects.filter(status__in=["Un", "Sub"]))
            # if tc_profile.storyteller:
            #     to_approve.extend(Aberrant.objects.filter(status__in=["Un", "Sub"]))
            return render(
                request,
                "accounts/index.html",
                {
                    "user": request.user,
                    "username": request.user.username,
                    "to_approve": to_approve,
                    "xp_requests": xp_requests,
                    "characters": characters,
                },
            )
        return redirect("/accounts/login/")
