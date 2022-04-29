from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from accounts.models import Profile
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
            return render(
                request,
                "accounts/index.html",
                {
                    "user": request.user,
                    "username": request.user.username,
                },
            )
        return redirect("/accounts/login/")
