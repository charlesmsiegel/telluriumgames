from exalted.models.characters.mortals import Merit, Specialty
from exalted.models.characters.utils import ABILITIES

Merit.objects.create(
    name="Allies", type="story", ratings=[1, 3, 5], merit_class="standard",
)
Merit.objects.create(
    name="Ambidextrous", type="innate", ratings=[1, 2], merit_class="standard",
)
Merit.objects.create(
    name="Artifact", type="story", ratings=[2, 3, 4, 5], merit_class="standard",
)
Merit.objects.create(
    name="Backing", type="story", ratings=[2, 3, 4], merit_class="standard",
)
Merit.objects.create(
    name="Boundless Endurance",
    type="purchased",
    ratings=[2],
    merit_class="standard",
    prereqs=[[("stamina", 3)], [("resistance", 3)],],
)
Merit.objects.create(
    name="Command", type="story", ratings=[2, 3, 4, 5], merit_class="standard",
)
Merit.objects.create(
    name="Contacts", type="story", ratings=[1, 3, 5], merit_class="standard",
)
Merit.objects.create(
    name="Cult", type="story", ratings=[1, 2, 3, 4, 5], merit_class="standard",
)
Merit.objects.create(
    name="Danger Sense",
    type="innate",
    ratings=[3],
    merit_class="standard",
    prereqs=[[("perception", 3)], [("awareness", 3)],],
)
Merit.objects.create(
    name="Demesne", type="story", ratings=[2, 4], merit_class="standard",
)
Merit.objects.create(
    name="Direction Sense", type="innate", ratings=[1], merit_class="standard",
)
Merit.objects.create(
    name="Eidetic Memory", type="innate", ratings=[2], merit_class="standard",
)
Merit.objects.create(
    name="Familiar", type="story", ratings=[1, 2, 3], merit_class="standard",
)
Merit.objects.create(
    name="Fast Reflexes",
    type="purchased",
    ratings=[3],
    merit_class="standard",
    prereqs=[[("wits", 3)],],
)
Merit.objects.create(
    name="Fleet of Foot",
    type="purchased",
    ratings=[4],
    merit_class="standard",
    prereqs=[[("dexterity", 3)]],
)
Merit.objects.create(
    name="Followers", type="story", ratings=[1, 2, 3], merit_class="standard",
)
Merit.objects.create(
    name="Giant",
    type="innate",
    ratings=[4],
    merit_class="standard",
    prereqs=[[("stamina", 3)]],
)
Merit.objects.create(
    name="Hearthstone", type="story", ratings=[2, 4], merit_class="standard",
)
Merit.objects.create(
    name="Hideous", type="innate", ratings=[0], merit_class="standard",
)
Merit.objects.create(
    name="Influence", type="story", ratings=[1, 2, 3, 4, 5], merit_class="standard",
)
Merit.objects.create(
    name="Iron Stomach",
    type="purchased",
    ratings=[1],
    merit_class="standard",
    prereqs=[[("stamina", 3)], [("resistance", 3)],],
)
Merit.objects.create(
    name="Language", type="purchased", ratings=[1], merit_class="standard",
)
Merit.objects.create(
    name="Manse", type="story", ratings=[3, 5], merit_class="standard",
)
Merit.objects.create(
    name="Mentor", type="story", ratings=[1, 2, 3], merit_class="standard",
)
Merit.objects.create(
    name="Martial Artist",
    type="purchased",
    ratings=[4],
    merit_class="standard",
    prereqs=[[("brawl", 1)]],
)
Merit.objects.create(
    name="Mighty Thew",
    type="purchased",
    ratings=[1, 2, 3],
    merit_class="standard",
    prereqs=[[("strength", 3)]],
)
Merit.objects.create(
    name="Natural Immunity",
    type="innate",
    ratings=[2],
    merit_class="standard",
    prereqs=[[("stamina", 3)]],
)
Merit.objects.create(
    name="Pain Tolerance",
    type="purchased",
    ratings=[4],
    merit_class="standard",
    prereqs=[[("resistance", 4)]],
)
Merit.objects.create(
    name="Quick Draw",
    type="purchased",
    ratings=[1, 4],
    merit_class="standard",
    prereqs=[
        [("archery", 3)],
        [("brawl", 3)],
        [("melee", 3)],
        [("martial_arts", 3)],
        [("thrown", 3)],
    ],
)
Merit.objects.create(
    name="Retainers", type="story", ratings=[2, 4], merit_class="standard",
)
Merit.objects.create(
    name="Resources", type="story", ratings=[1, 2, 3, 4, 5], merit_class="standard",
)
Merit.objects.create(
    name="Selective Conception", type="innate", ratings=[1], merit_class="standard",
)
Merit.objects.create(
    name="Strong Lungs",
    type="purchased",
    ratings=[1],
    merit_class="standard",
    prereqs=[[("athletics", 3)]],
)
Merit.objects.create(
    name="Toxin Resistance",
    type="purchased",
    ratings=[3],
    merit_class="standard",
    prereqs=[[("stamina", 3)], [("resistance", 3)],],
)
Merit.objects.create(
    name="Chameleon", type="innate", ratings=[3], merit_class="supernatural",
)
Merit.objects.create(
    name="Claws/Fangs/Hooves/Horns",
    type="innate",
    ratings=[1, 4],
    merit_class="supernatural",
)
Merit.objects.create(
    name="Enhanced Sense", type="innate", ratings=[3], merit_class="supernatural",
)
Merit.objects.create(
    name="Exalted Healing", type="innate", ratings=[5], merit_class="supernatural",
)
Merit.objects.create(
    name="Extra Limbs", type="innate", ratings=[3], merit_class="supernatural",
)
Merit.objects.create(
    name="Gills", type="innate", ratings=[0], merit_class="supernatural",
)
Merit.objects.create(
    name="Poisoned Body", type="innate", ratings=[1, 2, 5], merit_class="supernatural",
)
Merit.objects.create(
    name="Quills", type="innate", ratings=[5], merit_class="supernatural",
)
Merit.objects.create(
    name="Subtlety",
    type="innate",
    ratings=[2],
    merit_class="supernatural",
    prereqs=[
        [("Claws/Fangs/Hooves/Horns", 1)],
        [("Quills", 1)],
        [("Extra Limbs", 1)],
        [("Tail", 1)],
        [("Unusual Hide", 1)],
        [("Wings", 1)],
    ],
)
Merit.objects.create(
    name="Tail", type="innate", ratings=[1, 2], merit_class="supernatural",
)
Merit.objects.create(
    name="Thaumaturgist", type="innate", ratings=[4], merit_class="supernatural",
)
Merit.objects.create(
    name="Unusual Hide",
    type="innate",
    ratings=[1, 2, 3, 4, 5],
    merit_class="supernatural",
)
Merit.objects.create(
    name="Venomous", type="innate", ratings=[3, 4], merit_class="supernatural",
)
Merit.objects.create(
    name="Wall Walking", type="innate", ratings=[4], merit_class="supernatural",
)
Merit.objects.create(
    name="Wings", type="innate", ratings=[3, 5], merit_class="supernatural",
)

for ability in ABILITIES:
    for i in range(10):
        Specialty.objects.create(
            name=f"{ability.replace('_', ' ').title()} Specialty {i}", ability=ability,
        )
