from django.shortcuts import redirect, render
from django.views.generic import View
import datetime

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
        s = Story.objects.create(name=request.POST["name"], chronicle=context["object"])
        return redirect(s)


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
        s = Scene.objects.create(
            name=request.POST["name"], story=context["object"], location=loc, date_played=datetime.date.today()
        )
        s.story.key_locations.add(loc)
        return redirect(s)


class SceneDetailView(View):
    def get_context(self, pk, user):
        scene = Scene.objects.get(pk=pk)
        return {
            "object": scene,
            "posts": Post.objects.filter(scene=scene),
            "post_form": PostForm(user=user, scene=scene),
            "add_char_form": AddCharForm(user=user, scene=scene),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        return render(request, "game/scene/detail.html", context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"], request.user)
        if "character_to_add" in request.POST.keys():
            c = CharacterModel.objects.get(pk=request.POST["character_to_add"])
            if c.npc:
                context["object"].story.key_npcs.add(c)
            else:
                context["object"].story.pcs.add(c)
            context["object"].characters.add(c)
        elif "close_scene" in request.POST.keys():
            context["object"].finished = True
            context["object"].save()
        elif "message" in request.POST.keys():
            character = CharacterModel.objects.get(pk=request.POST["character"])
            if "display_name" != "":
                display_name = character.name
            else:
                display_name = request.POST["display_name"]
            message = request.POST["message"]
            Post.objects.create(
                character=character,
                display_name=display_name,
                message=message,
                scene=context["object"],
            )
        return render(request, "game/scene/detail.html", context)
