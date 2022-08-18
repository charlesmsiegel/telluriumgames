from exalted.models.characters.mortals import ExMerit, ExSpecialty
from exalted.models.characters.solars import SolarCharm
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
    name="Influence",
    merit_type="story",
    ratings=[1, 2, 3, 4, 5],
    merit_class="standard",
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
    name="Resources",
    merit_type="story",
    ratings=[1, 2, 3, 4, 5],
    merit_class="standard",
)
ExMerit.objects.create(
    name="Selective Conception",
    merit_type="innate",
    ratings=[1],
    merit_class="standard",
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
    name="Exalted Healing",
    merit_type="innate",
    ratings=[5],
    merit_class="supernatural",
)
ExMerit.objects.create(
    name="Extra Limbs", merit_type="innate", ratings=[3], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Gills", merit_type="innate", ratings=[0], merit_class="supernatural",
)
ExMerit.objects.create(
    name="Poisoned Body",
    merit_type="innate",
    ratings=[1, 2, 5],
    merit_class="supernatural",
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

wise_arrow = SolarCharm.objects.create(
    name="Wise Arrow",
    mote_cost=1,
    ability="archery",
    min_ability=2,
    min_essence=1,
    charm_type="supplemental",
    keywords=['uniform'],
    duration="instant",
)
wise_arrow.add_source("Exalted 3rd Edition", 225)
sight_without_eyes = SolarCharm.objects.create(
    name="Sight Without Eyes",
    mote_cost=1,
    ability="archery",
    min_ability=3,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="tick",
)
sight_without_eyes.prerequisites.add(wise_arrow)
sight_without_eyes.add_source("Exalted 3rd Edition", 225)
blood_without_balance = SolarCharm.objects.create(
    name="Blood Without Balance",
    mote_cost=3,
    ability="archery",
    min_ability=4,
    min_essence=1,
    charm_type="reflexive",
    keywords=['decisive-only'],
    duration="instant",
)
blood_without_balance.prerequisites.add(sight_without_eyes)
blood_without_balance.add_source("Exalted 3rd Edition", 226)
force_without_fire = SolarCharm.objects.create(
    name="Force Without Fire",
    mote_cost=3,
    ability="archery",
    min_ability=4,
    min_essence=1,
    charm_type="supplemental",
    keywords=['withering-only'],
    duration="instant",
)
force_without_fire.prerequisites.add(sight_without_eyes)
force_without_fire.add_source("Exalted 3rd Edition", 226)
trance_of_unhesitating_speed = SolarCharm.objects.create(
    name="Trance of Unhesitating Speed",
    mote_cost=4,
    willpower_cost=1,
    ability="archery",
    min_ability=3,
    min_essence=1,
    charm_type="simple",
    keywords=["decisive-only"],
    duration="instant",
)
trance_of_unhesitating_speed.prerequisites.add(wise_arrow)
trance_of_unhesitating_speed.add_source("Exalted 3rd Edition", 226)
phantom_arrow_technique = SolarCharm.objects.create(
    name="Phantom Arrow Technique",
    mote_cost=1,
    ability="archery",
    min_ability=3,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="instant",
)
phantom_arrow_technique.add_source("Exalted 3rd Edition", 227)
fiery_arrow_attack = SolarCharm.objects.create(
    name="Fiery Arrow Attack",
    mote_cost=2,
    ability="archery",
    min_ability=4,
    min_essence=1,
    charm_type="supplemental",
    keywords=["decisive-only"],
    duration="instant",
)
fiery_arrow_attack.prerequisites.add(phantom_arrow_technique)
fiery_arrow_attack.add_source("Exalted 3rd Edition", 227)
there_is_no_wind = SolarCharm.objects.create(
    name="There Is No Wing",
    mote_cost=3,
    ability="archery",
    min_ability=5,
    min_essence=2,
    charm_type="reflexive",
    keywords=["dual"],
    duration="instant",
)
there_is_no_wind.prerequisites.add(sight_without_eyes)
there_is_no_wind.add_source("Exalted 3rd Edition", 227)
accuracy_without_distance = SolarCharm.objects.create(
    name="Accuracy Without Distance",
    mote_cost=1,
    willpower_cost=1,
    ability="archery",
    min_ability=5,
    min_essence=2,
    charm_type="reflexive",
    keywords=["decisive-only"],
    duration="instant",
)
accuracy_without_distance.prerequisites.add(force_without_fire)
accuracy_without_distance.add_source("Exalted 3rd Edition", 227)
arrow_storm_technique = SolarCharm.objects.create(
    name="Arrow Storm Technique",
    mote_cost=5,
    willpower_cost=1,
    ability="archery",
    min_ability=5,
    min_essence=2,
    charm_type="simple",
    keywords=["decisive-only"],
    duration="instant",
)
arrow_storm_technique.prerequisites.add(trance_of_unhesitating_speed)
arrow_storm_technique.add_source("Exalted 3rd Edition", 227)
flashing_vengeance_draw = SolarCharm.objects.create(
    name="Flashing Vengeance Draw",
    mote_cost=3,
    willpower_cost=0,
    ability="archery",
    min_ability=5,
    min_essence=2,
    charm_type="supplemental",
    keywords=[],
    duration="instant",
)
flashing_vengeance_draw.prerequisites.add(trance_of_unhesitating_speed)
flashing_vengeance_draw.add_source("Exalted 3rd Edition", 228)
hunters_swift_answer = SolarCharm.objects.create(
    name="Hunter's Swift Answer",
    mote_cost=5,
    willpower_cost=1,
    ability="archery",
    min_ability=5,
    min_essence=2,
    charm_type="reflexive",
    keywords=["uniform"],
    duration="instant",
)
hunters_swift_answer.prerequisites.add(flashing_vengeance_draw)
hunters_swift_answer.add_source("Exalted 3rd Edition", 228)
immaculate_golden_bow = SolarCharm.objects.create(
    name="Immaculate Golden Bow",
    mote_cost=5,
    willpower_cost=1,
    ability="archery",
    min_ability=4,
    min_essence=2,
    charm_type="simple",
    keywords=[],
    duration="scene",
)
immaculate_golden_bow.prerequisites.add(phantom_arrow_technique)
immaculate_golden_bow.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
