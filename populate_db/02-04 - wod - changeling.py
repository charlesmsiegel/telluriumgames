from wod.models.characters.changeling import CtDLegacy, House, Kith
from wod.models.characters.human import WoDSpecialty

Kith.objects.create(
    name="Boggan",
    affinity="actor",
    birthrights=["Craftwork", "Social Dynamics"],
    frailty="Call of the Needy",
)
Kith.objects.create(
    name="Clurichaun",
    affinity="actor",
    birthrights=["Twinkling of an Eye", "Fighting Words"],
    frailty="Hoard",
)
Kith.objects.create(
    name="Eshu",
    affinity="scene",
    birthrights=["Serendipity", "Talecraft"],
    frailty="Recklessness",
)
Kith.objects.create(
    name="Nocker",
    affinity="prop",
    birthrights=["Make it Work", "Fix-It"],
    frailty="Perfect is the Enemy of Done",
)
Kith.objects.create(
    name="Piskey",
    affinity="actor",
    birthrights=["Nimble", "Blending In"],
    frailty="Light-Fingers",
)
Kith.objects.create(
    name="Pooka",
    affinity="nature",
    birthrights=["Shapechanging", "Confidante"],
    frailty="Untruths",
)
Kith.objects.create(
    name="Redcap",
    affinity="nature",
    birthrights=["Dark Appetite", "Bully Browbeat"],
    frailty="Bad Attitude",
)
Kith.objects.create(
    name="Satyr",
    affinity="fae",
    birthrights=["Gift of Pan", "Physical Prowess"],
    frailty="Passion's Curse",
)
Kith.objects.create(
    name="Selkie",
    affinity="nature",
    birthrights=["Seal Form", "Ocean's Grace"],
    frailty="Seal Coat",
)
Kith.objects.create(
    name="Arcadian Sidhe",
    affinity="time",
    birthrights=["Unearthly Beauty", "Noble Bearing"],
    frailty="Curse of Banality",
)
Kith.objects.create(
    name="Autumn Sidhe",
    affinity="fae",
    birthrights=["Unearthly Beauty", "Noble Bearing"],
    frailty="Adoration",
)
Kith.objects.create(
    name="Sluagh",
    affinity="prop",
    birthrights=["Squirm", "Sharpened Senses"],
    frailty="Curse of Silence",
)
Kith.objects.create(
    name="Troll",
    affinity="fae",
    birthrights=["Titan's Power", "Strong of Will and Body"],
    frailty="Bond of Duty",
)

House.objects.create(
    name="House Aesin",
    court="unseelie",
    boon="Speak with forest animals",
    flaw="Cannot gain Glamour through Rapture",
    factions=["The Virtue Council", "The Berserkers"],
)
House.objects.create(
    name="House Ailil",
    court="unseelie",
    boon="-1 diff on manipulation",
    flaw="Willpower roll to admit being wrong, and +1 penalty to all Social rolls when they've lost face",
    factions=[
        "The Guardians of the Silver Dragon",
        "Les Amoureux",
        "The Disinherited",
        "The Lock-Keepers",
    ],
)
House.objects.create(
    name="House Balor",
    court="unseelie",
    boon="No Glamour loss from cold iron, can soak cold iron damage at diff 10.",
    flaw="Deformed",
    factions=[
        "The Eyes of Balor",
        "Masters of the Dance",
        "The Old Firm",
        "The Guardians of the Gates",
        "The Riders of the Fell",
        "Scarlet Eye Solutions",
    ],
)
House.objects.create(
    name="House Beaumayn", court="seelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Danaan", court="unseelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Daireann", court="unseelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Dougal", court="seelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Eiluned", court="seelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Fiona", court="seelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Gwydion", court="seelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Leanhaun", court="unseelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Liam", court="seelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Scathach", court="seelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="House Varich", court="unseelie", boon="", flaw="", factions=[],
)
House.objects.create(
    name="", court="", boon="", flaw="", factions=[],
)
House.objects.create(
    name="", court="", boon="", flaw="", factions=[],
)
House.objects.create(
    name="", court="", boon="", flaw="", factions=[],
)
House.objects.create(
    name="", court="", boon="", flaw="", factions=[],
)


CtDLegacy.objects.create(
    name="Bumpkin", court="seelie",
)
CtDLegacy.objects.create(
    name="Courtier", court="seelie",
)
CtDLegacy.objects.create(
    name="Crafter", court="seelie",
)
CtDLegacy.objects.create(
    name="Dandy", court="seelie",
)
CtDLegacy.objects.create(
    name="Hermit", court="seelie",
)
CtDLegacy.objects.create(
    name="Orchid", court="seelie",
)
CtDLegacy.objects.create(
    name="Paladin", court="seelie",
)
CtDLegacy.objects.create(
    name="Panderer", court="seelie",
)
CtDLegacy.objects.create(
    name="Regent", court="seelie",
)
CtDLegacy.objects.create(
    name="Sage", court="seelie",
)
CtDLegacy.objects.create(
    name="Saint", court="seelie",
)
CtDLegacy.objects.create(
    name="Squire", court="seelie",
)
CtDLegacy.objects.create(
    name="Troubadour", court="seelie",
)
CtDLegacy.objects.create(
    name="Wayfarer", court="seelie",
)


CtDLegacy.objects.create(
    name="Beast", court="unseelie",
)
CtDLegacy.objects.create(
    name="Fatalist", court="unseelie",
)
CtDLegacy.objects.create(
    name="Fool", court="unseelie",
)
CtDLegacy.objects.create(
    name="Grotesque", court="unseelie",
)
CtDLegacy.objects.create(
    name="Knave", court="unseelie",
)
CtDLegacy.objects.create(
    name="Outlaw", court="unseelie",
)
CtDLegacy.objects.create(
    name="Pandora", court="unseelie",
)
CtDLegacy.objects.create(
    name="Peacock", court="unseelie",
)
CtDLegacy.objects.create(
    name="Rake", court="unseelie",
)
CtDLegacy.objects.create(
    name="Riddler", court="unseelie",
)
CtDLegacy.objects.create(
    name="Ringleader", court="unseelie",
)
CtDLegacy.objects.create(
    name="Rogue", court="unseelie",
)
CtDLegacy.objects.create(
    name="Savage", court="unseelie",
)
CtDLegacy.objects.create(
    name="Wretch", court="unseelie",
)

WoDSpecialty.objects.get_or_create(name="Long Jumping", stat="strength")
WoDSpecialty.objects.get_or_create(name="Vice Grip", stat="strength")
WoDSpecialty.objects.get_or_create(name="Broad Shoulders", stat="strength")
WoDSpecialty.objects.get_or_create(name="Reserves of Strength", stat="strength")
WoDSpecialty.objects.get_or_create(name="Mighty Blows", stat="strength")
WoDSpecialty.objects.get_or_create(name="Catlike Reflexes", stat="dexterity")
WoDSpecialty.objects.get_or_create(name="Preternatural Grace", stat="dexterity")
WoDSpecialty.objects.get_or_create(name="Swift", stat="dexterity")
WoDSpecialty.objects.get_or_create(name="Steady Hand", stat="dexterity")
WoDSpecialty.objects.get_or_create(name="Sure-Footed", stat="dexterity")
WoDSpecialty.objects.get_or_create(name="Unyielding", stat="stamina")
WoDSpecialty.objects.get_or_create(name="Tireless", stat="stamina")
WoDSpecialty.objects.get_or_create(name="Resilient", stat="stamina")
WoDSpecialty.objects.get_or_create(name="Do-or-Die", stat="stamina")
WoDSpecialty.objects.get_or_create(name="Vigorous", stat="stamina")
WoDSpecialty.objects.get_or_create(name="Silver-Tongued", stat="charisma")
WoDSpecialty.objects.get_or_create(name="Eloquent", stat="charisma")
WoDSpecialty.objects.get_or_create(name="Captivating", stat="charisma")
WoDSpecialty.objects.get_or_create(name="Infectious Humor", stat="charisma")
WoDSpecialty.objects.get_or_create(name="Outgoing", stat="charisma")
WoDSpecialty.objects.get_or_create(name="Cunning", stat="manipulation")
WoDSpecialty.objects.get_or_create(name="Seductive", stat="manipulation")
WoDSpecialty.objects.get_or_create(name="Well-Reasoned", stat="manipulation")
WoDSpecialty.objects.get_or_create(name="Glib", stat="manipulation")
WoDSpecialty.objects.get_or_create(name="Fast-Talker", stat="manipulation")
WoDSpecialty.objects.get_or_create(name="Exotic", stat="appearance")
WoDSpecialty.objects.get_or_create(name="Commanding", stat="appearance")
WoDSpecialty.objects.get_or_create(name="Unconventional Looks", stat="appearance")
WoDSpecialty.objects.get_or_create(name="Captivating", stat="appearance")
WoDSpecialty.objects.get_or_create(name="Style", stat="appearance")
WoDSpecialty.objects.get_or_create(name="Vigilant", stat="perception")
WoDSpecialty.objects.get_or_create(name="Clairvoyant", stat="perception")
WoDSpecialty.objects.get_or_create(name="Discerning", stat="perception")
WoDSpecialty.objects.get_or_create(name="Insightful", stat="perception")
WoDSpecialty.objects.get_or_create(name="Detail-Oriented", stat="perception")
WoDSpecialty.objects.get_or_create(name="Scholarly", stat="intelligence")
WoDSpecialty.objects.get_or_create(name="Creative", stat="intelligence")
WoDSpecialty.objects.get_or_create(name="Subject Expertise", stat="intelligence")
WoDSpecialty.objects.get_or_create(name="Trivia", stat="intelligence")
WoDSpecialty.objects.get_or_create(name="Logical", stat="intelligence")
WoDSpecialty.objects.get_or_create(name="Instinctive", stat="wits")
WoDSpecialty.objects.get_or_create(name="Clever Retorts", stat="wits")
WoDSpecialty.objects.get_or_create(name="Pre-Emptive", stat="wits")
WoDSpecialty.objects.get_or_create(name="Change of Plans", stat="wits")
WoDSpecialty.objects.get_or_create(name="Cool Headed", stat="wits")
WoDSpecialty.objects.get_or_create(name="Eavesdropping", stat="alertness")
WoDSpecialty.objects.get_or_create(name="Danger Sense", stat="alertness")
WoDSpecialty.objects.get_or_create(name="Fine Details", stat="alertness")
WoDSpecialty.objects.get_or_create(name="Wilderness", stat="alertness")
WoDSpecialty.objects.get_or_create(name="Streets", stat="alertness")
WoDSpecialty.objects.get_or_create(name="Acrobatics", stat="athletics")
WoDSpecialty.objects.get_or_create(name="Parkour", stat="athletics")
WoDSpecialty.objects.get_or_create(name="Mountain Climbing", stat="athletics")
WoDSpecialty.objects.get_or_create(name="Track and Field", stat="athletics")
WoDSpecialty.objects.get_or_create(name="Swimming", stat="athletics")
WoDSpecialty.objects.get_or_create(name="Any Martial Arts Style", stat="brawl")
WoDSpecialty.objects.get_or_create(name="Dirty Fighting", stat="brawl")
WoDSpecialty.objects.get_or_create(name="Wrestling", stat="brawl")
WoDSpecialty.objects.get_or_create(name="Boxing", stat="brawl")
WoDSpecialty.objects.get_or_create(name="Warrior's Halo", stat="brawl")
WoDSpecialty.objects.get_or_create(name="Desires", stat="empathy")
WoDSpecialty.objects.get_or_create(name="Falsehoods", stat="empathy")
WoDSpecialty.objects.get_or_create(name="Emotions", stat="empathy")
WoDSpecialty.objects.get_or_create(name="Motives", stat="empathy")
WoDSpecialty.objects.get_or_create(name="Matters of the Heart", stat="empathy")
WoDSpecialty.objects.get_or_create(name="Inspiring Speeches", stat="expression")
WoDSpecialty.objects.get_or_create(name="Fiction", stat="expression")
WoDSpecialty.objects.get_or_create(name="Poetry", stat="expression")
WoDSpecialty.objects.get_or_create(name="Rhetoric", stat="expression")
WoDSpecialty.objects.get_or_create(name="Social Media", stat="expression")
WoDSpecialty.objects.get_or_create(name="Veiled Threats", stat="intimidation")
WoDSpecialty.objects.get_or_create(name="Pulling Rank", stat="intimidation")
WoDSpecialty.objects.get_or_create(name="Violence", stat="intimidation")
WoDSpecialty.objects.get_or_create(name="Blackmail", stat="intimidation")
WoDSpecialty.objects.get_or_create(name="The Look", stat="intimidation")
WoDSpecialty.objects.get_or_create(name="Cantrips", stat="kenning")
WoDSpecialty.objects.get_or_create(name="Oaths", stat="kenning")
WoDSpecialty.objects.get_or_create(name="Enchantment", stat="kenning")
WoDSpecialty.objects.get_or_create(name="Trods", stat="kenning")
WoDSpecialty.objects.get_or_create(name="Hidden Magic", stat="kenning")
WoDSpecialty.objects.get_or_create(name="Compelling", stat="leadership")
WoDSpecialty.objects.get_or_create(name="Military", stat="leadership")
WoDSpecialty.objects.get_or_create(name="Oration", stat="leadership")
WoDSpecialty.objects.get_or_create(name="Friendly", stat="leadership")
WoDSpecialty.objects.get_or_create(name="Dictatorial", stat="leadership")
WoDSpecialty.objects.get_or_create(name="Fencing", stat="streetwise")
WoDSpecialty.objects.get_or_create(name="Gangs", stat="streetwise")
WoDSpecialty.objects.get_or_create(name="Drugs", stat="streetwise")
WoDSpecialty.objects.get_or_create(name="I Know a Guy", stat="streetwise")
WoDSpecialty.objects.get_or_create(name="Information", stat="streetwise")
WoDSpecialty.objects.get_or_create(name="Diversions", stat="subterfuge")
WoDSpecialty.objects.get_or_create(name="Seduction", stat="subterfuge")
WoDSpecialty.objects.get_or_create(name="The Long Con", stat="subterfuge")
WoDSpecialty.objects.get_or_create(name="Little White Lies", stat="subterfuge")
WoDSpecialty.objects.get_or_create(name="It Wasn't Me", stat="subterfuge")
WoDSpecialty.objects.get_or_create(name="Falconry", stat="animal_ken")
WoDSpecialty.objects.get_or_create(name="Big Cats", stat="animal_ken")
WoDSpecialty.objects.get_or_create(name="Attack Training", stat="animal_ken")
WoDSpecialty.objects.get_or_create(name="Sea Creatures", stat="animal_ken")
WoDSpecialty.objects.get_or_create(name="Farm Animals", stat="animal_ken")
WoDSpecialty.objects.get_or_create(name="Metalworking", stat="crafts")
WoDSpecialty.objects.get_or_create(name="Leatherworking", stat="crafts")
WoDSpecialty.objects.get_or_create(name="Sculpture", stat="crafts")
WoDSpecialty.objects.get_or_create(name="Machinery", stat="crafts")
WoDSpecialty.objects.get_or_create(name="Home Repair", stat="crafts")
WoDSpecialty.objects.get_or_create(name="Off Road", stat="drive")
WoDSpecialty.objects.get_or_create(name="Heavy Traffic", stat="drive")
WoDSpecialty.objects.get_or_create(name="Curves", stat="drive")
WoDSpecialty.objects.get_or_create(name="Muscle Cars", stat="drive")
WoDSpecialty.objects.get_or_create(name="Like You Stole It", stat="drive")
WoDSpecialty.objects.get_or_create(name="High Society", stat="etiquette")
WoDSpecialty.objects.get_or_create(name="Boardrooms", stat="etiquette")
WoDSpecialty.objects.get_or_create(name="Particular Kiths", stat="etiquette")
WoDSpecialty.objects.get_or_create(name="Seelie Court", stat="etiquette")
WoDSpecialty.objects.get_or_create(name="Unseelie Court", stat="etiquette")
WoDSpecialty.objects.get_or_create(name="Quick Draw", stat="firearms")
WoDSpecialty.objects.get_or_create(name="Gunsmith", stat="firearms")
WoDSpecialty.objects.get_or_create(name="Fast Reload", stat="firearms")
WoDSpecialty.objects.get_or_create(name="Pistols", stat="firearms")
WoDSpecialty.objects.get_or_create(name="Rifles", stat="firearms")
WoDSpecialty.objects.get_or_create(name="Pickpocketing", stat="larceny")
WoDSpecialty.objects.get_or_create(name="Misdirection", stat="larceny")
WoDSpecialty.objects.get_or_create(name="Hot-Wiring", stat="larceny")
WoDSpecialty.objects.get_or_create(name="Forgery", stat="larceny")
WoDSpecialty.objects.get_or_create(name="Sleight-of-Hand", stat="larceny")
WoDSpecialty.objects.get_or_create(name="Disarming", stat="melee")
WoDSpecialty.objects.get_or_create(name="Improvised Weapons", stat="melee")
WoDSpecialty.objects.get_or_create(name="Riposte", stat="melee")
WoDSpecialty.objects.get_or_create(name="Rapiers", stat="melee")
WoDSpecialty.objects.get_or_create(name="Blessed Opa", stat="melee")
WoDSpecialty.objects.get_or_create(name="Dancing", stat="performance")
WoDSpecialty.objects.get_or_create(name="Acting", stat="performance")
WoDSpecialty.objects.get_or_create(name="Specific Instrument", stat="performance")
WoDSpecialty.objects.get_or_create(name="Evoke Emotion", stat="performance")
WoDSpecialty.objects.get_or_create(name="Storytelling", stat="performance")
WoDSpecialty.objects.get_or_create(name="Hiding", stat="stealth")
WoDSpecialty.objects.get_or_create(name="Shadowing", stat="stealth")
WoDSpecialty.objects.get_or_create(name="Crowds", stat="stealth")
WoDSpecialty.objects.get_or_create(name="Urban", stat="stealth")
WoDSpecialty.objects.get_or_create(name="Silent Movement", stat="stealth")
WoDSpecialty.objects.get_or_create(name="Foraging", stat="survival")
WoDSpecialty.objects.get_or_create(name="Specific Environments", stat="survival")
WoDSpecialty.objects.get_or_create(name="Tracking", stat="survival")
WoDSpecialty.objects.get_or_create(name="Hunting", stat="survival")
WoDSpecialty.objects.get_or_create(name="Urban Exploration", stat="survival")
WoDSpecialty.objects.get_or_create(name="Linguistics", stat="academics")
WoDSpecialty.objects.get_or_create(name="Ethics", stat="academics")
WoDSpecialty.objects.get_or_create(name="Teaching", stat="academics")
WoDSpecialty.objects.get_or_create(name="Clovis Culture", stat="academics")
WoDSpecialty.objects.get_or_create(name="Music Theory", stat="academics")
WoDSpecialty.objects.get_or_create(name="Zero Day Exploits", stat="computer")
WoDSpecialty.objects.get_or_create(
    name="Specific Programming Language", stat="computer"
)
WoDSpecialty.objects.get_or_create(name="Internet Research", stat="computer")
WoDSpecialty.objects.get_or_create(name="Database Administration", stat="computer")
WoDSpecialty.objects.get_or_create(name="Hacking", stat="computer")
WoDSpecialty.objects.get_or_create(name="Cryptography", stat="enigmas")
WoDSpecialty.objects.get_or_create(name="Ancient Mysteries", stat="enigmas")
WoDSpecialty.objects.get_or_create(name="Riddles", stat="enigmas")
WoDSpecialty.objects.get_or_create(name="Lateral Thinking", stat="enigmas")
WoDSpecialty.objects.get_or_create(name="Logical Leaps", stat="enigmas")
WoDSpecialty.objects.get_or_create(name="Faerie Lore", stat="gremayre")
WoDSpecialty.objects.get_or_create(name="Enchantment", stat="gremayre")
WoDSpecialty.objects.get_or_create(name="Tarot", stat="gremayre")
WoDSpecialty.objects.get_or_create(name="Prodigals", stat="gremayre")
WoDSpecialty.objects.get_or_create(name="Glamour", stat="gremayre")
WoDSpecialty.objects.get_or_create(name="Forensics", stat="investigation")
WoDSpecialty.objects.get_or_create(name="Internet Research", stat="investigation")
WoDSpecialty.objects.get_or_create(name="Search", stat="investigation")
WoDSpecialty.objects.get_or_create(name="Shadowing", stat="investigation")
WoDSpecialty.objects.get_or_create(name="Criminal Psychology", stat="investigation")
WoDSpecialty.objects.get_or_create(name="Courtroom Protocol", stat="law")
WoDSpecialty.objects.get_or_create(name="Police Procedure", stat="law")
WoDSpecialty.objects.get_or_create(name="Criminal", stat="law")
WoDSpecialty.objects.get_or_create(name="Kithain Law", stat="law")
WoDSpecialty.objects.get_or_create(name="The Escheat", stat="law")
WoDSpecialty.objects.get_or_create(name="Emergency Care", stat="medicine")
WoDSpecialty.objects.get_or_create(name="Pathology", stat="medicine")
WoDSpecialty.objects.get_or_create(name="Recreational Pharmaceuticals", stat="medicine")
WoDSpecialty.objects.get_or_create(name="Neurology", stat="medicine")
WoDSpecialty.objects.get_or_create(name="Nutrition", stat="medicine")
WoDSpecialty.objects.get_or_create(name="Congress", stat="politics")
WoDSpecialty.objects.get_or_create(name="State", stat="politics")
WoDSpecialty.objects.get_or_create(name="Neighborhood", stat="politics")
WoDSpecialty.objects.get_or_create(name="Parliament of Dreams", stat="politics")
WoDSpecialty.objects.get_or_create(name="Unseelie Court", stat="politics")
WoDSpecialty.objects.get_or_create(name="Experiments", stat="science")
WoDSpecialty.objects.get_or_create(name="Theory", stat="science")
WoDSpecialty.objects.get_or_create(name="Mathematics", stat="science")
WoDSpecialty.objects.get_or_create(name="Geology", stat="science")
WoDSpecialty.objects.get_or_create(name="Relativity", stat="science")
WoDSpecialty.objects.get_or_create(name="Telecom", stat="technology")
WoDSpecialty.objects.get_or_create(name="Computers", stat="technology")
WoDSpecialty.objects.get_or_create(name="Jury-Rigging", stat="technology")
WoDSpecialty.objects.get_or_create(name="Robots", stat="technology")
WoDSpecialty.objects.get_or_create(name="Security", stat="technology")
