from wod.models.characters.changeling import CtDLegacy, House, Kith
from wod.models.characters.human import WoDSpecialty

Kith.objects.create(
    name="Boggan",
    affinity="actor",
    birthrights=["Craftwork", "Social Dynamics"],
    frailty="Call of the Needy",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 88)
Kith.objects.create(
    name="Clurichaun",
    affinity="actor",
    birthrights=["Twinkling of an Eye", "Fighting Words"],
    frailty="Hoard",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 90)
Kith.objects.create(
    name="Eshu",
    affinity="scene",
    birthrights=["Serendipity", "Talecraft"],
    frailty="Recklessness",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 92)
Kith.objects.create(
    name="Nocker",
    affinity="prop",
    birthrights=["Make it Work", "Fix-It"],
    frailty="Perfect is the Enemy of Done",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 94)
Kith.objects.create(
    name="Piskey",
    affinity="actor",
    birthrights=["Nimble", "Blending In"],
    frailty="Light-Fingers",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 96)
Kith.objects.create(
    name="Pooka",
    affinity="nature",
    birthrights=["Shapechanging", "Confidante"],
    frailty="Untruths",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 98)
Kith.objects.create(
    name="Redcap",
    affinity="nature",
    birthrights=["Dark Appetite", "Bully Browbeat"],
    frailty="Bad Attitude",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 100)
Kith.objects.create(
    name="Satyr",
    affinity="fae",
    birthrights=["Gift of Pan", "Physical Prowess"],
    frailty="Passion's Curse",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 102)
Kith.objects.create(
    name="Selkie",
    affinity="nature",
    birthrights=["Seal Form", "Ocean's Grace"],
    frailty="Seal Coat",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 104)
Kith.objects.create(
    name="Arcadian Sidhe",
    affinity="time",
    birthrights=["Unearthly Beauty", "Noble Bearing"],
    frailty="Curse of Banality",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 106)
Kith.objects.create(
    name="Autumn Sidhe",
    affinity="fae",
    birthrights=["Unearthly Beauty", "Noble Bearing"],
    frailty="Adoration",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 108)
Kith.objects.create(
    name="Sluagh",
    affinity="prop",
    birthrights=["Squirm", "Sharpened Senses"],
    frailty="Curse of Silence",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 110)
Kith.objects.create(
    name="Troll",
    affinity="fae",
    birthrights=["Titan's Power", "Strong of Will and Body"],
    frailty="Bond of Duty",
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 112)

House.objects.create(
    name="House Aesin",
    court="unseelie",
    boon="Speak with forest animals",
    flaw="Cannot gain Glamour through Rapture",
    factions=["The Virtue Council", "The Berserkers"],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 119)
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
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 120)
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
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 122)
House.objects.create(
    name="House Beaumayn", court="seelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 123)
House.objects.create(
    name="House Danaan", court="unseelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 124)
House.objects.create(
    name="House Daireann", court="unseelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 126)
House.objects.create(
    name="House Dougal", court="seelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 127)
House.objects.create(
    name="House Eiluned", court="seelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 128)
House.objects.create(
    name="House Fiona", court="seelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 129)
House.objects.create(
    name="House Gwydion", court="seelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 131)
House.objects.create(
    name="House Leanhaun", court="unseelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 132)
House.objects.create(
    name="House Liam", court="seelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 133)
House.objects.create(
    name="House Scathach", court="seelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 135)
House.objects.create(
    name="House Varich", court="unseelie", boon="", flaw="", factions=[],
).add_source("Changeling: the Dreaming 20th Anniversary Edition", 136)


CtDLegacy.objects.create(name="Bumpkin", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 156
)
CtDLegacy.objects.create(name="Courtier", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 156
)
CtDLegacy.objects.create(name="Crafter", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 156
)
CtDLegacy.objects.create(name="Dandy", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 156
)
CtDLegacy.objects.create(name="Hermit", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 156
)
CtDLegacy.objects.create(name="Orchid", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 156
)
CtDLegacy.objects.create(name="Paladin", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 157
)
CtDLegacy.objects.create(name="Panderer", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 157
)
CtDLegacy.objects.create(name="Regent", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 157
)
CtDLegacy.objects.create(name="Sage", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 158
)
CtDLegacy.objects.create(name="Saint", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 158
)
CtDLegacy.objects.create(name="Squire", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 158
)
CtDLegacy.objects.create(name="Troubadour", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 158
)
CtDLegacy.objects.create(name="Wayfarer", court="seelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 158
)


CtDLegacy.objects.create(name="Beast", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 158
)
CtDLegacy.objects.create(name="Fatalist", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 158
)
CtDLegacy.objects.create(name="Fool", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 158
)
CtDLegacy.objects.create(name="Grotesque", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 159
)
CtDLegacy.objects.create(name="Knave", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 159
)
CtDLegacy.objects.create(name="Outlaw", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 159
)
CtDLegacy.objects.create(name="Pandora", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 159
)
CtDLegacy.objects.create(name="Peacock", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 159
)
CtDLegacy.objects.create(name="Rake", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 159
)
CtDLegacy.objects.create(name="Riddler", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 159
)
CtDLegacy.objects.create(name="Ringleader", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 159
)
CtDLegacy.objects.create(name="Rogue", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 159
)
CtDLegacy.objects.create(name="Savage", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 160
)
CtDLegacy.objects.create(name="Wretch", court="unseelie",).add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 160
)

WoDSpecialty.objects.get_or_create(name="Long Jumping", stat="strength")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 160
)
WoDSpecialty.objects.get_or_create(name="Vice Grip", stat="strength")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 160
)
WoDSpecialty.objects.get_or_create(name="Broad Shoulders", stat="strength")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 160)
WoDSpecialty.objects.get_or_create(name="Reserves of Strength", stat="strength")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 160)
WoDSpecialty.objects.get_or_create(name="Mighty Blows", stat="strength")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 160
)
WoDSpecialty.objects.get_or_create(name="Catlike Reflexes", stat="dexterity")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 160)
WoDSpecialty.objects.get_or_create(name="Preternatural Grace", stat="dexterity")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 160)
WoDSpecialty.objects.get_or_create(name="Swift", stat="dexterity")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 160
)
WoDSpecialty.objects.get_or_create(name="Steady Hand", stat="dexterity")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 160
)
WoDSpecialty.objects.get_or_create(name="Sure-Footed", stat="dexterity")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 160
)
WoDSpecialty.objects.get_or_create(name="Unyielding", stat="stamina")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Tireless", stat="stamina")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Resilient", stat="stamina")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Do-or-Die", stat="stamina")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Vigorous", stat="stamina")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Silver-Tongued", stat="charisma")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 161)
WoDSpecialty.objects.get_or_create(name="Eloquent", stat="charisma")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Captivating", stat="charisma")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Infectious Humor", stat="charisma")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 161)
WoDSpecialty.objects.get_or_create(name="Outgoing", stat="charisma")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Cunning", stat="manipulation")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Seductive", stat="manipulation")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Well-Reasoned", stat="manipulation")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 161)
WoDSpecialty.objects.get_or_create(name="Glib", stat="manipulation")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Fast-Talker", stat="manipulation")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 161)
WoDSpecialty.objects.get_or_create(name="Exotic", stat="appearance")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Commanding", stat="appearance")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Unconventional Looks", stat="appearance")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 161)
WoDSpecialty.objects.get_or_create(name="Captivating", stat="appearance")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Style", stat="appearance")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Vigilant", stat="perception")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Clairvoyant", stat="perception")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Discerning", stat="perception")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Insightful", stat="perception")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 161
)
WoDSpecialty.objects.get_or_create(name="Detail-Oriented", stat="perception")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 161)
WoDSpecialty.objects.get_or_create(name="Scholarly", stat="intelligence")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Creative", stat="intelligence")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Subject Expertise", stat="intelligence")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 162)
WoDSpecialty.objects.get_or_create(name="Trivia", stat="intelligence")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Logical", stat="intelligence")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Instinctive", stat="wits")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Clever Retorts", stat="wits")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Pre-Emptive", stat="wits")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Change of Plans", stat="wits")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Cool Headed", stat="wits")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Eavesdropping", stat="alertness")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 162)
WoDSpecialty.objects.get_or_create(name="Danger Sense", stat="alertness")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Fine Details", stat="alertness")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Wilderness", stat="alertness")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Streets", stat="alertness")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Acrobatics", stat="athletics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Parkour", stat="athletics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Mountain Climbing", stat="athletics")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 162)
WoDSpecialty.objects.get_or_create(name="Track and Field", stat="athletics")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 162)
WoDSpecialty.objects.get_or_create(name="Swimming", stat="athletics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Any Martial Arts Style", stat="brawl")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 162)
WoDSpecialty.objects.get_or_create(name="Dirty Fighting", stat="brawl")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Wrestling", stat="brawl")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Boxing", stat="brawl")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Warrior's Halo", stat="brawl")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 162
)
WoDSpecialty.objects.get_or_create(name="Desires", stat="empathy")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Falsehoods", stat="empathy")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Emotions", stat="empathy")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Motives", stat="empathy")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Matters of the Heart", stat="empathy")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 163)
WoDSpecialty.objects.get_or_create(name="Inspiring Speeches", stat="expression")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 163)
WoDSpecialty.objects.get_or_create(name="Fiction", stat="expression")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Poetry", stat="expression")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Rhetoric", stat="expression")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Social Media", stat="expression")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 163)
WoDSpecialty.objects.get_or_create(name="Veiled Threats", stat="intimidation")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 163)
WoDSpecialty.objects.get_or_create(name="Pulling Rank", stat="intimidation")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 163)
WoDSpecialty.objects.get_or_create(name="Violence", stat="intimidation")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Blackmail", stat="intimidation")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="The Look", stat="intimidation")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Cantrips", stat="kenning")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Oaths", stat="kenning")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Enchantment", stat="kenning")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Trods", stat="kenning")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Hidden Magic", stat="kenning")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Compelling", stat="leadership")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Military", stat="leadership")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Oration", stat="leadership")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Friendly", stat="leadership")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Dictatorial", stat="leadership")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Fencing", stat="streetwise")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Gangs", stat="streetwise")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Drugs", stat="streetwise")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="I Know a Guy", stat="streetwise")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 163)
WoDSpecialty.objects.get_or_create(name="Information", stat="streetwise")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 163
)
WoDSpecialty.objects.get_or_create(name="Diversions", stat="subterfuge")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 164
)
WoDSpecialty.objects.get_or_create(name="Seduction", stat="subterfuge")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 164
)
WoDSpecialty.objects.get_or_create(name="The Long Con", stat="subterfuge")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 164)
WoDSpecialty.objects.get_or_create(name="Little White Lies", stat="subterfuge")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 164)
WoDSpecialty.objects.get_or_create(name="It Wasn't Me", stat="subterfuge")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 164)
WoDSpecialty.objects.get_or_create(name="Falconry", stat="animal_ken")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Big Cats", stat="animal_ken")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Attack Training", stat="animal_ken")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 165)
WoDSpecialty.objects.get_or_create(name="Sea Creatures", stat="animal_ken")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 165)
WoDSpecialty.objects.get_or_create(name="Farm Animals", stat="animal_ken")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 165)
WoDSpecialty.objects.get_or_create(name="Metalworking", stat="crafts")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Leatherworking", stat="crafts")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Sculpture", stat="crafts")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Machinery", stat="crafts")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Home Repair", stat="crafts")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Off Road", stat="drive")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Heavy Traffic", stat="drive")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Curves", stat="drive")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Muscle Cars", stat="drive")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Like You Stole It", stat="drive")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 165)
WoDSpecialty.objects.get_or_create(name="High Society", stat="etiquette")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Boardrooms", stat="etiquette")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Particular Kiths", stat="etiquette")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 165)
WoDSpecialty.objects.get_or_create(name="Seelie Court", stat="etiquette")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Unseelie Court", stat="etiquette")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 165)
WoDSpecialty.objects.get_or_create(name="Quick Draw", stat="firearms")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Gunsmith", stat="firearms")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Fast Reload", stat="firearms")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Pistols", stat="firearms")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Rifles", stat="firearms")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Pickpocketing", stat="larceny")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Misdirection", stat="larceny")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Hot-Wiring", stat="larceny")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Forgery", stat="larceny")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 165
)
WoDSpecialty.objects.get_or_create(name="Sleight-of-Hand", stat="larceny")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 165)
WoDSpecialty.objects.get_or_create(name="Disarming", stat="melee")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Improvised Weapons", stat="melee")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 166)
WoDSpecialty.objects.get_or_create(name="Riposte", stat="melee")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Rapiers", stat="melee")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Blessed Opa", stat="melee")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Dancing", stat="performance")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Acting", stat="performance")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Specific Instrument", stat="performance")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 166)
WoDSpecialty.objects.get_or_create(name="Evoke Emotion", stat="performance")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 166)
WoDSpecialty.objects.get_or_create(name="Storytelling", stat="performance")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 166)
WoDSpecialty.objects.get_or_create(name="Hiding", stat="stealth")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Shadowing", stat="stealth")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Crowds", stat="stealth")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Urban", stat="stealth")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Silent Movement", stat="stealth")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 166)
WoDSpecialty.objects.get_or_create(name="Foraging", stat="survival")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Specific Environments", stat="survival")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 166)
WoDSpecialty.objects.get_or_create(name="Tracking", stat="survival")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Hunting", stat="survival")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 166
)
WoDSpecialty.objects.get_or_create(name="Urban Exploration", stat="survival")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 166)
WoDSpecialty.objects.get_or_create(name="Linguistics", stat="academics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Ethics", stat="academics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Teaching", stat="academics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Clovis Culture", stat="academics")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Music Theory", stat="academics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Zero Day Exploits", stat="computer")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(
    name="Specific Programming Language", stat="computer"
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Internet Research", stat="computer")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Database Administration", stat="computer")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Hacking", stat="computer")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Cryptography", stat="enigmas")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Ancient Mysteries", stat="enigmas")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Riddles", stat="enigmas")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Lateral Thinking", stat="enigmas")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Logical Leaps", stat="enigmas")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Faerie Lore", stat="gremayre")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Enchantment", stat="gremayre")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Tarot", stat="gremayre")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Prodigals", stat="gremayre")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Glamour", stat="gremayre")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Forensics", stat="investigation")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Internet Research", stat="investigation")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Search", stat="investigation")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Shadowing", stat="investigation")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Criminal Psychology", stat="investigation")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 167)
WoDSpecialty.objects.get_or_create(name="Courtroom Protocol", stat="law")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Police Procedure", stat="law")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Criminal", stat="law")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Kithain Law", stat="law")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="The Escheat", stat="law")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 167
)
WoDSpecialty.objects.get_or_create(name="Emergency Care", stat="medicine")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 168)
WoDSpecialty.objects.get_or_create(name="Pathology", stat="medicine")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(
    name="Recreational Pharmaceuticals", stat="medicine"
)[0].add_source("Changeling: the Dreaming 20th Anniversary Edition", 168)
WoDSpecialty.objects.get_or_create(name="Neurology", stat="medicine")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Nutrition", stat="medicine")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Congress", stat="politics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="State", stat="politics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Neighborhood", stat="politics")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Parliament of Dreams", stat="politics")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 168)
WoDSpecialty.objects.get_or_create(name="Unseelie Court", stat="politics")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 168)
WoDSpecialty.objects.get_or_create(name="Experiments", stat="science")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Theory", stat="science")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Mathematics", stat="science")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Geology", stat="science")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Relativity", stat="science")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Telecom", stat="technology")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Computers", stat="technology")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Jury-Rigging", stat="technology")[
    0
].add_source("Changeling: the Dreaming 20th Anniversary Edition", 168)
WoDSpecialty.objects.get_or_create(name="Robots", stat="technology")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
WoDSpecialty.objects.get_or_create(name="Security", stat="technology")[0].add_source(
    "Changeling: the Dreaming 20th Anniversary Edition", 168
)
