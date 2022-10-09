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
            "stories": Story.objects.filter(chronicle=chronicle),
            "form": StoryCreationForm(),
            "characters": CharacterModel.objects.filter(chronicle=chronicle),
            "locations": LocationModel.objects.filter(chronicle=chronicle),
            "items": ItemModel.objects.filter(chronicle=chronicle),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/chronicle/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return redirect(context['object'].add_story(request.POST["name"]))


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
        return redirect(context["object"].add_scene(request.POST["name"], loc))


class SceneDetailView(View):
    def get_context(self, pk, user=None):
        scene = Scene.objects.get(pk=pk)
        if user is not None:
            p = PostForm(user=user, scene=scene)
            a = AddCharForm(user=user, scene=scene)
        else:
            p = None
            a = None
        return {
            "object": scene,
            "posts": Post.objects.filter(scene=scene),
            "post_form": p,
            "add_char_form": a,
        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = self.get_context(kwargs["pk"], request.user)
        else:
            context = self.get_context(kwargs["pk"])
        return render(request, "game/scene/detail.html", context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = self.get_context(kwargs["pk"], request.user)
        else:
            context = self.get_context(kwargs["pk"])
        if "character_to_add" in request.POST.keys():
            c = CharacterModel.objects.get(pk=request.POST["character_to_add"])
            context["object"].add_character(c)
        elif "close_scene" in request.POST.keys():
            context["object"].finished = True
            context["object"].save()
        elif "message" in request.POST.keys():
            character = CharacterModel.objects.get(pk=request.POST["character"])
            context["object"].add_post(character, request.POST["display_name"], request.POST["message"])
        return render(request, "game/scene/detail.html", context)
