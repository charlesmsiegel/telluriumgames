from collections import defaultdict, namedtuple

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from core.utils import level_name, tree_sort
from wod.forms import MageForm, RandomCharacterForm
from wod.models.characters.human import (
    Archetype,
    Character,
    Group,
    Human,
    MeritFlaw,
    MeritFlawRating,
    Specialty,
)
from wod.models.characters.mage import (
    Cabal,
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
    Resonance,
    ResRating,
    Rote,
)
from wod.models.characters.mage.utils import PRIMARY_ABILITIES
from wod.models.characters.werewolf import (
    Camp,
    Charm,
    Gift,
    Pack,
    RenownIncident,
    Rite,
    SpiritCharacter,
    Totem,
    Tribe,
    Werewolf,
)
from wod.models.items.human import Item
from wod.models.items.mage import Grimoire, Library, Wonder
from wod.models.items.werewolf import Fetish
from wod.models.locations.human import City, Location
from wod.models.locations.mage import (
    Chantry,
    Node,
    NodeMeritFlaw,
    NodeMeritFlawRating,
    NodeResonanceRating,
    Sector,
)
from wod.models.locations.werewolf import Caern

EmptyRote = namedtuple("EmptyRote", ["name", "spheres"])
empty_rote = EmptyRote("", "")


# Create your views here.
