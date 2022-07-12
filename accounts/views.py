from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from django.contrib.auth.models import User
from accounts.models import Profile
from cod.models.characters.mortal import Mortal
from tc.models.characters.human import Human
from wod.models.characters.human import Character
from exalted.models.characters.mortals import Mortal as ExMortal

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
            
            profile = Profile.objects.get(user=request.user)
            to_approve = []
            xp_requests = []
            characters = []
            characters.extend(Mortal.objects.filter(player=request.user))
            characters.extend(Character.objects.filter(player=request.user))
            characters.extend(Human.objects.filter(player=request.user))
            characters.extend(ExMortal.objects.filter(player=request.user))
            characters.sort(key=lambda x: x.name)
            if profile.cod_st:
                to_approve.extend(Mortal.objects.filter(status__in=["Un", "Sub"]))
            if profile.wod_st:
                to_approve.extend(Character.objects.filter(status__in=["Un", "Sub"]))
            if profile.tc_st:
                to_approve.extend(Human.objects.filter(status__in=["Un", "Sub"]))
            if profile.exalted_st:
                to_approve.extend(ExMortal.objects.filter(status__in=["Un", "Sub"]))
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
