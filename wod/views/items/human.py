from django.views.generic import CreateView, DetailView, UpdateView

from wod.models.items.human import WoDItem, MeleeWeapon, RangedWeapon, ThrownWeapon, Weapon


class ItemDetailView(DetailView):
    model = WoDItem
    template_name = "wod/items/human/item/detail.html"


class ItemCreateView(CreateView):
    model = WoDItem
    fields = "__all__"
    template_name = "wod/items/human/item/create.html"


class ItemUpdateView(UpdateView):
    model = WoDItem
    fields = "__all__"
    template_name = "wod/items/human/item/create.html"


class WeaponDetailView(DetailView):
    model = Weapon
    template_name = "wod/items/human/weapon/detail.html"


class WeaponCreateView(CreateView):
    model = Weapon
    fields = "__all__"
    template_name = "wod/items/human/weapon/create.html"


class WeaponUpdateView(UpdateView):
    model = Weapon
    fields = "__all__"
    template_name = "wod/items/human/weapon/create.html"


class MeleeWeaponDetailView(DetailView):
    model = MeleeWeapon
    template_name = "wod/items/human/meleeweapon/detail.html"


class MeleeWeaponCreateView(CreateView):
    model = MeleeWeapon
    fields = "__all__"
    template_name = "wod/items/human/meleeweapon/create.html"


class MeleeWeaponUpdateView(UpdateView):
    model = MeleeWeapon
    fields = "__all__"
    template_name = "wod/items/human/meleeweapon/create.html"


class RangedWeaponDetailView(DetailView):
    model = RangedWeapon
    template_name = "wod/items/human/rangedweapon/detail.html"


class RangedWeaponCreateView(CreateView):
    model = RangedWeapon
    fields = "__all__"
    template_name = "wod/items/human/rangedweapon/create.html"


class RangedWeaponUpdateView(UpdateView):
    model = RangedWeapon
    fields = "__all__"
    template_name = "wod/items/human/rangedweapon/create.html"


class ThrownWeaponDetailView(DetailView):
    model = ThrownWeapon
    template_name = "wod/items/human/thrownweapon/detail.html"


class ThrownWeaponCreateView(CreateView):
    model = ThrownWeapon
    fields = "__all__"
    template_name = "wod/items/human/thrownweapon/create.html"


class ThrownWeaponUpdateView(UpdateView):
    model = ThrownWeapon
    fields = "__all__"
    template_name = "wod/items/human/thrownweapon/create.html"
