from game.models.chronicle import ObjectType
from tc.models.characters.aberrant import MegaEdge, Power, Tag, Transformation
from tc.models.characters.human import (
    Edge,
    EnhancedEdge,
    PathConnection,
    Specialty,
    TCPath,
    Trick,
)
from tc.models.characters.talent import MomentOfInspiration, TCGift

Specialty.objects.get_or_create(skill="aim", name="Rifle")[0]
Specialty.objects.get_or_create(skill="aim", name="Pistol")[0]
Specialty.objects.get_or_create(skill="aim", name="Bow")[0]
Specialty.objects.get_or_create(skill="aim", name="Specific Weapon")[0]
Specialty.objects.get_or_create(skill="athletics", name="Climbing")[0]
Specialty.objects.get_or_create(skill="athletics", name="Crossfit")[0]
Specialty.objects.get_or_create(skill="athletics", name="Running")[0]
Specialty.objects.get_or_create(skill="athletics", name="Specific Sport")[0]
Specialty.objects.get_or_create(skill="athletics", name="Baseball")[0]
Specialty.objects.get_or_create(skill="athletics", name="Basketball")[0]
Specialty.objects.get_or_create(skill="athletics", name="Hockey")[0]
Specialty.objects.get_or_create(skill="athletics", name="Swimming")[0]
Specialty.objects.get_or_create(skill="close_combat", name="Dirty Tricks")[0]
Specialty.objects.get_or_create(skill="close_combat", name="Martial Art Style")[0]
Specialty.objects.get_or_create(skill="close_combat", name="Aikido")[0]
Specialty.objects.get_or_create(skill="close_combat", name="Boxing")[0]
Specialty.objects.get_or_create(skill="close_combat", name="Krav Maga")[0]
Specialty.objects.get_or_create(skill="close_combat", name="Weapon Type")[0]
Specialty.objects.get_or_create(skill="close_combat", name="Axe")[0]
Specialty.objects.get_or_create(skill="close_combat", name="Baton")[0]
Specialty.objects.get_or_create(skill="close_combat", name="Sword")[0]
Specialty.objects.get_or_create(skill="command", name="Battlefield Tactics")[0]
Specialty.objects.get_or_create(skill="command", name="Bureaucracy")[0]
Specialty.objects.get_or_create(skill="command", name="Military Organization")[0]
Specialty.objects.get_or_create(skill="culture", name="High Society")[0]
Specialty.objects.get_or_create(skill="culture", name="Pop Music")[0]
Specialty.objects.get_or_create(skill="culture", name="Science-Fiction")[0]
Specialty.objects.get_or_create(skill="culture", name="World Religion")[0]
Specialty.objects.get_or_create(skill="empathy", name="Lie Detection")[0]
Specialty.objects.get_or_create(skill="empathy", name="Negotiation")[0]
Specialty.objects.get_or_create(skill="empathy", name="Psychology")[0]
Specialty.objects.get_or_create(skill="enigmas", name="Crime Scene Investigation")[0]
Specialty.objects.get_or_create(skill="enigmas", name="Hacking")[0]
Specialty.objects.get_or_create(skill="enigmas", name="Math")[0]
Specialty.objects.get_or_create(skill="humanities", name="Research")[0]
Specialty.objects.get_or_create(skill="humanities", name="Specific Field")[0]
Specialty.objects.get_or_create(skill="humanities", name="Law")[0]
Specialty.objects.get_or_create(skill="humanities", name="History")[0]
Specialty.objects.get_or_create(skill="humanities", name="Specific Language")[0]
Specialty.objects.get_or_create(skill="integrity", name="Concealing Emotions")[0]
Specialty.objects.get_or_create(skill="integrity", name="Meditation")[0]
Specialty.objects.get_or_create(skill="integrity", name="Resisting Pain")[0]
Specialty.objects.get_or_create(skill="larceny", name="Concealed Weapons")[0]
Specialty.objects.get_or_create(skill="larceny", name="Security Systems")[0]
Specialty.objects.get_or_create(skill="larceny", name="Sneaking")[0]
Specialty.objects.get_or_create(skill="medicine", name="Field of Medicine")[0]
Specialty.objects.get_or_create(skill="medicine", name="First Aid")[0]
Specialty.objects.get_or_create(skill="medicine", name="Surgery")[0]
Specialty.objects.get_or_create(skill="persuasion", name="Fast-Talking")[0]
Specialty.objects.get_or_create(skill="persuasion", name="Interrogation")[0]
Specialty.objects.get_or_create(skill="persuasion", name="Seduction")[0]
Specialty.objects.get_or_create(skill="pilot", name="Dangerous Maneuvers")[0]
Specialty.objects.get_or_create(skill="pilot", name="Specific Terrain")[0]
Specialty.objects.get_or_create(skill="pilot", name="City Streets")[0]
Specialty.objects.get_or_create(skill="pilot", name="Orbit")[0]
Specialty.objects.get_or_create(skill="pilot", name="Underwater")[0]
Specialty.objects.get_or_create(skill="pilot", name="Vehicle Type")[0]
Specialty.objects.get_or_create(skill="pilot", name="Car")[0]
Specialty.objects.get_or_create(skill="pilot", name="Plane")[0]
Specialty.objects.get_or_create(skill="pilot", name="Starship")[0]
Specialty.objects.get_or_create(skill="science", name="Field of Study")[0]
Specialty.objects.get_or_create(skill="science", name="Astronomy")[0]
Specialty.objects.get_or_create(skill="science", name="Chemistry")[0]
Specialty.objects.get_or_create(skill="science", name="Physics")[0]
Specialty.objects.get_or_create(skill="science", name="Fringe Science")[0]
Specialty.objects.get_or_create(skill="science", name="R&D")[0]
Specialty.objects.get_or_create(skill="survival", name="Animal Handling")[0]
Specialty.objects.get_or_create(skill="survival", name="Navigation")[0]
Specialty.objects.get_or_create(skill="survival", name="Tracking")[0]
Specialty.objects.get_or_create(skill="technology", name="Automotive")[0]
Specialty.objects.get_or_create(skill="technology", name="Laser Rifle")[0]
Specialty.objects.get_or_create(skill="technology", name="Supercomputer")[0]
Specialty.objects.get_or_create(skill="technology", name="Electronics")[0]
Specialty.objects.get_or_create(skill="technology", name="Repair Equipment")[0]
Specialty.objects.get_or_create(skill="technology", name="Other Device")[0]

gun_tool = Trick.objects.get_or_create(name="Gun Tool", skill="aim",)[0]
hidden_arsenal = Trick.objects.get_or_create(name="Hidden Arsenal", skill="aim",)[0]
Trick.objects.get_or_create(name="I Wasn't Aiming at You", skill="aim",)[0]
Trick.objects.get_or_create(name="Shoot to Injure", skill="aim",)[0]
Trick.objects.get_or_create(name="It's All in the Reflexes", skill="athletics",)[0]
Trick.objects.get_or_create(name="Mighty Lifter", skill="athletics",)[0]
Trick.objects.get_or_create(name="No Barrier", skill="athletics",)[0]
Trick.objects.get_or_create(name="Physical Actor", skill="athletics",)[0]
Trick.objects.get_or_create(name="Deadly Strike", skill="close_combat",)[0]
Trick.objects.get_or_create(name="Sucker Punch", skill="close_combat",)[0]
Trick.objects.get_or_create(name="Fast Planning", skill="close_combat",)[0]
Trick.objects.get_or_create(name="Inspiring Example", skill="command",)[0]
Trick.objects.get_or_create(name="Motivational Speaker", skill="command",)[0]
Trick.objects.get_or_create(name="Top Dog", skill="command",)[0]
Trick.objects.get_or_create(name="Grain of Truth", skill="culture",)[0]
Trick.objects.get_or_create(name="Members Only", skill="culture",)[0]
Trick.objects.get_or_create(name="That's My Favorite, Too!", skill="culture",)[0]
Trick.objects.get_or_create(name="Cold Reader", skill="empathy",)[0]
Trick.objects.get_or_create(name="Rumor Has It", skill="empathy",)[0]
Trick.objects.get_or_create(name="Six Degrees", skill="empathy",)[0]
Trick.objects.get_or_create(name="The Crack in the Ice", skill="empathy",)[0]
Trick.objects.get_or_create(name="Connecting the Dots", skill="empathy",)[0]
Trick.objects.get_or_create(name="Did the Math", skill="empathy",)[0]
Trick.objects.get_or_create(name="Elite Hacker", skill="enigmas",)[0]
Trick.objects.get_or_create(name="Instant Solution", skill="enigmas",)[0]
Trick.objects.get_or_create(name="Befuddling Jargon", skill="humanities",)[0]
Trick.objects.get_or_create(name="Everything in Context", skill="humanities",)[0]
Trick.objects.get_or_create(name="Legal Authority", skill="humanities",)[0]
Trick.objects.get_or_create(name="Meditative Stance", skill="integrity",)[0]
Trick.objects.get_or_create(name="Poker Face", skill="integrity",)[0]
Trick.objects.get_or_create(name="Strength of Conviction", skill="integrity",)[0]
Trick.objects.get_or_create(name="Tough Nut", skill="integrity",)[0]
Trick.objects.get_or_create(name="Always Have an Exit", skill="larceny",)[0]
Trick.objects.get_or_create(name="Handcuff Houdini", skill="larceny",)[0]
Trick.objects.get_or_create(name="Set a Thief", skill="larceny",)[0]
Trick.objects.get_or_create(name="That Was Already Mine", skill="larceny",)[0]
Trick.objects.get_or_create(name="Diagnostic Expert", skill="medicine",)[0]
Trick.objects.get_or_create(name="Medical Advantage", skill="medicine",)[0]
Trick.objects.get_or_create(name="Quick Aid", skill="medicine",)[0]
Trick.objects.get_or_create(name="Walking Wounded", skill="medicine",)[0]
Trick.objects.get_or_create(name="Captivating Personality", skill="persuasion",)[0]
Trick.objects.get_or_create(name="Devilishly Good Looking", skill="persuasion",)[0]
Trick.objects.get_or_create(name="Easy to Love", skill="persuasion",)[0]
Trick.objects.get_or_create(name="Backseat Driver", skill="pilot",)[0]
Trick.objects.get_or_create(name="Collision Artist", skill="pilot",)[0]
Trick.objects.get_or_create(name="Fighter Pilot", skill="pilot",)[0]
Trick.objects.get_or_create(name="I Can Figure It Out", skill="pilot",)[0]
Trick.objects.get_or_create(name="R&D Expert", skill="science",)[0]
Trick.objects.get_or_create(name="Scientific Method", skill="science",)[0]
Trick.objects.get_or_create(name="Scientific Polymath", skill="science",)[0]
Trick.objects.get_or_create(name="King of Beasts", skill="survival",)[0]
Trick.objects.get_or_create(name="Tricky Situation", skill="survival",)[0]
Trick.objects.get_or_create(name="Versus Wild", skill="survival",)[0]
Trick.objects.get_or_create(name="Without a Trace", skill="survival",)[0]
Trick.objects.get_or_create(name="Ahead of Your Time", skill="technology",)[0]
Trick.objects.get_or_create(name="Engineer's Eye", skill="technology",)[0]
Trick.objects.get_or_create(name="It's Not a Bug, It's a Feature", skill="technology")[
    0
]
Trick.objects.get_or_create(name="Overwatch", skill="technology")[0]

always_prepared = Edge.objects.get_or_create(name="Always Prepared", ratings=[1],)[0]
artistic_talent = Edge.objects.get_or_create(
    name="Artistic Talent", ratings=[1, 2, 3],
)[0]
danger_sense = Edge.objects.get_or_create(name="Danger Sense", ratings=[1],)[0]
direction_sense = Edge.objects.get_or_create(name="Direction Sense", ratings=[1],)[0]
ironwill = Edge.objects.get_or_create(name="Iron Will", ratings=[1, 2, 3],)[0]
library = Edge.objects.get_or_create(name="Library", ratings=[1, 2, 3],)[0]
lightning_calculator = Edge.objects.get_or_create(
    name="Lightning Calculator", ratings=[2],
)[0]
photographic_memory = Edge.objects.get_or_create(
    name="Photographic Memory", ratings=[1, 2, 3],
)[0]
small_unit_tactics = Edge.objects.get_or_create(
    name="Small Unit Tactics", ratings=[2], prereqs=[[("path", 1)]],
)[0]
speed_reading = Edge.objects.get_or_create(
    name="Speed Reading", ratings=[1], prereqs=[[("cunning", 3)]]
)[0]
adrenaline_spike = Edge.objects.get_or_create(name="Adrenaline Spike", ratings=[2],)[0]
ambidextrous = Edge.objects.get_or_create(name="Ambidextrous", ratings=[1],)[0]
breath_control = Edge.objects.get_or_create(name="Breath Control", ratings=[1],)[0]
fast_draw = Edge.objects.get_or_create(
    name="Fast Draw", ratings=[1], prereqs=[[("aim", 1), ("close_combat", 1)]]
)[0]
hair_trigger_reflexes = Edge.objects.get_or_create(
    name="Hair Trigger Reflexes", ratings=[1],
)[0]
keen_sense_sight = Edge.objects.get_or_create(name="Keen Sense (Sight)", ratings=[1],)[
    0
]
keen_sense_hearing = Edge.objects.get_or_create(
    name="Keen Sense (Hearing)", ratings=[1],
)[0]
keen_sense_touch = Edge.objects.get_or_create(name="Keen Sense (Touch)", ratings=[1],)[
    0
]
keen_sense_smell_and_taste = Edge.objects.get_or_create(
    name="Keen Sense (Smell and Taste)", ratings=[1],
)[0]
hardy = Edge.objects.get_or_create(name="Hardy", ratings=[1, 2, 3],)[0]
ms_fix_it = Edge.objects.get_or_create(name="Ms. Fix It", ratings=[2],)[0]
swift = Edge.objects.get_or_create(name="Swift", ratings=[1],)[0]
tough_cookie = Edge.objects.get_or_create(name="Tough Cookie", ratings=[2],)[0]
weak_spots = Edge.objects.get_or_create(name="Weak Spots", ratings=[1],)[0]
alternate_identity = Edge.objects.get_or_create(
    name="Alternate Identity", ratings=[1, 2], prereqs=[[("path", 2)]]
)[0]
animal_ken = Edge.objects.get_or_create(name="Animal Ken", ratings=[1, 2],)[0]
big_hearted = Edge.objects.get_or_create(name="Big Hearted", ratings=[1],)[0]
covert = Edge.objects.get_or_create(
    name="Covert", ratings=[1, 2, 3], prereqs=[[("path", 3)]]
)[0]
fame = Edge.objects.get_or_create(name="Fame", ratings=[1, 2, 3],)[0]
patron = Edge.objects.get_or_create(
    name="Patron", ratings=[1, 2, 3], prereqs=[[("path", 1)]]
)[0]
safe_house = Edge.objects.get_or_create(name="Safe House", ratings=[1],)[0]
skilled_liar = Edge.objects.get_or_create(name="Skilled Liar", ratings=[2],)[0]
striking = Edge.objects.get_or_create(name="Striking", ratings=[2],)[0]
wealth = Edge.objects.get_or_create(name="Wealth", ratings=[1, 2, 3, 4, 5],)[0]
demolitions_training = Edge.objects.get_or_create(
    name="Demolitions Training",
    ratings=[1, 2, 3],
    prereqs=[[("path", 1), ("technology", 1)]],
)[0]
forceful_martial_arts = Edge.objects.get_or_create(
    name="Forceful Martial Arts",
    ratings=[1, 2, 3],
    prereqs=[[("close_combat", 2), ("might", 2)]],
)[0]
free_running = Edge.objects.get_or_create(
    name="Free Running", ratings=[1, 2, 3], prereqs=[[("athletics", 1)]]
)[0]
precise_martial_arts = Edge.objects.get_or_create(
    name="Precise Martial Arts",
    ratings=[1, 2, 3],
    prereqs=[[("dexterity", 2), ("close_combat", 2)]],
)[0]
sniper = Edge.objects.get_or_create(
    name="Sniper",
    ratings=[1, 2, 3],
    prereqs=[[("path", 1), ("resolve", 3), ("aim", 2)]],
)[0]
armor_expert = Edge.objects.get_or_create(
    name="Armor Expert", ratings=[1], prereqs=[[("stamina", 3)]]
)[0]
cool_under_fire = Edge.objects.get_or_create(
    name="Cool Under Fire", ratings=[2], prereqs=[[("integrity", 2)]]
)[0]
deflection_adept = Edge.objects.get_or_create(
    name="Deflection Adept", ratings=[2], prereqs=[[("survival", 2)]]
)[0]
one_against_an_ocean = Edge.objects.get_or_create(
    name="One Against An Ocean", ratings=[2], prereqs=[[("close_combat", 2)]]
)[0]
trick_shooter = Edge.objects.get_or_create(
    name="Trick Shooter", ratings=[3], prereqs=[[("aim", 2)]]
)[0]
waiting_to_greet_the_storm = Edge.objects.get_or_create(
    name="Waiting to Greet the Storm", ratings=[2], prereqs=[[("integrity", 3)]]
)[0]
artifact = Edge.objects.get_or_create(name="Artifact", ratings=[1, 2, 3, 4, 5],)[0]
endurance = Edge.objects.get_or_create(name="Endurance", ratings=[3],)[0]
superior_trait_intellect = Edge.objects.get_or_create(
    name="Superior Trait (Intellect)", ratings=[2]
)[0]
superior_trait_cunning = Edge.objects.get_or_create(
    name="Superior Trait (Cunning)", ratings=[2]
)[0]
superior_trait_resolve = Edge.objects.get_or_create(
    name="Superior Trait (Resolve)", ratings=[2]
)[0]
superior_trait_might = Edge.objects.get_or_create(
    name="Superior Trait (Might)", ratings=[2],
)[0]
superior_trait_dexterity = Edge.objects.get_or_create(
    name="Superior Trait (Dexterity)", ratings=[2]
)[0]
superior_trait_stamina = Edge.objects.get_or_create(
    name="Superior Trait (Stamina)", ratings=[2]
)[0]
superior_trait_presence = Edge.objects.get_or_create(
    name="Superior Trait (Presence)", ratings=[2]
)[0]
superior_trait_manipulation = Edge.objects.get_or_create(
    name="Superior Trait (Manipulation)", ratings=[2]
)[0]
superior_trait_composure = Edge.objects.get_or_create(
    name="Superior Trait (Composure)", ratings=[2]
)[0]

attunement = Edge.objects.get_or_create(name="Attunement", ratings=[1, 2, 3, 4, 5],)[0]
dormancy = Edge.objects.get_or_create(name="Dormancy", ratings=[1, 2],)[0]
eufiber = Edge.objects.get_or_create(name="Eufiber", ratings=[1, 2, 3, 4, 5],)[0]
borrowed_resources = Edge.objects.get_or_create(
    name="Borrowed Resources", ratings=[2], prereqs=[[("path", 1)]]
)[0]
call_for_backup = Edge.objects.get_or_create(
    name="Call For Backup", ratings=[1, 2, 3], prereqs=[[("path", 1)]]
)[0]
chrysalis = Edge.objects.get_or_create(
    name="Chrysalis", ratings=[2], prereqs=[[("path", 1)]]
)[0]
earned_trust = Edge.objects.get_or_create(
    name="Earned Trust", ratings=[1, 2], prereqs=[[("path", 1)]]
)[0]
friends_everywhere = Edge.objects.get_or_create(
    name="Friends Everywhere", ratings=[1, 2], prereqs=[[("path", 1)]]
)[0]
microgravity_training = Edge.objects.get_or_create(
    name="Microgravity Training",
    ratings=[1, 2, 3],
    prereqs=[[("path", 1), ("Direction Sense", 1)]],
)[0]
well_equipped = Edge.objects.get_or_create(
    name="Well-Equipped", ratings=[1, 2], prereqs=[[("path", 1)]]
)[0]
followers = Edge.objects.get_or_create(name="Followers", ratings=[1, 2, 3, 4, 5],)[0]

anonymous = EnhancedEdge.objects.get_or_create(
    name="Anonymous", prereqs=[[("Covert", 3)]]
)[0]
armory = EnhancedEdge.objects.get_or_create(name="Armory", prereqs=[[("Artifact", 5)]])[
    0
]
indomitable = EnhancedEdge.objects.get_or_create(
    name="Indomitable", prereqs=[[("Iron Will", 3)]]
)[0]
loaded = EnhancedEdge.objects.get_or_create(name="Loaded", prereqs=[[("Wealth", 5)]])[0]
respected_authority = EnhancedEdge.objects.get_or_create(
    name="Respected Authority", prereqs=[[("Fame", 3)]]
)[0]
wondrous_item = EnhancedEdge.objects.get_or_create(
    name="Wondrous Item", prereqs=[[("Artifact", 3)]]
)[0]

adventurer = TCPath.objects.get_or_create(
    name="Adventurer",
    type="origin",
    skills=["aim", "athletics", "pilot", "survival"],
    gift_keywords=["might", "pilot", "survival"],
)[0]
adventurer.edges.add(
    breath_control,
    cool_under_fire,
    demolitions_training,
    direction_sense,
    fast_draw,
    free_running,
    hardy,
    swift,
)
adventurer.save()
PathConnection.objects.get_or_create(name="High-risk Hobbyists", path=adventurer)[0]
PathConnection.objects.get_or_create(name="Bomb Disposal Experts", path=adventurer)[0]
PathConnection.objects.get_or_create(name="Travel Enthusiasts", path=adventurer)[0]
life_of_privilege = TCPath.objects.get_or_create(
    name="Life of Privilege",
    type="origin",
    skills=["command", "culture", "integrity", "persuasion"],
    gift_keywords=["presence", "pilot", "survival"],
)[0]
life_of_privilege.edges.add(fame, patron, skilled_liar, wealth)
life_of_privilege.save()
PathConnection.objects.get_or_create(name="School Alumni", path=life_of_privilege)[0]
PathConnection.objects.get_or_create(
    name="College Club Membership", path=life_of_privilege
)[0]
PathConnection.objects.get_or_create(
    name="Local Political Affiliates", path=life_of_privilege
)[0]
military_brat = TCPath.objects.get_or_create(
    name="Military Brat",
    type="origin",
    skills=["command", "enigmas", "integrity", "technology"],
    gift_keywords=["resolve", "integrity", "technology"],
)[0]
military_brat.edges.add(
    adrenaline_spike,
    danger_sense,
    fast_draw,
    ironwill,
    patron,
    small_unit_tactics,
    demolitions_training,
    forceful_martial_arts,
    free_running,
    precise_martial_arts,
    sniper,
)
military_brat.save()
x = PathConnection.objects.get_or_create(name="Past Teacher", path=military_brat)[0]
x = PathConnection.objects.get_or_create(name="Military Commander", path=military_brat)[
    0
]
x = PathConnection.objects.get_or_create(name="Steadfast Friend", path=military_brat)[0]
street_rat = TCPath.objects.get_or_create(
    name="Street Rat",
    type="origin",
    skills=["athletics", "enigmas", "larceny", "survival"],
    gift_keywords=["cunning", "larceny", "survival"],
)[0]
street_rat.edges.add(
    adrenaline_spike,
    alternate_identity,
    always_prepared,
    danger_sense,
    hair_trigger_reflexes,
    hardy,
    ms_fix_it,
    tough_cookie,
)
street_rat.save()
x = PathConnection.objects.get_or_create(name="Street Gangs", path=street_rat)[0]
x = PathConnection.objects.get_or_create(name="Street Mentor", path=street_rat)[0]
x = PathConnection.objects.get_or_create(name="Helpful Family Member", path=street_rat)[
    0
]
x = PathConnection.objects.get_or_create(name="Store Clerks", path=street_rat)[0]
suburbia = TCPath.objects.get_or_create(
    name="Suburbia",
    type="origin",
    skills=["culture", "empathy", "humanities", "technology"],
    gift_keywords=["manipulation", "culture", "empathy"],
)[0]
suburbia.edges.add(artistic_talent, big_hearted, library, patron, wealth)
suburbia.save()
x = PathConnection.objects.get_or_create(name="Favorite Professor", path=suburbia)[0]
x = PathConnection.objects.get_or_create(name="Neighbor Friend", path=suburbia)[0]
x = PathConnection.objects.get_or_create(name="Influential Teacher", path=suburbia)[0]
survivalist = TCPath.objects.get_or_create(
    name="Survivalist",
    type="origin",
    skills=["aim", "close_combat", "medicine", "survival"],
    gift_keywords=["stamina", "medicine", "survival"],
)[0]
survivalist.edges.add(
    always_prepared,
    animal_ken,
    covert,
    direction_sense,
    hardy,
    ironwill,
    keen_sense_sight,
    keen_sense_hearing,
    keen_sense_touch,
    keen_sense_smell_and_taste,
    swift,
)
survivalist.save()
x = PathConnection.objects.get_or_create(name="Park Ranger", path=survivalist)[0]
x = PathConnection.objects.get_or_create(name="Conspiracy Groups", path=survivalist)[0]
x = PathConnection.objects.get_or_create(name="RV Neighborhood", path=survivalist)[0]
charismatic_leader = TCPath.objects.get_or_create(
    name="Charismatic Leader",
    type="role",
    skills=["command", "empathy", "humanities", "persuasion"],
    gift_keywords=["manipulation", "command", "humanities"],
)[0]
charismatic_leader.edges.add(fame, ironwill, skilled_liar, striking, wealth)
charismatic_leader.save()
x = PathConnection.objects.get_or_create(
    name="Corporate Board", path=charismatic_leader
)[0]
x = PathConnection.objects.get_or_create(name="Megachurch", path=charismatic_leader)[0]
x = PathConnection.objects.get_or_create(
    name="Political Allies", path=charismatic_leader
)[0]
combat_specialist = TCPath.objects.get_or_create(
    name="Combat Specialist",
    type="role",
    skills=["aim", "athletics", "close_combat", "integrity"],
    gift_keywords=["might", "aim", "close_combat"],
)[0]
combat_specialist.edges.add(
    alternate_identity,
    armor_expert,
    breath_control,
    fast_draw,
    hair_trigger_reflexes,
    small_unit_tactics,
    trick_shooter,
    weak_spots,
    demolitions_training,
    forceful_martial_arts,
    free_running,
    precise_martial_arts,
    sniper,
)
combat_specialist.save()
x = PathConnection.objects.get_or_create(name="Military Unit", path=combat_specialist,)[
    0
]
x = PathConnection.objects.get_or_create(
    name="Police Officers", path=combat_specialist,
)[0]
x = PathConnection.objects.get_or_create(
    name="Training Master", path=combat_specialist,
)[0]
detective = TCPath.objects.get_or_create(
    name="Detective",
    type="role",
    skills=["aim", "enigmas", "integrity", "persuasion"],
    gift_keywords=["cunning", "aim", "enigmas"],
)[0]
detective.edges.add(
    alternate_identity,
    fast_draw,
    library,
    photographic_memory,
    swift,
    tough_cookie,
    demolitions_training,
    forceful_martial_arts,
    free_running,
    precise_martial_arts,
    sniper,
)
detective.save()
x = PathConnection.objects.get_or_create(name="Police Officers", path=detective)[0]
x = PathConnection.objects.get_or_create(name="Paid Informant", path=detective)[0]
x = PathConnection.objects.get_or_create(name="News Reporter", path=detective)[0]
x = PathConnection.objects.get_or_create(
    name="Friendly Neighborhood Watch", path=detective
)[0]
medical_practitioner = TCPath.objects.get_or_create(
    name="Medical Practitioner",
    type="role",
    skills=["empathy", "medicine", "science", "survival"],
    gift_keywords=["resolve", "medicine", "science"],
)[0]
medical_practitioner.edges.add(
    always_prepared,
    ambidextrous,
    big_hearted,
    ironwill,
    keen_sense_sight,
    keen_sense_hearing,
    keen_sense_touch,
    keen_sense_smell_and_taste,
    library,
    wealth,
)
medical_practitioner.save()
x = PathConnection.objects.get_or_create(name="Surgeon", path=medical_practitioner)[0]
x = PathConnection.objects.get_or_create(name="Pharmacists", path=medical_practitioner)[
    0
]
x = PathConnection.objects.get_or_create(
    name="Thankful Patient", path=medical_practitioner
)[0]
x = PathConnection.objects.get_or_create(name="EMTs", path=medical_practitioner)[0]
pilot_path = TCPath.objects.get_or_create(
    name="Pilot",
    type="role",
    skills=["aim", "close_combat", "pilot", "technology"],
    gift_keywords=["dexterity", "pilot", "technology"],
)[0]
pilot_path.edges.add(
    ambidextrous,
    cool_under_fire,
    demolitions_training,
    direction_sense,
    hair_trigger_reflexes,
    ms_fix_it,
    patron,
    tough_cookie,
)
pilot_path.save()
x = PathConnection.objects.get_or_create(name="Important Client", path=pilot_path)[0]
x = PathConnection.objects.get_or_create(name="Criminal Organization", path=pilot_path)[
    0
]
x = PathConnection.objects.get_or_create(name="Indebted Passenger", path=pilot_path)[0]
sneak = TCPath.objects.get_or_create(
    name="The Sneak",
    type="role",
    skills=["athletics", "enigmas", "larceny", "technology"],
    gift_keywords=["composure", "athletics", "larceny"],
)[0]
sneak.edges.add(
    adrenaline_spike,
    alternate_identity,
    covert,
    free_running,
    photographic_memory,
    skilled_liar,
)
sneak.save()
x = PathConnection.objects.get_or_create(name="Criminal Organization", path=sneak)[0]
x = PathConnection.objects.get_or_create(name="Best Friend", path=sneak)[0]
x = PathConnection.objects.get_or_create(name="Police Insider", path=sneak)[0]
technology_expert = TCPath.objects.get_or_create(
    name="Technology Expert",
    type="role",
    skills=["culture", "enigmas", "science", "technology"],
    gift_keywords=["intellect", "science", "technology"],
)[0]
technology_expert.edges.add(
    demolitions_training,
    library,
    lightning_calculator,
    ms_fix_it,
    patron,
    weak_spots,
    swift,
)
technology_expert.save()
x = PathConnection.objects.get_or_create(
    name="Chop Shop Worker", path=technology_expert
)[0]
x = PathConnection.objects.get_or_create(
    name="Research Scientists", path=technology_expert
)[0]
x = PathConnection.objects.get_or_create(
    name="Machinist Friend", path=technology_expert
)[0]

athlete = TCPath.objects.get_or_create(
    name="Athlete", type="role", skills=["aim", "athletics", "culture", "integrity"]
)[0]
athlete.edges.add(adrenaline_spike, ambidextrous, fame, hardy, swift, wealth)
athlete.save()
x = PathConnection.objects.get_or_create(name="Agent", path=athlete)[0]
x = PathConnection.objects.get_or_create(name="Fans", path=athlete)[0]
x = PathConnection.objects.get_or_create(name="Manager", path=athlete)[0]
x = PathConnection.objects.get_or_create(name="Sports Journalist", path=athlete)[0]
x = PathConnection.objects.get_or_create(name="Teammates", path=athlete)[0]
celebrity = TCPath.objects.get_or_create(
    name="Celebrity",
    type="role",
    skills=["culture", "empathy", "humanities", "persuasion"],
)[0]
celebrity.edges.add(
    artistic_talent,
    big_hearted,
    fame,
    followers,
    patron,
    skilled_liar,
    striking,
    wealth,
)
celebrity.save()
x = PathConnection.objects.get_or_create(name="Fans", path=celebrity)[0]
x = PathConnection.objects.get_or_create(name="Fellow Celebrities", path=celebrity)[0]
x = PathConnection.objects.get_or_create(name="Legal Counsel", path=celebrity)[0]
x = PathConnection.objects.get_or_create(name="Manager", path=celebrity)[0]
x = PathConnection.objects.get_or_create(name="Politicians", path=celebrity)[0]
consultant = TCPath.objects.get_or_create(
    name="Consultant",
    type="role",
    skills=[
        "integrity",
        "persuasion",
        "culture",
        "humanities",
        "medicine",
        "science",
        "technology",
    ],
)[0]
consultant.edges.add(always_prepared, fame, patron, striking, wealth)
consultant.save()
x = PathConnection.objects.get_or_create(name="Academic", path=consultant)[0]
x = PathConnection.objects.get_or_create(name="Corporate Executive", path=consultant)[0]
x = PathConnection.objects.get_or_create(name="Elite Agency", path=consultant)[0]
x = PathConnection.objects.get_or_create(name="Government Official", path=consultant)[0]
x = PathConnection.objects.get_or_create(
    name="Media Agent or Personality", path=consultant
)[0]
x = PathConnection.objects.get_or_create(name="Policy Wonk", path=consultant)[0]
corporate = TCPath.objects.get_or_create(
    name="Corporate",
    type="role",
    skills=["command", "humanities", "integrity", "persuasion"],
)[0]
corporate.edges.add(library, patron, skilled_liar, wealth)
corporate.save()
x = PathConnection.objects.get_or_create(name="Corporate Executives", path=corporate)[0]
x = PathConnection.objects.get_or_create(name="Experts", path=corporate)[0]
x = PathConnection.objects.get_or_create(name="Lawyers", path=corporate)[0]
x = PathConnection.objects.get_or_create(name="Financiers", path=corporate)[0]
x = PathConnection.objects.get_or_create(name="Investors", path=corporate)[0]

aeon_society = TCPath.objects.get_or_create(
    name="&AElig;on Society",
    type="society",
    skills=["humanities", "persuasion", "science", "larceny"],
)[0]
aeon_society.edges.add(
    borrowed_resources,
    earned_trust,
    followers,
    library,
    wealth,
    alternate_identity,
    skilled_liar,
)
aeon_society.save()
x = PathConnection.objects.get_or_create(name="&AElig;on Council", path=aeon_society)[0]
x = PathConnection.objects.get_or_create(name="Project Utopia", path=aeon_society)[0]
x = PathConnection.objects.get_or_create(name="Team Tomorrow", path=aeon_society)[0]
x = PathConnection.objects.get_or_create(
    name="International Relief Agencies", path=aeon_society
)[0]
x = PathConnection.objects.get_or_create(
    name="Allies in Government positions", path=aeon_society
)[0]
x = PathConnection.objects.get_or_create(name="Grateful Citizens", path=aeon_society)[0]
project_utopia = TCPath.objects.get_or_create(
    name="Project Utopia",
    type="society",
    skills=["athletics", "close_combat", "command", "integrity"],
)[0]
project_utopia.edges.add(
    call_for_backup,
    friends_everywhere,
    library,
    small_unit_tactics,
    big_hearted,
    fame,
    patron,
    wealth,
)
project_utopia.save()
x = PathConnection.objects.get_or_create(name="&AElig;on Society", path=project_utopia)[
    0
]
x = PathConnection.objects.get_or_create(name="Project Utopia", path=project_utopia)[0]
x = PathConnection.objects.get_or_create(name="Team Tomorrow", path=project_utopia)[0]
x = PathConnection.objects.get_or_create(
    name="Squad of Peacekeepers", path=project_utopia
)[0]
x = PathConnection.objects.get_or_create(
    name="Doctor from Nova Affairs", path=project_utopia
)[0]
x = PathConnection.objects.get_or_create(name="DeVries Recruiter", path=project_utopia)[
    0
]
teragen = TCPath.objects.get_or_create(
    name="Teragen",
    type="society",
    skills=["command", "culture", "integrity", "persuasion"],
)[0]
teragen.edges.add(
    chrysalis,
    covert,
    eufiber,
    fame,
    followers,
    ironwill,
    patron,
    skilled_liar,
    striking,
    wealth,
)
teragen.save()
x = PathConnection.objects.get_or_create(name="Celebrity Rebel", path=teragen)[0]
x = PathConnection.objects.get_or_create(name="Former Utopian", path=teragen)[0]
x = PathConnection.objects.get_or_create(name="Mystic Seeker", path=teragen)[0]
x = PathConnection.objects.get_or_create(name="Nova Rights Activist", path=teragen)[0]
x = PathConnection.objects.get_or_create(name="Salon Philosopher", path=teragen)[0]
x = PathConnection.objects.get_or_create(name="Would-be Cult Leader", path=teragen)[0]
directive = TCPath.objects.get_or_create(
    name="The Directive",
    type="society",
    skills=["aim", "larceny", "integrity", "technology"],
)[0]
directive.edges.add(
    well_equipped,
    covert,
    always_prepared,
    hair_trigger_reflexes,
    ironwill,
    small_unit_tactics,
    sniper,
)
directive.save()
x = PathConnection.objects.get_or_create(
    name="Government Intelligence Agent", path=directive
)[0]
x = PathConnection.objects.get_or_create(
    name="Law Enforcement Officer", path=directive
)[0]
x = PathConnection.objects.get_or_create(name="Military Special Ops", path=directive)[0]
x = PathConnection.objects.get_or_create(
    name="Scientific or Technical Expert", path=directive
)[0]
elites = TCPath.objects.get_or_create(
    name="Elites",
    type="society",
    skills=["aim", "athletics", "close_combat", "integrity"],
)[0]
elites.edges.add(always_prepared, danger_sense, fame, hardy, small_unit_tactics, wealth)
elites.save()
x = PathConnection.objects.get_or_create(name="Elite Celebrity", path=elites)[0]
x = PathConnection.objects.get_or_create(name="Former Soldier", path=elites)[0]
x = PathConnection.objects.get_or_create(name="Nova Ronin", path=elites)[0]
x = PathConnection.objects.get_or_create(name="Paramilitary Commander", path=elites)[0]
x = PathConnection.objects.get_or_create(name="Security Consultant", path=elites)[0]
daedalus_league = TCPath.objects.get_or_create(
    name="The Daedalus League",
    type="society",
    skills=["athletics", "pilot", "science", "technology"],
)[0]
daedalus_league.edges.add(
    microgravity_training,
    breath_control,
    direction_sense,
    fame,
    hardy,
    keen_sense_sight,
    keen_sense_hearing,
    keen_sense_touch,
    keen_sense_smell_and_taste,
    ms_fix_it,
)
daedalus_league.save()
x = PathConnection.objects.get_or_create(name="Project Utopia", path=daedalus_league)[0]
x = PathConnection.objects.get_or_create(name="NASA", path=daedalus_league)[0]
x = PathConnection.objects.get_or_create(name="ESA", path=daedalus_league)[0]
x = PathConnection.objects.get_or_create(
    name="State or Private Space Agencies", path=daedalus_league
)[0]
x = PathConnection.objects.get_or_create(
    name="Spacesuit Designer", path=daedalus_league
)[0]
x = PathConnection.objects.get_or_create(
    name="Astronomy Hobbyist", path=daedalus_league
)[0]
x = PathConnection.objects.get_or_create(
    name="Astrophysics Professor", path=daedalus_league
)[0]
x = PathConnection.objects.get_or_create(name="Test Pilot", path=daedalus_league)[0]

nine = TCPath.objects.get_or_create(
    name="9",
    type="society",
    skills=["aim", "larceny", "integrity", "technology"],
    gift_keywords=["aim", "larceny", "technology"],
)[0]
nine.edges.add(
    always_prepared, covert, hair_trigger_reflexes, small_unit_tactics, sniper, wealth
)
nine.save()
PathConnection.objects.get_or_create(name="FBI Agent", path=nine)[0]
PathConnection.objects.get_or_create(name="Safe House Owner", path=nine)[0]
PathConnection.objects.get_or_create(name="Weapons Dealer", path=nine)[0]
PathConnection.objects.get_or_create(name="Lab Worker", path=nine)[0]

aeon_society = TCPath.objects.get_or_create(
    name="Aeon Society",
    type="society",
    skills=["aim", "close_combat", "enigmas", "pilot"],
    gift_keywords=["close_combat", "enigmas", "pilot"],
)[0]
aeon_society.edges.add(always_prepared, direction_sense, artifact, library, wealth)
aeon_society.save()
PathConnection.objects.get_or_create(name="High Political Figure", path=aeon_society)[0]
PathConnection.objects.get_or_create(name="Military Advisor", path=aeon_society)[0]
PathConnection.objects.get_or_create(
    name="Large Charity Fund Manager", path=aeon_society
)[0]

archangel = TCPath.objects.get_or_create(
    name="Archangel",
    type="society",
    skills=["close_combat", "empathy", "integrity", "persuasion"],
    gift_keywords=["close_combat", "empathy", "persuasion"],
)[0]
archangel.edges.add(
    adrenaline_spike,
    big_hearted,
    endurance,
    ironwill,
    patron,
    skilled_liar,
    speed_reading,
)
archangel.save()
PathConnection.objects.get_or_create(name="Pro Bono Lawyer", path=archangel)[0]
PathConnection.objects.get_or_create(name="Witness Protection Officer", path=archangel)[
    0
]
PathConnection.objects.get_or_create(name="Homeland Security Officer", path=archangel)[
    0
]
PathConnection.objects.get_or_create(
    name="Criminal with a Heart of Gold", path=archangel
)[0]
PathConnection.objects.get_or_create(name="Hactivist", path=archangel)[0]

global_cartography_initiative = TCPath.objects.get_or_create(
    name="The Global Cartography Initiative",
    type="society",
    skills=["enigmas", "humanities", "larceny", "survival"],
    gift_keywords=["enigmas", "humanities", "survival"],
)[0]
global_cartography_initiative.edges.add(artifact, direction_sense, library, patron)
global_cartography_initiative.save()
PathConnection.objects.get_or_create(
    name="Black Market Artifact Dealer", path=global_cartography_initiative
)[0]
PathConnection.objects.get_or_create(
    name="Smuggler", path=global_cartography_initiative
)[0]
PathConnection.objects.get_or_create(
    name="Museum Curator", path=global_cartography_initiative
)[0]
PathConnection.objects.get_or_create(
    name="Border Guard", path=global_cartography_initiative
)[0]
PathConnection.objects.get_or_create(
    name="Journalist", path=global_cartography_initiative
)[0]
PathConnection.objects.get_or_create(
    name="Mercenery", path=global_cartography_initiative
)[0]
PathConnection.objects.get_or_create(name="Pirate", path=global_cartography_initiative)[
    0
]
PathConnection.objects.get_or_create(
    name="Pirate Hunter", path=global_cartography_initiative
)[0]

neptune_foundation = TCPath.objects.get_or_create(
    name="The Neptune Foundation",
    type="society",
    skills=["command", "integrity", "medicine", "persuasion"],
    gift_keywords=["command", "integrity", "persuasion"],
)[0]
neptune_foundation.edges.add(
    fame,
    ironwill,
    keen_sense_sight,
    keen_sense_hearing,
    keen_sense_touch,
    keen_sense_smell_and_taste,
    patron,
    photographic_memory,
    superior_trait_intellect,
    superior_trait_cunning,
    superior_trait_resolve,
    superior_trait_might,
    superior_trait_dexterity,
    superior_trait_stamina,
    superior_trait_presence,
    superior_trait_manipulation,
    superior_trait_composure,
)
neptune_foundation.save()
PathConnection.objects.get_or_create(name="Aid Worker", path=neptune_foundation)[0]
PathConnection.objects.get_or_create(
    name="Emergency Services", path=neptune_foundation
)[0]
PathConnection.objects.get_or_create(name="ER Doctor", path=neptune_foundation)[0]
PathConnection.objects.get_or_create(
    name="Free-Clinic Volunteer", path=neptune_foundation
)[0]
PathConnection.objects.get_or_create(
    name="Local Government Representative", path=neptune_foundation
)[0]

pharoahs_lightkeepers = TCPath.objects.get_or_create(
    name="The Pharoah's Lightkeepers",
    type="society",
    skills=["aim", "close_combat", "enigmas", "pilot"],
    gift_keywords=["enigmas", "humanities", "larceny"],
)[0]
pharoahs_lightkeepers.edges.add(
    artifact, danger_sense, library, skilled_liar, small_unit_tactics, sniper
)
pharoahs_lightkeepers.save()
PathConnection.objects.get_or_create(name="Journalists", path=pharoahs_lightkeepers)[0]
PathConnection.objects.get_or_create(
    name="Military Personnel", path=pharoahs_lightkeepers
)[0]
PathConnection.objects.get_or_create(
    name="Other Lightkeeper Teams", path=pharoahs_lightkeepers
)[0]
PathConnection.objects.get_or_create(
    name="Police Officers", path=pharoahs_lightkeepers
)[0]


alert_status_1 = TCPath.objects.get_or_create(
    name="Alert Status 1",
    type="society",
    skills=["aim", "enigmas", "persuasion", "technology"],
    gift_keywords=["aim", "persuasion", "technology"],
)[0]
alert_status_1.edges.add(
    alternate_identity,
    armor_expert,
    cool_under_fire,
    covert,
    direction_sense,
    sniper,
    trick_shooter,
)
alert_status_1.save()
PathConnection.objects.get_or_create(name="Committee Member", path=alert_status_1)[0]
PathConnection.objects.get_or_create(
    name="National Intelligence Director", path=alert_status_1
)[0]
PathConnection.objects.get_or_create(
    name="Friendly Agent of a Rival Nation", path=alert_status_1
)[0]

la_revolte_eclatante = TCPath.objects.get_or_create(
    name="La Revolte Eclatante",
    type="society",
    skills=["aim", "medicine", "pilot", "technology"],
    gift_keywords=["aim", "medicine", "pilot"],
)[0]
la_revolte_eclatante.edges.add(
    alternate_identity,
    cool_under_fire,
    demolitions_training,
    safe_house,
    small_unit_tactics,
    swift,
    tough_cookie,
    weak_spots,
)
la_revolte_eclatante.save()
PathConnection.objects.get_or_create(
    name="Idealistic Priests", path=la_revolte_eclatante
)[0]
PathConnection.objects.get_or_create(
    name="Labor Organizers", path=la_revolte_eclatante
)[0]
PathConnection.objects.get_or_create(
    name="Medical Relief Personnel", path=la_revolte_eclatante
)[0]
PathConnection.objects.get_or_create(name="Street Gangs", path=la_revolte_eclatante)[0]
PathConnection.objects.get_or_create(
    name="Violent Anarchists", path=la_revolte_eclatante
)[0]

les_fantomes = TCPath.objects.get_or_create(
    name="Les Fantomes",
    type="society",
    skills=["athletics", "culture", "larceny", "technology"],
    gift_keywords=["athletics", "culture", "larceny"],
)[0]
les_fantomes.edges.add(covert, free_running, safe_house, skilled_liar, wealth)
les_fantomes.save()
PathConnection.objects.get_or_create(name="Fence", path=les_fantomes)[0]
PathConnection.objects.get_or_create(name="Forger", path=les_fantomes)[0]
PathConnection.objects.get_or_create(
    name="Grateful Museum Official", path=les_fantomes
)[0]
PathConnection.objects.get_or_create(
    name="Grudgingly Respectful Interpol Agent", path=les_fantomes
)[0]

noer = TCPath.objects.get_or_create(
    name="National Office of Emergency Research",
    type="society",
    skills=["command", "enigmas", "humanities", "persuasion"],
    gift_keywords=["command", "enigmas", "humanities"],
)[0]
noer.edges.add(
    always_prepared, artifact, covert, patron, small_unit_tactics, speed_reading
)
noer.save()
PathConnection.objects.get_or_create(name="Anonymous Online Source", path=noer)[0]
PathConnection.objects.get_or_create(name="Off-Record Inside Informant", path=noer)[0]
PathConnection.objects.get_or_create(
    name="Paraphysical Research Study Group", path=noer
)[0]
PathConnection.objects.get_or_create(name="UFO Witness", path=noer)[0]

theseus_club = TCPath.objects.get_or_create(
    name="The Theseus Club",
    type="society",
    skills=["aim", "athletics", "larceny", "technology"],
    gift_keywords=["aim", "athletics", "larceny"],
)[0]
theseus_club.edges.add(
    alternate_identity,
    always_prepared,
    endurance,
    danger_sense,
    demolitions_training,
    small_unit_tactics,
    trick_shooter,
)
theseus_club.save()
PathConnection.objects.get_or_create(name="FBI Agent", path=theseus_club)[0]
PathConnection.objects.get_or_create(
    name="Local Hunting-Club President", path=theseus_club
)[0]
PathConnection.objects.get_or_create(name="Wealthy Do-Gooder", path=theseus_club)[0]

transcendant_alliance = TCPath.objects.get_or_create(
    name="The Transcendent Alliance",
    type="society",
    skills=["culture", "medicine", "science", "technology"],
    gift_keywords=["medicine", "science", "technology"],
)[0]
transcendant_alliance.edges.add(
    lightning_calculator,
    ms_fix_it,
    photographic_memory,
    superior_trait_intellect,
    superior_trait_cunning,
    superior_trait_resolve,
    superior_trait_might,
    superior_trait_dexterity,
    superior_trait_stamina,
    superior_trait_presence,
    superior_trait_manipulation,
    superior_trait_composure,
    weak_spots,
    wealth,
)
transcendant_alliance.save()
PathConnection.objects.get_or_create(
    name="Cutting-Edge Scientists", path=transcendant_alliance
)[0]
PathConnection.objects.get_or_create(
    name="Gray-Market Pharmaceutical Manufacturers", path=transcendant_alliance
)[0]
PathConnection.objects.get_or_create(
    name="International Smugglers", path=transcendant_alliance
)[0]
PathConnection.objects.get_or_create(
    name="Skilled Programmers", path=transcendant_alliance
)[0]

triton_foundation = TCPath.objects.get_or_create(
    name="Triton Foundation",
    type="society",
    skills=["enigmas", "medicine", "persuasion", "science"],
    gift_keywords=["medicine", "persuasion", "science"],
)[0]
triton_foundation.edges.add(
    ambidextrous,
    big_hearted,
    ironwill,
    library,
    superior_trait_intellect,
    superior_trait_cunning,
    superior_trait_resolve,
    superior_trait_might,
    superior_trait_dexterity,
    superior_trait_stamina,
    superior_trait_presence,
    superior_trait_manipulation,
    superior_trait_composure,
    wealth,
)
triton_foundation.save()
PathConnection.objects.get_or_create(name="Medical Researcher", path=triton_foundation)[
    0
]
PathConnection.objects.get_or_create(name="Famous Surgeon", path=triton_foundation)[0]
PathConnection.objects.get_or_create(
    name="President of a Charity", path=triton_foundation
)[0]
PathConnection.objects.get_or_create(
    name="Local Public Leader", path=triton_foundation
)[0]
PathConnection.objects.get_or_create(
    name="Dean of a Research College", path=triton_foundation
)[0]

MomentOfInspiration.objects.get_or_create(
    name="Chance Birth",
    attributes=[
        "might",
        "dexterity",
        "stamina",
        "presence",
        "manipulation",
        "composure",
        "intellect",
        "cunning",
        "resolve",
    ],
)[0]
MomentOfInspiration.objects.get_or_create(
    name="Exposure to Flux", attributes=["might", "dexterity", "stamina"]
)[0]
MomentOfInspiration.objects.get_or_create(
    name="Life-Threatening Accidenct", attributes=["stamina"]
)[0]
MomentOfInspiration.objects.get_or_create(
    name="Personal Failure", attributes=["resolve"]
)[0]
MomentOfInspiration.objects.get_or_create(
    name="Saving Someone Else's Life", attributes=["composure"]
)[0]
MomentOfInspiration.objects.get_or_create(
    name="Social Challenge", attributes=["presence", "manipulation", "composure"]
)[0]
MomentOfInspiration.objects.get_or_create(
    name="Sudden Realization", attributes=["cunning"]
)[0]
MomentOfInspiration.objects.get_or_create(
    name="Tragic Loss", attributes=["intellect", "cunning", "resolve"]
)[0]
MomentOfInspiration.objects.get_or_create(name="Violence", attributes=["might"])[0]

TCGift.objects.get_or_create(
    name="A Friend in Every Port", keywords=["constant", "luck"]
)[0]
TCGift.objects.get_or_create(
    name="A Great Memory for Faces", keywords=["constant", "luck"]
)[0]
TCGift.objects.get_or_create(name="Always Connected", keywords=["constant", "luck"])[0]
TCGift.objects.get_or_create(name="Armor of Fate", keywords=["constant", "luck"])[0]
TCGift.objects.get_or_create(
    name="Battlefield Entanglement", keywords=["constant", "luck"]
)[0]
TCGift.objects.get_or_create(name="I Respect You", keywords=["momentary", "luck"])[0]
TCGift.objects.get_or_create(name="Determined Defender", keywords=["constant", "luck"])[
    0
]
TCGift.objects.get_or_create(name="Device Mogul", keywords=["momentary", "luck"])[0]
TCGift.objects.get_or_create(
    name="Don't Scratch the Paint!", keywords=["momentary", "luck"]
)[0]
TCGift.objects.get_or_create(name="Easily Dismissed", keywords=["constant", "luck"])[0]
TCGift.objects.get_or_create(name="Fairweather Friend", keywords=["momentary", "luck"])[
    0
]
TCGift.objects.get_or_create(name="For You", keywords=["momentary", "luck"])[0]
TCGift.objects.get_or_create(
    name="Destined for Damage", keywords=["momentary", "luck"]
)[0]
TCGift.objects.get_or_create(name="Impeccable Timing", keywords=["constant", "luck"])[0]
TCGift.objects.get_or_create(name="Knee Deep in Brass", keywords=["momentary", "luck"])[
    0
]
TCGift.objects.get_or_create(name="Love and Loss", keywords=["momentary", "luck"])[0]
TCGift.objects.get_or_create(name="Navigation Hazard", keywords=["constant", "luck"])[0]
TCGift.objects.get_or_create(name="Roll the Dice", keywords=["momentary", "luck"])[0]
TCGift.objects.get_or_create(name="Name in the Lights", keywords=["constant", "luck"])[
    0
]
TCGift.objects.get_or_create(
    name="Stash in Every City",
    keywords=["momentary", "luck"],
    prereqs=[[("Wealth", 3)]],
)[0]
TCGift.objects.get_or_create(name="Untouchable", keywords=["momentary", "luck"])[0]
TCGift.objects.get_or_create(
    name="Voiding the Warranty", keywords=["momentary", "luck"]
)[0]
TCGift.objects.get_or_create(name="Whodunnit", keywords=["momentary", "luck"])[0]
TCGift.objects.get_or_create(name="X Marks the Spot", keywords=["momentary", "luck"])[0]
TCGift.objects.get_or_create(
    name="Acme of Unchallenged Reason",
    keywords=["intellect", "momentary"],
    prereqs=[[("intellect", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Instant Expert",
    keywords=["intellect", "momentary"],
    prereqs=[[("intellect", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Rosetta Stone",
    keywords=["intellect", "constant"],
    prereqs=[[("humanities", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Apex Cunning", keywords=["cunning", "momentary"], prereqs=[[("cunning", 4)]]
)[0]
TCGift.objects.get_or_create(
    name="Behold the Halo",
    keywords=["cunning", "momentary", "manipulation"],
    prereqs=[[("cunning", 3)], [("manipulation", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Mirrored Sunglasses",
    keywords=["cunning", "constant"],
    prereqs=[[("cunning", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Don't Mess With Me",
    keywords=["composure", "momentary"],
    prereqs=[[("composure", 5)]],
)[0]
TCGift.objects.get_or_create(
    name="Internal Thermostat",
    keywords=["composure", "resolve", "stamina", "constant"],
)[0]
TCGift.objects.get_or_create(
    name="The Late, Late Shift",
    keywords=["composure", "constant", "resolve", "stamina"],
    prereqs=[[("composure", 2)], [("resolve", 2)], [("stamina", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Superlative Poise",
    keywords=["composure", "constant"],
    prereqs=[[("composure", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Fists of Stone", keywords=["might", "constant"], prereqs=[[("might", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Last-Ditch Effort", keywords=["might", "momentary"], prereqs=[[("might", 4)]]
)[0]
TCGift.objects.get_or_create(
    name="Speak Softly", keywords=["might", "constant"], prereqs=[[("might", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Eyes Life a Cat",
    keywords=["dexterity", "constant"],
    prereqs=[[("larceny", 1)]],
)[0]
TCGift.objects.get_or_create(
    name="On the Head of a Pin",
    keywords=["dexterity", "constant"],
    prereqs=[[("dexterity", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Pretty Damned Fast", keywords=["dexterity", "momentary"]
)[0]
TCGift.objects.get_or_create(
    name="Cast-Iron Stomach",
    keywords=["stamina", "constant"],
    prereqs=[[("stamina", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Iron Lungs", keywords=["stamina", "constant"], prereqs=[[("stamina", 2)]]
)[0]
TCGift.objects.get_or_create(
    name="Unrelenting", keywords=["stamina", "momentary"], prereqs=[[("stamina", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Evil Overlord", keywords=["presence", "momentary"], prereqs=[[("command", 2)]]
)[0]
TCGift.objects.get_or_create(
    name="Love Me and Despair",
    keywords=["presence", "constant"],
    prereqs=[[("presence", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="The Room Where It Happens", keywords=["presence", "momentary"]
)[0]
TCGift.objects.get_or_create(
    name="But Before I Die",
    keywords=["manipulation", "momentary"],
    prereqs=[[("manipulation", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Contain the Calamity",
    keywords=["manipulation", "momentary"],
    prereqs=[[("manipulation", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Never a Stranger",
    keywords=["manipulation", "constant"],
    prereqs=[[("manipulation", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Second Chance, First Impression",
    keywords=["manipulation", "momentary"],
    prereqs=[[("manipulation", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Calm Blue Ocean",
    keywords=["resolve", "momentary"],
    prereqs=[[("resolve", 4)]],
)[0]
TCGift.objects.get_or_create(
    name="Indomitable Will",
    keywords=["resolve", "constant", "integrity"],
    prereqs=[[("resolve", 2)], [("integrity", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="An Extension of Myself",
    keywords=["constant", "aim", "close_combat"],
    prereqs=[[("aim", 3)], [("close_combat", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Murderous Totality",
    keywords=["aim", "momentary", "close_combat"],
    prereqs=[[("aim", 3)], [("close_combat", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Sharpshooter", keywords=["momentary", "aim"], prereqs=[[("aim", 4)]]
)[0]
TCGift.objects.get_or_create(name="Steady Hands", keywords=["constant", "aim"])[0]
TCGift.objects.get_or_create(
    name="Trigger Discipline", keywords=["constant", "aim"], prereqs=[[("aim", 2)]]
)[0]
TCGift.objects.get_or_create(
    name="Warrior's Eye", keywords=["momentary", "aim", "close_combat"]
)[0]
TCGift.objects.get_or_create(name="Contortionist", keywords=["constant", "athletics"])[
    0
]
TCGift.objects.get_or_create(
    name="Fight Choreographer",
    keywords=["constant", "athletics", "close_combat"],
    prereqs=[[("athletics", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Lightning Reflexes",
    keywords=["constant", "athletics", "empathy"],
    prereqs=[[("athletics", 2)], [("empathy", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Moving Target",
    keywords=["constant", "athletics"],
    prereqs=[[("athletics", 2)]],
)[0]
TCGift.objects.get_or_create(name="Swan Dive", keywords=["momentary", "athletics"])[0]
TCGift.objects.get_or_create(
    name="Enhanced Impact",
    keywords=["momentary", "close_combat"],
    prereqs=[[("close_combat", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Hidden Advantage",
    keywords=["momentary", "close_combat", "larceny"],
    prereqs=[[("close_combat", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Say That To My Face",
    keywords=["momentary", "close_combat", "command"],
    prereqs=[[("close_combat", 2)], [("command", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="After School Special",
    keywords=["momentary", "command", "persuasion"],
    prereqs=[[("command", 4)], [("persuasion", 4)]],
)[0]
TCGift.objects.get_or_create(
    name="Chess Master", keywords=["momentary", "command"], prereqs=[[("command", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Curses!",
    keywords=["momentary", "command", "persuasion"],
    prereqs=[[("command", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="The In and In",
    keywords=["constant", "command", "larceny"],
    prereqs=[[("larceny", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Public Education",
    keywords=["momentary", "command", "culture", "humanities", "science", "technology"],
    prereqs=[
        [("command", 2), ("culture", 3)],
        [("command", 2), ("humanities", 3)],
        [("command", 2), ("science", 3)],
        [("command", 2), ("technology", 3)],
    ],
)[0]
TCGift.objects.get_or_create(name="Rousing Speech", keywords=["momentary", "command"])[
    0
]
TCGift.objects.get_or_create(
    name="Theatre of Conflict", keywords=["momentary", "command"]
)[0]
TCGift.objects.get_or_create(
    name="Disposable Minion",
    keywords=["momentary", "command"],
    prereqs=[[("command", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Cold Read", keywords=["constant", "culture", "empathy"]
)[0]
TCGift.objects.get_or_create(
    name="Forgettable",
    keywords=["momentary", "culture", "larceny"],
    prereqs=[[("culture", 3)], [("larceny", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Politico", keywords=["momentary", "culture"], prereqs=[[("culture", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="The Right Climate",
    keywords=["momentary", "culture", "empathy"],
    prereqs=[[("culture", 3)], [("empathy", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Ripped From the Headlines", keywords=["constant", "culture"]
)[0]
TCGift.objects.get_or_create(name="That's Bad Luck", keywords=["constant", "culture"])[
    0
]
TCGift.objects.get_or_create(name="The Hook", keywords=["constant", "empathy"])[0]
TCGift.objects.get_or_create(
    name="I Know That Feel",
    keywords=["momentary", "empathy"],
    prereqs=[[("empathy", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Know Thine Enemy",
    keywords=["momentary", "empathy"],
    prereqs=[[("empathy", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Method Actor", keywords=["momentary", "empathy"], prereqs=[[("empathy", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="True Friendship", keywords=["constant", "empathy"], prereqs=[[("empathy", 5)]]
)[0]
TCGift.objects.get_or_create(
    name="Code Talker", keywords=["momentary", "enigmas"], prereqs=[[("enigmas", 2)]]
)[0]
TCGift.objects.get_or_create(
    name="Deep System Scan",
    keywords=["momentary", "enigmas", "technology"],
    prereqs=[[("enigmas", 3)], [("technology", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Fortean Experience",
    keywords=["momentary", "enigmas", "science"],
    prereqs=[[("enigmas", 1), ("science", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Irons in the Fire",
    keywords=[
        "momentary",
        "enigmas",
        "humanities",
        "medicine",
        "science",
        "technology",
    ],
    prereqs=[
        [("enigmas", 3)],
        [("humanities", 3)],
        [("medicine", 3)],
        [("science", 3)],
        [("technology", 3)],
    ],
)[0]
TCGift.objects.get_or_create(
    name="Mystery Archaeology", keywords=["constant", "enigmas"]
)[0]
TCGift.objects.get_or_create(
    name="Plot Twist", keywords=["momentary", "enigmas"], prereqs=[[("enigmas", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Loophole", keywords=["momentary", "humanities"], prereqs=[[("humanities", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="No Stone Unturned", keywords=["constant", "humanities", "science"]
)[0]
TCGift.objects.get_or_create(
    name="Repeating History", keywords=["momentary", "humanities"]
)[0]
TCGift.objects.get_or_create(
    name="Steganographer",
    keywords=["constant", "humanities"],
    prereqs=[[("humanities", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Don't Lie to Me",
    keywords=["constant", "integrity"],
    prereqs=[[("integrity", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Reverse-Engineering Calamity", keywords=["momentary", "integrity"]
)[0]
TCGift.objects.get_or_create(
    name="Self-Sense", keywords=["constant", "integrity", "medicine"]
)[0]
TCGift.objects.get_or_create(
    name="Shameless Lying Smile",
    keywords=["momentary", "integrity", "persuasion"],
    prereqs=[[("integrity", 2)], [("persuasion", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Take it on the Chin", keywords=["momentary", "integrity"]
)[0]
TCGift.objects.get_or_create(
    name="Unquestionable",
    keywords=["momentary", "integrity"],
    prereqs=[[("integrity", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="A Special Present",
    keywords=["momentary", "larceny"],
    prereqs=[[("larceny", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="What Tripwire?", keywords=["momentary", "larceny"], prereqs=[[("larceny", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Listen In", keywords=["momentary", "larceny"], prereqs=[[("larceny", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Nimble-Fingered",
    keywords=["momentary", "larceny"],
    prereqs=[[("larceny", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Slip the Cuffs",
    keywords=["momentary", "larceny", "technology"],
    prereqs=[[("larceny", 2)], [("technology", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Doctor of Destruction",
    keywords=["constant", "aim", "close_combat", "medicine"],
    prereqs=[[("medicine", 4)]],
)[0]
TCGift.objects.get_or_create(
    name="Home-Cooked Meal",
    keywords=["constant", "medicine"],
    prereqs=[[("medicine", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Instant Diagnosis",
    keywords=["momentary", "medicine"],
    prereqs=[[("medicine", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Shot Caller",
    keywords=["momentary", "aim", "close_combat", "medicine"],
    prereqs=[[("medicine", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Worse Than It Looks",
    keywords=["momentary", "medicine"],
    prereqs=[[("medicine", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Disarming Candor", keywords=["momentary", "persuasion"]
)[0]
TCGift.objects.get_or_create(
    name="I'm On The List",
    keywords=["momentary", "persuasion"],
    prereqs=[[("persuasion", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Scathing Insult",
    keywords=["constant", "persusion"],
    prereqs=[[("persuasion", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Steely Gaze",
    keywords=["momentary", "persuasion", "manipulation", "composure"],
    prereqs=[
        [("persuasion", 2), ("presence", 3)],
        [("persuasion", 2), ("manipulation", 3)],
        [("persuasion", 2), ("composure", 3)],
    ],
)[0]
TCGift.objects.get_or_create(
    name="Daredevil", keywords=["momentary", "pilot"], prereqs=[[("pilot", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Greased Lightning", keywords=["momentary", "pilot"], prereqs=[[("pilot", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Head 'Em Off At The Pass", keywords=["constant", "pilot"]
)[0]
TCGift.objects.get_or_create(
    name="Look Ma, No Hands!", keywords=["momentary", "pilot"], prereqs=[[("pilot", 3)]]
)[0]
TCGift.objects.get_or_create(
    name="Wheelman", keywords=["constant", "pilot"], prereqs=[[("pilot", 2)]]
)[0]
TCGift.objects.get_or_create(
    name="Eureka!", keywords=["constant", "science"], prereqs=[[("science", 3)]]
)[0]
TCGift.objects.get_or_create(name="Discovery Rush", keywords=["momentary", "science"])[
    0
]
TCGift.objects.get_or_create(
    name="Blind Spots", keywords=["constant", "survival"], prereqs=[[("survival", 2)]]
)[0]
TCGift.objects.get_or_create(
    name="Get the Drop", keywords=["momentary", "survival"], prereqs=[[("survival", 2)]]
)[0]
TCGift.objects.get_or_create(
    name="Internal Compass", keywords=["constant", "survival"]
)[0]
TCGift.objects.get_or_create(
    name="Know Your Quarry",
    keywords=["momentary", "survival"],
    prereqs=[[("survival", 2)]],
)[0]
TCGift.objects.get_or_create(
    name="Savage Beast", keywords=["momentary", "survival"], prereqs=[[("survival", 2)]]
)[0]
TCGift.objects.get_or_create(
    name="Through Wild Eyes", keywords=["momentary", "survival"]
)[0]
TCGift.objects.get_or_create(
    name="Whisperer", keywords=["constant", "survival"], prereqs=[[("survival", 2)]]
)[0]
TCGift.objects.get_or_create(
    name="Wilderness Guide",
    keywords=["momentary", "survival"],
    prereqs=[[("survival", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Cut the Red Wire", keywords=["momentary", "technology"]
)[0]
TCGift.objects.get_or_create(
    name="Digital Crackerjack", keywords=["momentary", "technology"]
)[0]
TCGift.objects.get_or_create(
    name="Quick Fix",
    keywords=["momentary", "technology"],
    prereqs=[[("technology", 3)]],
)[0]
TCGift.objects.get_or_create(
    name="Sawed Off",
    keywords=["momentary", "technology"],
    prereqs=[[("technology", 3)]],
)[0]

accuracy = MegaEdge.objects.get_or_create(
    name="Accuracy", ratings=[1, 2, 3, 4, 5], prereqs=[[("mega_dexterity", 2)]]
)[0]
adaptation = MegaEdge.objects.get_or_create(
    name="Adaptation", ratings=[1], prereqs=[[("mega_stamina", 2)]]
)[0]
x = MegaEdge.objects.get_or_create(name="Animal Mastery", ratings=[1, 2],)[0]
x = MegaEdge.objects.get_or_create(name="Body Modification", ratings=[1, 2, 3, 4, 5],)[
    0
]
calming_composure = MegaEdge.objects.get_or_create(
    name="Calming Composure", ratings=[1], prereqs=[[("mega_composure", 1)]]
)[0]
compelling_presence = MegaEdge.objects.get_or_create(
    name="Compelling Presence", ratings=[2], prereqs=[[("mega_presence", 2)]]
)[0]
defense = MegaEdge.objects.get_or_create(
    name="Defense",
    ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    prereqs=[[("mega_cunning", 1), ("mega_dexterity", 1)]],
)[0]
dense_flesh = MegaEdge.objects.get_or_create(
    name="Dense Flesh",
    ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    prereqs=[[("mega_stamina", 1)]],
)[0]
detection = MegaEdge.objects.get_or_create(
    name="Detection", ratings=[1, 2, 3, 4, 5], prereqs=[[("mega_cunning", 1)]]
)[0]
digital_manipulation = MegaEdge.objects.get_or_create(
    name="Digital Manipulation",
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("mega_intellect", 1)]],
)[0]
digital_scan = MegaEdge.objects.get_or_create(
    name="Digital Scan", ratings=[1], prereqs=[[("mega_cunning", 1)]]
)[0]
dreadful_presence = MegaEdge.objects.get_or_create(
    name="Dreadful Presence", ratings=[1], prereqs=[[("mega_presence", 1)]]
)[0]
fast_worker = MegaEdge.objects.get_or_create(
    name="Fast Worker", ratings=[2], prereqs=[[("mega_resolve", 1)]]
)[0]
foresight = MegaEdge.objects.get_or_create(
    name="Foresight",
    ratings=[1],
    prereqs=[[("mega_cunning", 1), ("mega_intellect", 1)]],
)[0]
x = MegaEdge.objects.get_or_create(name="Homunculus", ratings=[1],)[0]
hypnotic_presence = MegaEdge.objects.get_or_create(
    name="Hypnotic Presence", ratings=[1], prereqs=[[("mega_manipulation", 1)]]
)[0]
immediate_connection = MegaEdge.objects.get_or_create(
    name="Immediate Connection", ratings=[1], prereqs=[[("mega_presence", 1)]]
)[0]
immunity = MegaEdge.objects.get_or_create(
    name="Immunity", ratings=[1], prereqs=[[("mega_stamina", 1)]]
)[0]
instant_expert = MegaEdge.objects.get_or_create(
    name="Instant Expert", ratings=[1], prereqs=[[("mega_intellect", 1)]]
)[0]
instant_influence = MegaEdge.objects.get_or_create(
    name="Instant Influence",
    ratings=[1],
    prereqs=[[("mega_presence", 1), ("mega_manipulation", 1)]],
)[0]
inventor = MegaEdge.objects.get_or_create(
    name="Inventor", ratings=[2], prereqs=[[("mega_intellect", 1)]]
)[0]
mass_influence = MegaEdge.objects.get_or_create(
    name="Mass Influence",
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("mega_manipulation", 1), ("mega_presence", 1)]],
)[0]
mastermind = MegaEdge.objects.get_or_create(
    name="Mastermind", ratings=[1], prereqs=[[("mega_intellect", 1)]]
)[0]
mega_crush = MegaEdge.objects.get_or_create(
    name="Mega-Crush", ratings=[1], prereqs=[[("mega_might", 1)]]
)[0]
mega_hearing = MegaEdge.objects.get_or_create(
    name="Mega-Hearing", ratings=[1], prereqs=[[("mega_cunning", 1)]]
)[0]
mega_lifting = MegaEdge.objects.get_or_create(
    name="Mega-Lifting", ratings=[1], prereqs=[[("mega_might", 1)]]
)[0]
mega_scent = MegaEdge.objects.get_or_create(
    name="Mega-Scent", ratings=[1], prereqs=[[("mega_cunning", 1)]]
)[0]
mega_speed = MegaEdge.objects.get_or_create(
    name="Mega-Speed", ratings=[1], prereqs=[[("mega_dexterity", 1)]]
)[0]
mega_vision = MegaEdge.objects.get_or_create(
    name="Mega-Vision", ratings=[1], prereqs=[[("mega_cunning", 1)]]
)[0]
micro_manipulation = MegaEdge.objects.get_or_create(
    name="Micro-Manipulation", ratings=[1], prereqs=[[("mega_cunning", 1)]]
)[0]
mind_over_matter = MegaEdge.objects.get_or_create(
    name="Mind Over Matter", ratings=[1], prereqs=[[("mega_resolve", 1)]]
)[0]
x = MegaEdge.objects.get_or_create(name="Movement Mode", ratings=[1, 2, 3, 4, 5],)[0]
multitasking = MegaEdge.objects.get_or_create(
    name="Multitasking",
    ratings=[1],
    prereqs=[[("mega_dexterity", 1), ("mega_cunning", 1)]],
)[0]
overwhelming_denial = MegaEdge.objects.get_or_create(
    name="Overwhelming Denial",
    ratings=[1],
    prereqs=[[("mega_composure", 1), ("Dreadful Presence", 1)]],
)[0]
perfectionist = MegaEdge.objects.get_or_create(
    name="Perfectionist", ratings=[2], prereqs=[[("mega_intellect", 1)]]
)[0]
pretercognition = MegaEdge.objects.get_or_create(
    name="Pretercognition", ratings=[1], prereqs=[[("mega_cunning", 1)]]
)[0]
prodigy_aim = MegaEdge.objects.get_or_create(
    name="Prodigy (Aim)", ratings=[1], prereqs=[[("aim", 1)]]
)[0]
prodigy_athletics = MegaEdge.objects.get_or_create(
    name="Prodigy (Athletics)", ratings=[1], prereqs=[[("athletics", 1)]]
)[0]
prodigy_close_combat = MegaEdge.objects.get_or_create(
    name="Prodigy (Close Combat)", ratings=[1], prereqs=[[("close_combat", 1)]]
)[0]
prodigy_command = MegaEdge.objects.get_or_create(
    name="Prodigy (Command)", ratings=[1], prereqs=[[("command", 1)]]
)[0]
prodigy_culture = MegaEdge.objects.get_or_create(
    name="Prodigy (Culture)", ratings=[1], prereqs=[[("culture", 1)]]
)[0]
prodigy_empathy = MegaEdge.objects.get_or_create(
    name="Prodigy (Empathy)", ratings=[1], prereqs=[[("empathy", 1)]]
)[0]
prodigy_enigmas = MegaEdge.objects.get_or_create(
    name="Prodigy (Enigmas)", ratings=[1], prereqs=[[("enigmas", 1)]]
)[0]
prodigy_humanities = MegaEdge.objects.get_or_create(
    name="Prodigy (Humanities)", ratings=[1], prereqs=[[("humanities", 1)]]
)[0]
prodigy_integrity = MegaEdge.objects.get_or_create(
    name="Prodigy (Integrity)", ratings=[1], prereqs=[[("integrity", 1)]]
)[0]
prodigy_larceny = MegaEdge.objects.get_or_create(
    name="Prodigy (Larceny)", ratings=[1], prereqs=[[("larceny", 1)]]
)[0]
prodigy_medicine = MegaEdge.objects.get_or_create(
    name="Prodigy (Medicine)", ratings=[1], prereqs=[[("medicine", 1)]]
)[0]
prodigy_persuasion = MegaEdge.objects.get_or_create(
    name="Prodigy (Persuasion)", ratings=[1], prereqs=[[("persuasion", 1)]]
)[0]
prodigy_pilot = MegaEdge.objects.get_or_create(
    name="Prodigy (Pilot)", ratings=[1], prereqs=[[("pilot", 1)]]
)[0]
prodigy_science = MegaEdge.objects.get_or_create(
    name="Prodigy (Science)", ratings=[1], prereqs=[[("science", 1)]]
)[0]
prodigy_survival = MegaEdge.objects.get_or_create(
    name="Prodigy (Survival)", ratings=[1], prereqs=[[("survival", 1)]]
)[0]
prodigy_technology = MegaEdge.objects.get_or_create(
    name="Prodigy (Technology)", ratings=[1], prereqs=[[("technology", 1)]]
)[0]
prolific = MegaEdge.objects.get_or_create(
    name="Prolific", ratings=[1, 2, 3, 4, 5], prereqs=[[("mega_cunning", 2)]]
)[0]
q_tech = MegaEdge.objects.get_or_create(
    name="Q-Tech", ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],
)[0]
quantum_conversion = MegaEdge.objects.get_or_create(
    name="Quantum Conversion", ratings=[1],
)[0]
quantum_leap = MegaEdge.objects.get_or_create(
    name="Quantum Leap", ratings=[1], prereqs=[[("mega_might", 2)]]
)[0]
x = MegaEdge.objects.get_or_create(name="Quantum Sense", ratings=[1],)[0]
quickness = MegaEdge.objects.get_or_create(
    name="Quickness", ratings=[1], prereqs=[[("mega_dexterity", 1)]]
)[0]
rapid_strike = MegaEdge.objects.get_or_create(
    name="Rapid Strike",
    ratings=[1],
    prereqs=[[("mega_dexterity", 1), ("mega_cunning", 1)]],
)[0]
regeneration = MegaEdge.objects.get_or_create(
    name="Regeneration",
    ratings=[1],
    prereqs=[[("mega_stamina", 1), ("mega_resolve", 1)]],
)[0]
resourceful = MegaEdge.objects.get_or_create(
    name="Resourceful", ratings=[2], prereqs=[[("mega_cunning", 2)]]
)[0]
revealing_composure = MegaEdge.objects.get_or_create(
    name="Revealing Composure", ratings=[1], prereqs=[[("mega_composure", 1)]]
)[0]
revealing_read = MegaEdge.objects.get_or_create(
    name="Revealing Read", ratings=[1], prereqs=[[("mega_cunning", 1)]]
)[0]
spectrum_vision = MegaEdge.objects.get_or_create(
    name="Spectrum Vision", ratings=[1], prereqs=[[("Mega Vision", 1)]]
)[0]
scanning_sense = MegaEdge.objects.get_or_create(
    name="Scanning Sense", ratings=[1, 2, 3], prereqs=[[("Spectrum Vision", 1)]]
)[0]
sensory_shield = MegaEdge.objects.get_or_create(
    name="Sensory Shield",
    ratings=[1],
    prereqs=[[("mega_cunning", 1), ("mega_resolve", 1), ("mega_stamina", 1)]],
)[0]
shockwave = MegaEdge.objects.get_or_create(
    name="Shockwave", ratings=[1], prereqs=[[("mega_might", 1)]]
)[0]
subtle_presence = MegaEdge.objects.get_or_create(
    name="Subtle Presence", ratings=[1], prereqs=[[("mega_composure", 1)]]
)[0]
telecommunication = MegaEdge.objects.get_or_create(
    name="Telecommunication", ratings=[1],
)[0]
technique = MegaEdge.objects.get_or_create(
    name="Technique", ratings=[1, 2, 3, 4, 5], prereqs=[[("quantum", "dots")]]
)[0]
technologist = MegaEdge.objects.get_or_create(
    name="Technologist", ratings=[2], prereqs=[[("mega_resolve", 1)]]
)[0]
telepresence = MegaEdge.objects.get_or_create(
    name="Telepresence", ratings=[1], prereqs=[[("Mass Influence", 3)]]
)[0]
thunderclap = MegaEdge.objects.get_or_create(
    name="Thunderclap", ratings=[1], prereqs=[[("mega_might", 1)]]
)[0]
toughness = MegaEdge.objects.get_or_create(
    name="Toughness",
    ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    prereqs=[[("quantum", "dots")]],
)[0]
ultraperipheral_perception = MegaEdge.objects.get_or_create(
    name="Ultraperipherial Perception", ratings=[1], prereqs=[[("mega_cunning", 1)]]
)[0]
universal_translator = MegaEdge.objects.get_or_create(
    name="Universal Translator", ratings=[1], prereqs=[[("mega_intellect", 3)]]
)[0]

absorption = Power.objects.get_or_create(
    name="Absorption",
    quantum_minimum=2,
    action_type="reflexive",
    cost=0,
    dicepool="Quantum+Power",
    range="personal",
    duration="continuous",
)[0]
broad = Tag.objects.get_or_create(name="Broad", ratings=[2],)[0]
broad.permitted_powers.add(absorption)
broad.save()
siphon = Tag.objects.get_or_create(name="Siphon", ratings=[1],)[0]
siphon.permitted_powers.add(absorption)
siphon.save()
boost = Power.objects.get_or_create(
    name="Boost",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=2,
    dicepool="",
    range="personal",
    duration="continuous",
)[0]
extra_attribute = Tag.objects.get_or_create(name="Extra Attribute", ratings=[1],)[0]
extra_attribute.permitted_powers.add(boost)
extra_attribute.save()
variable_attribute = Tag.objects.get_or_create(name="Variable Attribute", ratings=[1],)[
    0
]
variable_attribute.permitted_powers.add(boost)
variable_attribute.save()
cloak = Power.objects.get_or_create(
    name="Cloak",
    quantum_minimum=2,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="maintained",
)[0]
chemical = Tag.objects.get_or_create(name="Chemical", ratings=[1],)[0]
chemical.permitted_powers.add(cloak)
chemical.save()
density = Power.objects.get_or_create(
    name="Density",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)[0]
non_living = Tag.objects.get_or_create(name="Non-Living", ratings=[1],)[0]
non_living.permitted_powers.add(density)
non_living.save()
elemental_mastery = Power.objects.get_or_create(
    name="Elemental Mastery",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=0,
    dicepool="",
    range="personal",
    duration="instantaneous",
)[0]
environmental_anima = Power.objects.get_or_create(
    name="Environmental Anima",
    quantum_minimum=-1,
    action_type="ordinary",
    cost=1,
    dicepool="",
    range="medium",
    duration="maintained",
)[0]
continuous = Tag.objects.get_or_create(name="Continuous", ratings=[1],)[0]
continuous.permitted_powers.add(environmental_anima)
continuous.save()
non_terrestrial = Tag.objects.get_or_create(name="Non-Terrestrial", ratings=[1],)[0]
non_terrestrial.permitted_powers.add(environmental_anima)
non_terrestrial.save()
flight = Power.objects.get_or_create(
    name="Flight",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=2,
    dicepool="",
    range="personal",
    duration="maintained",
)[0]
surfing = Tag.objects.get_or_create(name="Surfing", ratings=[-1],)[0]
surfing.permitted_powers.add(flight)
surfing.save()
growth = Power.objects.get_or_create(
    name="Growth",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)[0]
healing = Power.objects.get_or_create(
    name="Healing",
    quantum_minimum=2,
    action_type="ordinary",
    cost=1,
    dicepool="Quantum+Power",
    range="close",
    duration="instantaneous",
)[0]
illusion = Power.objects.get_or_create(
    name="Illusion",
    quantum_minimum=2,
    action_type="ordinary",
    cost=3,
    dicepool="Quantum+Power",
    range="visual",
    duration="continuous",
)[0]
molecular_chameleon = Power.objects.get_or_create(
    name="Molecular Chameleon",
    quantum_minimum=4,
    action_type="ordinary",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)[0]
defensive = Tag.objects.get_or_create(name="Defensive", ratings=[2],)[0]
defensive.permitted_powers.add(molecular_chameleon)
defensive.save()
energy_chameleon = Tag.objects.get_or_create(name="Energy Chameleon", ratings=[1],)[0]
energy_chameleon.permitted_powers.add(molecular_chameleon)
energy_chameleon.save()
extra_properties = Tag.objects.get_or_create(name="Extra Properties", ratings=[1],)[0]
extra_properties.permitted_powers.add(molecular_chameleon)
extra_properties.save()
molecular_manipulation = Power.objects.get_or_create(
    name="Molecular Manipulation",
    quantum_minimum=3,
    action_type="ordinary",
    cost=1,
    dicepool="Quantum+Power",
    range="medium",
    duration="continuous",
)[0]
morph = Power.objects.get_or_create(
    name="Morph",
    quantum_minimum=-1,
    quantum_offset=-3,
    action_type="reflexive",
    cost=1,
    dicepool="Quantum+Power",
    range="personal",
    duration="maintained",
)[0]
form_mastery = Tag.objects.get_or_create(name="Form Mastery", ratings=[1],)[0]
form_mastery.permitted_powers.add(morph)
form_mastery.save()
phasing = Power.objects.get_or_create(
    name="Phasing",
    quantum_minimum=2,
    action_type="reflexive",
    cost=2,
    dicepool="",
    range="personal",
    duration="continuous",
)[0]
restricted_to_phase_state = Tag.objects.get_or_create(
    name="Restricted to Phase State", ratings=[-1],
)[0]
restricted_to_phase_state.permitted_powers.add(phasing)
restricted_to_phase_state.save()
plasticity = Power.objects.get_or_create(
    name="Plasticity",
    quantum_minimum=2,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="maintained",
)[0]
quantum_agent = Power.objects.get_or_create(
    name="Quantum Agent",
    quantum_minimum=-1,
    action_type="ordinary",
    cost=3,
    dicepool="",
    range="medium",
    duration="continuous",
)[0]
horde = Tag.objects.get_or_create(name="Horde", ratings=[1],)[0]
horde.permitted_powers.add(quantum_agent)
horde.save()
independent = Tag.objects.get_or_create(name="Independent", ratings=[1],)[0]
independent.permitted_powers.add(quantum_agent)
independent.save()
memory_absorption = Tag.objects.get_or_create(name="Memory Absorption", ratings=[1],)[0]
memory_absorption.permitted_powers.add(quantum_agent)
memory_absorption.save()
sensory_link = Tag.objects.get_or_create(name="Sensory Link", ratings=[1],)[0]
sensory_link.permitted_powers.add(quantum_agent)
sensory_link.save()
quantum_anima = Power.objects.get_or_create(
    name="Quantum Anima",
    quantum_minimum=-1,
    action_type="ordinary",
    cost=2,
    dicepool="Quantum+Power",
    range="long",
    duration="continuous",
)[0]
quantum_attack = Power.objects.get_or_create(
    name="Quantum Attack",
    quantum_minimum=-1,
    action_type="ordinary",
    cost=2,
    dicepool="Close Combat+Dexterity or Might, or Aim+Dexterity",
    range="close",
    duration="instantaneous",
)[0]
quantum_aura = Power.objects.get_or_create(
    name="Quantum Aura",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="maintained",
)[0]
quantum_construct = Power.objects.get_or_create(
    name="Quantum Construct",
    quantum_minimum=-1,
    quantum_offset=1,
    action_type="ordinary",
    cost=2,
    dicepool="",
    range="medium",
    duration="maintained",
)[0]

durability = Tag.objects.get_or_create(name="Durability", ratings=[1],)[0]
durability.permitted_powers.add(quantum_construct)
durability.save()
invisibility = Tag.objects.get_or_create(name="Invisibility", ratings=[1],)[0]
invisibility.permitted_powers.add(quantum_construct)
invisibility.save()
multiple = Tag.objects.get_or_create(
    name="Multiple", ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],
)[0]
multiple.permitted_powers.add(quantum_construct)
multiple.save()
selective = Tag.objects.get_or_create(
    name="Selective", ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],
)[0]
selective.permitted_powers.add(quantum_construct)
selective.save()
size = Tag.objects.get_or_create(name="Size", ratings=[1],)[0]
size.permitted_powers.add(quantum_construct)
size.save()
quantum_deflection = Power.objects.get_or_create(
    name="Quantum Deflection",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=2,
    dicepool="Quantum+Power",
    range="personal",
    duration="instantaneous",
)[0]
quantum_disruption = Power.objects.get_or_create(
    name="Quantum Disruption",
    quantum_minimum=3,
    action_type="ordinary",
    cost=2,
    dicepool="Quantum+Power",
    range="medium",
    duration="instantaneous",
)[0]
quantum_field = Power.objects.get_or_create(
    name="Quantum Field",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="maintained",
)[0]
quantum_imprint = Power.objects.get_or_create(
    name="Quantum Imprint",
    quantum_minimum=4,
    action_type="ordinary",
    cost=2,
    dicepool="Quantum+Power",
    range="close",
    duration="continuous",
)[0]
extra_power = Tag.objects.get_or_create(name="Extra Power", ratings=[1],)[0]
extra_power.permitted_powers.add(quantum_imprint)
extra_power.save()
impersonation = Tag.objects.get_or_create(name="Impersonation", ratings=[2],)[0]
impersonation.permitted_powers.add(quantum_imprint)
impersonation.save()
theft = Tag.objects.get_or_create(name="Theft", ratings=[2],)[0]
theft.permitted_powers.add(quantum_imprint)
theft.save()
quantum_leech = Power.objects.get_or_create(
    name="Quantum Leech",
    quantum_minimum=2,
    action_type="ordinary",
    cost=1,
    dicepool="Quantum+Power",
    range="close",
    duration="instantaneous",
)[0]
remote_perception = Power.objects.get_or_create(
    name="Remote Perception",
    quantum_minimum=3,
    action_type="ordinary",
    cost=2,
    dicepool="Quantum+Power",
    range="visual",
    duration="continuous",
)[0]
shrinking = Power.objects.get_or_create(
    name="Shrinking",
    quantum_minimum=-1,
    quantum_offset=-1,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)[0]
growth_momentum = Tag.objects.get_or_create(name="Growth Momentum", ratings=[1],)[0]
growth_momentum.permitted_powers.add(shrinking)
growth_momentum.save()
tiny_titan = Tag.objects.get_or_create(name="Tiny Titan", ratings=[1],)[0]
tiny_titan.permitted_powers.add(shrinking)
tiny_titan.save()
shroud = Power.objects.get_or_create(
    name="Shroud",
    quantum_minimum=2,
    action_type="ordinary",
    cost=2,
    dicepool="",
    range="short",
    duration="maintained",
)[0]
variable = Tag.objects.get_or_create(name="Variable", ratings=[1],)[0]
variable.permitted_powers.add(phasing, shroud, environmental_anima)
variable.save()
broadband = Tag.objects.get_or_create(name="Broadband", ratings=[1],)[0]
broadband.permitted_powers.add(shroud, cloak)
broadband.save()
dual = Tag.objects.get_or_create(name="Dual", ratings=[1],)[0]
dual.permitted_powers.add(shroud)
dual.save()
teleport = Power.objects.get_or_create(
    name="Teleport",
    quantum_minimum=-1,
    quantum_offset=1,
    action_type="reflexive",
    cost=2,
    dicepool="",
    range="personal",
    duration="instantaneous",
)[0]
transformation = Power.objects.get_or_create(
    name="Transformation",
    quantum_minimum=4,
    action_type="ordinary",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)[0]
extra_traits = Tag.objects.get_or_create(name="Extra Traits", ratings=[1],)[0]
extra_traits.permitted_powers.add(transformation)
extra_traits.save()
reflexive = Tag.objects.get_or_create(name="Reflexive", ratings=[2],)[0]
reflexive.permitted_powers.add(transformation, quantum_disruption)
reflexive.save()
transmutation = Power.objects.get_or_create(
    name="Transmutation",
    quantum_minimum=4,
    action_type="ordinary",
    cost=3,
    dicepool="Quantum+Power",
    range="close",
    duration="instantaneous",
)[0]
warp = Power.objects.get_or_create(
    name="Warp",
    quantum_minimum=-1,
    quantum_offset=2,
    action_type="ordinary",
    cost=2,
    dicepool="",
    range="close",
    duration="continuous",
)[0]

x = Tag.objects.get_or_create(name="Aggravated", ratings=[2],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Area", ratings=[2, 4, 6, 8],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Beam", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Bestow", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Bestow Only", ratings=[0],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Blinding", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Brutal", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Charge", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Complete", ratings=[3],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Damaging", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Deadly", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Deafening", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Destructive", ratings=[2],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Disintegrating", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Duration", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Electrical", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Entangle", ratings=[2],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Environmental", ratings=[1, 2],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Gas", ratings=[3],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Hard Armor", ratings=[1, 3, 5],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Immune", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Impervious", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Impose", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Impose Only", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Incendiary", ratings=[2],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Intrinsic", ratings=[0],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Modular", ratings=[1, 2, 3],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Non-Lethal", ratings=[2],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Non-Penetrating", ratings=[0],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Piercing", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Poison", ratings=[2, 3],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Pushing", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Ramp Up", ratings=[-1, -2, -3],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Ranged", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Reduced Cost", ratings=[2, 4, 6, 8, 10, 12],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Reduced Duration", ratings=[-1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Restricted", ratings=[-1, -2, -3],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Smashing", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Sonic", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Spread", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Stun", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Subtle", ratings=[1, 2],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Thrown", ratings=[1],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.get_or_create(name="Vampiric", ratings=[2],)[0]
x.permitted_powers.add(*list(Power.objects.all()))
x.save()


aberrant_eyes = Transformation.objects.get_or_create(
    name="Aberrant Eyes", level="low",
)[0]
anima_aura = Transformation.objects.get_or_create(name="Anima Aura", level="low",)[0]
epidermal_shift = Transformation.objects.get_or_create(
    name="Epidermal Shift", level="low",
)[0]
feeding_requirement = Transformation.objects.get_or_create(
    name="Feeding Requirement", level="low",
)[0]
inhuman_beauty = Transformation.objects.get_or_create(
    name="Inhuman Beauty", level="low",
)[0]
life_bane = Transformation.objects.get_or_create(name="Life Bane", level="low",)[0]
psychological_shift = Transformation.objects.get_or_create(
    name="Psychological Shift", level="low",
)[0]
vocal_shift = Transformation.objects.get_or_create(name="Vocal Shift", level="low",)[0]
Transformation.objects.get_or_create(name="Allergic Reaction", level="medium",)[0]
Transformation.objects.get_or_create(name="Energy Bleed", level="medium",)[0]
Transformation.objects.get_or_create(name="Hypersensitivity", level="medium",)[0]
Transformation.objects.get_or_create(name="Physiological Shift", level="medium",)[0]
Transformation.objects.get_or_create(name="Power Loss", level="medium",)[0]
Transformation.objects.get_or_create(name="Psychological Disorder", level="medium",)[0]
Transformation.objects.get_or_create(name="Uncontrolled Dormancy", level="medium",)[0]
Transformation.objects.get_or_create(name="Uncontrolled Power", level="medium")[0]
Transformation.objects.get_or_create(name="Vulnerability", level="medium")[0]
Transformation.objects.get_or_create(name="Energy Emissions", level="high")[0]
Transformation.objects.get_or_create(name="Flux Emissions", level="high")[0]
Transformation.objects.get_or_create(name="Hardened Epidermis", level="high")[0]
Transformation.objects.get_or_create(name="Hyde Syndrome", level="high")[0]
Transformation.objects.get_or_create(name="Power Lock", level="high")[0]
Transformation.objects.get_or_create(
    name="Severe Psychological Disorder", level="high"
)[0]
Transformation.objects.get_or_create(name="Twisted Appearance", level="high")[0]

ObjectType.objects.get_or_create(
    name="Aberrant", type="char", system="tc", gameline="Aberrant"
)[0]
ObjectType.objects.get_or_create(
    name="Human", type="char", system="tc", gameline="Trinity Continuum"
)[0]
ObjectType.objects.get_or_create(
    name="Talent", type="char", system="tc", gameline="Trinity Continuum"
)[0]
