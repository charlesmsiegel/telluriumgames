from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from tc.models.characters.talent import MomentOfInspiration, Talent, TCGift
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
    template_name = "tc/characters/talent/talent/form.html"


class TalentUpdateView(UpdateView):
    model = Talent
    fields = "__all__"
    template_name = "tc/characters/talent/talent/form.html"


class GiftDetailView(DetailView):
    model = TCGift
    template_name = "tc/characters/talent/gift/detail.html"


class GiftCreateView(CreateView):
    model = TCGift
    fields = "__all__"
    template_name = "tc/characters/talent/gift/form.html"


class GiftUpdateView(UpdateView):
    model = TCGift
    fields = "__all__"
    template_name = "tc/characters/talent/gift/form.html"


class MomentOfInspirationDetailView(DetailView):
    model = MomentOfInspiration
    template_name = "tc/characters/talent/momentofinspiration/detail.html"


class MomentOfInspirationCreateView(CreateView):
    model = Talent
    fields = "__all__"
    template_name = "tc/characters/talent/momentofinspiration/form.html"


class MomentOfInspirationUpdateView(UpdateView):
    model = Talent
    fields = "__all__"
    template_name = "tc/characters/talent/momentofinspiration/form.html"
