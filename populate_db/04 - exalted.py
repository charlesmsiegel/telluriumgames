from exalted.models.characters.mortals import ExMerit, ExSpecialty
from exalted.models.characters.utils import ABILITIES

ExMerit.objects.create(
    name="Allies", merit_type="story", ratings=[1, 3, 5], merit_class="standard",
)
ExMerit.objects.create(
    name="Ambidextrous", merit_type="innate", ratings=[1, 2], merit_class="standard",
)
ExMerit.objects.create(
    name="Artifact", merit_type="story", ratings=[2, 3, 4, 5], merit_class="standard",
)
ExMerit.objects.create(
    name="Backing", merit_type="story", ratings=[2, 3, 4], merit_class="standard",
)
ExMerit.objects.create(
    name="Boundless Endurance",
    merit_type="purchased",
    ratings=[2],
    merit_class="standard",
    prereqs=[[("stamina", 3)], [("resistance", 3)],],
)
ExMerit.objects.create(
    name="Command", merit_type="story", ratings=[2, 3, 4, 5], merit_class="standard",
)
ExMerit.objects.create(
    name="Contacts", merit_type="story", ratings=[1, 3, 5], merit_class="standard",
)
ExMerit.objects.create(
    name="Cult", merit_type="story", ratings=[1, 2, 3, 4, 5], merit_class="standard",
)
ExMerit.objects.create(
    name="Danger Sense",
    merit_type="innate",
    ratings=[3],
    merit_class="standard",
    prereqs=[[("perception", 3)], [("awareness", 3)],],
)
ExMerit.objects.create(
    name="Demesne", merit_type="story", ratings=[2, 4], merit_class="standard",
)
ExMerit.objects.create(
    name="Direction Sense", merit_type="innate", ratings=[1], merit_class="standard",
)
ExMerit.objects.create(
    name="Eidetic Memory", merit_type="innate", ratings=[2], merit_class="standard",
)
ExMerit.objects.create(
    name="Familiar", merit_type="story", ratings=[1, 2, 3], merit_class="standard",
)
ExMerit.objects.create(
    name="Fast Reflexes",
    merit_type="purchased",
    ratings=[3],
    merit_class="standard",
    prereqs=[[("wits", 3)],],
)
ExMerit.objects.create(
    name="Fleet of Foot",
    merit_type="purchased",
    ratings=[4],
    merit_class="standard",
    prereqs=[[("dexterity", 3)]],
)
ExMerit.objects.create(
    name="Followers", merit_type="story", ratings=[1, 2, 3], merit_class="standard",
)
ExMerit.objects.create(
    name="Giant",
    merit_type="innate",
    ratings=[4],
    merit_class="standard",
    prereqs=[[("stamina", 3)]],
)
ExMerit.objects.create(
    name="Hearthstone", merit_type="story", ratings=[2, 4], merit_class="standard",
)
ExMerit.objects.create(
    name="Hideous", merit_type="innate", ratings=[0], merit_class="standard",
)
ExMerit.objects.create(
    name="Influence", merit_type="story", ratings=[1, 2, 3, 4, 5], merit_class="standard",
)
ExMerit.objects.create(
    name="Iron Stomach",
    merit_type="purchased",
    ratings=[1],
    merit_class="standard",
    prereqs=[[("stamina", 3)], [("resistance", 3)],],
)
ExMerit.objects.create(
    name="Language", merit_type="purchased", ratings=[1], merit_class="standard",
)
ExMerit.objects.create(
    name="Manse", merit_type="story", ratings=[3, 5], merit_class="standard",
)
ExMerit.objects.create(
    name="Mentor", merit_type="story", ratings=[1, 2, 3], merit_class="standard",
)
ExMerit.objects.create(
    name="Martial Artist",
    merit_type="purchased",
    ratings=[4],
    merit_class="standard",
    prereqs=[[("brawl", 1)]],
)
ExMerit.objects.create(
    name="Mighty Thew",
    merit_type="purchased",
    ratings=[1, 2, 3],
    merit_class="standard",
    prereqs=[[("strength", 3)]],
)
ExMerit.objects.create(
    name="Natural Immunity",
    merit_type="innate",
    ratings=[2],
    merit_class="standard",
    prereqs=[[("stamina", 3)]],
)
ExMerit.objects.create(
    name="Pain Tolerance",
    merit_type="purchased",
    ratings=[4],
    merit_class="standard",
    prereqs=[[("resistance", 4)]],
)
ExMerit.objects.create(
    name="Quick Draw",
    merit_type="purchased",
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
ExMerit.objects.create(
    name="Retainers", merit_type="story", ratings=[2, 4], merit_class="standard",
)
ExMerit.objects.create(
    name="Resources", merit_type="story", ratings=[1, 2, 3, 4, 5], merit_class="standard",
)
ExMerit.objects.create(
    name="Selective Conception", merit_type="innate", ratings=[1], merit_class="standard",
)
ExMerit.objects.create(
    name="Strong Lungs",
    merit_type="purchased",
    ratings=[1],
    merit_class="standard",
    prereqs=[[("athletics", 3)]],
)
ExMerit.objects.create(
    name="Toxin Resistance",
    merit_type="purchased",
    ratings=[3],
    merit_class="standard",
    prereqs=[[("stamina", 3)], [("resistance", 3)],],
)
ExMerit.objects.create(
    name="Chameleon", merit_type="innate", ratings=[3], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Claws/Fangs/Hooves/Horns",
    merit_type="innate",
    ratings=[1, 4],
    merit_class="supernatural",
)
ExMerit.objects.create(
    name="Enhanced Sense", merit_type="innate", ratings=[3], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Exalted Healing", merit_type="innate", ratings=[5], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Extra Limbs", merit_type="innate", ratings=[3], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Gills", merit_type="innate", ratings=[0], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Poisoned Body", merit_type="innate", ratings=[1, 2, 5], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Quills", merit_type="innate", ratings=[5], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Subtlety",
    merit_type="innate",
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
ExMerit.objects.create(
    name="Tail", merit_type="innate", ratings=[1, 2], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Thaumaturgist", merit_type="innate", ratings=[4], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Unusual Hide",
    merit_type="innate",
    ratings=[1, 2, 3, 4, 5],
    merit_class="supernatural",
)
ExMerit.objects.create(
    name="Venomous", merit_type="innate", ratings=[3, 4], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Wall Walking", merit_type="innate", ratings=[4], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Wings", merit_type="innate", ratings=[3, 5], merit_class="supernatural",
)

for ability in ABILITIES:
    for i in range(10):
        ExSpecialty.objects.create(
            name=f"{ability.replace('_', ' ').title()} Specialty {i}", ability=ability,
        )
