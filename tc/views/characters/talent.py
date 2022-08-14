from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from tc.models.characters.talent import TCGift, MomentOfInspiration, Talent
from tc.views.characters.human import HumanDetailView


class TalentDetailView(HumanDetailView):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/talent/talent/detail.html", context)

    def get_context(self, pk):
        context = super().get_context(pk=pk)
        return context


class TalentCreateView(CreateView):
    model = Talent
    fields = "__all__"
    template_name = "tc/characters/talent/talent/create.html"


class TalentUpdateView(UpdateView):
    model = Talent
    fields = "__all__"
    template_name = "tc/characters/talent/talent/update.html"


class GiftDetailView(DetailView):
    model = TCGift
    template_name = "tc/characters/talent/gift/detail.html"


class GiftCreateView(CreateView):
    model = TCGift
    fields = "__all__"
    template_name = "tc/characters/talent/gift/create.html"


class GiftUpdateView(UpdateView):
    model = TCGift
    fields = "__all__"
    template_name = "tc/characters/talent/gift/update.html"


class MomentOfInspirationDetailView(DetailView):
    model = MomentOfInspiration
    template_name = "tc/characters/talent/momentofinspiration/detail.html"


class MomentOfInspirationCreateView(CreateView):
    model = Talent
    fields = "__all__"
    template_name = "tc/characters/talent/momentofinspiration/create.html"


class MomentOfInspirationUpdateView(UpdateView):
    model = Talent
    fields = "__all__"
    template_name = "tc/characters/talent/momentofinspiration/update.html"
