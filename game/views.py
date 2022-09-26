from django.shortcuts import render
from django.views.generic import DetailView, View

from game.models import Chronicle, Story, Scene, Post


# Create your views here.
class ChronicleDetailView(View):
    def get_context(self, pk):
        chronicle = Chronicle.objects.get(pk=pk)
        return {
            "object": chronicle,
            "stories": Story.objects.filter(chronicle=chronicle),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/chronicle/detail.html", context)


class StoryDetailView(View):
    def get_context(self, pk):
        story = Story.objects.get(pk=pk)
        return {
            "object": story,
            "scenes": Scene.objects.filter(story=story),
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/story/detail.html", context)


class SceneDetailView(View):
    def get_context(self, pk):
        scene = Scene.objects.get(pk=pk)
        return {"object": scene, "posts": Post.objects.filter(scene=scene)}

    def get(self, request, *args, **kwargs):
        context = self.get_context(kwargs["pk"])
        return render(request, "game/scene/detail.html", context)
