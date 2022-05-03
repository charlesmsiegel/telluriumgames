from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from accounts.models import CoDProfile, WoDProfile, TCProfile
from cod.models import Mortal

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
            # TODO: Handle other Profiles
            if cod_profile.storyteller:
                to_approve = Mortal.objects.filter(status__in=["Un", "Sub"])
                xp_requests = []
            else:
                to_approve = []
                xp_requests = []
            return render(
                request,
                "accounts/index.html",
                {
                    "user": request.user,
                    "username": request.user.username,
                    "to_approve": to_approve,
                    "xp_requests": xp_requests,
                },
            )
        return redirect("/accounts/login/")
