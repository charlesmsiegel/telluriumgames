from wod.models.characters.changeling import Kith, House

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
    factions=["The Guardians of the Silver Dragon", "Les Amoureux", "The Disinherited", "The Lock-Keepers"],
)
House.objects.create(
    name="House Balor",
    court="unseelie",
    boon="No Glamour loss from cold iron, can soak cold iron damage at diff 10.",
    flaw="Deformed",
    factions=["The Eyes of Balor", "Masters of the Dance", "The Old Firm", "The Guardians of the Gates", "The Riders of the Fell", "Scarlet Eye Solutions"],
)
House.objects.create(
    name="House Beaumayn",
    court="seelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Danaan",
    court="unseelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Daireann",
    court="unseelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Dougal",
    court="seelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Eiluned",
    court="seelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Fiona",
    court="seelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Gwydion",
    court="seelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Leanhaun",
    court="unseelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Liam",
    court="seelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Scathach",
    court="seelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="House Varich",
    court="unseelie",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="",
    court="",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="",
    court="",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="",
    court="",
    boon="",
    flaw="",
    factions=[],
)
House.objects.create(
    name="",
    court="",
    boon="",
    flaw="",
    factions=[],
)
