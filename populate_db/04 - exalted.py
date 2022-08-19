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
wise_arrow.add_source("Exalted 3rd Edition", 255)
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
sight_without_eyes.add_source("Exalted 3rd Edition", 255)
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
blood_without_balance.add_source("Exalted 3rd Edition", 256)
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
force_without_fire.add_source("Exalted 3rd Edition", 256)
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
trance_of_unhesitating_speed.add_source("Exalted 3rd Edition", 256)
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
phantom_arrow_technique.add_source("Exalted 3rd Edition", 257)
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
fiery_arrow_attack.add_source("Exalted 3rd Edition", 257)
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
there_is_no_wind.add_source("Exalted 3rd Edition", 257)
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
accuracy_without_distance.add_source("Exalted 3rd Edition", 257)
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
arrow_storm_technique.add_source("Exalted 3rd Edition", 257)
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
flashing_vengeance_draw.add_source("Exalted 3rd Edition", 258)
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
hunters_swift_answer.add_source("Exalted 3rd Edition", 258)
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
immaculate_golden_bow.add_source("Exalted 3rd Edition", 258)
dazzling_flare_attack = SolarCharm.objects.create(
    name="Dazzling Flare Attack",
    mote_cost=3,
    willpower_cost=0,
    ability="archery",
    min_ability=5,
    min_essence=2,
    charm_type="reflexive",
    keywords=["decisive-only"],
    duration="instant",
)
dazzling_flare_attack.prerequisites.add(fiery_arrow_attack)
dazzling_flare_attack.add_source("Exalted 3rd Edition", 258)
seven_omens_shot = SolarCharm.objects.create(
    name="Seven Omens Shot",
    mote_cost=3,
    willpower_cost=1,
    ability="archery",
    min_ability=5,
    min_essence=3,
    charm_type="simple",
    keywords=["decisive-only"],
    duration="instant",
)
seven_omens_shot.prerequisites.add(accuracy_without_distance)
seven_omens_shot.add_source("Exalted 3rd Edition", 258)
revolving_bow_discipline = SolarCharm.objects.create(
    name="Revolving Bow Discipline",
    mote_cost=6,
    willpower_cost=1,
    ability="archery",
    min_ability=5,
    min_essence=3,
    charm_type="simple",
    keywords=["perilous", "withering-only"],
    duration="instant",
)
revolving_bow_discipline.prerequisites.add(arrow_storm_technique)
revolving_bow_discipline.add_source("Exalted 3rd Edition", 258)
finishing_snipe = SolarCharm.objects.create(
    name="Finishing Snipe",
    mote_cost=7,
    willpower_cost=0,
    ability="archery",
    min_ability=5,
    min_essence=3,
    charm_type="reflexive",
    keywords=["decivisive-only"],
    duration="instant",
)
finishing_snipe.prerequisites.add(hunters_swift_answer)
finishing_snipe.add_source("Exalted 3rd Edition", 259)
rain_of_feathered_death = SolarCharm.objects.create(
    name="Rain of Feathered Death",
    mote_cost=3,
    willpower_cost=1,
    ability="archery",
    min_ability=5,
    min_essence=3,
    charm_type="simple",
    keywords=["decisive-only"],
    duration="instant",
)
rain_of_feathered_death.prerequisites.add(phantom_arrow_technique)
rain_of_feathered_death.add_source("Exalted 3rd Edition", 259)
shadow_seeking_arrow = SolarCharm.objects.create(
    name="Shadow-Seeking Arrow",
    mote_cost=3,
    willpower_cost=0,
    initiative_cost=2,
    ability="archery",
    min_ability=5,
    min_essence=3,
    charm_type="reflexive",
    keywords=["uniform"],
    duration="instant",
)
shadow_seeking_arrow.prerequisites.add(dazzling_flare_attack)
shadow_seeking_arrow.add_source("Exalted 3rd Edition", 259)
searing_sunfire_interdiction = SolarCharm.objects.create(
    name="Searing Sunfire Interdiction",
    mote_cost=4,
    willpower_cost=1,
    initiative_cost=1,
    ability="archery",
    min_ability=5,
    min_essence=3,
    charm_type="simple",
    keywords=["decisive-only"],
    duration="instant",
)
searing_sunfire_interdiction.prerequisites.add(dazzling_flare_attack)
searing_sunfire_interdiction.add_source("Exalted 3rd Edition", 259)
solar_spike = SolarCharm.objects.create(
    name="Solar Spike",
    mote_cost=5,
    willpower_cost=1,
    ability="archery",
    min_ability=5,
    min_essence=3,
    charm_type="simple",
    keywords=["decisive-only"],
    duration="instant",
)
solar_spike.prerequisites.add(dazzling_flare_attack)
solar_spike.add_source("Exalted 3rd Edition", 260)
heart_eating_incineration = SolarCharm.objects.create(
    name="Heart-Eating Incineration",
    mote_cost=3,
    anima_cost=3,
    willpower_cost=0,
    ability="archery",
    min_ability=5,
    min_essence=3,
    charm_type="reflexive",
    keywords=["decisive-only"],
    duration="instant",
)
heart_eating_incineration.prerequisites.add(solar_spike)
heart_eating_incineration.add_source("Exalted 3rd Edition", 260)
dust_and_ash_sleight = SolarCharm.objects.create(
    name="Dust and Ash Sleight",
    mote_cost=3,
    willpower_cost=0,
    ability="archery",
    min_ability=5,
    min_essence=4,
    charm_type="reflexive",
    keywords=["decisive-only"],
    duration="instant",
)
dust_and_ash_sleight.prerequisites.add(seven_omens_shot)
dust_and_ash_sleight.add_source("Exalted 3rd Edition", 260)
heavens_crash_down = SolarCharm.objects.create(
    name="Heavens Crash Down",
    mote_cost=6,
    initiative_cost=2,
    willpower_cost=1,
    ability="archery",
    min_ability=5,
    min_essence=4,
    charm_type="reflexive",
    keywords=["clash", "perilous", "withering-only"],
    duration="instant",
)
heavens_crash_down.prerequisites.add(revolving_bow_discipline)
heavens_crash_down.add_source("Exalted 3rd Edition", 260)
streaming_arrow_stance = SolarCharm.objects.create(
    name="Streaming Arrow Stance",
    mote_cost=6,
    willpower_cost=0,
    ability="archery",
    min_ability=5,
    min_essence=4,
    charm_type="simple",
    keywords=[],
    duration="scene",
)
streaming_arrow_stance.prerequisites.add(finishing_snipe)
streaming_arrow_stance.add_source("Exalted 3rd Edition", 261)
whispered_prayer_of_judgment = SolarCharm.objects.create(
    name="Whispered Prayer of Judgment",
    mote_cost=1,
    willpower_cost=0,
    ability="archery",
    min_ability=5,
    min_essence=5,
    charm_type="supplemental",
    keywords=["uniform"],
    duration="instant",
)
whispered_prayer_of_judgment.prerequisites.add(streaming_arrow_stance)
whispered_prayer_of_judgment.add_source("Exalted 3rd Edition", 261)

graceful_crane_stance = SolarCharm.objects.create(
    name="Graceful Crane Stance",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=1,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="scene",
)
monkey_leap_technique = SolarCharm.objects.create(
    name="Monkey Leap Technique",
    mote_cost=2,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=2,
    min_essence=1,
    charm_type="supplemental",
    keywords=[],
    duration="Instant",
)
soaring_crane_leap = SolarCharm.objects.create(
    name="Soaring Crane Leap",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=3,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
soaring_crane_leap.prerequisites.add(monkey_leap_technique)
foe_vaulting_method = SolarCharm.objects.create(
    name="Foe-Vaulting Method",
    mote_cost=0,
    initiative_cost=3,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=2,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
foe_vaulting_method.prerequisites.add(graceful_crane_stance, monkey_leap_technique)
lightning_speed = SolarCharm.objects.create(
    name="Lightning Speed",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=3,
    min_essence=1,
    charm_type="supplemental",
    keywords=[],
    duration="Instant",
)
winning_stride_discipline = SolarCharm.objects.create(
    name="Winning Stride Discipline",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=4,
    min_essence=1,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
winning_stride_discipline.prerequisites.add(lightning_speed)
increasing_strength_exercise = SolarCharm.objects.create(
    name="Increasing Strength Exercise",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=3,
    min_essence=1,
    charm_type="simple",
    keywords=[],
    duration="scene",
)
ten_ox_meditation = SolarCharm.objects.create(
    name="Ten Ox Meditation",
    mote_cost=2,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=1,
    charm_type="supplemental",
    keywords=[],
    duration="feat",
)
ten_ox_meditation.prerequisites.add(increasing_strength_exercise)
thunderbolt_attack_prana = SolarCharm.objects.create(
    name="Thunderbolt Attack Prana",
    mote_cost=4,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="athletics",
    min_ability=3,
    min_essence=1,
    charm_type="supplemental",
    keywords=["decisive-only"],
    duration="Instant",
)
thunderbolt_attack_prana.prerequisites.add(increasing_strength_exercise, monkey_leap_technique)
feather_foot_style = SolarCharm.objects.create(
    name="Feather Foot Style",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=3,
    min_essence=1,
    charm_type="reflexive",
    keywords=["mute"],
    duration="running",
)
feather_foot_style.prerequisites.add(graceful_crane_stance, lightning_speed)
spider_foot_style = SolarCharm.objects.create(
    name="Spider Foot Style",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=4,
    min_essence=1,
    charm_type="reflexive",
    keywords=["mute"],
    duration="turns",
)
spider_foot_style.prerequisites.add(feather_foot_style)
unbound_eagle_approach = SolarCharm.objects.create(
    name="Unbound Eagle Approach",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=4,
    min_essence=2,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
unbound_eagle_approach.prerequisites.add(soaring_crane_leap)
leaping_tiger_attack = SolarCharm.objects.create(
    name="Leaping Tiger Attack",
    mote_cost=4,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="athletics",
    min_ability=5,
    min_essence=2,
    charm_type="supplemental",
    keywords=["dual"],
    duration="Instant",
)
leaping_tiger_attack.prerequisites.add(graceful_crane_stance, lightning_speed)
racing_hare_method = SolarCharm.objects.create(
    name="Racing Hare Method",
    mote_cost=5,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="athletics",
    min_ability=4,
    min_essence=2,
    charm_type="reflexive",
    keywords=[],
    duration="hour",
)
racing_hare_method.prerequisites.add(lightning_speed)
onrush_burst_method = SolarCharm.objects.create(
    name="Onrush Burst Method",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=3,
    min_essence=2,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
onrush_burst_method.prerequisites.add(lightning_speed)
arete_driven_marathon_stride = SolarCharm.objects.create(
    name="Arete-Driven Marathon Stride",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=2,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
arete_driven_marathon_stride.prerequisites.add(winning_stride_discipline)
armor_eating_strike = SolarCharm.objects.create(
    name="Armor-Eating Strike",
    mote_cost=1,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=3,
    min_essence=2,
    charm_type="supplemental",
    keywords=["decisive-only"],
    duration="Instant",
)
armor_eating_strike.prerequisites.add(increasing_strength_exercise)
thunders_might = SolarCharm.objects.create(
    name="Thunder’s Might",
    mote_cost=5,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=2,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
thunders_might.prerequisites.add(increasing_strength_exercise)
mountain_crossing_leap_technique = SolarCharm.objects.create(
    name="Mountain-Crossing Leap Technique",
    mote_cost=7,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="athletics",
    min_ability=5,
    min_essence=3,
    charm_type="simple",
    keywords=[],
    duration="leaping",
)
mountain_crossing_leap_technique.prerequisites.add(unbound_eagle_approach)
eagle_wing_style = SolarCharm.objects.create(
    name="Eagle-Wing Style",
    mote_cost=5,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="athletics",
    min_ability=5,
    min_essence=3,
    charm_type="reflexive",
    keywords=[],
    duration="Indefinite",
)
eagle_wing_style.prerequisites.add(mountain_crossing_leap_technique)
demon_wasting_rush = SolarCharm.objects.create(
    name="Demon-Wasting Rush",
    mote_cost=5,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="athletics",
    min_ability=5,
    min_essence=3,
    charm_type="supplemental",
    keywords=[],
    duration="Instant",
)
demon_wasting_rush.prerequisites.add(racing_hare_method)
hurricane_spirit_speed = SolarCharm.objects.create(
    name="Hurricane Spirit Speed",
    mote_cost=0,
    initiative_cost=1,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=3,
    charm_type="supplemental",
    keywords=[],
    duration="Instant",
)
hurricane_spirit_speed.prerequisites.add(arete_driven_marathon_stride)
godspeed_steps = SolarCharm.objects.create(
    name="Godspeed Steps",
    mote_cost=4,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="athletics",
    min_ability=5,
    min_essence=3,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
godspeed_steps.prerequisites.add(arete_driven_marathon_stride, racing_hare_method)
power_suffusing_form_technique = SolarCharm.objects.create(
    name="Power Suffusing Form Technique",
    mote_cost=4,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=3,
    charm_type="supplemental",
    keywords=[],
    duration="Instant",
)
power_suffusing_form_technique.prerequisites.add(thunders_might)
legion_aurochs_method = SolarCharm.objects.create(
    name="Legion Aurochs Method",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=3,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
legion_aurochs_method.prerequisites.add(power_suffusing_form_technique)
triumph_forged_god_body = SolarCharm.objects.create(
    name="Triumph-Forged God-Body",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=3,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
triumph_forged_god_body.prerequisites.add(arete_driven_marathon_stride, ten_ox_meditation, unbound_eagle_approach)
one_extra_step = SolarCharm.objects.create(
    name="One Extra Step",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=4,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
one_extra_step.prerequisites.add(godspeed_steps)
bonfire_anima_wings = SolarCharm.objects.create(
    name="Bonfire Anima Wings",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=4,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
bonfire_anima_wings.prerequisites.add(eagle_wing_style, onrush_burst_method)
aegis_of_unstoppable_force = SolarCharm.objects.create(
    name="Aegis of Unstoppable Force",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=4,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
aegis_of_unstoppable_force.prerequisites.add(legion_aurochs_method)
living_wind_approach = SolarCharm.objects.create(
    name="Living Wind Approach",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="athletics",
    min_ability=5,
    min_essence=5,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
living_wind_approach.prerequisites.add(one_extra_step)
nine_aeons_thew = SolarCharm.objects.create(
    name="Nine Aeons Thew",
    mote_cost=1,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="athletics",
    min_ability=5,
    min_essence=5,
    charm_type="supplemental",
    keywords=[],
    duration="Instant",
)
nine_aeons_thew.prerequisites.add(aegis_of_unstoppable_force)

sensory_acuity_prana = SolarCharm.objects.create(
    name="Sensory Acuity Prana",
    mote_cost=5,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=2,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="scene",
)
surprise_anticipation_method = SolarCharm.objects.create(
    name="Surprise Anticipation Method",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=3,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
surprise_anticipation_method.prerequisites.add(sensory_acuity_prana)
keen_sight_technique = SolarCharm.objects.create(
    name="Keen Sight Technique",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="awareness",
    min_ability=3,
    min_essence=1,
    charm_type="simple",
    keywords=[],
    duration="scene",
)
keen_sight_technique.prerequisites.add(sensory_acuity_prana)
unswerving_eye_method = SolarCharm.objects.create(
    name="Unswerving Eye Method",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=4,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
unswerving_eye_method.prerequisites.add(keen_sight_technique)
keen_taste_and_smell_technique = SolarCharm.objects.create(
    name="Keen Taste and Smell Technique",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="awareness",
    min_ability=3,
    min_essence=1,
    charm_type="simple",
    keywords=[],
    duration="scene",
)
keen_taste_and_smell_technique.prerequisites.add(sensory_acuity_prana)
genius_palate_summation = SolarCharm.objects.create(
    name="Genius Palate Summation",
    mote_cost=2,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=3,
    min_essence=1,
    charm_type="simple",
    keywords=[],
    duration="Instant",
)
genius_palate_summation.prerequisites.add(keen_taste_and_smell_technique)
foe_scenting_method = SolarCharm.objects.create(
    name="Foe-Scenting Method",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=4,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
foe_scenting_method.prerequisites.add(keen_taste_and_smell_technique)
keen_hearing_and_touch_technique = SolarCharm.objects.create(
    name="Keen Hearing and Touch Technique",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="awareness",
    min_ability=3,
    min_essence=1,
    charm_type="simple",
    keywords=[],
    duration="scene",
)
keen_hearing_and_touch_technique.prerequisites.add(sensory_acuity_prana)
studied_ear_espial = SolarCharm.objects.create(
    name="Studied Ear Espial",
    mote_cost=1,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=3,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
studied_ear_espial.prerequisites.add(keen_hearing_and_touch_technique)
eyeless_harbinger_awareness = SolarCharm.objects.create(
    name="Eyeless Harbinger Awareness",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=3,
    min_essence=1,
    charm_type="reflexive",
    keywords=[],
    duration="scene",
)
eyeless_harbinger_awareness.prerequisites.add(keen_hearing_and_touch_technique)
awakening_eye = SolarCharm.objects.create(
    name="Awakening Eye",
    mote_cost=5,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="awareness",
    min_ability=4,
    min_essence=1,
    charm_type="supplemental",
    keywords=[],
    duration="Instant",
)
# awakening_eye.prerequisites.add(any_two_keen_(sense)_techniques)
inner_eye_focus = SolarCharm.objects.create(
    name="Inner Eye Focus",
    mote_cost=4,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=5,
    min_essence=2,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
inner_eye_focus.prerequisites.add(unswerving_eye_method)
scent_honing_prana = SolarCharm.objects.create(
    name="Scent-Honing Prana",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=5,
    min_essence=2,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
scent_honing_prana.prerequisites.add(foe_scenting_method)
knowing_beyond_silence = SolarCharm.objects.create(
    name="Knowing Beyond Silence",
    mote_cost=2,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=4,
    min_essence=2,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
knowing_beyond_silence.prerequisites.add(studied_ear_espial)
living_pulse_perception = SolarCharm.objects.create(
    name="Living Pulse Perception",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=4,
    min_essence=2,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
living_pulse_perception.prerequisites.add(eyeless_harbinger_awareness)
roused_dragon_detection = SolarCharm.objects.create(
    name="Roused Dragon Detection",
    mote_cost=1,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="awareness",
    min_ability=5,
    min_essence=2,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
roused_dragon_detection.prerequisites.add(knowing_beyond_silence, living_pulse_perception)
unsurpassed_sight_discipline = SolarCharm.objects.create(
    name="Unsurpassed Sight Discipline",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=5,
    min_essence=3,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
unsurpassed_sight_discipline.prerequisites.add(keen_sight_technique)
blink = SolarCharm.objects.create(
    name="Blink",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=1,
    ability="awareness",
    min_ability=5,
    min_essence=3,
    charm_type="reflexive",
    keywords=[],
    duration="Instant",
)
blink.prerequisites.add(inner_eye_focus)
unsurpassed_taste_and_smell_discipline = SolarCharm.objects.create(
    name="Unsurpassed Taste and Smell Discipline",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=5,
    min_essence=3,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
unsurpassed_taste_and_smell_discipline.prerequisites.add(keen_taste_and_smell_technique)
unsurpassed_hearing_and_touch_discipline = SolarCharm.objects.create(
    name="Unsurpassed Hearing and Touch Discipline",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=5,
    min_essence=3,
    charm_type="permanent",
    keywords=[],
    duration="Permanent",
)
unsurpassed_hearing_and_touch_discipline.prerequisites.add(keen_hearing_and_touch_technique)
dedicated_unerring_ear = SolarCharm.objects.create(
    name="Dedicated Unerring Ear",
    mote_cost=3,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="awareness",
    min_ability=5,
    min_essence=4,
    charm_type="reflexive",
    keywords=[],
    duration="Indefinite",
)
dedicated_unerring_ear.prerequisites.add(unsurpassed_hearing_and_touch_discipline)
eye_of_the_unconquered_sun = SolarCharm.objects.create(
    name="Eye of the Unconquered Sun",
    mote_cost=10,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost= 1,
    ability="awareness",
    min_ability=5,
    min_essence=4,
    charm_type="simple",
    keywords=[],
    duration="turn",
)
# eye_of_the_unconquered_sun.prerequisites.add(awakening_eye, any_3_non_excellency_awareness_charms)









x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="brawl",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="bureaucracy",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="craft",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="dodge",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="integrity",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="investigation",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="larceny",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="linguistics",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="lore",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="martial_arts",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="medicine",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="melee",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="occult",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="performance",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)

x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="presence",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)

x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="resistance",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)

x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="",
    min_ability=0,
    min_essence=0,
    charm_type="ride",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)

x = SolarCharm.objects.create(
    name="",
    mote_cost=0,
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="sail",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="socialize",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="stealth",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="survival",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="thrown",
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
    initiative_cost=0,
    anima_cost=0,
    willpower_cost=0,
    ability="war",
    min_ability=0,
    min_essence=0,
    charm_type="",
    keywords=[],
    duration="",
)
x.prerequisites.add()
x.add_source("Exalted 3rd Edition", 228)
