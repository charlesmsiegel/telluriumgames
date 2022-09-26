# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View

from accounts.forms import CustomUSerCreationForm
from core.models import CharacterModel, LocationModel, ItemModel
from game.models import Chronicle


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
        char = [x for x in context['to_approve'] if x.name in request.POST.keys()][0]
        char.status = "App"
        char.save()
        context = self.get_context(request.user)
        return render(request, "accounts/index.html", context,)

    def get_context(self, user):
        xp_requests = []

        to_approve = CharacterModel.objects.filter(status__in=["Un", "Sub"])
        chronicles_sted = [
            x for x in Chronicle.objects.all() if user in x.storytellers.all()
        ]
        to_approve = [x for x in to_approve if x.chronicle in chronicles_sted]

        return {
            "user": user,
            "username": user.username,
            "to_approve": to_approve,
            "xp_requests": xp_requests,
            "characters": CharacterModel.objects.filter(owner=user).order_by("name"),
            "locations": LocationModel.objects.filter(owner=user).order_by("name"),
            "items": ItemModel.objects.filter(owner=user).order_by("name"),
        }

