# TODO: Fix all prereqs and combine like things
from tc.models.characters.aberrant import MegaEdge, Power, Tag, Transformation
from tc.models.characters.human import (
    Edge,
    EnhancedEdge,
    Path,
    PathConnection,
    Specialty,
    Trick,
)
from tc.models.characters.talent import Gift, MomentOfInspiration

Specialty.objects.create(skill="aim", name="Rifle")
Specialty.objects.create(skill="aim", name="Pistol")
Specialty.objects.create(skill="aim", name="Bow")
Specialty.objects.create(skill="aim", name="Specific Weapon")
Specialty.objects.create(skill="athletics", name="Climbing")
Specialty.objects.create(skill="athletics", name="Crossfit")
Specialty.objects.create(skill="athletics", name="Running")
Specialty.objects.create(skill="athletics", name="Specific Sport")
Specialty.objects.create(skill="athletics", name="Baseball")
Specialty.objects.create(skill="athletics", name="Basketball")
Specialty.objects.create(skill="athletics", name="Hockey")
Specialty.objects.create(skill="athletics", name="Swimming")
Specialty.objects.create(skill="close_combat", name="Dirty Tricks")
Specialty.objects.create(skill="close_combat", name="Martial Art Style")
Specialty.objects.create(skill="close_combat", name="Aikido")
Specialty.objects.create(skill="close_combat", name="Boxing")
Specialty.objects.create(skill="close_combat", name="Krav Maga")
Specialty.objects.create(skill="close_combat", name="Weapon Type")
Specialty.objects.create(skill="close_combat", name="Axe")
Specialty.objects.create(skill="close_combat", name="Baton")
Specialty.objects.create(skill="close_combat", name="Sword")
Specialty.objects.create(skill="command", name="Battlefield Tactics")
Specialty.objects.create(skill="command", name="Bureaucracy")
Specialty.objects.create(skill="command", name="Military Organization")
Specialty.objects.create(skill="culture", name="High Society")
Specialty.objects.create(skill="culture", name="Pop Music")
Specialty.objects.create(skill="culture", name="Science-Fiction")
Specialty.objects.create(skill="culture", name="World Religion")
Specialty.objects.create(skill="empathy", name="Lie Detection")
Specialty.objects.create(skill="empathy", name="Negotiation")
Specialty.objects.create(skill="empathy", name="Psychology")
Specialty.objects.create(skill="enigmas", name="Crime Scene Investigation")
Specialty.objects.create(skill="enigmas", name="Hacking")
Specialty.objects.create(skill="enigmas", name="Math")
Specialty.objects.create(skill="humanities", name="Research")
Specialty.objects.create(skill="humanities", name="Specific Field")
Specialty.objects.create(skill="humanities", name="Law")
Specialty.objects.create(skill="humanities", name="History")
Specialty.objects.create(skill="humanities", name="Specific Language")
Specialty.objects.create(skill="integrity", name="Concealing Emotions")
Specialty.objects.create(skill="integrity", name="Meditation")
Specialty.objects.create(skill="integrity", name="Resisting Pain")
Specialty.objects.create(skill="larceny", name="Concealed Weapons")
Specialty.objects.create(skill="larceny", name="Security Systems")
Specialty.objects.create(skill="larceny", name="Sneaking")
Specialty.objects.create(skill="medicine", name="Field of Medicine")
Specialty.objects.create(skill="medicine", name="First Aid")
Specialty.objects.create(skill="medicine", name="Surgery")
Specialty.objects.create(skill="persuasion", name="Fast-Talking")
Specialty.objects.create(skill="persuasion", name="Interrogation")
Specialty.objects.create(skill="persuasion", name="Seduction")
Specialty.objects.create(skill="pilot", name="Dangerous Maneuvers")
Specialty.objects.create(skill="pilot", name="Specific Terrain")
Specialty.objects.create(skill="pilot", name="City Streets")
Specialty.objects.create(skill="pilot", name="Orbit")
Specialty.objects.create(skill="pilot", name="Underwater")
Specialty.objects.create(skill="pilot", name="Vehicle Type")
Specialty.objects.create(skill="pilot", name="Car")
Specialty.objects.create(skill="pilot", name="Plane")
Specialty.objects.create(skill="pilot", name="Starship")
Specialty.objects.create(skill="science", name="Field of Study")
Specialty.objects.create(skill="science", name="Astronomy")
Specialty.objects.create(skill="science", name="Chemistry")
Specialty.objects.create(skill="science", name="Physics")
Specialty.objects.create(skill="science", name="Fringe Science")
Specialty.objects.create(skill="science", name="R&D")
Specialty.objects.create(skill="survival", name="Animal Handling")
Specialty.objects.create(skill="survival", name="Navigation")
Specialty.objects.create(skill="survival", name="Tracking")
Specialty.objects.create(skill="technology", name="Automotive")
Specialty.objects.create(skill="technology", name="Laser Rifle")
Specialty.objects.create(skill="technology", name="Supercomputer")
Specialty.objects.create(skill="technology", name="Electronics")
Specialty.objects.create(skill="technology", name="Repair Equipment")
Specialty.objects.create(skill="technology", name="Other Device")

gun_tool = Trick.objects.create(
    name="Gun Tool",
    skill="aim",
)
hidden_arsenal = Trick.objects.create(
    name="Hidden Arsenal",
    skill="aim",
)
Trick.objects.create(
    name="I Wasn't Aiming at You",
    skill="aim",
)
Trick.objects.create(
    name="Shoot to Injure",
    skill="aim",
)
Trick.objects.create(
    name="It's All in the Reflexes",
    skill="athletics",
)
Trick.objects.create(
    name="Mighty Lifter",
    skill="athletics",
)
Trick.objects.create(
    name="No Barrier",
    skill="athletics",
)
Trick.objects.create(
    name="Physical Actor",
    skill="athletics",
)
Trick.objects.create(
    name="Deadly Strike",
    skill="close_combat",
)
Trick.objects.create(
    name="Sucker Punch",
    skill="close_combat",
)
Trick.objects.create(
    name="Fast Planning",
    skill="close_combat",
)
Trick.objects.create(
    name="Inspiring Example",
    skill="command",
)
Trick.objects.create(
    name="Motivational Speaker",
    skill="command",
)
Trick.objects.create(
    name="Top Dog",
    skill="command",
)
Trick.objects.create(
    name="Grain of Truth",
    skill="culture",
)
Trick.objects.create(
    name="Members Only",
    skill="culture",
)
Trick.objects.create(
    name="That's My Favorite, Too!",
    skill="culture",
)
Trick.objects.create(
    name="Cold Reader",
    skill="empathy",
)
Trick.objects.create(
    name="Rumor Has It",
    skill="empathy",
)
Trick.objects.create(
    name="Six Degrees",
    skill="empathy",
)
Trick.objects.create(
    name="The Crack in the Ice",
    skill="empathy",
)
Trick.objects.create(
    name="Connecting the Dots",
    skill="empathy",
)
Trick.objects.create(
    name="Did the Math",
    skill="empathy",
)
Trick.objects.create(
    name="Elite Hacker",
    skill="enigmas",
)
Trick.objects.create(
    name="Instant Solution",
    skill="enigmas",
)
Trick.objects.create(
    name="Befuddling Jargon",
    skill="humanities",
)
Trick.objects.create(
    name="Everything in Context",
    skill="humanities",
)
Trick.objects.create(
    name="Legal Authority",
    skill="humanities",
)
Trick.objects.create(
    name="Meditative Stance",
    skill="integrity",
)
Trick.objects.create(
    name="Poker Face",
    skill="integrity",
)
Trick.objects.create(
    name="Strength of Conviction",
    skill="integrity",
)
Trick.objects.create(
    name="Tough Nut",
    skill="integrity",
)
Trick.objects.create(
    name="Always Have an Exit",
    skill="larceny",
)
Trick.objects.create(
    name="Handcuff Houdini",
    skill="larceny",
)
Trick.objects.create(
    name="Set a Thief",
    skill="larceny",
)
Trick.objects.create(
    name="That Was Already Mine",
    skill="larceny",
)
Trick.objects.create(
    name="Diagnostic Expert",
    skill="medicine",
)
Trick.objects.create(
    name="Medical Advantage",
    skill="medicine",
)
Trick.objects.create(
    name="Quick Aid",
    skill="medicine",
)
Trick.objects.create(
    name="Walking Wounded",
    skill="medicine",
)
Trick.objects.create(
    name="Captivating Personality",
    skill="persuasion",
)
Trick.objects.create(
    name="Devilishly Good Looking",
    skill="persuasion",
)
Trick.objects.create(
    name="Easy to Love",
    skill="persuasion",
)
Trick.objects.create(
    name="Backseat Driver",
    skill="pilot",
)
Trick.objects.create(
    name="Collision Artist",
    skill="pilot",
)
Trick.objects.create(
    name="Fighter Pilot",
    skill="pilot",
)
Trick.objects.create(
    name="I Can Figure It Out",
    skill="pilot",
)
Trick.objects.create(
    name="R&D Expert",
    skill="science",
)
Trick.objects.create(
    name="Scientific Method",
    skill="science",
)
Trick.objects.create(
    name="Scientific Polymath",
    skill="science",
)
Trick.objects.create(
    name="King of Beasts",
    skill="survival",
)
Trick.objects.create(
    name="Tricky Situation",
    skill="survival",
)
Trick.objects.create(
    name="Versus Wild",
    skill="survival",
)
Trick.objects.create(
    name="Without a Trace",
    skill="survival",
)
Trick.objects.create(
    name="Ahead of Your Time",
    skill="technology",
)
Trick.objects.create(
    name="Engineer's Eye",
    skill="technology",
)
Trick.objects.create(name="It's Not a Bug, It's a Feature", skill="technology")
Trick.objects.create(name="Overwatch", skill="technology")

always_prepared = Edge.objects.create(name="Always Prepared", ratings=[1],)
artistic_talent = Edge.objects.create(name="Artistic Talent", ratings=[1, 2, 3],)
danger_sense = Edge.objects.create(name="Danger Sense", ratings=[1],)
direction_sense = Edge.objects.create(name="Direction Sense", ratings=[1],)
ironwill = Edge.objects.create(name="Iron Will", ratings=[1, 2, 3],)
library = Edge.objects.create(name="Library", ratings=[1, 2, 3],)
lightning_calculator = Edge.objects.create(name="Lightning Calculator", ratings=[2],)
photographic_memory = Edge.objects.create(name="Photographic Memory", ratings=[1, 2, 3],)
small_unit_tactics = Edge.objects.create(name="Small Unit Tactics", ratings=[2], prereqs=[("path", 1)],)
speed_reading = Edge.objects.create(name="Speed Reading", ratings=[1], prereqs=[("cunning", 3)])
adrenaline_spike = Edge.objects.create(name="Adrenaline Spike", ratings=[2],)
ambidextrous = Edge.objects.create(name="Ambidextrous", ratings=[1],)
breath_control = Edge.objects.create(name="Breath Control", ratings=[1],)
fast_draw = Edge.objects.create(name="Fast Draw", ratings=[1], prereqs=[("aim", 1), ("close_combat", 1)])
hair_trigger_reflexes = Edge.objects.create(name="Hair Trigger Reflexes", ratings=[1],)
keen_sense_sight = Edge.objects.create(name="Keen Sense (Sight)", ratings=[1],)
keen_sense_hearing = Edge.objects.create(name="Keen Sense (Hearing)", ratings=[1],)
keen_sense_touch = Edge.objects.create(name="Keen Sense (Touch)", ratings=[1],)
keen_sense_smell_and_taste = Edge.objects.create(name="Keen Sense (Smell and Taste)", ratings=[1],)
hardy = Edge.objects.create(name="Hardy", ratings=[1, 2, 3],)
ms_fix_it = Edge.objects.create(name="Ms. Fix It", ratings=[2],)
swift = Edge.objects.create(name="Swift", ratings=[1],)
tough_cookie = Edge.objects.create(name="Tough Cookie", ratings=[2],)
weak_spots = Edge.objects.create(name="Weak Spots", ratings=[1],)
alternate_identity = Edge.objects.create(name="Alternate Identity", ratings=[1, 2], prereqs=[("path", 2)])
animal_ken = Edge.objects.create(name="Animal Ken", ratings=[1, 2],)
big_hearted = Edge.objects.create(name="Big Hearted", ratings=[1],)
covert = Edge.objects.create(name="Covert", ratings=[1, 2, 3], prereqs=[("path", 3)])
fame = Edge.objects.create(name="Fame", ratings=[1, 2, 3],)
patron = Edge.objects.create(name="Patron", ratings=[1, 2, 3], prereqs=[("path", 1)])
safe_house = Edge.objects.create(name="Safe House", ratings=[1],)
skilled_liar = Edge.objects.create(name="Skilled Liar", ratings=[2],)
striking = Edge.objects.create(name="Striking", ratings=[2],)
wealth = Edge.objects.create(name="Wealth", ratings=[1, 2, 3, 4, 5],)
demolitions_training = Edge.objects.create(name="Demolitions Training", ratings=[1, 2, 3], prereqs=[("path", 1), ("technology", 1)])
forceful_martial_arts = Edge.objects.create(name="Forceful Martial Arts", ratings=[1, 2, 3], prereqs=[("close_combat", 2), ("might", 2)])
free_running = Edge.objects.create(name="Free Running", ratings=[1, 2, 3], prereqs=[("athletics", 1)])
precise_martial_arts = Edge.objects.create(name="Precise Martial Arts", ratings=[1, 2, 3], prereqs=[("dexterity", 2), ("close_combat", 2)])
sniper = Edge.objects.create(name="Sniper", ratings=[1, 2, 3], prereqs=[("path", 1), ("resolve", 3), ("aim", 2)])
armor_expert = Edge.objects.create(name="Armor Expert", ratings=[1], prereqs=[("stamina", 3)])
cool_under_fire = Edge.objects.create(name="Cool Under Fire", ratings=[2], prereqs=[("integrity", 2)])
deflection_adept = Edge.objects.create(name="Deflection Adept", ratings=[2], prereqs=[("survival", 2)])
one_against_an_ocean = Edge.objects.create(name="One Against An Ocean", ratings=[2], prereqs=[("close_combat", 2)])
trick_shooter = Edge.objects.create(name="Trick Shooter", ratings=[3], prereqs=[("aim", 2)])
waiting_to_greet_the_storm = Edge.objects.create(name="Waiting to Greet the Storm", ratings=[2], prereqs=[("integrity", 3)])
artifact = Edge.objects.create(name="Artifact", ratings=[1, 2, 3, 4, 5],)
endurance = Edge.objects.create(name="Endurance", ratings=[3],)
superior_trait_intellect = Edge.objects.create(name="Superior Trait (Intellect)", ratings=[2])
superior_trait_cunning = Edge.objects.create(name="Superior Trait (Cunning)", ratings=[2])
superior_trait_resolve = Edge.objects.create(name="Superior Trait (Resolve)", ratings=[2])
superior_trait_might = Edge.objects.create(name="Superior Trait (Might)", ratings=[2],)
superior_trait_dexterity = Edge.objects.create(name="Superior Trait (Dexterity)", ratings=[2])
superior_trait_stamina = Edge.objects.create(name="Superior Trait (Stamina)", ratings=[2])
superior_trait_presence = Edge.objects.create(name="Superior Trait (Presence)", ratings=[2])
superior_trait_manipulation = Edge.objects.create(name="Superior Trait (Manipulation)", ratings=[2])
superior_trait_composure = Edge.objects.create(name="Superior Trait (Composure)", ratings=[2])

attunement = Edge.objects.create(name="Attunement", ratings=[1, 2, 3, 4, 5],)
dormancy = Edge.objects.create(name="Dormancy", ratings=[1, 2],)
eufiber = Edge.objects.create(name="Eufiber", ratings=[1, 2, 3, 4, 5],)
borrowed_resources = Edge.objects.create(name="Borrowed Resources", ratings=[2], prereqs=[("path", 1)])
call_for_backup = Edge.objects.create(name="Call For Backup", ratings=[1, 2, 3], prereqs=[("path", 1)])
chrysalis = Edge.objects.create(name="Chrysalis", ratings=[2], prereqs=[("path", 1)])
earned_trust = Edge.objects.create(name="Earned Trust", ratings=[1, 2], prereqs=[("path", 1)])
friends_everywhere = Edge.objects.create(name="Friends Everywhere", ratings=[1, 2], prereqs=[("path", 1)])
microgravity_training = Edge.objects.create(name="Microgravity Training", ratings=[1, 2, 3], prereqs=[("path", 1), ("Direction Sense", 1)])
well_equipped = Edge.objects.create(name="Well-Equipped", ratings=[1, 2], prereqs=[("path", 1)])
followers = Edge.objects.create(name="Followers", ratings=[1, 2, 3, 4, 5],)

anonymous = EnhancedEdge.objects.create(name="Anonymous", prereqs=[("Covert", 3)])
armory = EnhancedEdge.objects.create(name="Armory", prereqs=[("Artifact", 5)])
indomitable = EnhancedEdge.objects.create(name="Indomitable", prereqs=[("Iron Will", 3)])
loaded = EnhancedEdge.objects.create(name="Loaded", prereqs=[("Wealth", 5)])
respected_authority = EnhancedEdge.objects.create(name="Respected Authority", prereqs=[("Fame", 3)])
wondrous_item = EnhancedEdge.objects.create(name="Wondrous Item", prereqs=[("Artifact", 3)])

adventurer = Path.objects.create(name="Adventurer", type="origin", skills=["aim", "athletics", "pilot", "survival"], gift_keywords=["might", "pilot", "survival"])
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
PathConnection.objects.create(name="High-risk Hobbyists", path=adventurer)
PathConnection.objects.create(name="Bomb Disposal Experts", path=adventurer)
PathConnection.objects.create(name="Travel Enthusiasts", path=adventurer)
life_of_privilege = Path.objects.create(name="Life of Privilege", type="origin", skills=["command", "culture", "integrity", "persuasion"], gift_keywords=["presence", "pilot", "survival"])
life_of_privilege.edges.add(fame, patron, skilled_liar, wealth)
life_of_privilege.save()
PathConnection.objects.create(name="School Alumni", path=life_of_privilege)
PathConnection.objects.create(name="College Club Membership", path=life_of_privilege)
PathConnection.objects.create(name="Local Political Affiliates", path=life_of_privilege)
military_brat = Path.objects.create(name="Military Brat", type="origin", skills=["command", "enigmas", "integrity", "technology"], gift_keywords=["resolve", "integrity", "technology"])
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
x = PathConnection.objects.create(name="Past Teacher", path=military_brat)
x = PathConnection.objects.create(name="Military Commander", path=military_brat)
x = PathConnection.objects.create(name="Steadfast Friend", path=military_brat)
street_rat = Path.objects.create(name="Street Rat", type="origin", skills=["athletics", "enigmas", "larceny", "survival"], gift_keywords=["cunning", "larceny", "survival"])
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
x = PathConnection.objects.create(name="Street Gangs", path=street_rat)
x = PathConnection.objects.create(name="Street Mentor", path=street_rat)
x = PathConnection.objects.create(name="Helpful Family Member", path=street_rat)
x = PathConnection.objects.create(name="Store Clerks", path=street_rat)
suburbia = Path.objects.create(name="Suburbia", type="origin", skills=["culture", "empathy", "humanities", "technology"], gift_keywords=["manipulation", "culture", "empathy"])
suburbia.edges.add(artistic_talent, big_hearted, library, patron, wealth)
suburbia.save()
x = PathConnection.objects.create(name="Favorite Professor", path=suburbia)
x = PathConnection.objects.create(name="Neighbor Friend", path=suburbia)
x = PathConnection.objects.create(name="Influential Teacher", path=suburbia)
survivalist = Path.objects.create(name="Survivalist", type="origin", skills=["aim", "close_combat", "medicine", "survival"], gift_keywords=["stamina", "medicine", "survival"])
survivalist.edges.add(
    always_prepared,
    animal_ken,
    covert,
    direction_sense,
    hardy,
    ironwill,
    keen_sense_sight, keen_sense_hearing, keen_sense_touch, keen_sense_smell_and_taste, 
    swift,
)
survivalist.save()
x = PathConnection.objects.create(name="Park Ranger", path=survivalist)
x = PathConnection.objects.create(name="Conspiracy Groups", path=survivalist)
x = PathConnection.objects.create(name="RV Neighborhood", path=survivalist)
charismatic_leader = Path.objects.create(name="Charismatic Leader", type="role", skills=["command", "empathy", "humanities", "persuasion"], gift_keywords=["manipulation", "command", "humanities"])
charismatic_leader.edges.add(fame, ironwill, skilled_liar, striking, wealth)
charismatic_leader.save()
x = PathConnection.objects.create(name="Corporate Board", path=charismatic_leader)
x = PathConnection.objects.create(name="Megachurch", path=charismatic_leader)
x = PathConnection.objects.create(name="Political Allies", path=charismatic_leader)
combat_specialist = Path.objects.create(name="Combat Specialist", type="role", skills=["aim", "athletics", "close_combat", "integrity"], gift_keywords=["might", "aim", "close_combat"])
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
x = PathConnection.objects.create(name="Military Unit", path=combat_specialist,)
x = PathConnection.objects.create(name="Police Officers", path=combat_specialist,)
x = PathConnection.objects.create(name="Training Master", path=combat_specialist,)
detective = Path.objects.create(name="Detective", type="role", skills=["aim", "enigmas", "integrity", "persuasion"], gift_keywords=["cunning", "aim", "enigmas"])
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
x = PathConnection.objects.create(name="Police Officers", path=detective)
x = PathConnection.objects.create(name="Paid Informant", path=detective)
x = PathConnection.objects.create(name="News Reporter", path=detective)
x = PathConnection.objects.create(name="Friendly Neighborhood Watch", path=detective)
medical_practitioner = Path.objects.create(name="Medical Practitioner", type="role", skills=["empathy", "medicine", "science", "survival"], gift_keywords=["resolve", "medicine", "science"])
medical_practitioner.edges.add(
    always_prepared, ambidextrous, big_hearted, ironwill, keen_sense_sight, keen_sense_hearing, keen_sense_touch, keen_sense_smell_and_taste, library, wealth
)
medical_practitioner.save()
x = PathConnection.objects.create(name="Surgeon", path=medical_practitioner)
x = PathConnection.objects.create(name="Pharmacists", path=medical_practitioner)
x = PathConnection.objects.create(name="Thankful Patient", path=medical_practitioner)
x = PathConnection.objects.create(name="EMTs", path=medical_practitioner)
pilot_path = Path.objects.create(name="Pilot", type="role", skills=["aim", "close_combat", "pilot", "technology"], gift_keywords=["dexterity", "pilot", "technology"])
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
x = PathConnection.objects.create(name="Important Client", path=pilot_path)
x = PathConnection.objects.create(name="Criminal Organization", path=pilot_path)
x = PathConnection.objects.create(name="Indebted Passenger", path=pilot_path)
sneak = Path.objects.create(name="The Sneak", type="role", skills=["athletics", "enigmas", "larceny", "technology"], gift_keywords=["composure", "athletics", "larceny"])
sneak.edges.add(
    adrenaline_spike,
    alternate_identity,
    covert,
    free_running,
    photographic_memory,
    skilled_liar,
)
sneak.save()
x = PathConnection.objects.create(name="Criminal Organization", path=sneak)
x = PathConnection.objects.create(name="Best Friend", path=sneak)
x = PathConnection.objects.create(name="Police Insider", path=sneak)
technology_expert = Path.objects.create(name="Technology Expert", type="role", skills=["culture", "enigmas", "science", "technology"], gift_keywords=["intellect", "science", "technology"])
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
x = PathConnection.objects.create(name="Chop Shop Worker", path=technology_expert)
x = PathConnection.objects.create(name="Research Scientists", path=technology_expert)
x = PathConnection.objects.create(name="Machinist Friend", path=technology_expert)

athlete = Path.objects.create(name="Athlete", type="role", skills=["aim", "athletics", "culture", "integrity"])
athlete.edges.add(adrenaline_spike, ambidextrous, fame, hardy, swift, wealth)
athlete.save()
x = PathConnection.objects.create(name="Agent", path=athlete)
x = PathConnection.objects.create(name="Fans", path=athlete)
x = PathConnection.objects.create(name="Manager", path=athlete)
x = PathConnection.objects.create(name="Sports Journalist", path=athlete)
x = PathConnection.objects.create(name="Teammates", path=athlete)
celebrity = Path.objects.create(name="Celebrity", type="role", skills=["culture", "empathy", "humanities", "persuasion"])
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
x = PathConnection.objects.create(name="Fans", path=celebrity)
x = PathConnection.objects.create(name="Fellow Celebrities", path=celebrity)
x = PathConnection.objects.create(name="Legal Counsel", path=celebrity)
x = PathConnection.objects.create(name="Manager", path=celebrity)
x = PathConnection.objects.create(name="Politicians", path=celebrity)
consultant = Path.objects.create(name="Consultant", type="role", skills=["integrity", "persuasion", "culture", "humanities","medicine", "science", "technology",])
consultant.edges.add(always_prepared, fame, patron, striking, wealth)
consultant.save()
x = PathConnection.objects.create(name="Academic", path=consultant)
x = PathConnection.objects.create(name="Corporate Executive", path=consultant)
x = PathConnection.objects.create(name="Elite Agency", path=consultant)
x = PathConnection.objects.create(name="Government Official", path=consultant)
x = PathConnection.objects.create(name="Media Agent or Personality", path=consultant)
x = PathConnection.objects.create(name="Policy Wonk", path=consultant)
corporate = Path.objects.create(name="Corporate", type="role", skills=["command", "humanities", "integrity", "persuasion"])
corporate.edges.add(library, patron, skilled_liar, wealth)
corporate.save()
x = PathConnection.objects.create(name="Corporate Executives", path=corporate)
x = PathConnection.objects.create(name="Experts", path=corporate)
x = PathConnection.objects.create(name="Lawyers", path=corporate)
x = PathConnection.objects.create(name="Financiers", path=corporate)
x = PathConnection.objects.create(name="Investors", path=corporate)

aeon_society = Path.objects.create(name="&AElig;on Society", type="society", skills=["humanities", "persuasion", "science", "larceny"])
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
x = PathConnection.objects.create(name="&AElig;on Council", path=aeon_society)
x = PathConnection.objects.create(name="Project Utopia", path=aeon_society)
x = PathConnection.objects.create(name="Team Tomorrow", path=aeon_society)
x = PathConnection.objects.create(
    name="International Relief Agencies", path=aeon_society
)
x = PathConnection.objects.create(
    name="Allies in Government positions", path=aeon_society
)
x = PathConnection.objects.create(name="Grateful Citizens", path=aeon_society)
project_utopia = Path.objects.create(name="Project Utopia", type="society", skills=["athletics", "close_combat", "command", "integrity"])
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
x = PathConnection.objects.create(name="&AElig;on Society", path=project_utopia)
x = PathConnection.objects.create(name="Project Utopia", path=project_utopia)
x = PathConnection.objects.create(name="Team Tomorrow", path=project_utopia)
x = PathConnection.objects.create(name="Squad of Peacekeepers", path=project_utopia)
x = PathConnection.objects.create(name="Doctor from Nova Affairs", path=project_utopia)
x = PathConnection.objects.create(name="DeVries Recruiter", path=project_utopia)
teragen = Path.objects.create(name="Teragen", type="society", skills=["command", "culture", "integrity", "persuasion"])
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
x = PathConnection.objects.create(name="Celebrity Rebel", path=teragen)
x = PathConnection.objects.create(name="Former Utopian", path=teragen)
x = PathConnection.objects.create(name="Mystic Seeker", path=teragen)
x = PathConnection.objects.create(name="Nova Rights Activist", path=teragen)
x = PathConnection.objects.create(name="Salon Philosopher", path=teragen)
x = PathConnection.objects.create(name="Would-be Cult Leader", path=teragen)
directive = Path.objects.create(name="The Directive", type="society", skills=["aim", "larceny", "integrity", "technology"])
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
x = PathConnection.objects.create(name="Government Intelligence Agent", path=directive)
x = PathConnection.objects.create(name="Law Enforcement Officer", path=directive)
x = PathConnection.objects.create(name="Military Special Ops", path=directive)
x = PathConnection.objects.create(name="Scientific or Technical Expert", path=directive)
elites = Path.objects.create(name="Elites", type="society", skills=["aim", "athletics", "close_combat", "integrity"])
elites.edges.add(always_prepared, danger_sense, fame, hardy, small_unit_tactics, wealth)
elites.save()
x = PathConnection.objects.create(name="Elite Celebrity", path=elites)
x = PathConnection.objects.create(name="Former Soldier", path=elites)
x = PathConnection.objects.create(name="Nova Ronin", path=elites)
x = PathConnection.objects.create(name="Paramilitary Commander", path=elites)
x = PathConnection.objects.create(name="Security Consultant", path=elites)
daedalus_league = Path.objects.create(name="The Daedalus League", type="society", skills=["athletics", "pilot", "science", "technology"])
daedalus_league.edges.add(
    microgravity_training,
    breath_control,
    direction_sense,
    fame,
    hardy,
    keen_sense_sight, keen_sense_hearing, keen_sense_touch, keen_sense_smell_and_taste,
    ms_fix_it,
)
daedalus_league.save()
x = PathConnection.objects.create(name="Project Utopia", path=daedalus_league)
x = PathConnection.objects.create(name="NASA", path=daedalus_league)
x = PathConnection.objects.create(name="ESA", path=daedalus_league)
x = PathConnection.objects.create(
    name="State or Private Space Agencies", path=daedalus_league
)
x = PathConnection.objects.create(name="Spacesuit Designer", path=daedalus_league)
x = PathConnection.objects.create(name="Astronomy Hobbyist", path=daedalus_league)
x = PathConnection.objects.create(name="Astrophysics Professor", path=daedalus_league)
x = PathConnection.objects.create(name="Test Pilot", path=daedalus_league)

nine = Path.objects.create(name="9", type="society", skills=["aim", "larceny", "integrity", "technology"], gift_keywords=["aim", "larceny", "technology"])
nine.edges.add(always_prepared, covert, hair_trigger_reflexes, small_unit_tactics, sniper, wealth)
nine.save()
PathConnection.objects.create(name="FBI Agent", path=nine)
PathConnection.objects.create(name="Safe House Owner", path=nine)
PathConnection.objects.create(name="Weapons Dealer", path=nine)
PathConnection.objects.create(name="Lab Worker", path=nine)

aeon_society = Path.objects.create(name="Aeon Society", type="society", skills=["aim", "close_combat", "enigmas", "pilot"], gift_keywords=["close_combat", "enigmas", "pilot"])
aeon_society.edges.add(always_prepared, direction_sense, artifact, library, wealth)
aeon_society.save()
PathConnection.objects.create(name="High Political Figure", path=aeon_society)
PathConnection.objects.create(name="Military Advisor", path=aeon_society)
PathConnection.objects.create(name="Large Charity Fund Manager", path=aeon_society)

archangel = Path.objects.create(name="Archangel", type="society", skills=["close_combat", "empathy", "integrity", "persuasion"], gift_keywords=["close_combat", "empathy", "persuasion"])
archangel.edges.add(adrenaline_spike, big_hearted, endurance, ironwill, patron, skilled_liar, speed_reading)
archangel.save()
PathConnection.objects.create(name="Pro Bono Lawyer", path=archangel)
PathConnection.objects.create(name="Witness Protection Officer", path=archangel)
PathConnection.objects.create(name="Homeland Security Officer", path=archangel)
PathConnection.objects.create(name="Criminal with a Heart of Gold", path=archangel)
PathConnection.objects.create(name="Hactivist", path=archangel)

global_cartography_initiative = Path.objects.create(name="The Global Cartography Initiative", type="society", skills=["enigmas", "humanities", "larceny", "survival"], gift_keywords=["enigmas", "humanities", "survival"])
global_cartography_initiative.edges.add(artifact, direction_sense, library, patron)
global_cartography_initiative.save()
PathConnection.objects.create(name="Black Market Artifact Dealer", path=global_cartography_initiative)
PathConnection.objects.create(name="Smuggler", path=global_cartography_initiative)
PathConnection.objects.create(name="Museum Curator", path=global_cartography_initiative)
PathConnection.objects.create(name="Border Guard", path=global_cartography_initiative)
PathConnection.objects.create(name="Journalist", path=global_cartography_initiative)
PathConnection.objects.create(name="Mercenery", path=global_cartography_initiative)
PathConnection.objects.create(name="Pirate", path=global_cartography_initiative)
PathConnection.objects.create(name="Pirate Hunter", path=global_cartography_initiative)

neptune_foundation = Path.objects.create(name="The Neptune Foundation", type="society", skills=["command", "integrity", "medicine", "persuasion"], gift_keywords=["command", "integrity", "persuasion"])
neptune_foundation.edges.add(fame, ironwill, keen_sense_sight, keen_sense_hearing, keen_sense_touch, keen_sense_smell_and_taste, patron, photographic_memory, superior_trait_intellect, superior_trait_cunning, superior_trait_resolve, superior_trait_might, superior_trait_dexterity, superior_trait_stamina, superior_trait_presence, superior_trait_manipulation, superior_trait_composure)
neptune_foundation.save()
PathConnection.objects.create(name="Aid Worker", path=neptune_foundation)
PathConnection.objects.create(name="Emergency Services", path=neptune_foundation)
PathConnection.objects.create(name="ER Doctor", path=neptune_foundation)
PathConnection.objects.create(name="Free-Clinic Volunteer", path=neptune_foundation)
PathConnection.objects.create(name="Local Government Representative", path=neptune_foundation)

pharoahs_lightkeepers = Path.objects.create(name="The Pharoah's Lightkeepers", type="society", skills=["aim", "close_combat", "enigmas", "pilot"], gift_keywords=["enigmas", "humanities", "larceny"])
pharoahs_lightkeepers.edges.add(artifact, danger_sense, library, skilled_liar, small_unit_tactics, sniper)
pharoahs_lightkeepers.save()
PathConnection.objects.create(name="Journalists", path=pharoahs_lightkeepers)
PathConnection.objects.create(name="Military Personnel", path=pharoahs_lightkeepers)
PathConnection.objects.create(name="Other Lightkeeper Teams", path=pharoahs_lightkeepers)
PathConnection.objects.create(name="Police Officers", path=pharoahs_lightkeepers)


alert_status_1 = Path.objects.create(name="Alert Status 1", type="society", skills=["aim", "enigmas", "persuasion", "technology"], gift_keywords=["aim", "persuasion", "technology"])
alert_status_1.edges.add(alternate_identity, armor_expert, cool_under_fire, covert, direction_sense, sniper, trick_shooter)
alert_status_1.save()
PathConnection.objects.create(name="Committee Member", path=alert_status_1)
PathConnection.objects.create(name="National Intelligence Director", path=alert_status_1)
PathConnection.objects.create(name="Friendly Agent of a Rival Nation", path=alert_status_1)

la_revolte_eclatante = Path.objects.create(name="La Revolte Eclatante", type="society", skills=["aim", "medicine", "pilot", "technology"], gift_keywords=["aim", "medicine", "pilot"])
la_revolte_eclatante.edges.add(alternate_identity, cool_under_fire, demolitions_training, safe_house, small_unit_tactics, swift, tough_cookie, weak_spots)
la_revolte_eclatante.save()
PathConnection.objects.create(name="Idealistic Priests", path=la_revolte_eclatante)
PathConnection.objects.create(name="Labor Organizers", path=la_revolte_eclatante)
PathConnection.objects.create(name="Medical Relief Personnel", path=la_revolte_eclatante)
PathConnection.objects.create(name="Street Gangs", path=la_revolte_eclatante)
PathConnection.objects.create(name="Violent Anarchists", path=la_revolte_eclatante)

les_fantomes = Path.objects.create(name="Les Fantomes", type="society", skills=["athletics", "culture", "larceny", "technology"], gift_keywords=["athletics", "culture", "larceny"])
les_fantomes.edges.add(covert, free_running, safe_house, skilled_liar, wealth)
les_fantomes.save()
PathConnection.objects.create(name="Fence", path=les_fantomes)
PathConnection.objects.create(name="Forger", path=les_fantomes)
PathConnection.objects.create(name="Grateful Museum Official", path=les_fantomes)
PathConnection.objects.create(name="Grudgingly Respectful Interpol Agent", path=les_fantomes)

noer = Path.objects.create(name="National Office of Emergency Research", type="society", skills=["command", "enigmas", "humanities", "persuasion"], gift_keywords=["command", "enigmas", "humanities"])
noer.edges.add(always_prepared, artifact, covert, patron, small_unit_tactics, speed_reading)
noer.save()
PathConnection.objects.create(name="Anonymous Online Source", path=noer)
PathConnection.objects.create(name="Off-Record Inside Informant", path=noer)
PathConnection.objects.create(name="Paraphysical Research Study Group", path=noer)
PathConnection.objects.create(name="UFO Witness", path=noer)

theseus_club = Path.objects.create(name="The Theseus Club", type="society", skills=["aim", "athletics", "larceny", "technology"], gift_keywords=["aim", "athletics", "larceny"])
theseus_club.edges.add(alternate_identity, always_prepared, endurance, danger_sense, demolitions_training, small_unit_tactics, trick_shooter)
theseus_club.save()
PathConnection.objects.create(name="FBI Agent", path=theseus_club)
PathConnection.objects.create(name="Local Hunting-Club President", path=theseus_club)
PathConnection.objects.create(name="Wealthy Do-Gooder", path=theseus_club)

transcendant_alliance = Path.objects.create(name="The Transcendent Alliance", type="society", skills=["culture", "medicine", "science", "technology"], gift_keywords=["medicine", "science", "technology"])
transcendant_alliance.edges.add(lightning_calculator, ms_fix_it, photographic_memory, superior_trait_intellect, superior_trait_cunning, superior_trait_resolve, superior_trait_might, superior_trait_dexterity, superior_trait_stamina, superior_trait_presence, superior_trait_manipulation, superior_trait_composure, weak_spots, wealth)
transcendant_alliance.save()
PathConnection.objects.create(name="Cutting-Edge Scientists", path=transcendant_alliance)
PathConnection.objects.create(name="Gray-Market Pharmaceutical Manufacturers", path=transcendant_alliance)
PathConnection.objects.create(name="International Smugglers", path=transcendant_alliance)
PathConnection.objects.create(name="Skilled Programmers", path=transcendant_alliance)

triton_foundation = Path.objects.create(name="Triton Foundation", type="society", skills=["enigmas", "medicine", "persuasion", "science"], gift_keywords=["medicine", "persuasion", "science"])
triton_foundation.edges.add(ambidextrous, big_hearted, ironwill, library, superior_trait_intellect, superior_trait_cunning, superior_trait_resolve, superior_trait_might, superior_trait_dexterity, superior_trait_stamina, superior_trait_presence, superior_trait_manipulation, superior_trait_composure, wealth)
triton_foundation.save()
PathConnection.objects.create(name="Medical Researcher", path=triton_foundation)
PathConnection.objects.create(name="Famous Surgeon", path=triton_foundation)
PathConnection.objects.create(name="President of a Charity", path=triton_foundation)
PathConnection.objects.create(name="Local Public Leader", path=triton_foundation)
PathConnection.objects.create(name="Dean of a Research College", path=triton_foundation)

MomentOfInspiration.objects.create(name="Chance Birth", attributes=["might", "dexterity", "stamina", "presence", "manipulation", "composure", "intellect", "cunning", "resolve"])
MomentOfInspiration.objects.create(name="Exposure to Flux", attributes=["might", "dexterity", "stamina"])
MomentOfInspiration.objects.create(name="Life-Threatening Accidenct", attributes=["stamina"])
MomentOfInspiration.objects.create(name="Personal Failure", attributes=["resolve"])
MomentOfInspiration.objects.create(name="Saving Someone Else's Life", attributes=["composure"])
MomentOfInspiration.objects.create(name="Social Challenge", attributes=["presence", "manipulation", "composure"])
MomentOfInspiration.objects.create(name="Sudden Realization", attributes=["cunning"])
MomentOfInspiration.objects.create(name="Tragic Loss", attributes=["intellect", "cunning", "resolve"])
MomentOfInspiration.objects.create(name="Violence", attributes=["might"])

Gift.objects.create(name="A Friend in Every Port", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="A Great Memory for Faces", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="Always Connected", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="Armor of Fate", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="Battlefield Entanglement", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="I Respect You", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Determined Defender", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="Device Mogul", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Don't Scratch the Paint!", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Easily Dismissed", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="Fairweather Friend", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="For You", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Destined for Damage", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Impeccable Timing", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="Knee Deep in Brass", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Love and Loss", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Navigation Hazard", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="Roll the Dice", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Name in the Lights", keywords=["constant", "luck"], prereqs=[])
Gift.objects.create(name="Stash in Every City", keywords=["momentary", "luck"], prereqs=[("Wealth", 3)])
Gift.objects.create(name="Untouchable", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Voiding the Warranty", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Whodunnit", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="X Marks the Spot", keywords=["momentary", "luck"], prereqs=[])
Gift.objects.create(name="Acme of Unchallenged Reason", keywords=["intellect", "momentary"], prereqs=[("intellect", 3)])
Gift.objects.create(name="Instant Expert", keywords=["intellect", "momentary"], prereqs=[("intellect", 3)])
Gift.objects.create(name="Rosetta Stone", keywords=["intellect", "constant"], prereqs=[("humanities", 2)])
Gift.objects.create(name="Apex Cunning", keywords=["cunning", "momentary"], prereqs=[("cunning", 4)])
Gift.objects.create(name="Behold the Halo (Cunning)", keywords=["cunning", "momentary"], prereqs=[("cunning", 3)])
Gift.objects.create(name="Behold the Halo (Manipulation)", keywords=["manipulation", "momentary"], prereqs=[("manipulation", 3)])
Gift.objects.create(name="Mirrored Sunglasses", keywords=["cunning", "constant"], prereqs=[("cunning", 2)])
Gift.objects.create(name="Don't Mess With Me", keywords=["composure", "momentary"], prereqs=[("composure", 5)])
Gift.objects.create(name="Internal Thermostat", keywords=["composure", "resolve", "stamina", "constant"], prereqs=[])
Gift.objects.create(name="The Late, Late Shift (Composure)", keywords=["composure", "constant"], prereqs=[("composure", 2)])
Gift.objects.create(name="The Late, Late Shift (Resolve)", keywords=["resolve", "constant"], prereqs=[("resolve", 2)])
Gift.objects.create(name="The Late, Late Shift (Stamina)", keywords=["stamina", "constant"], prereqs=[("stamina", 2)])
Gift.objects.create(name="Superlative Poise", keywords=["composure", "constant"], prereqs=[("composure", 3)])
Gift.objects.create(name="Fists of Stone", keywords=["might", "constant"], prereqs=[("might", 3)])
Gift.objects.create(name="Last-Ditch Effort", keywords=["might", "momentary"], prereqs=[("might", 4)])
Gift.objects.create(name="Speak Softly", keywords=["might", "constant"], prereqs=[("might", 3)])
Gift.objects.create(name="Eyes Life a Cat", keywords=["dexterity", "constant"], prereqs=[("larceny", 1)])
Gift.objects.create(name="On the Head of a Pin", keywords=["dexterity", "constant"], prereqs=[("dexterity", 2)])
Gift.objects.create(name="Pretty Damned Fast", keywords=["dexterity", "momentary"], prereqs=[])
Gift.objects.create(name="Cast-Iron Stomach", keywords=["stamina", "constant"], prereqs=[("stamina", 3)])
Gift.objects.create(name="Iron Lungs", keywords=["stamina", "constant"], prereqs=[("stamina", 2)])
Gift.objects.create(name="Unrelenting", keywords=["stamina", "momentary"], prereqs=[("stamina", 3)])
Gift.objects.create(name="Evil Overlord", keywords=["presence", "momentary"], prereqs=[("command", 2)])
Gift.objects.create(name="Love Me and Despair", keywords=["presence", "constant"], prereqs=[("presence", 3)])
Gift.objects.create(name="The Room Where It Happens", keywords=["presence", "momentary"], prereqs=[])
Gift.objects.create(name="But Before I Die", keywords=["manipulation", "momentary"], prereqs=[("manipulation", 3)])
Gift.objects.create(name="Contain the Calamity", keywords=["manipulation", "momentary"], prereqs=[("manipulation", 3)])
Gift.objects.create(name="Never a Stranger", keywords=["manipulation", "constant"], prereqs=[("manipulation", 2)])
Gift.objects.create(name="Second Chance, First Impression", keywords=["manipulation", "momentary"], prereqs=[("manipulation", 2)])
Gift.objects.create(name="Calm Blue Ocean", keywords=["resolve", "momentary"], prereqs=[("resolve", 4)])
Gift.objects.create(name="Indomitable Will (Resolve)", keywords=["resolve", "constant"], prereqs=[("resolve", 2)])
Gift.objects.create(name="Indomitable Will (Integrity)", keywords=["resolve", "constant"], prereqs=[("integrity", 3)])
Gift.objects.create(name="An Extension of Myself (Aim)", keywords=["constant", "aim"], prereqs=[("aim", 3)])
Gift.objects.create(name="An Extension of Myself (Close Combat)", keywords=["constant", "close_combat"], prereqs=[("close_combat", 3)])
Gift.objects.create(name="Murderous Totality (Aim)", keywords=["aim" "momentary"], prereqs=[("aim", 3)])
Gift.objects.create(name="Murderous Totality (Close Combat)", keywords=["close_combat", "momentary"], prereqs=[("close_combat", 3)])
Gift.objects.create(name="Sharpshooter", keywords=["momentary", "aim"], prereqs=[("aim", 4)])
Gift.objects.create(name="Steady Hands", keywords=["constant", "aim"], prereqs=[])
Gift.objects.create(name="Trigger Discipline", keywords=["constant", "aim"], prereqs=[("aim", 2)])
Gift.objects.create(name="Warrior's Eye", keywords=["momentary", "aim", "close_combat"], prereqs=[])
Gift.objects.create(name="Contortionist", keywords=["constant", "athletics"], prereqs=[])
Gift.objects.create(name="Fight Choreographer", keywords=["constant", "athletics", "close_combat"], prereqs=[("athletics", 2)])
Gift.objects.create(name="Lightning Reflexes (Athletics)", keywords=["constant", "athletics"], prereqs=[("athletics", 2)])
Gift.objects.create(name="Lightning Reflexes (Empathy)", keywords=["constant", "empathy"], prereqs=[("empathy", 2)])
Gift.objects.create(name="Moving Target", keywords=["constant", "athletics"], prereqs=[("athletics", 2)])
Gift.objects.create(name="Swan Dive", keywords=["momentary", "athletics"], prereqs=[])
Gift.objects.create(name="Enhanced Impact", keywords=["momentary", "close_combat"], prereqs=[("close_combat", 3)])
Gift.objects.create(name="Hidden Advantage", keywords=["momentary", "close_combat", "larceny"], prereqs=[("close_combat", 3)])
Gift.objects.create(name="Say That To My Face (Close Combat)", keywords=["momentary", "close_combat"], prereqs=[("close_combat", 2)])
Gift.objects.create(name="Say That To My Face (Command)", keywords=["momentary", "command"], prereqs=[("command", 2)])
Gift.objects.create(name="After School Special (Command)", keywords=["momentary", "command"], prereqs=[("command", 4)])
Gift.objects.create(name="After School Special (Persuasion)", keywords=["momentary", "persuasion"], prereqs=[("persuasion", 4)])
Gift.objects.create(name="Chess Master", keywords=["momentary", "command"], prereqs=[("command", 3)])
Gift.objects.create(name="Curses!", keywords=["momentary", "command", "persuasion"], prereqs=[("command", 2)])
Gift.objects.create(name="The In and In", keywords=["constant", "command", "larceny"], prereqs=[("larceny", 2)])
Gift.objects.create(name="Public Education (Culture)", keywords=["momentary", "command", "culture"], prereqs=[("command", 2), ("culture", 3)])
Gift.objects.create(name="Public Education (Humanities)", keywords=["momentary", "command", "humanities"], prereqs=[("command", 2), ("humanities", 3)])
Gift.objects.create(name="Public Education (Science)", keywords=["momentary", "command", "science"], prereqs=[("command", 2), ("science", 3)])
Gift.objects.create(name="Public Education (Technology)", keywords=["momentary", "command", "technology"], prereqs=[("command", 2), ("technology", 3)])
Gift.objects.create(name="Rousing Speech", keywords=["momentary", "command"], prereqs=[])
Gift.objects.create(name="Theatre of Conflict", keywords=["momentary", "command"], prereqs=[])
Gift.objects.create(name="Disposable Minion", keywords=["momentary", "command"], prereqs=[("command", 3)])
Gift.objects.create(name="Cold Read", keywords=["constant", "culture", "empathy"], prereqs=[])
Gift.objects.create(name="Forgettable (Culture)", keywords=["momentary", "culture"], prereqs=[("culture", 3)])
Gift.objects.create(name="Forgettable (Larceny)", keywords=["momentary", "larceny"], prereqs=[("larceny", 3)])
Gift.objects.create(name="Politico", keywords=["momentary", "culture"], prereqs=[("culture", 3)])
Gift.objects.create(name="The Right Climate (Culture)", keywords=["momentary", "culture"], prereqs=[("culture", 3)])
Gift.objects.create(name="The Right Climate (Empathy)", keywords=["momentary", "empathy"], prereqs=[("empathy", 3)])
Gift.objects.create(name="Ripped From the Headlines", keywords=["constant", "culture"], prereqs=[])
Gift.objects.create(name="That's Bad Luck", keywords=["constant", "culture"], prereqs=[])
Gift.objects.create(name="The Hook", keywords=["constant", "empathy"], prereqs=[])
Gift.objects.create(name="I Know That Feel", keywords=["momentary", "empathy"], prereqs=[("empathy", 3)])
Gift.objects.create(name="Know Thine Enemy", keywords=["momentary", "empathy"], prereqs=[("empathy", 2)])
Gift.objects.create(name="Method Actor", keywords=["momentary", "empathy"], prereqs=[("empathy", 3)])
Gift.objects.create(name="True Friendship", keywords=["constant", "empathy"], prereqs=[("empathy", 5)])
Gift.objects.create(name="Code Talker", keywords=["momentary", "enigmas"], prereqs=[("enigmas", 2)])
Gift.objects.create(name="Deep System Scan (Enigmas)", keywords=["momentary", "enigmas"], prereqs=[("enigmas", 3)])
Gift.objects.create(name="Deep System Scan (Technology)", keywords=["momentary", "technology"], prereqs=[("technology", 3)])
Gift.objects.create(name="Fortean Experience", keywords=["momentary", "enigmas", "science"], prereqs=[("enigmas", 1), ("science", 3)])
Gift.objects.create(name="Irons in the Fire (Enigmas)", keywords=["momentary", "enigmas"], prereqs=[("enigmas", 3)])
Gift.objects.create(name="Irons in the Fire (Humanities)", keywords=["momentary", "humanities"], prereqs=[("humanities", 3)])
Gift.objects.create(name="Irons in the Fire (Medicine)", keywords=["momentary", "medicine"], prereqs=[("medicine", 3)])
Gift.objects.create(name="Irons in the Fire (Science)", keywords=["momentary", "science"], prereqs=[("science", 3)])
Gift.objects.create(name="Irons in the Fire (Technology)", keywords=["momentary", "technology"], prereqs=[("technology", 3)])
Gift.objects.create(name="Mystery Archaeology", keywords=["constant", "enigmas"], prereqs=[])
Gift.objects.create(name="Plot Twist", keywords=["momentary", "enigmas"], prereqs=[("enigmas", 3)])
Gift.objects.create(name="Loophole", keywords=["momentary", "humanities"], prereqs=[("humanities", 3)])
Gift.objects.create(name="No Stone Unturned", keywords=["constant", "humanities", "science"], prereqs=[])
Gift.objects.create(name="Repeating History", keywords=["momentary", "humanities"], prereqs=[])
Gift.objects.create(name="Steganographer", keywords=["constant", "humanities"], prereqs=[("humanities", 3)])
Gift.objects.create(name="Don't Lie to Me", keywords=["constant", "integrity"], prereqs=[("integrity", 2)])
Gift.objects.create(name="Reverse-Engineering Calamity", keywords=["momentary", "integrity"], prereqs=[])
Gift.objects.create(name="Self-Sense", keywords=["constant", "integrity", "medicine"], prereqs=[])
Gift.objects.create(name="Shameless Lying Smile (Integrity)", keywords=["momentary", "integrity"], prereqs=[("integrity", 2)])
Gift.objects.create(name="Shameless Lying Smile (Persuasion)", keywords=["momentary", "persuasion"], prereqs=[("persuasion", 2)])
Gift.objects.create(name="Take it on the Chin", keywords=["momentary", "integrity"], prereqs=[])
Gift.objects.create(name="Unquestionable", keywords=["momentary", "integrity"], prereqs=[("integrity", 3)])
Gift.objects.create(name="A Special Present", keywords=["momentary", "larceny"], prereqs=[("larceny", 2)])
Gift.objects.create(name="What Tripwire?", keywords=["momentary", "larceny"], prereqs=[("larceny", 3)])
Gift.objects.create(name="Listen In", keywords=["momentary", "larceny"], prereqs=[("larceny", 3)])
Gift.objects.create(name="Nimble-Fingered", keywords=["momentary", "larceny"], prereqs=[("larceny", 2)])
Gift.objects.create(name="Slip the Cuffs (Larceny)", keywords=["momentary", "larceny"], prereqs=[("larceny", 2)])
Gift.objects.create(name="Slip the Cuffs (Technology)", keywords=["momentary", "technology"], prereqs=[("technology", 2)])
Gift.objects.create(name="Doctor of Destruction", keywords=["constant", "aim", "close_combat", "medicine"], prereqs=[("medicine", 4)])
Gift.objects.create(name="Home-Cooked Meal", keywords=["constant", "medicine"], prereqs=[("medicine", 3)])
Gift.objects.create(name="Instant Diagnosis", keywords=["momentary", "medicine"], prereqs=[("medicine", 2)])
Gift.objects.create(name="Shot Caller", keywords=["momentary", "aim", "close_combat", "medicine"], prereqs=[("medicine", 3)])
Gift.objects.create(name="Worse Than It Looks", keywords=["momentary", "medicine"], prereqs=[("medicine", 3)])
Gift.objects.create(name="Disarming Candor", keywords=["momentary", "persuasion"], prereqs=[])
Gift.objects.create(name="I'm On The List", keywords=["momentary", "persuasion"], prereqs=[("persuasion", 3)])
Gift.objects.create(name="Scathing Insult", keywords=["constant", "persusion"], prereqs=[("persuasion", 2)])
Gift.objects.create(name="Steely Gaze (Presence)", keywords=["momentary", "persuasion"], prereqs=[("persuasion", 2), ("presence", 3)])
Gift.objects.create(name="Steely Gaze (Manipulation)", keywords=["momentary", "persuasion"], prereqs=[("persuasion", 2), ("manipulation", 3)])
Gift.objects.create(name="Steely Gaze (Composure)", keywords=["momentary", "persuasion"], prereqs=[("persuasion", 2), ("composure", 3)])
Gift.objects.create(name="Daredevil", keywords=["momentary", "pilot"], prereqs=[("pilot", 3)])
Gift.objects.create(name="Greased Lightning", keywords=["momentary", "pilot"], prereqs=[("pilot", 3)])
Gift.objects.create(name="Head 'Em Off At The Pass", keywords=["constant", 'pilot'], prereqs=[])
Gift.objects.create(name="Look Ma, No Hands!", keywords=["momentary", "pilot"], prereqs=[("pilot", 3)])
Gift.objects.create(name="Wheelman", keywords=["constant", "pilot"], prereqs=[('pilot', 2)])
Gift.objects.create(name="Eureka!", keywords=["constant", "science"], prereqs=[("science", 3)])
Gift.objects.create(name="Discovery Rush", keywords=["momentary", "science"], prereqs=[])
Gift.objects.create(name="Blind Spots", keywords=["constant", "survival"], prereqs=[("survival", 2)])
Gift.objects.create(name="Get the Drop", keywords=["momentary", "survival"], prereqs=[("survival", 2)])
Gift.objects.create(name="Internal Compass", keywords=["constant", "survival"], prereqs=[])
Gift.objects.create(name="Know Your Quarry", keywords=["momentary", "survival"], prereqs=[("survival", 2)])
Gift.objects.create(name="Savage Beast", keywords=["momentary", "survival"], prereqs=[("survival", 2)])
Gift.objects.create(name="Through Wild Eyes", keywords=["momentary", "survival"], prereqs=[])
Gift.objects.create(name="Whisperer", keywords=["constant", "survival"], prereqs=[("survival", 2)])
Gift.objects.create(name="Wilderness Guide", keywords=["momentary", "survival"], prereqs=[("survival", 3)])
Gift.objects.create(name="Cut the Red Wire", keywords=["momentary", "technology"], prereqs=[])
Gift.objects.create(name="Digital Crackerjack", keywords=["momentary", "technology"], prereqs=[])
Gift.objects.create(name="Quick Fix", keywords=["momentary", "technology"], prereqs=[("technology", 3)])
Gift.objects.create(name="Sawed Off", keywords=["momentary", "technology"], prereqs=[("technology", 3)])

accuracy = MegaEdge.objects.create(name="Accuracy", ratings=[1, 2, 3, 4, 5], prereqs=[("mega_dexterity", 2)])
adaptation = MegaEdge.objects.create(name="Adaptation", ratings=[1], prereqs=[("mega_stamina", 2)])
x = MegaEdge.objects.create(name="Animal Mastery", ratings=[1, 2],)
x = MegaEdge.objects.create(name="Body Modification", ratings=[1, 2, 3, 4, 5],)
calming_composure = MegaEdge.objects.create(name="Calming Composure", ratings=[1], prereqs=[("mega_composure", 1)])
compelling_presence = MegaEdge.objects.create(name="Compelling Presence", ratings=[2], prereqs=[("mega_presence", 2)])
defense = MegaEdge.objects.create(name="Defense", ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9], prereqs=[("mega_cunning", 1), ("mega_dexterity", 1)])
dense_flesh = MegaEdge.objects.create(name="Dense Flesh", ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9], prereqs=[("mega_stamina", 1)])
detection = MegaEdge.objects.create(name="Detection", ratings=[1, 2, 3, 4, 5], prereqs=[("mega_cunning", 1)])
digital_manipulation = MegaEdge.objects.create(name="Digital Manipulation", ratings=[1, 2, 3, 4, 5], prereqs=[("mega_intellect", 1)])
digital_scan = MegaEdge.objects.create(name="Digital Scan", ratings=[1], prereqs=[("mega_cunning", 1)])
dreadful_presence = MegaEdge.objects.create(name="Dreadful Presence", ratings=[1], prereqs=[("mega_presence", 1)])
fast_worker = MegaEdge.objects.create(name="Fast Worker", ratings=[2], prereqs=[("mega_resolve", 1)])
foresight = MegaEdge.objects.create(name="Foresight", ratings=[1], prereqs=[("mega_cunning", 1), ("mega_intellect", 1)])
x = MegaEdge.objects.create(name="Homunculus", ratings=[1],)
hypnotic_presence = MegaEdge.objects.create(name="Hypnotic Presence", ratings=[1], prereqs=[("mega_manipulation", 1)])
immediate_connection = MegaEdge.objects.create(name="Immediate Connection", ratings=[1], prereqs=[("mega_presence", 1)])
immunity = MegaEdge.objects.create(name="Immunity", ratings=[1], prereqs=[("mega_stamina", 1)])
instant_expert = MegaEdge.objects.create(name="Instant Expert", ratings=[1], prereqs=[("mega_intellect", 1)])
instant_influence = MegaEdge.objects.create(name="Instant Influence", ratings=[1], prereqs=[("mega_presence", 1), ("mega_manipulation", 1)])
inventor = MegaEdge.objects.create(name="Inventor", ratings=[2], prereqs=[("mega_intellect", 1)])
mass_influence = MegaEdge.objects.create(name="Mass Influence", ratings=[1, 2, 3, 4, 5], prereqs=[("mega_manipulation", 1), ("mega_presence", 1)])
mastermind = MegaEdge.objects.create(name="Mastermind", ratings=[1], prereqs=[("mega_intellect", 1)])
mega_crush = MegaEdge.objects.create(name="Mega-Crush", ratings=[1], prereqs=[("mega_might", 1)])
mega_hearing = MegaEdge.objects.create(name="Mega-Hearing", ratings=[1], prereqs=[("mega_cunning", 1)])
mega_lifting = MegaEdge.objects.create(name="Mega-Lifting", ratings=[1], prereqs=[("mega_might", 1)])
mega_scent = MegaEdge.objects.create(name="Mega-Scent", ratings=[1], prereqs=[("mega_cunning", 1)])
mega_speed = MegaEdge.objects.create(name="Mega-Speed", ratings=[1], prereqs=[("mega_dexterity", 1)])
mega_vision = MegaEdge.objects.create(name="Mega-Vision", ratings=[1], prereqs=[("mega_cunning", 1)])
micro_manipulation = MegaEdge.objects.create(name="Micro-Manipulation", ratings=[1], prereqs=[("mega_cunning", 1)])
mind_over_matter = MegaEdge.objects.create(name="Mind Over Matter", ratings=[1], prereqs=[("mega_resolve", 1)])
x = MegaEdge.objects.create(name="Movement Mode", ratings=[1, 2, 3, 4, 5],)
multitasking = MegaEdge.objects.create(name="Multitasking", ratings=[1], prereqs=[("mega_dexterity", 1), ("mega_cunning", 1)])
overwhelming_denial = MegaEdge.objects.create(name="Overwhelming Denial", ratings=[1], prereqs=[("mega_composure", 1), ("Dreadful Presence", 1)])
perfectionist = MegaEdge.objects.create(name="Perfectionist", ratings=[2], prereqs=[("mega_intellect", 1)])
pretercognition = MegaEdge.objects.create(name="Pretercognition", ratings=[1], prereqs=[("mega_cunning", 1)])
prodigy_aim = MegaEdge.objects.create(name="Prodigy (Aim)", ratings=[1], prereqs=[("aim", 1)])
prodigy_athletics = MegaEdge.objects.create(name="Prodigy (Athletics)", ratings=[1], prereqs=[("athletics", 1)])
prodigy_close_combat = MegaEdge.objects.create(name="Prodigy (Close Combat)", ratings=[1], prereqs=[("close_combat", 1)])
prodigy_command = MegaEdge.objects.create(name="Prodigy (Command)", ratings=[1], prereqs=[("command", 1)])
prodigy_culture = MegaEdge.objects.create(name="Prodigy (Culture)", ratings=[1], prereqs=[("culture", 1)])
prodigy_empathy = MegaEdge.objects.create(name="Prodigy (Empathy)", ratings=[1], prereqs=[("empathy", 1)])
prodigy_enigmas = MegaEdge.objects.create(name="Prodigy (Enigmas)", ratings=[1], prereqs=[("enigmas", 1)])
prodigy_humanities = MegaEdge.objects.create(name="Prodigy (Humanities)", ratings=[1], prereqs=[("humanities", 1)])
prodigy_integrity = MegaEdge.objects.create(name="Prodigy (Integrity)", ratings=[1], prereqs=[("integrity", 1)])
prodigy_larceny = MegaEdge.objects.create(name="Prodigy (Larceny)", ratings=[1], prereqs=[("larceny", 1)])
prodigy_medicine = MegaEdge.objects.create(name="Prodigy (Medicine)", ratings=[1], prereqs=[("medicine", 1)])
prodigy_persuasion = MegaEdge.objects.create(name="Prodigy (Persuasion)", ratings=[1], prereqs=[("persuasion", 1)])
prodigy_pilot = MegaEdge.objects.create(name="Prodigy (Pilot)", ratings=[1], prereqs=[("pilot", 1)])
prodigy_science = MegaEdge.objects.create(name="Prodigy (Science)", ratings=[1], prereqs=[("science", 1)])
prodigy_survival = MegaEdge.objects.create(name="Prodigy (Survival)", ratings=[1], prereqs=[("survival", 1)])
prodigy_technology = MegaEdge.objects.create(name="Prodigy (Technology)", ratings=[1], prereqs=[("technology", 1)])
prolific = MegaEdge.objects.create(name="Prolific", ratings=[1, 2, 3, 4, 5], prereqs=[("mega_cunning", 2)])
q_tech = MegaEdge.objects.create(name="Q-Tech", ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],)
quantum_conversion = MegaEdge.objects.create(name="Quantum Conversion", ratings=[1],)
quantum_leap = MegaEdge.objects.create(name="Quantum Leap", ratings=[1], prereqs=[("mega_might", 2)])
x = MegaEdge.objects.create(name="Quantum Sense", ratings=[1],)
quickness = MegaEdge.objects.create(name="Quickness", ratings=[1], prereqs=[("mega_dexterity", 1)])
rapid_strike = MegaEdge.objects.create(name="Rapid Strike", ratings=[1], prereqs=[("mega_dexterity", 1), ("mega_cunning", 1)])
regeneration = MegaEdge.objects.create(name="Regeneration", ratings=[1], prereqs=[("mega_stamina", 1), ("mega_resolve", 1)])
resourceful = MegaEdge.objects.create(name="Resourceful", ratings=[2], prereqs=[("mega_cunning", 2)])
revealing_composure = MegaEdge.objects.create(name="Revealing Composure", ratings=[1], prereqs=[("mega_composure", 1)])
revealing_read = MegaEdge.objects.create(name="Revealing Read", ratings=[1], prereqs=[("mega_cunning", 1)])
spectrum_vision = MegaEdge.objects.create(name="Spectrum Vision", ratings=[1], prereqs=[("Mega Vision", 1)])
scanning_sense = MegaEdge.objects.create(name="Scanning Sense", ratings=[1, 2, 3], prereqs=[("Spectrum Vision", 1)])
sensory_shield = MegaEdge.objects.create(name="Sensory Shield", ratings=[1], prereqs=[("mega_cunning", 1), ("mega_resolve", 1), ("mega_stamina", 1)])
shockwave = MegaEdge.objects.create(name="Shockwave", ratings=[1], prereqs=[("mega_might", 1)])
subtle_presence = MegaEdge.objects.create(name="Subtle Presence", ratings=[1], prereqs=[("mega_composure", 1)])
telecommunication = MegaEdge.objects.create(name="Telecommunication", ratings=[1],)
technique = MegaEdge.objects.create(name="Technique", ratings=[1, 2, 3, 4, 5], prereqs=[("quantum", "dots")])
technologist = MegaEdge.objects.create(name="Technologist", ratings=[2], prereqs=[("mega_resolve", 1)])
telepresence = MegaEdge.objects.create(name="Telepresence", ratings=[1], prereqs=[("Mass Influence", 3)])
thunderclap = MegaEdge.objects.create(name="Thunderclap", ratings=[1], prereqs=[("mega_might", 1)])
toughness = MegaEdge.objects.create(name="Toughness", ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],  prereqs=[("quantum", "dots")])
ultraperipheral_perception = MegaEdge.objects.create(name="Ultraperipherial Perception", ratings=[1], prereqs=[("mega_cunning", 1)])
universal_translator = MegaEdge.objects.create(name="Universal Translator", ratings=[1], prereqs=[("mega_intellect", 3)])

absorption = Power.objects.create(
    name="Absorption",
    quantum_minimum=2,
    action_type="reflexive",
    cost=0,
    dicepool="Quantum+Power",
    range="personal",
    duration="continuous",
)
broad = Tag.objects.create(name="Broad", ratings=[2],)
broad.permitted_powers.add(absorption)
broad.save()
siphon = Tag.objects.create(name="Siphon", ratings=[1],)
siphon.permitted_powers.add(absorption)
siphon.save()
boost = Power.objects.create(
    name="Boost",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=2,
    dicepool="",
    range="personal",
    duration="continuous",
)
extra_attribute = Tag.objects.create(name="Extra Attribute", ratings=[1],)
extra_attribute.permitted_powers.add(boost)
extra_attribute.save()
variable_attribute = Tag.objects.create(name="Variable Attribute", ratings=[1],)
variable_attribute.permitted_powers.add(boost)
variable_attribute.save()
cloak = Power.objects.create(
    name="Cloak",
    quantum_minimum=2,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="maintained",
)
chemical = Tag.objects.create(name="Chemical", ratings=[1],)
chemical.permitted_powers.add(cloak)
chemical.save()
density = Power.objects.create(
    name="Density",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)
non_living = Tag.objects.create(name="Non-Living", ratings=[1],)
non_living.permitted_powers.add(density)
non_living.save()
elemental_mastery = Power.objects.create(
    name="Elemental Mastery",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=0,
    dicepool="",
    range="personal",
    duration="instantaneous",
)
environmental_anima = Power.objects.create(
    name="Environmental Anima",
    quantum_minimum=-1,
    action_type="ordinary",
    cost=1,
    dicepool="",
    range="medium",
    duration="maintained",
)
continuous = Tag.objects.create(name="Continuous", ratings=[1],)
continuous.permitted_powers.add(environmental_anima)
continuous.save()
non_terrestrial = Tag.objects.create(name="Non-Terrestrial", ratings=[1],)
non_terrestrial.permitted_powers.add(environmental_anima)
non_terrestrial.save()
flight = Power.objects.create(
    name="Flight",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=2,
    dicepool="",
    range="personal",
    duration="maintained",
)
surfing = Tag.objects.create(name="Surfing", ratings=[-1],)
surfing.permitted_powers.add(flight)
surfing.save()
growth = Power.objects.create(
    name="Growth",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)
healing = Power.objects.create(
    name="Healing",
    quantum_minimum=2,
    action_type="ordinary",
    cost=1,
    dicepool="Quantum+Power",
    range="close",
    duration="instantaneous",
)
illusion = Power.objects.create(
    name="Illusion",
    quantum_minimum=2,
    action_type="ordinary",
    cost=3,
    dicepool="Quantum+Power",
    range="visual",
    duration="continuous",
)
molecular_chameleon = Power.objects.create(
    name="Molecular Chameleon",
    quantum_minimum=4,
    action_type="ordinary",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)
defensive = Tag.objects.create(name="Defensive", ratings=[2],)
defensive.permitted_powers.add(molecular_chameleon)
defensive.save()
energy_chameleon = Tag.objects.create(name="Energy Chameleon", ratings=[1],)
energy_chameleon.permitted_powers.add(molecular_chameleon)
energy_chameleon.save()
extra_properties = Tag.objects.create(name="Extra Properties", ratings=[1],)
extra_properties.permitted_powers.add(molecular_chameleon)
extra_properties.save()
molecular_manipulation = Power.objects.create(
    name="Molecular Manipulation",
    quantum_minimum=3,
    action_type="ordinary",
    cost=1,
    dicepool="Quantum+Power",
    range="medium",
    duration="continuous",
)
morph = Power.objects.create(
    name="Morph",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=1,
    dicepool="Quantum+Power",
    range="personal",
    duration="maintained",
)
form_mastery = Tag.objects.create(name="Form Mastery", ratings=[1],)
form_mastery.permitted_powers.add(morph)
form_mastery.save()
phasing = Power.objects.create(
    name="Phasing",
    quantum_minimum=2,
    action_type="reflexive",
    cost=2,
    dicepool="",
    range="personal",
    duration="continuous",
)
restricted_to_phase_state = Tag.objects.create(
    name="Restricted to Phase State", ratings=[-1],
)
restricted_to_phase_state.permitted_powers.add(phasing)
restricted_to_phase_state.save()
plasticity = Power.objects.create(
    name="Plasticity",
    quantum_minimum=2,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="maintained",
)
quantum_agent = Power.objects.create(
    name="Quantum Agent",
    quantum_minimum=-1,
    action_type="ordinary",
    cost=3,
    dicepool="",
    range="medium",
    duration="continuous",
)
horde = Tag.objects.create(name="Horde", ratings=[1],)
horde.permitted_powers.add(quantum_agent)
horde.save()
independent = Tag.objects.create(name="Independent", ratings=[1],)
independent.permitted_powers.add(quantum_agent)
independent.save()
memory_absorption = Tag.objects.create(name="Memory Absorption", ratings=[1],)
memory_absorption.permitted_powers.add(quantum_agent)
memory_absorption.save()
sensory_link = Tag.objects.create(name="Sensory Link", ratings=[1],)
sensory_link.permitted_powers.add(quantum_agent)
sensory_link.save()
quantum_anima = Power.objects.create(
    name="Quantum Anima",
    quantum_minimum=-1,
    action_type="ordinary",
    cost=2,
    dicepool="Quantum+Power",
    range="long",
    duration="continuous",
)
quantum_attack = Power.objects.create(
    name="Quantum Attack",
    quantum_minimum=-1,
    action_type="ordinary",
    cost=2,
    dicepool="Close Combat+Dexterity or Might, or Aim+Dexterity",
    range="close",
    duration="instantaneous",
)
quantum_aura = Power.objects.create(
    name="Quantum Aura",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="maintained",
)
quantum_construct = Power.objects.create(
    name="Quantum Construct",
    quantum_minimum=-1,  # Dots+1
    action_type="ordinary",
    cost=2,
    dicepool="",
    range="medium",
    duration="maintained",
)

durability = Tag.objects.create(name="Durability", ratings=[1],)
durability.permitted_powers.add(quantum_construct)
durability.save()
invisibility = Tag.objects.create(name="Invisibility", ratings=[1],)
invisibility.permitted_powers.add(quantum_construct)
invisibility.save()
multiple = Tag.objects.create(name="Multiple", ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],)
multiple.permitted_powers.add(quantum_construct)
multiple.save()
selective = Tag.objects.create(name="Selective", ratings=[1, 2, 3, 4, 5, 6, 7, 8, 9],)
selective.permitted_powers.add(quantum_construct)
selective.save()
size = Tag.objects.create(name="Size", ratings=[1],)
size.permitted_powers.add(quantum_construct)
size.save()
quantum_deflection = Power.objects.create(
    name="Quantum Deflection",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=2,
    dicepool="Quantum+Power",
    range="personal",
    duration="instantaneous",
)
quantum_disruption = Power.objects.create(
    name="Quantum Disruption",
    quantum_minimum=3,
    action_type="ordinary",
    cost=2,
    dicepool="Quantum+Power",
    range="medium",
    duration="instantaneous",
)
quantum_field = Power.objects.create(
    name="Quantum Field",
    quantum_minimum=-1,
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="maintained",
)
quantum_imprint = Power.objects.create(
    name="Quantum Imprint",
    quantum_minimum=4,
    action_type="ordinary",
    cost=2,
    dicepool="Quantum+Power",
    range="close",
    duration="continuous",
)
extra_power = Tag.objects.create(name="Extra Power", ratings=[1],)
extra_power.permitted_powers.add(quantum_imprint)
extra_power.save()
impersonation = Tag.objects.create(name="Impersonation", ratings=[2],)
impersonation.permitted_powers.add(quantum_imprint)
impersonation.save()
theft = Tag.objects.create(name="Theft", ratings=[2],)
theft.permitted_powers.add(quantum_imprint)
theft.save()
quantum_leech = Power.objects.create(
    name="Quantum Leech",
    quantum_minimum=2,
    action_type="ordinary",
    cost=1,
    dicepool="Quantum+Power",
    range="close",
    duration="instantaneous",
)
remote_perception = Power.objects.create(
    name="Remote Perception",
    quantum_minimum=3,
    action_type="ordinary",
    cost=2,
    dicepool="Quantum+Power",
    range="visual",
    duration="continuous",
)
shrinking = Power.objects.create(
    name="Shrinking",
    quantum_minimum=-1,  # Dots - 1
    action_type="reflexive",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)
growth_momentum = Tag.objects.create(name="Growth Momentum", ratings=[1],)
growth_momentum.permitted_powers.add(shrinking)
growth_momentum.save()
tiny_titan = Tag.objects.create(name="Tiny Titan", ratings=[1],)
tiny_titan.permitted_powers.add(shrinking)
tiny_titan.save()
shroud = Power.objects.create(
    name="Shroud",
    quantum_minimum=2,
    action_type="ordinary",
    cost=2,
    dicepool="",
    range="short",
    duration="maintained",
)
variable = Tag.objects.create(name="Variable", ratings=[1],)
variable.permitted_powers.add(phasing, shroud, environmental_anima)
variable.save()
broadband = Tag.objects.create(name="Broadband", ratings=[1],)
broadband.permitted_powers.add(shroud, cloak)
broadband.save()
dual = Tag.objects.create(name="Dual", ratings=[1],)
dual.permitted_powers.add(shroud)
dual.save()
teleport = Power.objects.create(
    name="Teleport",
    quantum_minimum=-1,  # Dots+1
    action_type="reflexive",
    cost=2,
    dicepool="",
    range="personal",
    duration="instantaneous",
)
transformation = Power.objects.create(
    name="Transformation",
    quantum_minimum=4,
    action_type="ordinary",
    cost=1,
    dicepool="",
    range="personal",
    duration="continuous",
)
extra_traits = Tag.objects.create(name="Extra Traits", ratings=[1],)
extra_traits.permitted_powers.add(transformation)
extra_traits.save()
reflexive = Tag.objects.create(name="Reflexive", ratings=[2],)
reflexive.permitted_powers.add(transformation, quantum_disruption)
reflexive.save()
transmutation = Power.objects.create(
    name="Transmutation",
    quantum_minimum=4,
    action_type="ordinary",
    cost=3,
    dicepool="Quantum+Power",
    range="close",
    duration="instantaneous",
)
warp = Power.objects.create(
    name="Warp",
    quantum_minimum=-1,  # DOTS+2
    action_type="ordinary",
    cost=2,
    dicepool="",
    range="close",
    duration="continuous",
)

x = Tag.objects.create(name="Aggravated", ratings=[2],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Area", ratings=[2, 4, 6, 8],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Beam", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Bestow", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Bestow Only", ratings=[0],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Blinding", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Brutal", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Charge", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Complete", ratings=[3],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Damaging", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Deadly", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Deafening", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Destructive", ratings=[2],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Disintegrating", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Duration", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Electrical", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Entangle", ratings=[2],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Environmental", ratings=[1, 2],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Gas", ratings=[3],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Hard Armor", ratings=[1, 3, 5],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Immune", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Impervious", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Impose", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Impose Only", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Incendiary", ratings=[2],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Intrinsic", ratings=[0],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Modular", ratings=[1, 2, 3],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Non-Lethal", ratings=[2],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Non-Penetrating", ratings=[0],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Piercing", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Poison", ratings=[2, 3],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Pushing", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Ramp Up", ratings=[-1, -2, -3],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Ranged", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Reduced Cost", ratings=[2, 4, 6, 8, 10, 12],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Reduced Duration", ratings=[-1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Restricted", ratings=[-1, -2, -3],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Smashing", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Sonic", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Spread", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Stun", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Subtle", ratings=[1, 2],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Thrown", ratings=[1],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()
x = Tag.objects.create(name="Vampiric", ratings=[2],)
x.permitted_powers.add(*list(Power.objects.all()))
x.save()


aberrant_eyes = Transformation.objects.create(
    name="Aberrant Eyes",
    level="low",
)
anima_aura = Transformation.objects.create(
    name="Anima Aura",
    level="low",
)
epidermal_shift = Transformation.objects.create(
    name="Epidermal Shift",
    level="low",
)
feeding_requirement = Transformation.objects.create(
    name="Feeding Requirement",
    level="low",
)
inhuman_beauty = Transformation.objects.create(
    name="Inhuman Beauty",
    level="low",
)
life_bane = Transformation.objects.create(
    name="Life Bane",
    level="low",
)
psychological_shift = Transformation.objects.create(
    name="Psychological Shift",
    level="low",
)
vocal_shift = Transformation.objects.create(
    name="Vocal Shift",
    level="low",
)
Transformation.objects.create(
    name="Allergic Reaction",
    level="medium",
)
Transformation.objects.create(
    name="Energy Bleed",
    level="medium",
)
Transformation.objects.create(
    name="Hypersensitivity",
    level="medium",
)
Transformation.objects.create(
    name="Physiological Shift",
    level="medium",
)
Transformation.objects.create(
    name="Power Loss",
    level="medium",
)
Transformation.objects.create(
    name="Psychological Disorder",
    level="medium",
)
Transformation.objects.create(
    name="Uncontrolled Dormancy",
    level="medium",
)
Transformation.objects.create(name="Uncontrolled Power", level="medium")
Transformation.objects.create(name="Vulnerability", level="medium")
Transformation.objects.create(name="Energy Emissions", level="high")
Transformation.objects.create(name="Flux Emissions", level="high")
Transformation.objects.create(name="Hardened Epidermis", level="high")
Transformation.objects.create(name="Hyde Syndrome", level="high")
Transformation.objects.create(name="Power Lock", level="high")
Transformation.objects.create(name="Severe Psychological Disorder", level="high")
Transformation.objects.create(name="Twisted Appearance", level="high")

