import datetime

from django.shortcuts import redirect, render
from django.views.generic import View

from core.models import CharacterModel, ItemModel, LocationModel
from game.forms import AddCharForm, PostForm, SceneCreationForm, StoryCreationForm
from game.models import Chronicle, Post, Scene, Story


# Create your views here.
class ChronicleDetailView(View):
    def get_context(self, pk):
        chronicle = Chronicle.objects.get(pk=pk)
        return {
            "object": chronicle,
            "stories": Story.objects.filter(chronicle=chronicle).order_by("start_date"),
            "form": StoryCreationForm(),
            "characters": CharacterModel.objects.filter(chronicle=chronicle).order_by(
                "name"
            ),
            "locations": LocationModel.objects.filter(chronicle=chronicle).order_by(
                "name"
            ),
            "items": ItemModel.objects.filter(chronicle=chronicle).order_by("name"),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/chronicle/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return redirect(context["object"].add_story(request.POST["name"]))


class StoryDetailView(View):
    def get_context(self, pk):
        story = Story.objects.get(pk=pk)
        return {
            "object": story,
            "scenes": Scene.objects.filter(story=story),
            "form": SceneCreationForm(chronicle=story.chronicle),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/story/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        loc = LocationModel.objects.get(pk=request.POST["location"])
        return redirect(
            context["object"].add_scene(
                request.POST["name"], loc, date_of_scene=request.POST["date_of_scene"]
            )
        )


class SceneDetailView(View):
    def get_context(self, pk, user):
        if not user.is_authenticated:
            user = None
        scene = Scene.objects.get(pk=pk)
        a = AddCharForm(user=user, scene=scene)
        num_chars = (a.fields["character_to_add"].queryset).count()
        return {
            "object": scene,
            "posts": Post.objects.filter(scene=scene),
            "post_form": PostForm(user=user, scene=scene),
            "add_char_form": a,
            "num_chars": num_chars,
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        return render(request, "game/scene/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        if "character_to_add" in request.POST.keys():
            c = CharacterModel.objects.get(pk=request.POST["character_to_add"])
            context["object"].add_character(c)
        elif "close_scene" in request.POST.keys():
            context["object"].close()
        elif "message" in request.POST.keys():
            character = CharacterModel.objects.get(pk=request.POST["character"])
            context["object"].add_post(
                character, request.POST["display_name"], request.POST["message"]
            )
        return render(request, "game/scene/detail.html", context)
