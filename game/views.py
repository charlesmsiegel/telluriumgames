from django.shortcuts import render, redirect
from django.views.generic import DetailView, View

from core.models import LocationModel
from game.models import Chronicle, Story, Scene, Post
from game.forms import StoryCreationForm, SceneCreationForm


# Create your views here.
class ChronicleDetailView(View):
    def get_context(self, pk):
        chronicle = Chronicle.objects.get(pk=pk)
        return {
            "object": chronicle,
            "stories": Story.objects.filter(chronicle=chronicle),
            "form": StoryCreationForm(),
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
        s = Scene.objects.create(
            name=request.POST["name"],
            story=context["object"],
            location=LocationModel.objects.get(pk=request.POST["location"]),
        )
        return redirect(s)


class SceneDetailView(View):
    def get_context(self, pk):
        scene = Scene.objects.get(pk=pk)
        return {"object": scene, "posts": Post.objects.filter(scene=scene)}

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/scene/detail.html", context)
