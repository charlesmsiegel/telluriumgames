from game.models.chronicle import ObjectType
from wod.models.characters.human import Archetype, MeritFlaw, WoDSpecialty
from wod.models.characters.werewolf import (
    BattleScar,
    Camp,
    FomoriPower,
    Gift,
    RenownIncident,
    Rite,
    SpiritCharacter,
    SpiritCharm,
    Totem,
    Tribe,
)
from wod.models.items.werewolf import Fetish

black_furies = Tribe.objects.get_or_create(name="Black Furies", willpower=3)[0]
bone_gnawers = Tribe.objects.get_or_create(name="Bone Gnawers", willpower=4)[0]
children_of_gaia = Tribe.objects.get_or_create(name="Children of Gaia", willpower=4)[0]
fianna = Tribe.objects.get_or_create(name="Fianna", willpower=3)[0]
get_of_fenris = Tribe.objects.get_or_create(name="Get of Fenris", willpower=3)[0]
glass_walker = Tribe.objects.get_or_create(name="Glass Walkers", willpower=3)[0]
red_talons = Tribe.objects.get_or_create(name="Red Talons", willpower=3)[0]
shadow_lords = Tribe.objects.get_or_create(name="Shadow Lords", willpower=3)[0]
silent_striders = Tribe.objects.get_or_create(name="Silent Striders", willpower=3)[0]
silver_fangs = Tribe.objects.get_or_create(name="Silver Fangs", willpower=3)[0]
stargazers = Tribe.objects.get_or_create(name="Stargazers", willpower=4)[0]
uktena = Tribe.objects.get_or_create(name="Uktena", willpower=3)[0]
wendigo = Tribe.objects.get_or_create(name="Wendigo", willpower=4)[0]

Tribe.objects.get_or_create(name="Black Spiral Dancers", willpower=3)[0]

Tribe.objects.get_or_create(name="Bunyip", willpower=4)[0]
Tribe.objects.get_or_create(name="Croatan", willpower=4)[0]
Tribe.objects.get_or_create(name="White Howlers", willpower=3)[0]

WoDSpecialty.objects.get_or_create(name="Steely Grip", stat="strength")[0]
WoDSpecialty.objects.get_or_create(name="Lower Body", stat="strength")[0]
WoDSpecialty.objects.get_or_create(name="Strength Reserves", stat="strength")[0]
WoDSpecialty.objects.get_or_create(name="Lightning Reflexes", stat="dexterity")[0]
WoDSpecialty.objects.get_or_create(name="Preternatural Grace", stat="dexterity")[0]
WoDSpecialty.objects.get_or_create(name="Nimble Fingers", stat="dexterity")[0]
WoDSpecialty.objects.get_or_create(name="Unbreakable", stat="stamina")[0]
WoDSpecialty.objects.get_or_create(name="Tireless", stat="stamina")[0]
WoDSpecialty.objects.get_or_create(name="Resilient", stat="stamina")[0]
WoDSpecialty.objects.get_or_create(name="Air of Confidence", stat="charisma")[0]
WoDSpecialty.objects.get_or_create(name="Captivating Voice", stat="charisma")[0]
WoDSpecialty.objects.get_or_create(name="Infectious Humor", stat="charisma")[0]
WoDSpecialty.objects.get_or_create(name="Forked Tongue", stat="manipulation")[0]
WoDSpecialty.objects.get_or_create(name="Unswerving Logic", stat="manipulation")[0]
WoDSpecialty.objects.get_or_create(name="Doubletalk", stat="manipulation")[0]
WoDSpecialty.objects.get_or_create(name="Seduction", stat="manipulation")[0]
WoDSpecialty.objects.get_or_create(name="Genial", stat="appearance")[0]
WoDSpecialty.objects.get_or_create(name="Exotic", stat="appearance")[0]
WoDSpecialty.objects.get_or_create(name="Alluring", stat="appearance")[0]
WoDSpecialty.objects.get_or_create(name="Noble Bearing", stat="appearance")[0]
WoDSpecialty.objects.get_or_create(
    name="Eyes in the Back of Your Head", stat="perception"
)[0]
WoDSpecialty.objects.get_or_create(name="Farsighted", stat="perception")[0]
WoDSpecialty.objects.get_or_create(name="Uncanny Instincts", stat="perception")[0]
WoDSpecialty.objects.get_or_create(name="Detail-Oriented", stat="perception")[0]
WoDSpecialty.objects.get_or_create(name="Lateral Problem Solver", stat="intelligence")[
    0
]
WoDSpecialty.objects.get_or_create(name="Creative Logic", stat="intelligence")[0]
WoDSpecialty.objects.get_or_create(name="Probability Calculation", stat="intelligence")[
    0
]
WoDSpecialty.objects.get_or_create(name="Trivia", stat="intelligence")[0]
WoDSpecialty.objects.get_or_create(name="Snappy Retorts", stat="wits")[0]
WoDSpecialty.objects.get_or_create(name="Ambushes", stat="wits")[0]
WoDSpecialty.objects.get_or_create(name="Cool-Headed", stat="wits")[0]
WoDSpecialty.objects.get_or_create(name="Cunning", stat="wits")[0]
WoDSpecialty.objects.get_or_create(name="Ambushes", stat="alertness")[0]
WoDSpecialty.objects.get_or_create(name="Eavesdropping", stat="alertness")[0]
WoDSpecialty.objects.get_or_create(name="Paranoia", stat="alertness")[0]
WoDSpecialty.objects.get_or_create(name="Traps", stat="alertness")[0]
WoDSpecialty.objects.get_or_create(name="Scents", stat="alertness")[0]
WoDSpecialty.objects.get_or_create(name="Specific sports", stat="athletics")[0]
WoDSpecialty.objects.get_or_create(name="Team Play", stat="athletics")[0]
WoDSpecialty.objects.get_or_create(name="Swimming", stat="athletics")[0]
WoDSpecialty.objects.get_or_create(name="Rock Climbing", stat="athletics")[0]
WoDSpecialty.objects.get_or_create(name="Tumbling", stat="athletics")[0]
WoDSpecialty.objects.get_or_create(name="Distance Trials", stat="athletics")[0]
WoDSpecialty.objects.get_or_create(name="Pentathlon", stat="athletics")[0]
WoDSpecialty.objects.get_or_create(name="Boxing", stat="brawl")[0]
WoDSpecialty.objects.get_or_create(name="Wrestling", stat="brawl")[0]
WoDSpecialty.objects.get_or_create(name="Dirty Infighting", stat="brawl")[0]
WoDSpecialty.objects.get_or_create(name="Weaponless Martial Arts", stat="brawl")[0]
WoDSpecialty.objects.get_or_create(name="Kailindo", stat="brawl")[0]
WoDSpecialty.objects.get_or_create(name="Sense Lies", stat="empathy")[0]
WoDSpecialty.objects.get_or_create(name="Hidden Motives", stat="empathy")[0]
WoDSpecialty.objects.get_or_create(name="Emotional States", stat="empathy")[0]
WoDSpecialty.objects.get_or_create(name="Personality Quirks", stat="empathy")[0]
WoDSpecialty.objects.get_or_create(name="Affairs of the Heart", stat="empathy")[0]
WoDSpecialty.objects.get_or_create(name="Rhetoric", stat="expression")[0]
WoDSpecialty.objects.get_or_create(name="Inspiriting Speeches", stat="expression")[0]
WoDSpecialty.objects.get_or_create(name="Poetry", stat="expression")[0]
WoDSpecialty.objects.get_or_create(name="Drama", stat="expression")[0]
WoDSpecialty.objects.get_or_create(name="Political Doubletalk", stat="expression")[0]
WoDSpecialty.objects.get_or_create(name="Social Media", stat="expression")[0]
WoDSpecialty.objects.get_or_create(name="Veiled Threats", stat="intimidation")[0]
WoDSpecialty.objects.get_or_create(name="Good Cop/Bad Cop", stat="intimidation")[0]
WoDSpecialty.objects.get_or_create(name="Blackmail", stat="intimidation")[0]
WoDSpecialty.objects.get_or_create(name="Phyiscal Threats", stat="intimidation")[0]
WoDSpecialty.objects.get_or_create(name="Revenge", stat="intimidation")[0]
WoDSpecialty.objects.get_or_create(name="Compelling", stat="leadership")[0]
WoDSpecialty.objects.get_or_create(name="Open", stat="leadership")[0]
WoDSpecialty.objects.get_or_create(name="Military", stat="leadership")[0]
WoDSpecialty.objects.get_or_create(name="Motivation", stat="leadership")[0]
WoDSpecialty.objects.get_or_create(name="Combat Readiness", stat="leadership")[0]
WoDSpecialty.objects.get_or_create(name="Shifting Forms", stat="primal_urge")[0]
WoDSpecialty.objects.get_or_create(name="Hunting", stat="primal_urge")[0]
WoDSpecialty.objects.get_or_create(name="Hunches", stat="primal_urge")[0]
WoDSpecialty.objects.get_or_create(name="Reacting", stat="primal_urge")[0]
WoDSpecialty.objects.get_or_create(name="Fencing", stat="streetwise")[0]
WoDSpecialty.objects.get_or_create(name="Illegal Drugs", stat="streetwise")[0]
WoDSpecialty.objects.get_or_create(name="Illegal Guns", stat="streetwise")[0]
WoDSpecialty.objects.get_or_create(name="Gangs", stat="streetwise")[0]
WoDSpecialty.objects.get_or_create(name="Unsecured Wifi", stat="streetwise")[0]
WoDSpecialty.objects.get_or_create(name="White Lies", stat="subterfuge")[0]
WoDSpecialty.objects.get_or_create(name="Seduction", stat="subterfuge")[0]
WoDSpecialty.objects.get_or_create(name="The Long Con", stat="subterfuge")[0]
WoDSpecialty.objects.get_or_create(name="Feigned Innocence", stat="subterfuge")[0]
WoDSpecialty.objects.get_or_create(name="Falconry", stat="animal_ken")[0]
WoDSpecialty.objects.get_or_create(name="Farm Animals", stat="animal_ken")[0]
WoDSpecialty.objects.get_or_create(name="Feral Animals", stat="animal_ken")[0]
WoDSpecialty.objects.get_or_create(name="Attack Training", stat="animal_ken")[0]
WoDSpecialty.objects.get_or_create(name="Horses", stat="animal_ken")[0]
WoDSpecialty.objects.get_or_create(name="Big Cats", stat="animal_ken")[0]
WoDSpecialty.objects.get_or_create(name="Dogs", stat="animal_ken")[0]
WoDSpecialty.objects.get_or_create(name="Woodwork", stat="crafts")[0]
WoDSpecialty.objects.get_or_create(name="Drawing/Painting", stat="crafts")[0]
WoDSpecialty.objects.get_or_create(name="Weaving", stat="crafts")[0]
WoDSpecialty.objects.get_or_create(name="Carving", stat="crafts")[0]
WoDSpecialty.objects.get_or_create(name="Sculpture", stat="crafts")[0]
WoDSpecialty.objects.get_or_create(name="Metalworking", stat="crafts")[0]
WoDSpecialty.objects.get_or_create(name="Auto Repair", stat="crafts")[0]
WoDSpecialty.objects.get_or_create(name="Off-road", stat="drive")[0]
WoDSpecialty.objects.get_or_create(name="Motorcycles", stat="drive")[0]
WoDSpecialty.objects.get_or_create(name="Heavy Traffic", stat="drive")[0]
WoDSpecialty.objects.get_or_create(name="High Speed", stat="drive")[0]
WoDSpecialty.objects.get_or_create(name="High Society", stat="etiquette")[0]
WoDSpecialty.objects.get_or_create(name="Moots", stat="etiquette")[0]
WoDSpecialty.objects.get_or_create(name="Tribal", stat="etiquette")[0]
WoDSpecialty.objects.get_or_create(name="Big Business", stat="etiquette")[0]
WoDSpecialty.objects.get_or_create(name="Rifles", stat="firearms")[0]
WoDSpecialty.objects.get_or_create(name="Pistols", stat="firearms")[0]
WoDSpecialty.objects.get_or_create(name="Submachine Guns", stat="firearms")[0]
WoDSpecialty.objects.get_or_create(name="Gunsmithing", stat="firearms")[0]
WoDSpecialty.objects.get_or_create(name="Marksmanship", stat="firearms")[0]
WoDSpecialty.objects.get_or_create(name="Trick Shots", stat="firearms")[0]
WoDSpecialty.objects.get_or_create(name="Pickpocketing", stat="larceny")[0]
WoDSpecialty.objects.get_or_create(name="Misdirection", stat="larceny")[0]
WoDSpecialty.objects.get_or_create(name="Lockpicking", stat="larceny")[0]
WoDSpecialty.objects.get_or_create(name="Hotwiring", stat="larceny")[0]
WoDSpecialty.objects.get_or_create(name="Safecracking", stat="larceny")[0]
WoDSpecialty.objects.get_or_create(name="Swords", stat="melee")[0]
WoDSpecialty.objects.get_or_create(name="Spears", stat="melee")[0]
WoDSpecialty.objects.get_or_create(name="Improvised Weaponry", stat="melee")[0]
WoDSpecialty.objects.get_or_create(name="Klaives", stat="melee")[0]
WoDSpecialty.objects.get_or_create(name="Dancing", stat="performance")[0]
WoDSpecialty.objects.get_or_create(name="Singing", stat="performance")[0]
WoDSpecialty.objects.get_or_create(name="Acting", stat="performance")[0]
WoDSpecialty.objects.get_or_create(name="Rock and Roll", stat="performance")[0]
WoDSpecialty.objects.get_or_create(name="Guitar Solos", stat="performance")[0]
WoDSpecialty.objects.get_or_create(name="Opera", stat="performance")[0]
WoDSpecialty.objects.get_or_create(name="Howling", stat="performance")[0]
WoDSpecialty.objects.get_or_create(name="Shadowing", stat="stealth")[0]
WoDSpecialty.objects.get_or_create(name="Urban", stat="stealth")[0]
WoDSpecialty.objects.get_or_create(name="Taking Point", stat="stealth")[0]
WoDSpecialty.objects.get_or_create(name="Crowds", stat="stealth")[0]
WoDSpecialty.objects.get_or_create(name="Hiding Objects", stat="stealth")[0]
WoDSpecialty.objects.get_or_create(name="Foraging", stat="survival")[0]
WoDSpecialty.objects.get_or_create(name="Tracking", stat="survival")[0]
WoDSpecialty.objects.get_or_create(name="Specific Environments", stat="survival")[0]
WoDSpecialty.objects.get_or_create(name="Trapping", stat="survival")[0]
WoDSpecialty.objects.get_or_create(name="Color Theory", stat="academics")[0]
WoDSpecialty.objects.get_or_create(name="Linguistics", stat="academics")[0]
WoDSpecialty.objects.get_or_create(name="Poststructuralism", stat="academics")[0]
WoDSpecialty.objects.get_or_create(name="Ethics", stat="academics")[0]
WoDSpecialty.objects.get_or_create(name="Metaphysics", stat="academics")[0]
WoDSpecialty.objects.get_or_create(name="Sumeria", stat="academics")[0]
WoDSpecialty.objects.get_or_create(name="Internet Research", stat="computer")[0]
WoDSpecialty.objects.get_or_create(name="Video Editing", stat="computer")[0]
WoDSpecialty.objects.get_or_create(name="Photo Manipulation", stat="computer")[0]
WoDSpecialty.objects.get_or_create(name="Programming", stat="computer")[0]
WoDSpecialty.objects.get_or_create(name="Computer Languages", stat="computer")[0]
WoDSpecialty.objects.get_or_create(name="Logic Problems", stat="enigmas")[0]
WoDSpecialty.objects.get_or_create(name="Lateral Thinking", stat="enigmas")[0]
WoDSpecialty.objects.get_or_create(name="Ancient Mysteries", stat="enigmas")[0]
WoDSpecialty.objects.get_or_create(
    name="Things Werewolves Were Not Meant to Know", stat="enigmas"
)[0]
WoDSpecialty.objects.get_or_create(name="Evidence", stat="investigation")[0]
WoDSpecialty.objects.get_or_create(name="Ballistics", stat="investigation")[0]
WoDSpecialty.objects.get_or_create(name="Forensics", stat="investigation")[0]
WoDSpecialty.objects.get_or_create(name="Fingerprints", stat="investigation")[0]
WoDSpecialty.objects.get_or_create(name="Searches", stat="investigation")[0]
WoDSpecialty.objects.get_or_create(name="Internet Research", stat="investigation")[0]
WoDSpecialty.objects.get_or_create(name="Fitting Punishments", stat="law")[0]
WoDSpecialty.objects.get_or_create(name="Litany Breaches", stat="law")[0]
WoDSpecialty.objects.get_or_create(name="Human Field", stat="law")[0]
WoDSpecialty.objects.get_or_create(name="Emergency Medicine", stat="medicine")[0]
WoDSpecialty.objects.get_or_create(name="Forensic Pathology", stat="medicine")[0]
WoDSpecialty.objects.get_or_create(name="Neurology", stat="medicine")[0]
WoDSpecialty.objects.get_or_create(name="Pharmacology", stat="medicine")[0]
WoDSpecialty.objects.get_or_create(name="Poison Treatments", stat="medicine")[0]
WoDSpecialty.objects.get_or_create(name="Garou Physiology", stat="medicine")[0]
WoDSpecialty.objects.get_or_create(name="Tarot", stat="occult")[0]
WoDSpecialty.objects.get_or_create(name="Witchcraft", stat="occult")[0]
WoDSpecialty.objects.get_or_create(name="Curses", stat="occult")[0]
WoDSpecialty.objects.get_or_create(name="Ghosts", stat="occult")[0]
WoDSpecialty.objects.get_or_create(name="Psychometry", stat="occult")[0]
WoDSpecialty.objects.get_or_create(name="Garou Lore", stat="occult")[0]
WoDSpecialty.objects.get_or_create(name="Accord", stat="rituals")[0]
WoDSpecialty.objects.get_or_create(name="Caern", stat="rituals")[0]
WoDSpecialty.objects.get_or_create(name="Death", stat="rituals")[0]
WoDSpecialty.objects.get_or_create(name="Mystic", stat="rituals")[0]
WoDSpecialty.objects.get_or_create(name="Punishment", stat="rituals")[0]
WoDSpecialty.objects.get_or_create(name="Renown", stat="rituals")[0]
WoDSpecialty.objects.get_or_create(name="Seasonal", stat="rituals")[0]
WoDSpecialty.objects.get_or_create(name="Minor", stat="rituals")[0]
WoDSpecialty.objects.get_or_create(name="Experiments", stat="science")[0]
WoDSpecialty.objects.get_or_create(name="Theory", stat="science")[0]
WoDSpecialty.objects.get_or_create(name="Chemistry", stat="science")[0]
WoDSpecialty.objects.get_or_create(name="Physics", stat="science")[0]
WoDSpecialty.objects.get_or_create(name="Biology", stat="science")[0]
WoDSpecialty.objects.get_or_create(name="Mathematics", stat="science")[0]
WoDSpecialty.objects.get_or_create(name="Astronomy", stat="science")[0]
WoDSpecialty.objects.get_or_create(name="Telecoms", stat="technology")[0]
WoDSpecialty.objects.get_or_create(name="Computers", stat="technology")[0]
WoDSpecialty.objects.get_or_create(name="Security", stat="technology")[0]
WoDSpecialty.objects.get_or_create(name="Communications", stat="technology")[0]
WoDSpecialty.objects.get_or_create(name="Jury-Rigging", stat="technology")[0]
WoDSpecialty.objects.get_or_create(name="Industrial Espionage", stat="technology")[0]

Gift.objects.get_or_create(
    name="Aprecraft's Blessings", rank=1, allowed={"garou": ["homid"]}
)[0]
Gift.objects.get_or_create(name="City Running", rank=1, allowed={"garou": ["homid"]})[0]
Gift.objects.get_or_create(
    name="Master of Fire",
    rank=1,
    allowed={"garou": ["homid", "Get of Fenris", "Croatan"]},
)[0]
Gift.objects.get_or_create(
    name="Persuasion",
    rank=1,
    allowed={"garou": ["homid", "philodox", "Fianna", "Glasswalkers"]},
)[0]
Gift.objects.get_or_create(name="Smell of Man", rank=1, allowed={"garou": ["homid"]})[0]
Gift.objects.get_or_create(
    name="Jam Technology", rank=2, allowed={"garou": ["homid", "Glasswalkers"]}
)[0]
Gift.objects.get_or_create(
    name="Mark of the Wolf", rank=2, allowed={"garou": ["homid"]}
)[0]
Gift.objects.get_or_create(
    name="Speech of the World", rank=2, allowed={"garou": ["homid", "Silent Striders"]}
)[0]
Gift.objects.get_or_create(name="Staredown", rank=2, allowed={"garou": ["homid"]})[0]
Gift.objects.get_or_create(
    name="Calm the Savage Beast",
    rank=3,
    allowed={"garou": ["homid", "Children of Gaia"]},
)[0]
Gift.objects.get_or_create(
    name="Cowing the Bullet", rank=3, allowed={"garou": ["homid"]}
)[0]
Gift.objects.get_or_create(name="Disquiet", rank=3, allowed={"garou": ["homid"]})[0]
Gift.objects.get_or_create(
    name="Reshape Object",
    rank=3,
    allowed={"garou": ["homid", "Bone Gnawers", "Fianna"]},
)[0]
Gift.objects.get_or_create(
    name="Body Shift", rank=4, allowed={"garou": ["homid", "ahroun", "Get of Fenris"]}
)[0]
Gift.objects.get_or_create(name="Bury the Wolf", rank=4, allowed={"garou": ["homid"]})[
    0
]
Gift.objects.get_or_create(name="Cocoon", rank=4, allowed={"garou": ["homid"]})[0]
Gift.objects.get_or_create(
    name="Spirit Ward", rank=4, allowed={"garou": ["homid", "theurge"]}
)[0]
Gift.objects.get_or_create(name="Assimilation", rank=5, allowed={"garou": ["homid"]})[0]
Gift.objects.get_or_create(name="Beyond Human", rank=5, allowed={"garou": ["homid"]})[0]
Gift.objects.get_or_create(name="Part the Veil", rank=5, allowed={"garou": ["homid"]})[
    0
]
Gift.objects.get_or_create(name="Create Element", rank=1, allowed={"garou": ["metis"]})[
    0
]
Gift.objects.get_or_create(
    name="Primal Anger", rank=1, allowed={"garou": ["metis", "White Howlers"]}
)[0]
Gift.objects.get_or_create(name="Rat Head", rank=1, allowed={"garou": ["metis"]})[0]
Gift.objects.get_or_create(
    name="Sense Wyrm",
    rank=1,
    allowed={
        "garou": [
            "metis",
            "theurge",
            "Black Furies",
            "Silent Striders",
            "Silver Fangs",
            "Stargazers",
            "Uktena",
            "Black Spiral Dancers",
            "White Howlers",
        ]
    },
)[0]
Gift.objects.get_or_create(name="Shed", rank=1, allowed={"garou": ["metis"]})[0]
Gift.objects.get_or_create(name="Burrow", rank=2, allowed={"garou": ["metis"]})[0]
Gift.objects.get_or_create(
    name="Curse of Hatred", rank=2, allowed={"garou": ["metis"]}
)[0]
Gift.objects.get_or_create(
    name="Form Mastery", rank=2, allowed={"garou": ["metis", "Black Furies", "Fianna"]}
)[0]
Gift.objects.get_or_create(
    name="Sense Silver", rank=2, allowed={"garou": ["metis", "ahroun", "Silver Fangs"]}
)[0]
Gift.objects.get_or_create(name="Chameleon", rank=2, allowed={"garou": ["metis"]})[0]
Gift.objects.get_or_create(
    name="Eyes of the Cat", rank=3, allowed={"garou": ["metis"]}
)[0]
Gift.objects.get_or_create(
    name="Mental Speech", rank=3, allowed={"garou": ["metis", "philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Shell", rank=3, allowed={"garou": ["metis", "Croatan"]}
)[0]
Gift.objects.get_or_create(
    name="Gift of the Porcupine", rank=4, allowed={"garou": ["metis"]}
)[0]
Gift.objects.get_or_create(name="Lash of Rage", rank=4, allowed={"garou": ["metis"]})[0]
Gift.objects.get_or_create(name="Rattler's Bite", rank=4, allowed={"garou": ["metis"]})[
    0
]
Gift.objects.get_or_create(name="Wither Limb", rank=4, allowed={"garou": ["metis"]})[0]
Gift.objects.get_or_create(name="Madness", rank=5, allowed={"garou": ["metis"]})[0]
Gift.objects.get_or_create(name="Protean Form", rank=5, allowed={"garou": ["metis"]})[0]
Gift.objects.get_or_create(name="Totem Gift", rank=5, allowed={"garou": ["metis"]})[0]
Gift.objects.get_or_create(
    name="Hare's Leap", rank=1, allowed={"garou": ["lupus", "Fianna"]}
)[0]
Gift.objects.get_or_create(
    name="Heightened Senses",
    rank=1,
    allowed={"garou": ["lupus", "galliard", "Black Furies"]},
)[0]
Gift.objects.get_or_create(
    name="Sense Prey", rank=1, allowed={"garou": ["lupus", "Bunyip"]}
)[0]
Gift.objects.get_or_create(
    name="Predator's Arsenal", rank=1, allowed={"garou": ["lupus"]}
)[0]
Gift.objects.get_or_create(name="Prey Mind", rank=1, allowed={"garou": ["lupus"]})[0]
Gift.objects.get_or_create(
    name="Axis Mundi", rank=2, allowed={"garou": ["lupus", "Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Eye of the Eagle", rank=2, allowed={"garou": ["lupus"]}
)[0]
Gift.objects.get_or_create(
    name="Name the Spirit", rank=2, allowed={"garou": ["lupus", "theurge"]}
)[0]
Gift.objects.get_or_create(name="Scent of Sight", rank=2, allowed={"garou": ["lupus"]})[
    0
]
Gift.objects.get_or_create(name="Catfeet", rank=3, allowed={"garou": ["lupus"]})[0]
Gift.objects.get_or_create(
    name="Monkey Tail", rank=3, allowed={"garou": ["lupus", "ragabash"]}
)[0]
Gift.objects.get_or_create(
    name="Sense the Unnatural", rank=3, allowed={"garou": ["lupus", "Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Silence the Weaver", rank=3, allowed={"garou": ["lupus"]}
)[0]
Gift.objects.get_or_create(
    name="Strength of Gaia", rank=3, allowed={"garou": ["lupus"]}
)[0]
Gift.objects.get_or_create(
    name="Beast Life",
    rank=4,
    allowed={"garou": ["lupus", "Black Furies", "Children of Gaia"]},
)[0]
Gift.objects.get_or_create(name="Gnaw", rank=4, allowed={"garou": ["lupus"]})[0]
Gift.objects.get_or_create(
    name="Scream of Gaia", rank=4, allowed={"garou": ["lupus", "Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Terror of the Dire Wolf", rank=4, allowed={"garou": ["lupus"]}
)[0]
Gift.objects.get_or_create(name="Elemental Gift", rank=5, allowed={"garou": ["lupus"]})[
    0
]
Gift.objects.get_or_create(
    name="Song of the Great Beast", rank=5, allowed={"garou": ["lupus"]}
)[0]
Gift.objects.get_or_create(
    name="Blur of the Milky Eye", rank=1, allowed={"garou": ["ragabash"]}
)[0]
Gift.objects.get_or_create(
    name="Infectious Laughter", rank=1, allowed={"garou": ["ragabash"]}
)[0]
Gift.objects.get_or_create(name="Liar's Face", rank=1, allowed={"garou": ["ragabash"]})[
    0
]
Gift.objects.get_or_create(name="Open Seal", rank=1, allowed={"garou": ["ragabash"]})[0]
Gift.objects.get_or_create(
    name="Scent of Running Water", rank=1, allowed={"garou": ["ragabash", "Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Blissful Ignorance",
    rank=2,
    allowed={"garou": ["ragabash", "Bone Gnawers", "Silent Striders"]},
)[0]
Gift.objects.get_or_create(
    name="Pulse of the Prey",
    rank=2,
    allowed={"garou": ["ragabash", "Black Furies", "Red Talons"]},
)[0]
Gift.objects.get_or_create(
    name="Spider's Song", rank=2, allowed={"garou": ["ragabash"]}
)[0]
Gift.objects.get_or_create(
    name="Taking the Forgotten", rank=2, allowed={"garou": ["ragabash"]}
)[0]
Gift.objects.get_or_create(name="Gremlins", rank=3, allowed={"garou": ["ragabash"]})[0]
Gift.objects.get_or_create(
    name="Liar's Craft", rank=3, allowed={"garou": ["ragabash"]}
)[0]
Gift.objects.get_or_create(
    name="Open Moon Bridge", rank=3, allowed={"garou": ["ragabash"]}
)[0]
Gift.objects.get_or_create(name="Pathfinder", rank=3, allowed={"garou": ["ragabash"]})[
    0
]
Gift.objects.get_or_create(
    name="Luna's Blessing", rank=4, allowed={"garou": ["ragabash"]}
)[0]
Gift.objects.get_or_create(
    name="Umbral Dodge", rank=4, allowed={"garou": ["ragabash"]}
)[0]
Gift.objects.get_or_create(name="Whelp Body", rank=4, allowed={"garou": ["ragabash"]})[
    0
]
Gift.objects.get_or_create(
    name="Thieving Talons of the Magpie", rank=5, allowed={"garou": ["ragabash"]}
)[0]
Gift.objects.get_or_create(
    name="Thousand Forms", rank=5, allowed={"garou": ["ragabash", "Black Furies"]}
)[0]
Gift.objects.get_or_create(name="Firebringer", rank=6, allowed={"garou": ["ragabash"]})[
    0
]
Gift.objects.get_or_create(
    name="Mother's Touch",
    rank=1,
    allowed={"garou": ["theurge", "Children of Gaia", "Bunyip"]},
)[0]
Gift.objects.get_or_create(name="Spirit Snare", rank=1, allowed={"garou": ["theurge"]})[
    0
]
Gift.objects.get_or_create(
    name="Spirit Speech", rank=1, allowed={"garou": ["theurge", "Uktena"]}
)[0]
Gift.objects.get_or_create(
    name="Umbral Tether", rank=1, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(
    name="Battle Mandala", rank=2, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(
    name="Command Spirit", rank=2, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(
    name="Sight From Beyond", rank=2, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(name="Exorcism", rank=3, allowed={"garou": ["theurge"]})[0]
Gift.objects.get_or_create(
    name="Pulse of the Invisible", rank=3, allowed={"garou": ["theurge", "Bunyip"]}
)[0]
Gift.objects.get_or_create(
    name="Umbral Camouflage", rank=3, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(name="Web Walker", rank=3, allowed={"garou": ["theurge"]})[0]
Gift.objects.get_or_create(
    name="Blurring the Mirror", rank=4, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(
    name="Grasp of Beyond", rank=4, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(name="Spirit Drain", rank=4, allowed={"garou": ["theurge"]})[
    0
]
Gift.objects.get_or_create(
    name="Feral Lobotomy", rank=5, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(
    name="Malleable Spirit", rank=5, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(
    name="Ultimate Argument of Logic", rank=5, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(
    name="As in the Beginning", rank=6, allowed={"garou": ["theurge"]}
)[0]
Gift.objects.get_or_create(
    name="Fangs of Judgment", rank=1, allowed={"garou": ["philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Resist Pain",
    rank=1,
    allowed={
        "garou": [
            "philodox",
            "Children of Gaia",
            "Get of Fenris",
            "Wendigo",
            "Black Spiral Dancers",
        ]
    },
)[0]
Gift.objects.get_or_create(
    name="Scent of the True Form", rank=1, allowed={"garou": ["philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Truth of Gaia", rank=1, allowed={"garou": ["philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Call to Duty", rank=2, allowed={"garou": ["philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Command the Gathering", rank=2, allowed={"garou": ["philodox", "galliard"]}
)[0]
Gift.objects.get_or_create(
    name="King of the Beasts", rank=2, allowed={"garou": ["philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Strength of Purpose", rank=2, allowed={"garou": ["philodox", "Croatan"]}
)[0]
Gift.objects.get_or_create(
    name="Scent of the Oathbreaker", rank=3, allowed={"garou": ["philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Sense Balance", rank=3, allowed={"garou": ["philodox", "Stargazers"]}
)[0]
Gift.objects.get_or_create(name="Weak Arm", rank=3, allowed={"garou": ["philodox"]})[0]
Gift.objects.get_or_create(
    name="Wisdom of the Ancient Ways",
    rank=3,
    allowed={"garou": ["philodox", "Wendigo"]},
)[0]
Gift.objects.get_or_create(name="Roll Over", rank=4, allowed={"garou": ["philodox"]})[0]
Gift.objects.get_or_create(
    name="Scent of Beyond", rank=4, allowed={"garou": ["philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Take the True Form", rank=4, allowed={"garou": ["philodox"]}
)[0]
Gift.objects.get_or_create(name="Geas", rank=5, allowed={"garou": ["philodox"]})[0]
Gift.objects.get_or_create(
    name="Wall of Granite", rank=5, allowed={"garou": ["philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Break the Bonds", rank=6, allowed={"garou": ["philodox", "galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Beast Speech", rank=1, allowed={"garou": ["galliard", "Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Call of the Wyld", rank=1, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Mindspeak", rank=1, allowed={"garou": ["galliard", "Croatan"]}
)[0]
Gift.objects.get_or_create(
    name="Perfect Recall", rank=1, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Call of the Wyrm", rank=2, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Distractions", rank=2, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(name="Dreamspeak", rank=2, allowed={"garou": ["galliard"]})[
    0
]
Gift.objects.get_or_create(
    name="Howls in the Night",
    rank=2,
    allowed={"garou": ["galliard", "Red Talons", "Shadow Lords", "White Howlers"]},
)[0]
Gift.objects.get_or_create(
    name="Eye of the Cobra", rank=3, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Song of Heroes", rank=3, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Song of Rage", rank=3, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Song of the Siren", rank=3, allowed={"garou": ["galliard", "Fianna"]}
)[0]
Gift.objects.get_or_create(
    name="Bridge Walker", rank=4, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Gift of Dreams", rank=4, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Shadows by the Firelight", rank=4, allowed={"garou": ["galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Fabric of the Mind", rank=4, allowed={"garou": ["galliard", "Uktena"]}
)[0]
Gift.objects.get_or_create(name="Head Games", rank=5, allowed={"garou": ["galliard"]})[
    0
]
Gift.objects.get_or_create(
    name="Falling Touch", rank=1, allowed={"garou": ["ahroun", "Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Inspiration", rank=1, allowed={"garou": ["ahroun", "Silver Fangs"]}
)[0]
Gift.objects.get_or_create(name="Pack Tactics", rank=1, allowed={"garou": ["ahroun"]})[
    0
]
Gift.objects.get_or_create(
    name="Razor Claws", rank=1, allowed={"garou": ["ahroun", "Get of Fenris"]}
)[0]
Gift.objects.get_or_create(name="Spur Claws", rank=1, allowed={"garou": ["ahroun"]})[0]
Gift.objects.get_or_create(
    name="Shield of Rage", rank=2, allowed={"garou": ["ahroun"]}
)[0]
Gift.objects.get_or_create(
    name="Spirit of the Fray", rank=2, allowed={"garou": ["ahroun"]}
)[0]
Gift.objects.get_or_create(
    name="True Fear", rank=2, allowed={"garou": ["ahroun", "Wendigo"]}
)[0]
Gift.objects.get_or_create(
    name="Combat Healing", rank=3, allowed={"garou": ["ahroun"]}
)[0]
Gift.objects.get_or_create(name="Heart of Fury", rank=3, allowed={"garou": ["ahroun"]})[
    0
]
Gift.objects.get_or_create(
    name="Silver Claws", rank=3, allowed={"garou": ["ahroun", "Silver Fangs"]}
)[0]
Gift.objects.get_or_create(name="Wind Claws", rank=3, allowed={"garou": ["ahroun"]})[0]
Gift.objects.get_or_create(
    name="Clenched Jaw", rank=4, allowed={"garou": ["ahroun", "Kucha Ekundu"]}
)[0]
Gift.objects.get_or_create(
    name="Full Moon's Light", rank=4, allowed={"garou": ["ahroun"]}
)[0]
Gift.objects.get_or_create(
    name="Stoking Fury's Furnace", rank=4, allowed={"garou": ["ahroun"]}
)[0]
Gift.objects.get_or_create(
    name="Kiss of Helios", rank=5, allowed={"garou": ["ahroun"]}
)[0]
Gift.objects.get_or_create(
    name="Strength of Will", rank=5, allowed={"garou": ["ahroun"]}
)[0]
Gift.objects.get_or_create(
    name="Unstoppable Warrior", rank=6, allowed={"garou": ["ahroun"]}
)[0]
Gift.objects.get_or_create(
    name="Breath of the Wyld", rank=1, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Man's Skin", rank=1, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Wyld Resurgence", rank=1, allowed={"garou": ["Black Furies", "Croatan"]}
)[0]
Gift.objects.get_or_create(
    name="Curse of Aeolus", rank=2, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Kali's Tongue", rank=2, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(name="Kneel", rank=2, allowed={"garou": ["Black Furies"]})[0]
Gift.objects.get_or_create(
    name="Coup de Grace", rank=3, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Heart Claw", rank=3, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Visceral Agony", rank=3, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Wings of PEgasus", rank=3, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Body Wrack", rank=4, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Wasp Talons", rank=4, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Gorgon's Gaze", rank=5, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(
    name="Wyld Warp", rank=5, allowed={"garou": ["Black Furies"]}
)[0]
Gift.objects.get_or_create(name="Cooking", rank=1, allowed={"garou": ["Bone Gnawers"]})[
    0
]
Gift.objects.get_or_create(
    name="Desperate Strength",
    rank=1,
    allowed={"garou": ["Bone Gnawers", "White Howlers"]},
)[0]
Gift.objects.get_or_create(
    name="Resist Toxin",
    rank=1,
    allowed={"garou": ["Bone Gnawers", "Fianna", "Black Spiral Dancers", "Bunyip"]},
)[0]
Gift.objects.get_or_create(
    name="Scent of Sweet Honey", rank=1, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Trash is Treasure", rank=1, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Between the Cracks", rank=2, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Cornered Rat's Ferocity", rank=2, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Guide of the Hound", rank=2, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Odious Aroma", rank=2, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Call the Rust", rank=3, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Gift of the Skunk", rank=3, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Gift of the Termite", rank=3, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Laugh of the Hyena", rank=3, allowed={"garou": ["Bone Gnawers"]}
)[0]
Gift.objects.get_or_create(
    name="Attunement",
    rank=4,
    allowed={"garou": ["Bone Gnawers", "Glasswalkers", "Silent Striders"]},
)[0]
Gift.objects.get_or_create(name="Blink", rank=4, allowed={"garou": ["Bone Gnawers"]})[0]
Gift.objects.get_or_create(name="Infest", rank=4, allowed={"garou": ["Bone Gnawers"]})[
    0
]
Gift.objects.get_or_create(name="Riot", rank=5, allowed={"garou": ["Bone Gnawers"]})[0]
Gift.objects.get_or_create(
    name="Survivor", rank=5, allowed={"garou": ["Bone Gnawers", "Croatan"]}
)[0]
Gift.objects.get_or_create(
    name="Brother's Scent", rank=1, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Jam Weapon", rank=1, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Mercy", rank=1, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Calm", rank=2, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Grandmother's Touch", rank=2, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Luna's Armor",
    rank=2,
    allowed={"garou": ["Children of Gaia", "Shadow Lords", "Silver Fangs"]},
)[0]
Gift.objects.get_or_create(
    name="Para Bellum", rank=2, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Unicorn's Arsenal", rank=2, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Dazzle", rank=3, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Lover's Touch", rank=3, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Spirit Friend", rank=3, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Serenity", rank=4, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="Strike the Air", rank=4, allowed={"garou": ["Children of Gaia", "Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Uncought Since the Primal Morn",
    rank=4,
    allowed={"garou": ["Children of Gaia"]},
)[0]
Gift.objects.get_or_create(
    name="Halo of the Sun", rank=5, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(
    name="The Living Wood", rank=5, allowed={"garou": ["Children of Gaia"]}
)[0]
Gift.objects.get_or_create(name="Faerie Light", rank=1, allowed={"garou": ["Fianna"]})[
    0
]
Gift.objects.get_or_create(name="Two Tongues", rank=1, allowed={"garou": ["Fianna"]})[0]
Gift.objects.get_or_create(name="Glib Tongue", rank=2, allowed={"garou": ["Fianna"]})[0]
Gift.objects.get_or_create(name="Flame Dance", rank=2, allowed={"garou": ["Fianna"]})[0]
Gift.objects.get_or_create(
    name="Howl of the Banshee", rank=2, allowed={"garou": ["Fianna"]}
)[0]
Gift.objects.get_or_create(
    name="Howl of the Unseen", rank=2, allowed={"garou": ["Fianna"]}
)[0]
Gift.objects.get_or_create(name="Faerie Kin", rank=3, allowed={"garou": ["Fianna"]})[0]
Gift.objects.get_or_create(name="Fair Fortune", rank=3, allowed={"garou": ["Fianna"]})[
    0
]
Gift.objects.get_or_create(
    name="Ley Lines", rank=3, allowed={"garou": ["Fianna", "White Howlers"]}
)[0]
Gift.objects.get_or_create(name="Balor's Gaze", rank=4, allowed={"garou": ["Fianna"]})[
    0
]
Gift.objects.get_or_create(name="Phantasm", rank=4, allowed={"garou": ["Fianna"]})[0]
Gift.objects.get_or_create(name="Call the Hunt", rank=5, allowed={"garou": ["Fianna"]})[
    0
]
Gift.objects.get_or_create(
    name="Fog on the Moor", rank=5, allowed={"garou": ["Fianna"]}
)[0]
Gift.objects.get_or_create(
    name="Gift of the Spriggan", rank=5, allowed={"garou": ["Fianna"]}
)[0]
Gift.objects.get_or_create(
    name="Lightning Reflexes", rank=1, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Visage of Fenris", rank=1, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Fangs of the North", rank=2, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Halt the Coward's Flight", rank=2, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Snarl of the Predator", rank=2, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Troll Skin", rank=2, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Might of Thor", rank=3, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Redirect Pain", rank=3, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Venom Blood", rank=3, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Heart of the Mountain", rank=4, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Hero's Stand", rank=4, allowed={"garou": ["Get of Fenris", "White Howlers"]}
)[0]
Gift.objects.get_or_create(
    name="Endurance of Heimdall", rank=5, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Horde of Valhalla", rank=5, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Fenris' Bite", rank=5, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Call Great Fenris", rank=6, allowed={"garou": ["Get of Fenris"]}
)[0]
Gift.objects.get_or_create(
    name="Control Simple Machine", rank=1, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Diagnostics", rank=1, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Plug and Play", rank=1, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Trick Shot", rank=1, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Cybersenses", rank=2, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Hands Full of Thunder", rank=2, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Power Surge", rank=2, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Steel Fur", rank=2, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Control Complex Machine", rank=3, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Intrusion", rank=3, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Electroshock", rank=3, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Elemental Favor", rank=3, allowed={"garou": ["Glass Walkers", "Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Doppelganger", rank=4, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Signal Rider", rank=4, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Tech Speak", rank=4, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Chaos Mechanics", rank=5, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Summon Net-Spider", rank=5, allowed={"garou": ["Glass Walkers"]}
)[0]
Gift.objects.get_or_create(
    name="Eye of the Hunter", rank=1, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Hidden Killer", rank=1, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Wolf at the Door", rank=1, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(name="Beastmind", rank=2, allowed={"garou": ["Red Talons"]})[
    0
]
Gift.objects.get_or_create(
    name="Shadows of the Impergium", rank=2, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Render Down", rank=3, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(name="Territory", rank=3, allowed={"garou": ["Red Talons"]})[
    0
]
Gift.objects.get_or_create(
    name="Trackless Waste", rank=3, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(name="Gorge", rank=4, allowed={"garou": ["Red Talons"]})[0]
Gift.objects.get_or_create(
    name="Howl of Death", rank=4, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Quicksand", rank=4, allowed={"garou": ["Red Talons", "Bunyip"]}
)[0]
Gift.objects.get_or_create(
    name="Curse of Lycaon", rank=5, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Gaia's Vengeance", rank=5, allowed={"garou": ["Red Talons", "White Howlers"]}
)[0]
Gift.objects.get_or_create(
    name="Scabwalker Curse", rank=5, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Shield of Gaia", rank=6, allowed={"garou": ["Red Talons"]}
)[0]
Gift.objects.get_or_create(
    name="Aura of Confidence", rank=1, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Fatal Flaw", rank=1, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Seizing the Edge", rank=1, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Shadow Weaving", rank=1, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Whisper Catching", rank=1, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Clap of Thunder", rank=2, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Cold Voice of Reason", rank=2, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Song of the Earth Mother", rank=2, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Direct the Storm", rank=3, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Icy Chill of Despair", rank=3, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Paralyzing Stare", rank=3, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Shadow Cutting", rank=3, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Under the Gun", rank=3, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Open Wounds",
    rank=4,
    allowed={"garou": ["Shadow Lords", "Black Spiral Dancers"]},
)[0]
Gift.objects.get_or_create(
    name="Durance", rank=4, allowed={"garou": ["Shadow Lords", "Uktena"]}
)[0]
Gift.objects.get_or_create(
    name="Strength of the Dominator", rank=4, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Obedience", rank=5, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Shadow Pack", rank=5, allowed={"garou": ["Shadow Lords"]}
)[0]
Gift.objects.get_or_create(
    name="Heaven's Guidance", rank=1, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Silence", rank=1, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Speed of Thought",
    rank=1,
    allowed={"garou": ["Silent Striders", "Kucha Ekundu"]},
)[0]
Gift.objects.get_or_create(
    name="Visions of Duat", rank=1, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Messenger's Fortitude", rank=2, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Tread Sebek's Back", rank=2, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Adaptation", rank=3, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Great Leap", rank=3, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Mark of the Death-Wolf", rank=3, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Black Mark", rank=4, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Dam the Heartflood", rank=4, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Speed Beyond Thought", rank=4, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Gate of the Moon", rank=5, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Reach the Umbra", rank=5, allowed={"garou": ["Silent Striders"]}
)[0]
Gift.objects.get_or_create(
    name="Eye of the Falcon", rank=1, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(
    name="Falcon's Grasp", rank=1, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(
    name="Lambent Flame", rank=1, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(name="Empathy", rank=2, allowed={"garou": ["Silver Fangs"]})[
    0
]
Gift.objects.get_or_create(
    name="Hand Blade", rank=2, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(
    name="Unity of the Pack", rank=2, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(
    name="Burning Blade", rank=3, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(
    name="Talons of the Falcon", rank=3, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(
    name="Wrath of Gaia", rank=3, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(name="Mastery", rank=4, allowed={"garou": ["Silver Fangs"]})[
    0
]
Gift.objects.get_or_create(
    name="Mindblock", rank=4, allowed={"garou": ["Silver Fangs", "Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Sidestep Death", rank=4, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(
    name="Luna's Avenger", rank=5, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(
    name="Paws of the Newborn Cub", rank=5, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(
    name="Renew the Cycle", rank=6, allowed={"garou": ["Silver Fangs"]}
)[0]
Gift.objects.get_or_create(name="Balance", rank=1, allowed={"garou": ["Stargazers"]})[0]
Gift.objects.get_or_create(
    name="Channeling", rank=1, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Iron Resolve", rank=1, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Inner Light", rank=2, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Inner Strength", rank=2, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Resist Temptation", rank=2, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Surface Attunement", rank=2, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(name="Wuxing", rank=2, allowed={"garou": ["Stargazers"]})[0]
Gift.objects.get_or_create(name="Clarity", rank=3, allowed={"garou": ["Stargazers"]})[0]
Gift.objects.get_or_create(
    name="Mericful Blow", rank=3, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Wind's Returning Favor", rank=3, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Preternatural Awareness", rank=4, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Circular Attack", rank=5, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(
    name="Harmorious Unity of the Emeral Mother",
    rank=5,
    allowed={"garou": ["Stargazers"]},
)[0]
Gift.objects.get_or_create(
    name="Wisdom of the Seer", rank=5, allowed={"garou": ["Stargazers"]}
)[0]
Gift.objects.get_or_create(name="Sense Magic", rank=1, allowed={"garou": ["Uktena"]})[0]
Gift.objects.get_or_create(
    name="Shroud", rank=1, allowed={"garou": ["Uktena", "Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Spirit of the Lizard", rank=1, allowed={"garou": ["Uktena"]}
)[0]
Gift.objects.get_or_create(
    name="Coils of the Serpent", rank=2, allowed={"garou": ["Uktena", "Bunyip"]}
)[0]
Gift.objects.get_or_create(name="Fetish Fetch", rank=2, allowed={"garou": ["Uktena"]})[
    0
]
Gift.objects.get_or_create(
    name="Shadows at Dawn", rank=2, allowed={"garou": ["Uktena"]}
)[0]
Gift.objects.get_or_create(
    name="Spirit of the Bird", rank=2, allowed={"garou": ["Uktena"]}
)[0]
Gift.objects.get_or_create(
    name="Spirit of the Fish", rank=2, allowed={"garou": ["Uktena"]}
)[0]
Gift.objects.get_or_create(name="Banish Totem", rank=3, allowed={"garou": ["Uktena"]})[
    0
]
Gift.objects.get_or_create(
    name="Chains of Mist", rank=3, allowed={"garou": ["Uktena"]}
)[0]
Gift.objects.get_or_create(name="Invisibility", rank=3, allowed={"garou": ["Uktena"]})[
    0
]
Gift.objects.get_or_create(
    name="Rending the Craft", rank=3, allowed={"garou": ["Uktena"]}
)[0]
Gift.objects.get_or_create(name="Scrying", rank=3, allowed={"garou": ["Uktena"]})[0]
Gift.objects.get_or_create(
    name="Call Elemental", rank=4, allowed={"garou": ["Uktena", "Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Hand of the Earth Lords", rank=4, allowed={"garou": ["Uktena", "Croatan"]}
)[0]
Gift.objects.get_or_create(name="Fetosj Dp;;", rank=5, allowed={"garou": ["Uktena"]})[0]
Gift.objects.get_or_create(
    name="Beat of the Heart-Drum", rank=1, allowed={"garou": ["Wendigo"]}
)[0]
Gift.objects.get_or_create(
    name="Call the Breeze", rank=1, allowed={"garou": ["Wendigo"]}
)[0]
Gift.objects.get_or_create(name="Camouflage", rank=1, allowed={"garou": ["Wendigo"]})[0]
Gift.objects.get_or_create(name="Ice Echo", rank=1, allowed={"garou": ["Wendigo"]})[0]
Gift.objects.get_or_create(name="Cutting Wind", rank=2, allowed={"garou": ["Wendigo"]})[
    0
]
Gift.objects.get_or_create(
    name="Claws of Frozen Death", rank=2, allowed={"garou": ["Wendigo"]}
)[0]
Gift.objects.get_or_create(name="Salmon Swim", rank=2, allowed={"garou": ["Wendigo"]})[
    0
]
Gift.objects.get_or_create(
    name="Speak with Wind Spirits", rank=2, allowed={"garou": ["Wendigo"]}
)[0]
Gift.objects.get_or_create(
    name="Blood of the North", rank=3, allowed={"garou": ["Wendigo"]}
)[0]
Gift.objects.get_or_create(name="Bloody Feast", rank=3, allowed={"garou": ["Wendigo"]})[
    0
]
Gift.objects.get_or_create(name="Sky Running", rank=3, allowed={"garou": ["Wendigo"]})[
    0
]
Gift.objects.get_or_create(
    name="Call of the Cannibal Spirit", rank=4, allowed={"garou": ["Wendigo"]}
)[0]
Gift.objects.get_or_create(
    name="Chill of Early Frost", rank=4, allowed={"garou": ["Wendigo"]}
)[0]
Gift.objects.get_or_create(
    name="Invoke the Spirits of the Storm", rank=5, allowed={"garou": ["Wendigo"]}
)[0]
Gift.objects.get_or_create(name="Heart of Ice", rank=5, allowed={"garou": ["Wendigo"]})[
    0
]
Gift.objects.get_or_create(
    name="See Past the Skin", rank=1, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Mask Taint", rank=5, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Bane Protector", rank=1, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Smell Fear", rank=2, allowed={"garou": ["Black Spiral Dancers", "philodox"]}
)[0]
Gift.objects.get_or_create(
    name="Ears of the Bat", rank=2, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Wyrm Hide", rank=2, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="A Thousand Voices",
    rank=2,
    allowed={"garou": ["Black Spiral Dancers", "theurge"]},
)[0]
Gift.objects.get_or_create(
    name="Allies Below", rank=2, allowed={"garou": ["Black Spiral Dancers", "galliard"]}
)[0]
Gift.objects.get_or_create(
    name="Horns of the Impaler",
    rank=2,
    allowed={"garou": ["Black Spiral Dancers", "ahroun"]},
)[0]
Gift.objects.get_or_create(
    name="Patagia", rank=3, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Foaming Fury", rank=3, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Beautiful Lie", rank=3, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Touch of the Eer",
    rank=3,
    allowed={"garou": ["Black Spiral Dancers", "ragabash"]},
)[0]
Gift.objects.get_or_create(
    name="Crawling Poison", rank=4, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Balefire", rank=5, allowed={"garou": ["Black Spiral Dancers"]}
)[0]
Gift.objects.get_or_create(
    name="Dream of a Thousand Cranes", rank=1, allowed={"garou": ["Hakken"]}
)[0]
Gift.objects.get_or_create(name="Fair Path", rank=1, allowed={"garou": ["Hakken"]})[0]
Gift.objects.get_or_create(
    name="Storm Winds Slash", rank=2, allowed={"garou": ["Hakken"]}
)[0]
Gift.objects.get_or_create(name="Dark of Night", rank=3, allowed={"garou": ["Hakken"]})[
    0
]
Gift.objects.get_or_create(
    name="Living Treasure", rank=4, allowed={"garou": ["Hakken"]}
)[0]
Gift.objects.get_or_create(name="Divine Wind", rank=5, allowed={"garou": ["Hakken"]})[0]

Gift.objects.get_or_create(
    name="Sheng-Nong's Eyes", rank=1, allowed={"garou": ["Boli Zousizhe"]}
)[0]
Gift.objects.get_or_create(
    name="Fu Xi's Honor", rank=2, allowed={"garou": ["Boli Zousizhe"]}
)[0]
Gift.objects.get_or_create(
    name="Yao's Commands", rank=3, allowed={"garou": ["Boli Zousizhe"]}
)[0]
Gift.objects.get_or_create(
    name="Yu's Endurance", rank=4, allowed={"garou": ["Boli Zousizhe"]}
)[0]
Gift.objects.get_or_create(
    name="Huang Di's Sacrifice", rank=5, allowed={"garou": ["Boli Zousizhe"]}
)[0]

Gift.objects.get_or_create(
    name="Feed the Pack", rank=2, allowed={"garou": ["Kucha Ekundu"]}
)[0]
Gift.objects.get_or_create(
    name="Predator's Many Eyes", rank=3, allowed={"garou": ["Kucha Ekundu"]}
)[0]
Gift.objects.get_or_create(
    name="Crocodile Pact", rank=5, allowed={"garou": ["Kucha Ekundu"]}
)[0]

Gift.objects.get_or_create(
    name="Bunyip's Spell", rank=1, allowed={"garou": ["Bunyip"]}
)[0]
Gift.objects.get_or_create(
    name="Crocodile's Cunning", rank=2, allowed={"garou": ["Bunyip"]}
)[0]
Gift.objects.get_or_create(
    name="Lonesome Voice of the Bunyip", rank=3, allowed={"garou": ["Bunyip"]}
)[0]
Gift.objects.get_or_create(
    name="Dance of the Lightning Snakes", rank=4, allowed={"garou": ["Bunyip"]}
)[0]
Gift.objects.get_or_create(
    name="Billabong Bridge", rank=5, allowed={"garou": ["Bunyip"]}
)[0]

Gift.objects.get_or_create(name="Turtle Body", rank=1, allowed={"garou": ["Croatan"]})[
    0
]
Gift.objects.get_or_create(name="Turtle Shell", rank=2, allowed={"garou": ["Croatan"]})[
    0
]
Gift.objects.get_or_create(
    name="Call Earth Spirit", rank=3, allowed={"garou": ["Croatan"]}
)[0]
Gift.objects.get_or_create(
    name="Stronger on Stone", rank=4, allowed={"garou": ["Croatan"]}
)[0]
Gift.objects.get_or_create(
    name="Katanka-Sonnak's Spear", rank=5, allowed={"garou": ["Croatan"]}
)[0]

Gift.objects.get_or_create(
    name="Haunting Howl", rank=1, allowed={"garou": ["White Howlers"]}
)[0]
Gift.objects.get_or_create(
    name="Pain-Strength", rank=2, allowed={"garou": ["White Howlers"]}
)[0]
Gift.objects.get_or_create(
    name="Sense of the Deep", rank=3, allowed={"garou": ["White Howlers"]}
)[0]
Gift.objects.get_or_create(
    name="Maddening Howl", rank=4, allowed={"garou": ["White Howlers"]}
)[0]
Gift.objects.get_or_create(
    name="Mad Strength", rank=5, allowed={"garou": ["White Howlers"]}
)[0]

Gift.objects.get_or_create(name="Eve's Touch", rank=1, allowed={"garou": ["kinfolk"]})[
    0
]
Gift.objects.get_or_create(
    name="Dona Nobis Pacem", rank=1, allowed={"garou": ["kinfolk"]}
)[0]
Gift.objects.get_or_create(name="Echoes", rank=1, allowed={"garou": ["kinfolk"]})[0]


Rite.objects.get_or_create(name="Rite of Cleansing", level=1, rite_type="accord")[0]
Rite.objects.get_or_create(name="Rite of Contrition", level=1, rite_type="accord")[0]
Rite.objects.get_or_create(name="Rite of Renunciation", level=2, rite_type="accord")[0]
Rite.objects.get_or_create(name="Rite of the Loyal PAck", level=3, rite_type="accord")[
    0
]
Rite.objects.get_or_create(name="Enchant the Forest", level=4, rite_type="accord")[0]
Rite.objects.get_or_create(name="Rite of the Opened Sky", level=4, rite_type="accord")[
    0
]
moot_rite = Rite.objects.get_or_create(name="Moot Rite", level=1, rite_type="caern")[0]
Rite.objects.get_or_create(name="Rite of the Opened Caern", level=1, rite_type="caern")[
    0
]
Rite.objects.get_or_create(
    name="Rite of the Glorious Past", level=3, rite_type="caern"
)[0]
Rite.objects.get_or_create(name="The Badger's Burrow", level=4, rite_type="caern")[0]
Rite.objects.get_or_create(
    name="Rite of the Opened Bridge", level=4, rite_type="caern"
)[0]
Rite.objects.get_or_create(
    name="Rite of the Shrouded Glen", level=4, rite_type="caern"
)[0]
rite_of_caern_building = Rite.objects.get_or_create(
    name="Rite of Caern Building", level=5, rite_type="caern"
)[0]
Rite.objects.get_or_create(
    name="Gathering for the Departed", level=1, rite_type="death"
)[0]
Rite.objects.get_or_create(name="Last Blessing", level=1, rite_type="death")[0]
Rite.objects.get_or_create(name="Rite of the Winter Wolf", level=3, rite_type="death")[
    0
]
Rite.objects.get_or_create(name="Baptism of Fire", level=1, rite_type="mystic")[0]
Rite.objects.get_or_create(name="Rite of Binding", level=1, rite_type="mystic")[0]
Rite.objects.get_or_create(name="Rite of Growth", level=1, rite_type="mystic")[0]
Rite.objects.get_or_create(name="Rite of Heritage", level=1, rite_type="mystic")[0]
Rite.objects.get_or_create(
    name="Rite of the Cardboard Palace", level=1, rite_type="mystic"
)[0]
Rite.objects.get_or_create(
    name="Rite of the Questing Stone", level=1, rite_type="mystic"
)[0]
Rite.objects.get_or_create(
    name="Rite of Talisman Dedication", level=1, rite_type="mystic"
)[0]
Rite.objects.get_or_create(name="Rite of Becoming", level=2, rite_type="mystic")[0]
Rite.objects.get_or_create(
    name="Rite of Spirit Awakening", level=2, rite_type="mystic"
)[0]
Rite.objects.get_or_create(name="Rite of Summoning", level=2, rite_type="mystic")[0]
Rite.objects.get_or_create(name="Rite of Sacred Rebirth", level=5, rite_type="mystic")[
    0
]
Rite.objects.get_or_create(
    name="Descent Into the Underworld", level=3, rite_type="mystic"
)[0]
Rite.objects.get_or_create(name="Rite of the Fetish", level=3, rite_type="mystic")[0]
Rite.objects.get_or_create(name="Rite of the Totem", level=3, rite_type="mystic")[0]
Rite.objects.get_or_create(name="Rite of the Jackdaw", level=1, rite_type="punishment")[
    0
]
rite_of_ostracism = Rite.objects.get_or_create(
    name="Rite of Ostracism", level=2, rite_type="punishment"
)[0]
stone_of_scorn = Rite.objects.get_or_create(
    name="Stone of Scorn", level=2, rite_type="punishment"
)[0]
rite_of_the_jackal = Rite.objects.get_or_create(
    name="Voice of the Jackal", level=2, rite_type="punishment"
)[0]
Rite.objects.get_or_create(name="The Hunt", level=3, rite_type="punishment")[0]
Rite.objects.get_or_create(
    name="Rite of the Omega Wolf", level=3, rite_type="punishment"
)[0]
Rite.objects.get_or_create(name="Satire Rite", level=3, rite_type="punishment")[0]
Rite.objects.get_or_create(
    name="The Rending of the Veil", level=4, rite_type="punishment"
)[0]
Rite.objects.get_or_create(
    name="Gaia's Vengeful Teeth", level=5, rite_type="punishment"
)[0]
Rite.objects.get_or_create(name="Rite of Boasting", level=1, rite_type="renown")[0]
rite_of_wounding = Rite.objects.get_or_create(
    name="Rite of Wounding", level=1, rite_type="renown"
)[0]
Rite.objects.get_or_create(name="Rite of Accomplishment", level=2, rite_type="renown")[
    0
]
rite_of_passage = Rite.objects.get_or_create(
    name="Rite of Passage", level=2, rite_type="renown"
)[0]
Rite.objects.get_or_create(name="Rite of Praise", level=2, rite_type="renown")[0]
Rite.objects.get_or_create(
    name="Rite of the Winter Winds", level=2, rite_type="seasonal"
)[0]
Rite.objects.get_or_create(name="Rite of Reawakening", level=2, rite_type="seasonal")[0]
Rite.objects.get_or_create(name="The Great Hunt", level=2, rite_type="seasonal")[0]
Rite.objects.get_or_create(name="The Long Vigil", level=3, rite_type="seasonal")[0]
Rite.objects.get_or_create(name="Bone Rhythms", level=0, rite_type="minor")[0]
Rite.objects.get_or_create(name="Breath of Gaia", level=0, rite_type="minor")[0]
Rite.objects.get_or_create(name="Greet the Moon", level=0, rite_type="minor")[0]
Rite.objects.get_or_create(name="Greet the Sun", level=0, rite_type="minor")[0]
Rite.objects.get_or_create(name="Hunting Prayer", level=0, rite_type="minor")[0]
Rite.objects.get_or_create(name="Prayer for the Prey", level=0, rite_type="minor")[0]

RenownIncident.objects.get_or_create(
    name="Besting someone (including a spirit) in a riddle contest",
    glory=0,
    honor=0,
    wisdom=3,
)[0]
RenownIncident.objects.get_or_create(
    name="Showing restriant in the face of certain death", glory=0, honor=1, wisdom=3
)[0]
RenownIncident.objects.get_or_create(
    name="Ending a threat without serious harm to any Garou", glory=0, honor=0, wisdom=5
)[0]
RenownIncident.objects.get_or_create(
    name="Surviving an Incapacitating wound", glory=2, honor=0, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Surviving any toxic waste attack", glory=2, honor=0, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Attacking a much more powerful force without aid", glory=0, honor=0, wisdom=-3
)[0]
RenownIncident.objects.get_or_create(
    name="Attacking a minion of the Wyrm without regard to personal safety",
    glory=3,
    honor=0,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Defeating a formidable supernatural threat not of the Wyrm (strand spider, master mage, fae warrior, Fera, etc.)",
    glory=2,
    honor=0,
    wisdom=0,
)[0]

RenownIncident.objects.get_or_create(
    name="Defeating a very powerful supernatual threat not of the Wyrm (archmage, fae sorcerer, etc.)",
    glory=3,
    honor=0,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Defeating a minor Wyrm threat (Kalus, a Bane-infested animal, young vampire, etc.)",
    glory=2,
    honor=0,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Defeating an average Wyrm threat (Blight Child, fomori, etc.)",
    glory=3,
    honor=0,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Defeating a strong Wyrm threat (Psychomachie, Black Spiral Dancer pack, etc.)",
    glory=5,
    honor=0,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Defeating a very powerful Wyrm threat (Nexus Crawler, elder vampires, etc.)",
    glory=7,
    honor=0,
    wisdom=0,
)[0]
# We are currently ignoring the four modifiers on 247 for killing, no other Garou harmed, not being hurt, and enemy with silver
RenownIncident.objects.get_or_create(
    name='Revealing, with certain proof, that a human or Kinfolk is "of the Wyrm"',
    glory=0,
    honor=0,
    wisdom=2,
)[0]
RenownIncident.objects.get_or_create(
    name='Falsely accusing a Kinfolk of being "of the Wyrm"',
    glory=0,
    honor=-2,
    wisdom=-3,
)[0]
RenownIncident.objects.get_or_create(
    name='Revealing, with certain proof, that an area or object is "of the Wyrm"',
    glory=0,
    honor=0,
    wisdom=3,
)[0]
RenownIncident.objects.get_or_create(
    name='Revealing, with certain proof, that a Garou is "of the Wyrm"',
    glory=0,
    honor=0,
    wisdom=6,
)[0]
RenownIncident.objects.get_or_create(
    name='Falsely accusing a Garou of being "of the Wyrm"', glory=0, honor=-5, wisdom=-4
)[0]
RenownIncident.objects.get_or_create(
    name="Purifying a Wyrm-tainted object, person, or place", glory=0, honor=0, wisdom=2
)[0]
RenownIncident.objects.get_or_create(
    name="Summoning an Incarna avatar", glory=0, honor=0, wisdom=2
)[0]
RenownIncident.objects.get_or_create(
    name="Traveling to any of the Umbral Realms and surviving",
    glory=3,
    honor=0,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Successfully completing a spirit quest in the Umbra",
    glory=0,
    honor=0,
    wisdom=3,
)[0]
RenownIncident.objects.get_or_create(
    name="Failing to succeed in a spirit quest in the Umbra",
    glory=0,
    honor=0,
    wisdom=-3,
)[0]
RenownIncident.objects.get_or_create(
    name="Having and properly following a prophetic dream", glory=0, honor=0, wisdom=5
)[0]
RenownIncident.objects.get_or_create(
    name="Giving a prophetic warning that later comes true", glory=0, honor=0, wisdom=5
)[0]
RenownIncident.objects.get_or_create(
    name="Ignoring omens, dreams, and the like for no good reason (i.e., suspecting they may be of the Wyrm)",
    glory=0,
    honor=0,
    wisdom=-3,
)[0]
RenownIncident.objects.get_or_create(
    name='Binding "inappropriate" items to oneself through the Rite of Talisman Dedication',
    glory=0,
    honor=0,
    wisdom=-2,
)[0]
RenownIncident.objects.get_or_create(
    name="Spending a year in ritualistic seclusion (fasting, meditation, etc.)",
    glory=0,
    honor=0,
    wisdom=5,
)[0]
RenownIncident.objects.get_or_create(
    name="Discovering a talen", glory=0, honor=0, wisdom=1
)[0]
RenownIncident.objects.get_or_create(
    name="Discovering a fetish", glory=0, honor=0, wisdom=2
)[0]
RenownIncident.objects.get_or_create(
    name="Discovering ancient Garou lore", glory=0, honor=0, wisdom=3
)[0]
RenownIncident.objects.get_or_create(
    name="Discovering a Pathstone", glory=0, honor=0, wisdom=4
)[0]
RenownIncident.objects.get_or_create(
    name="Discovering an ancient caern that was lost", glory=0, honor=0, wisdom=7
)[0]
RenownIncident.objects.get_or_create(
    name="Perfomring a Moot Rite", glory=0, honor=2, wisdom=0, rite=moot_rite
)[0]
RenownIncident.objects.get_or_create(
    name="Refusing to perform a Moot Rite when asked",
    glory=0,
    honor=-3,
    wisdom=0,
    rite=moot_rite,
)[0]
RenownIncident.objects.get_or_create(
    name="Missing a Moot Rite", glory=0, honor=0, wisdom=-1
)[0]

RenownIncident.objects.get_or_create(
    name="Performing a Rite of Passage",
    glory=0,
    honor=2,
    wisdom=1,
    rite=rite_of_passage,
)[0]
RenownIncident.objects.get_or_create(
    name="Receiving a Rite of Wounding",
    glory=2,
    honor=0,
    wisdom=0,
    rite=rite_of_wounding,
)[0]
RenownIncident.objects.get_or_create(
    name="Performing a Rite of Caern Building",
    glory=3,
    honor=5,
    wisdom=7,
    rite=rite_of_caern_building,
)[0]
RenownIncident.objects.get_or_create(
    name="Participating in a Rite of Caern Building", glory=0, honor=5, wisdom=3
)[0]
RenownIncident.objects.get_or_create(
    name="Participating in a successful Great Hunt rite", glory=3, honor=0, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Participating in a failed Great Hunt rite", glory=-2, honor=0, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Suffering the Rite of Ostracism",
    glory=-1,
    honor=-7,
    wisdom=-1,
    rite=rite_of_ostracism,
)[0]
RenownIncident.objects.get_or_create(
    name="Suffering the Stone of Scorn",
    glory=0,
    honor=-8,
    wisdom=-2,
    rite=stone_of_scorn,
)[0]
RenownIncident.objects.get_or_create(
    name="Suffering the Rite of the Jackal",
    glory=-2,
    honor=-7,
    wisdom=0,
    rite=rite_of_the_jackal,
)[0]
# No test currently for "has a punishment rite"
RenownIncident.objects.get_or_create(
    name="Performing a Punishment Rite", glory=0, honor=2, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Performing a Punishment Rite unjustly", glory=0, honor=-5, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Refusing to participate in a rite", glory=0, honor=0, wisdom=-1
)[0]
RenownIncident.objects.get_or_create(
    name="Giggling, joking, or otherwise being disrespectful during a rite",
    glory=0,
    honor=0,
    wisdom=-3,
)[0]
RenownIncident.objects.get_or_create(
    name="Learning a new rite", glory=0, honor=0, wisdom=1
)[0]
RenownIncident.objects.get_or_create(
    name="Discovering/creating a new rite", glory=0, honor=0, wisdom=5
)[0]
RenownIncident.objects.get_or_create(
    name="Discovering/creating a new gift", glory=0, honor=0, wisdom=7
)[0]
RenownIncident.objects.get_or_create(
    name="Creating a talen", glory=0, honor=0, wisdom=1
)[0]
RenownIncident.objects.get_or_create(
    name="Using a fetish for the good of the sept or tribe", glory=0, honor=0, wisdom=2
)[0]
RenownIncident.objects.get_or_create(
    name="Using a fetish for selfish reasons only", glory=0, honor=0, wisdom=-1
)[0]
RenownIncident.objects.get_or_create(
    name="Creating a fetish", glory=0, honor=0, wisdom=4
)[0]
RenownIncident.objects.get_or_create(
    name="Owning a klaive (awarded once, only after three moons of use)",
    glory=2,
    honor=1,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Owning a grand klaive (awarded once, only after three moons of use)",
    glory=3,
    honor=2,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Sacrificing a fetish for the good of the sept or tribe",
    glory=0,
    honor=0,
    wisdom=4,
)[0]
RenownIncident.objects.get_or_create(
    name="Accidentally breaking a fetish or talen", glory=0, honor=0, wisdom=-3
)[0]
RenownIncident.objects.get_or_create(
    name="Accidentally breaking or losing a klaive", glory=0, honor=-3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Helping guard a caern", glory=0, honor=1, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Staying at your post when on caern watch, even when tempted not to",
    glory=0,
    honor=2,
    wisdom=1,
)[0]
RenownIncident.objects.get_or_create(
    name="Not staying at your post when on watch", glory=0, honor=-3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Not helping guard a caern, even when asked to", glory=0, honor=-3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Keeping a caern safe from humans through trickery or negotiation",
    glory=0,
    honor=0,
    wisdom=4,
)[0]
RenownIncident.objects.get_or_create(
    name="Helping to prevent a caern from being overrun by the Wyrm",
    glory=3,
    honor=4,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Not prevenitng a caern from being overrun by the Wyrm",
    glory=-3,
    honor=-7,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Dying while defending a caern (posthumous)",
    glory=5,
    honor=8,
    wisdom=0,
    posthumous=True,
)[0]
RenownIncident.objects.get_or_create(
    name="Single-handedly preventing a caern from being taken by the Wyrm",
    glory=5,
    honor=8,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Teaching other Garou (depends on the depth of study)",
    glory=0,
    honor=3,
    wisdom=4,
)[0]
RenownIncident.objects.get_or_create(
    name="Learning the complete Silver Record (a lifetime's work)",
    glory=0,
    honor=7,
    wisdom=8,
    only_once=True,
)[0]
RenownIncident.objects.get_or_create(
    name="For a homid Garou, surviving to age 75",
    glory=0,
    honor=8,
    wisdom=10,
    breed="homid",
    only_once=True,
)[0]
RenownIncident.objects.get_or_create(
    name="For a lupus Garou, surviving to age 65",
    glory=0,
    honor=8,
    wisdom=10,
    breed="lupus",
    only_once=True,
)[0]

RenownIncident.objects.get_or_create(
    name="For a homid, ignoring one's wold nature for too long",
    glory=0,
    honor=0,
    wisdom=-3,
    breed="homid",
)[0]
RenownIncident.objects.get_or_create(
    name="For a metis, attempting to hide one's deformity",
    glory=0,
    honor=0,
    wisdom=-3,
    breed="metis",
)[0]
RenownIncident.objects.get_or_create(
    name="For a lupus, using too many human tools and other Weaver things",
    glory=0,
    honor=0,
    wisdom=-1,
    breed="lupus",
)[0]
RenownIncident.objects.get_or_create(
    name="Gaining the position of Pack leader", glory=0, honor=3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Living alone, without one's pack, except for ritual reasons",
    glory=0,
    honor=0,
    wisdom=-3,
)[0]
RenownIncident.objects.get_or_create(
    name="Performing regular duties and chores for the sept (gained at monthly Moot Rite)",
    glory=0,
    honor=1,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Failing to perform regular duties and chores for the sept (subtracted at monthly Moot Rite)",
    glory=0,
    honor=0,
    wisdom=-3,
)[0]
RenownIncident.objects.get_or_create(
    name="Disobeying a caern officer without good reason", glory=0, honor=-2, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Serving in any sept position for a year", glory=1, honor=3, wisdom=1
)[0]
RenownIncident.objects.get_or_create(
    name="Refusing any sept position", glory=-1, honor=-2, wisdom=-1
)[0]
RenownIncident.objects.get_or_create(
    name="Maintaining loyal service to a sept for a year", glory=1, honor=2, wisdom=1
)[0]
RenownIncident.objects.get_or_create(
    name="Maintaining loyal service to a tribe for a year", glory=1, honor=3, wisdom=1
)[0]
RenownIncident.objects.get_or_create(
    name="Upholding the Litany", glory=0, honor=3, wisdom=2
)[0]
RenownIncident.objects.get_or_create(
    name="Breaking the Litany", glory=0, honor=-6, wisdom=-3
)[0]
RenownIncident.objects.get_or_create(
    name="Participating in a just challenge", glory=1, honor=2, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Participating in an unjust challenge", glory=0, honor=-3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Challenging someone too far above or too far below your Rank",
    glory=0,
    honor=-3,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Giving good advice", glory=0, honor=0, wisdom=2
)[0]
RenownIncident.objects.get_or_create(
    name="Giving bad advice", glory=0, honor=0, wisdom=-2
)[0]
RenownIncident.objects.get_or_create(
    name="Mediating a dispute fairly", glory=0, honor=3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Mediating a dispute unfairly", glory=0, honor=-4, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Keeping one's promises", glory=0, honor=2, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Failing to keep one's promises", glory=0, honor=-3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(name="Being truthful", glory=0, honor=2, wisdom=0)[
    0
]
RenownIncident.objects.get_or_create(
    name="Being truthful in the face of extreme adversity", glory=0, honor=5, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Being deceptive", glory=0, honor=-3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Being deceptive in the face of extreme adversity", glory=0, honor=-1, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Having your trickery backfire", glory=0, honor=0, wisdom=-2
)[0]
RenownIncident.objects.get_or_create(
    name="Attempting to openly act outside one's auspice", glory=1, honor=-3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Telling a good story at a moot", glory=2, honor=0, wisdom=2
)[0]
RenownIncident.objects.get_or_create(
    name="Telling a true epic at a moot that is later retorld by others",
    glory=3,
    honor=1,
    wisdom=3,
)[0]
RenownIncident.objects.get_or_create(
    name="Telling an epic that is entered into the Silver Record",
    glory=0,
    honor=4,
    wisdom=6,
)[0]
RenownIncident.objects.get_or_create(
    name="Speaking dishonorably to one's elders", glory=0, honor=-3, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Speaking without permission at a moot", glory=0, honor=-1, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Speaking poorly of the Garou as a whole", glory=0, honor=-2, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Speaking poorly of one's auspice", glory=0, honor=-4, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Speaking poorly of one's tribe", glory=0, honor=-4, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Speaking poorly of one's pack", glory=0, honor=-6, wisdom=0
)[0]

RenownIncident.objects.get_or_create(
    name="Speaking poorly of another tribe (except Bone Gnawers)",
    glory=0,
    honor=-1,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Summoning help when there is no real danger present",
    glory=0,
    honor=-5,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Healing a fellow Garou (non-pack member) unselifishly",
    glory=0,
    honor=0,
    wisdom=1,
)[0]
RenownIncident.objects.get_or_create(
    name="Showing mercy to a wayward Garou", glory=0, honor=0, wisdom=3
)[0]
RenownIncident.objects.get_or_create(
    name="Protecting a helpless Garou", glory=0, honor=4, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Not protecting a helpless Garou", glory=0, honor=-5, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Protecting a helpless human", glory=0, honor=2, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Not protecting a helpless human", glory=0, honor=-1, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Protecting a helpless wolf", glory=0, honor=5, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Not protecting a helpless wolf", glory=0, honor=-6, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Supporting an innocent being accused of a crime (who is later proven innocent)",
    glory=0,
    honor=5,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Supporting an innocent being accused of a crime (who is later proven guilty)",
    glory=0,
    honor=-4,
    wisdom=0,
)[0]
RenownIncident.objects.get_or_create(
    name="Dying while defending your pack (posthumous)",
    glory=4,
    honor=6,
    wisdom=0,
    posthumous=True,
)[0]
RenownIncident.objects.get_or_create(
    name="Dying in defense of Gaia (posthumous)",
    glory=7,
    honor=7,
    wisdom=0,
    posthumous=True,
)[0]
RenownIncident.objects.get_or_create(
    name="Succumbing to a berserk frenzy", glory=0, honor=0, wisdom=-1
)[0]
RenownIncident.objects.get_or_create(
    name="Succumbing to a fox frenzy", glory=-1, honor=0, wisdom=-1
)[0]
RenownIncident.objects.get_or_create(
    name="Succumbing to a fox frenzy and abandoning your pack in time of need",
    glory=0,
    honor=-1,
    wisdom=-2,
)[0]
RenownIncident.objects.get_or_create(
    name="Succumbing to a berserk frenzy and injuring fellow Garou",
    glory=0,
    honor=0,
    wisdom=-3,
)[0]
RenownIncident.objects.get_or_create(
    name="Succumbing to the thrall of the Wyrm", glory=0, honor=0, wisdom=-4
)[0]
RenownIncident.objects.get_or_create(
    name="Performing a heinous act while in the thrall of the Wyrm (cannibalism, perversion, attacking your own packmates, etc.)",
    glory=0,
    honor=-3,
    wisdom=-1,
)[0]
RenownIncident.objects.get_or_create(
    name="Maintaining good relations with nearby Kinfolk", glory=0, honor=0, wisdom=2
)[0]
RenownIncident.objects.get_or_create(
    name="Having poor relations with nearby Kinfolk", glory=0, honor=0, wisdom=-3
)[0]
RenownIncident.objects.get_or_create(
    name="Choosing a mate and breeding", glory=0, honor=0, wisdom=3
)[0]
RenownIncident.objects.get_or_create(
    name="Choosing a mate, but not breeding", glory=0, honor=0, wisdom=-1
)[0]
RenownIncident.objects.get_or_create(
    name="Staying honorably mated for a year", glory=0, honor=2, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Protecting the Veil", glory=0, honor=4, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Harming or rending the Veil", glory=0, honor=-5, wisdom=0
)[0]
RenownIncident.objects.get_or_create(
    name="Repairing the Veil", glory=0, honor=3, wisdom=1
)[0]

Archetype.objects.get_or_create(name="Alpha")[0]
Archetype.objects.get_or_create(name="Architect")[0]
Archetype.objects.get_or_create(name="Barterer")[0]
Archetype.objects.get_or_create(name="Big Bad Wolf")[0]
Archetype.objects.get_or_create(name="Bon Vivant")[0]
Archetype.objects.get_or_create(name="Bravo")[0]
Archetype.objects.get_or_create(name="Caregiver")[0]
Archetype.objects.get_or_create(name="Celebrant")[0]
Archetype.objects.get_or_create(name="Competitor")[0]
Archetype.objects.get_or_create(name="Conformist")[0]
Archetype.objects.get_or_create(name="Conniver")[0]
Archetype.objects.get_or_create(name="Contrary")[0]
Archetype.objects.get_or_create(name="Cub")[0]
Archetype.objects.get_or_create(name="Director")[0]
Archetype.objects.get_or_create(name="Fanatic")[0]
Archetype.objects.get_or_create(name="Fatalist")[0]
Archetype.objects.get_or_create(name="Gallant")[0]
Archetype.objects.get_or_create(name="Guru")[0]
Archetype.objects.get_or_create(name="Idealist")[0]
Archetype.objects.get_or_create(name="Judge")[0]
Archetype.objects.get_or_create(name="Loner")[0]
Archetype.objects.get_or_create(name="Martyr")[0]
Archetype.objects.get_or_create(name="Pedagogue")[0]
Archetype.objects.get_or_create(name="Penitent")[0]
Archetype.objects.get_or_create(name="Perfectionist")[0]
Archetype.objects.get_or_create(name="Rebel")[0]
Archetype.objects.get_or_create(name="Rogue")[0]
Archetype.objects.get_or_create(name="Scientist")[0]
Archetype.objects.get_or_create(name="Soldier")[0]
Archetype.objects.get_or_create(name="Survivor")[0]
Archetype.objects.get_or_create(name="Thrill-Seeker")[0]
Archetype.objects.get_or_create(name="Traditionalist")[0]
Archetype.objects.get_or_create(name="Trickster")[0]
Archetype.objects.get_or_create(name="Visionary")[0]

Camp.objects.get_or_create(name="Amazons of Diana", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Bacchantes/Maenads", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Freebooters", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Moon-Daughters", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Order of Our Merciful Mother", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="The Sisterhood", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="The Temple of Artemis", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Deserters", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Frankenweilers", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Maneaters", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Hillfolk", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="The Hood", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Rat Finks", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Road Warders", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="The Swarm", tribe=bone_gnawers)[0]
Camp.objects.get_or_create(name="Aethera Inamorata", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="Angels in the Garden", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="The Anounted Ones", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="Bringers of Eternal Peace", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="Demeter's Daughters", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="Imminent Strike", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="The One Tree", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="The Patient Deed", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="Seekers of the Lost Tribes", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="Servants of Unicorn", tribe=children_of_gaia)[0]
Camp.objects.get_or_create(name="Brotherhood of Herne", tribe=fianna)[0]
Camp.objects.get_or_create(name="Children of Dire", tribe=fianna)[0]
Camp.objects.get_or_create(name="Grandchildren of Fionn", tribe=fianna)[0]
Camp.objects.get_or_create(name="Mother's Fundamentalists", tribe=fianna)[0]
Camp.objects.get_or_create(name="Songkeepers", tribe=fianna)[0]
Camp.objects.get_or_create(name="Tuatha de Fionn", tribe=fianna)[0]
Camp.objects.get_or_create(name="Whispering Rovers", tribe=fianna)[0]
Camp.objects.get_or_create(name="The Fangs of Garm", tribe=get_of_fenris)[0]
Camp.objects.get_or_create(name="The Glorious Fist of Wotan", tribe=get_of_fenris)[0]
Camp.objects.get_or_create(name="The Hand of Tyr", tribe=get_of_fenris)[0]
Camp.objects.get_or_create(name="Loki's Smile", tribe=get_of_fenris)[0]
Camp.objects.get_or_create(name="Mjolnir's Thunder", tribe=get_of_fenris)[0]
Camp.objects.get_or_create(name="The Swords of Heimdall", tribe=get_of_fenris)[0]
Camp.objects.get_or_create(name="The Valkyria of Freya", tribe=get_of_fenris)[0]
Camp.objects.get_or_create(name="Ymir's Sweat", tribe=get_of_fenris)[0]
Camp.objects.get_or_create(name="City Farmers", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="Corporate Wolves", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="Cyber Dogs", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="Dies Ultimae", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="Mechanical Awakening", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="Random Interrupts", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="Umbral Pilots", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="Urban Primitives", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="Wise Guys", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="The Dying Cubs", tribe=red_talons)[0]
Camp.objects.get_or_create(name="The Lodge of the Predator Kings", tribe=red_talons)[0]
Camp.objects.get_or_create(name="Warders of the Land", tribe=red_talons)[0]
Camp.objects.get_or_create(name="Whelp's Compromise", tribe=red_talons)[0]
Camp.objects.get_or_create(name="The Masks", tribe=shadow_lords)[0]
Camp.objects.get_or_create(name="Bringers of Light", tribe=shadow_lords)[0]
Camp.objects.get_or_create(name="Children of Crow", tribe=shadow_lords)[0]
Camp.objects.get_or_create(name="Judges of Doom", tribe=shadow_lords)[0]
Camp.objects.get_or_create(name="Lords of the Summit", tribe=shadow_lords)[0]
Camp.objects.get_or_create(name="Revolutionary Guard", tribe=shadow_lords)[0]
Camp.objects.get_or_create(name="Society of Nidhogg", tribe=shadow_lords)[0]
Camp.objects.get_or_create(name="The Bitter Hex", tribe=silent_striders)[0]
Camp.objects.get_or_create(name="The Dispossessed", tribe=silent_striders)[0]
Camp.objects.get_or_create(name="Harbingers", tribe=silent_striders)[0]
Camp.objects.get_or_create(name="Eaters of the Dead", tribe=silent_striders)[0]
Camp.objects.get_or_create(name="Seekers", tribe=silent_striders)[0]
Camp.objects.get_or_create(name="Swords of Night", tribe=silent_striders)[0]
Camp.objects.get_or_create(name="Wayfarers", tribe=silent_striders)[0]
Camp.objects.get_or_create(name="Grey Raptors", tribe=silver_fangs)[0]
Camp.objects.get_or_create(name="Ivory Priesthood", tribe=silver_fangs)[0]
Camp.objects.get_or_create(name="Masters of the Seal", tribe=silver_fangs)[0]
Camp.objects.get_or_create(name="Renewal", tribe=silver_fangs)[0]
Camp.objects.get_or_create(name="Ana-gamin", tribe=stargazers)[0]
Camp.objects.get_or_create(
    name="The Heavenly Successors of the Demon-Eater", tribe=stargazers
)[0]
Camp.objects.get_or_create(name="The Inner Path", tribe=stargazers)[0]
Camp.objects.get_or_create(name="Klaital Puk", tribe=stargazers)[0]
Camp.objects.get_or_create(name="Ouroboroans", tribe=stargazers)[0]
Camp.objects.get_or_create(name="The Sacred Thread", tribe=stargazers)[0]
Camp.objects.get_or_create(name="Trance Runners", tribe=stargazers)[0]
Camp.objects.get_or_create(name="The World Tree", tribe=stargazers)[0]
Camp.objects.get_or_create(name="The Zephyr", tribe=stargazers)[0]
Camp.objects.get_or_create(name="The Metastic Birth", tribe=stargazers)[0]
Camp.objects.get_or_create(name="Bane Tenders", tribe=uktena)[0]
Camp.objects.get_or_create(name="Earth Guides", tribe=uktena)[0]
Camp.objects.get_or_create(name="Path Dancers", tribe=uktena)[0]
Camp.objects.get_or_create(name="Scouts", tribe=uktena)[0]
Camp.objects.get_or_create(name="Skywalkers", tribe=uktena)[0]
Camp.objects.get_or_create(name="Society of Bitter Frost", tribe=uktena)[0]
Camp.objects.get_or_create(name="Web Walkers", tribe=uktena)[0]
Camp.objects.get_or_create(name="Wyld Children", tribe=uktena)[0]
Camp.objects.get_or_create(name="Gluskap's Lodge", tribe=wendigo)[0]
Camp.objects.get_or_create(name="Myeengun's Lodge", tribe=wendigo)[0]
Camp.objects.get_or_create(name="The Sacred Hoop", tribe=wendigo)[0]
Camp.objects.get_or_create(name="The Secret Hoop", tribe=wendigo)[0]
Camp.objects.get_or_create(name="The Warpath", tribe=wendigo)[0]
Camp.objects.get_or_create(name="Fang Breakers", tribe=None)[0]
Camp.objects.get_or_create(name="Ghost Dancers", tribe=None)[0]
Camp.objects.get_or_create(name="Lazarite Movement", tribe=None)[0]
Camp.objects.get_or_create(name="Hakken", tribe=shadow_lords)[0]
Camp.objects.get_or_create(name="Boli Zousizhe", tribe=glass_walker)[0]
Camp.objects.get_or_create(name="Kucha Ekundu", tribe=red_talons)[0]

Camp.objects.get_or_create(
    name="Lodge of the Moon", tribe=silver_fangs, camp_type="lodge"
)[0]
Camp.objects.get_or_create(
    name="Lodge of the Sun", tribe=silver_fangs, camp_type="lodge"
)[0]
Camp.objects.get_or_create(
    name="House Austere Howl", tribe=silver_fangs, camp_type="house"
)[0]
Camp.objects.get_or_create(
    name="The Blood-Red Crest", tribe=silver_fangs, camp_type="house"
)[0]
Camp.objects.get_or_create(
    name="Clan Crescent Moon", tribe=silver_fangs, camp_type="house"
)[0]
Camp.objects.get_or_create(
    name="House Gleaming Eye", tribe=silver_fangs, camp_type="house"
)[0]
Camp.objects.get_or_create(
    name="House Unbreakable Hearth", tribe=silver_fangs, camp_type="house"
)[0]
Camp.objects.get_or_create(
    name="House Wise Heart", tribe=silver_fangs, camp_type="house"
)[0]
Camp.objects.get_or_create(name="House Wyrmfoe", tribe=silver_fangs, camp_type="house")[
    0
]
Camp.objects.get_or_create(
    name="Renewalists", tribe=silver_fangs, camp_type="philosophy"
)[0]
Camp.objects.get_or_create(
    name="Royalists", tribe=silver_fangs, camp_type="philosophy"
)[0]

Fetish.objects.get_or_create(
    name="Apeskin",
    rank=1,
    gnosis=6,
    description="",
    spirit="Homid Ancestor-Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Harmony Flute",
    rank=1,
    gnosis=5,
    description="",
    spirit="Bird Spirit or Spirit of Peace, Calm, or Water",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Magpie's Swag",
    rank=1,
    gnosis=5,
    description="",
    spirit="Magpie or Marsupial Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Mirrorshades",
    rank=1,
    gnosis=7,
    description="",
    spirit="Glass Elemental",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Nyx's Bangle",
    rank=1,
    gnosis=6,
    description="",
    spirit="Night or Darkness Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Truth Earring",
    rank=1,
    gnosis=6,
    description="",
    spirit="Servant of Falcon",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Cup of the Alicorn",
    rank=2,
    gnosis=6,
    description="",
    spirit="Spirit of Healing or a Snake or Bear Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Chameleon Skin",
    rank=2,
    gnosis=7,
    description="",
    spirit="Chameleon Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Dagger of Retribution",
    rank=2,
    gnosis=5,
    description="",
    spirit="Vengeance Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Dream Stealer",
    rank=2,
    gnosis=5,
    description="",
    spirit="Dream Spirit or one of Cuckoo's Brood",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Spirit Tracer",
    rank=2,
    gnosis=5,
    description="",
    spirit="Predator Spirit or Spirit with the Tracking Charm",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Baneskin",
    rank=3,
    gnosis=7,
    description="",
    spirit="Parrot or Mockingbird Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Beast Mask",
    rank=3,
    gnosis=8,
    description="",
    spirit="Appropriate Animal Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="D'siah",
    rank=3,
    gnosis=6,
    description="",
    spirit="War Spirit, usually Cobra's Brood",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Fang Dagger",
    rank=3,
    gnosis=6,
    description="",
    spirit="Snake Spirit or Spirit of War, Pain, or Death",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Partridge Wing",
    rank=3,
    gnosis=7,
    description="",
    spirit="Spirit of Water or Forgetfulness",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Phoebe's Veil",
    rank=3,
    gnosis=7,
    description="",
    spirit="Lune, Chameleon Spirit, Spirit of Illusion or Shadow",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Sanctuary Chimes",
    rank=3,
    gnosis=6,
    description="",
    spirit="Spirit of Protection or a Turtle Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Sun Whip",
    rank=3,
    gnosis=7,
    description="",
    spirit="Spirit of Flame or Sunlight",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Wind Whistle",
    rank=3,
    gnosis=5,
    description="",
    spirit="Wind Elemental",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Feathered Cloak",
    rank=4,
    gnosis=8,
    description="",
    spirit="Bird Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Ironhammer",
    rank=4,
    gnosis=5,
    description="",
    spirit="Spirit if War",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Klaive", rank=4, gnosis=6, description="", spirit="War Spirit", display=False,
)[0]
Fetish.objects.get_or_create(
    name="Labrys of Isthmene",
    rank=4,
    gnosis=7,
    description="",
    spirit="War Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Monkey Puzzle",
    rank=4,
    gnosis=6,
    description="",
    spirit="Ghost, Spirit of Illusion, or Trickster Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Spirit Whistle",
    rank=4,
    gnosis=8,
    description="",
    spirit="Screech-Owl Spirit, Spirit of Madness or Discord",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Personal Umbral Digital Application",
    rank=4,
    gnosis=8,
    description="",
    spirit="Bee Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Unbroken Cord",
    rank=4,
    gnosis=6,
    description="",
    spirit="Unity Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Grand Klaive",
    rank=5,
    gnosis=7,
    description="",
    spirit="War Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Jarlhammer",
    rank=5,
    gnosis=6,
    description="",
    spirit="Spirits of War and Silver",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Runestones",
    rank=5,
    gnosis=7,
    description="",
    spirit="Spirit of Time, Dream, Enigmas, or Wisdom",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Bane Arrows",
    rank=0,
    gnosis=4,
    description="",
    spirit="Spirit of War, Air or Pain",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Chiropteran Spies",
    rank=0,
    gnosis=6,
    description="",
    spirit="Bat Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Death Dust",
    rank=0,
    gnosis=6,
    description="",
    spirit="Spirit of Death, Communication, or Divination",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Gaia's Breath",
    rank=0,
    gnosis=5,
    description="",
    spirit="Spirit of Healing",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Moon Glow", rank=0, gnosis=8, description="", spirit="Lune", display=False,
)[0]
Fetish.objects.get_or_create(
    name="Moon Sign",
    rank=0,
    gnosis=5,
    description="",
    spirit="Lune, Wyld Spirit, or Wolf Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Nightshade",
    rank=0,
    gnosis=5,
    description="",
    spirit="Spirit of Night or Darkness",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Wind Snorkel",
    rank=0,
    gnosis=3,
    description="",
    spirit="Air Elemental",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Wym Scale",
    rank=0,
    gnosis=8,
    description="",
    spirit="Wyrm Spirit",
    display=False,
)[0]

Fetish.objects.get_or_create(
    name="Horn of Distress",
    rank=1,
    gnosis=3,
    description="",
    spirit="Peacock or Air Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Amulet of Kinship",
    rank=2,
    gnosis=5,
    description="",
    spirit="Ancestor Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Klaive Hammer",
    rank=3,
    gnosis=5,
    description="",
    spirit="Balance, Light, or Fire Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Test Vial",
    rank=0,
    gnosis=3,
    description="",
    spirit="Ancestor, Divination, or Crow Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Hero's Mead",
    rank=0,
    gnosis=5,
    description="",
    spirit="Thunder Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Long Whispers",
    rank=0,
    gnosis=7,
    description="",
    spirit="Dove or Pigeon Spirit",
    display=False,
)[0]
Fetish.objects.get_or_create(
    name="Dire Call", rank=0, gnosis=9, description="", spirit="Lune", display=False,
)[0]

SpiritCharm.objects.get_or_create(name="Airt Sense")[0]
SpiritCharm.objects.get_or_create(name="Materialize")[0]
SpiritCharm.objects.get_or_create(name="Realm Sense")[0]
SpiritCharm.objects.get_or_create(name="Re-form")[0]
SpiritCharm.objects.get_or_create(name="Armor")[0]
SpiritCharm.objects.get_or_create(name="Blast")[0]
SpiritCharm.objects.get_or_create(name="Cleanse the Blight")[0]
SpiritCharm.objects.get_or_create(name="Control Electrical Systems")[0]
SpiritCharm.objects.get_or_create(name="Create Fires")[0]
SpiritCharm.objects.get_or_create(name="Create Wind")[0]
SpiritCharm.objects.get_or_create(name="Illuminate")[0]
SpiritCharm.objects.get_or_create(name="Flood")[0]
SpiritCharm.objects.get_or_create(name="Freeze")[0]
SpiritCharm.objects.get_or_create(name="Healing")[0]
SpiritCharm.objects.get_or_create(name="Peek")[0]
SpiritCharm.objects.get_or_create(name="Shapeshift")[0]
SpiritCharm.objects.get_or_create(name="Shatter Glass")[0]
SpiritCharm.objects.get_or_create(name="Short Out")[0]
SpiritCharm.objects.get_or_create(name="Swift Flight")[0]
SpiritCharm.objects.get_or_create(name="Tracking")[0]
SpiritCharm.objects.get_or_create(name="Umbraquake")[0]
SpiritCharm.objects.get_or_create(name="Updraft")[0]
SpiritCharm.objects.get_or_create(name="Blighted Touch")[0]
SpiritCharm.objects.get_or_create(name="Corruption")[0]
SpiritCharm.objects.get_or_create(name="Incite Frenze")[0]
SpiritCharm.objects.get_or_create(name="Possession")[0]
SpiritCharm.objects.get_or_create(name="Calcify")[0]
SpiritCharm.objects.get_or_create(name="Solidify Reality")[0]
SpiritCharm.objects.get_or_create(name="Spirit Static")[0]
SpiritCharm.objects.get_or_create(name="Break Reality")[0]
SpiritCharm.objects.get_or_create(name="Disorient")[0]

for g in Gift.objects.all():
    SpiritCharm.objects.get_or_create(name=g.name)[0]

SpiritCharacter.objects.get_or_create(
    name="Deer", willpower=4, rage=4, gnosis=6, essence=14, display=False
)[0]
x = SpiritCharacter.objects.get_or_create(
    name="Falcon", willpower=8, rage=6, gnosis=5, essence=19, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Swift Flight"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Snake", willpower=5, rage=6, gnosis=8, essence=19, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Paralyzing Stare"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Wolf", willpower=6, rage=7, gnosis=5, essence=18, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Tracking"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Glade Child (Sapling)",
    willpower=7,
    rage=3,
    gnosis=8,
    essence=20,
    display=False,
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Cleanse the Blight", "Realm Sense"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Glade Child (Mature)",
    willpower=7,
    rage=3,
    gnosis=8,
    essence=35,
    display=False,
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Cleanse the Blight", "Realm Sense"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Glade Child (Ancient)",
    willpower=7,
    rage=3,
    gnosis=8,
    essence=50,
    display=False,
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Cleanse the Blight", "Realm Sense"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Lune", willpower=8, rage=4, gnosis=7, essence=19, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Open Moon Bridge"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Stormcrows", willpower=9, rage=7, gnosis=6, essence=22, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Create Wind", "Tracking"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="The Wendigo", willpower=7, rage=10, gnosis=5, essence=32, display=False
)[0]
x.charms.set(
    SpiritCharm.objects.filter(
        name__in=["Blast", "Create Wind", "Freeze", "Materialize", "Tracking"]
    )
)
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="The Wild Hunt (Huntsman)",
    willpower=10,
    rage=10,
    gnosis=5,
    essence=40,
    display=False,
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Armor", "Materialize", "Tracking"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="The Wild Hunt (The Hounds)",
    willpower=6,
    rage=7,
    gnosis=2,
    essence=18,
    display=False,
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Materialize", "Tracking"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Ancestor Spirit", willpower=6, rage=8, gnosis=7, essence=21, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=[]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Earth Elemental", willpower=9, rage=4, gnosis=5, essence=20, display=False
)[0]
x.charms.set(
    SpiritCharm.objects.filter(name__in=["Armor", "Materialize", "Umbraquake"])
)
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Air Elemental", willpower=3, rage=8, gnosis=7, essence=18, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Create Wind", "Updraft"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Fire Elemental", willpower=5, rage=10, gnosis=5, essence=20, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Blast", "Create Fires"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Water Elemental", willpower=6, rage=4, gnosis=10, essence=20, display=False
)[0]
x.charms.set(
    SpiritCharm.objects.filter(name__in=["Cleanse the Blight", "Flood", "Healing"])
)
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Glass Elemental", willpower=4, rage=7, gnosis=7, essence=18, display=False
)[0]
x.charms.set(
    SpiritCharm.objects.filter(name__in=["Blast", "Materialize", "Shatter Glass"])
)
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Electricity Elemental",
    willpower=6,
    rage=7,
    gnosis=5,
    essence=18,
    display=False,
)[0]
x.charms.set(
    SpiritCharm.objects.filter(
        name__in=["Blast", "Control Electrical Systems", "Short Out"]
    )
)
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Chimerling", willpower=3, rage=5, gnosis=10, essence=18, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Shapeshift"]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Engling", willpower=5, rage=1, gnosis=10, essence=16, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=[]))
x.save()
x = SpiritCharacter.objects.get_or_create(
    name="Curiosi", willpower=5, rage=3, gnosis=9, essence=17, display=False
)[0]
x.charms.set(SpiritCharm.objects.filter(name__in=["Illuminate"]))
x.save()

for spirit in SpiritCharacter.objects.all():
    for x in SpiritCharm.objects.filter(
        name__in=["Airt Sense", "Materialize", "Realm Sense", "Re-Form",]
    ):
        spirit.charms.add(x)


Totem.objects.get_or_create(
    name="Falcon",
    cost=5,
    totem_type="respect",
    individual_traits="2 points of Honor Renown",
    pack_traits="Three Dots of Leadership and 4 Willpower points per story",
    ban="Death before Dishonor",
)[0]
Totem.objects.get_or_create(
    name="Grandfather Thunder",
    cost=7,
    totem_type="respect",
    individual_traits="1 point of Honor Renown, 2 dice on intimidate rolls when invoking Thunder's name",
    pack_traits="3 dots of Etiquette, 5 points of Willpower per Story, interest of the Shadow Lords",
    ban="Must not show unearned respect",
)[0]
Totem.objects.get_or_create(
    name="Pegasus",
    cost=4,
    totem_type="respect",
    individual_traits="2 points of Honor Renown",
    pack_traits="3 dots of Animal Ken and 3 points of Willpower per story, friendship of the Black Furies",
    ban="Cannot refuse to help females of any species",
)[0]
Totem.objects.get_or_create(
    name="Stag",
    cost=6,
    totem_type="respect",
    individual_traits="3 points of Honor Renown, 1 point of Stamina only for long-distance running",
    pack_traits="3 dots of Survival and 3 points of Willpower per story, Fianne and the Fae are well-disposed towards the pack",
    ban="Cannot refuse to aid the Fae and must always respect their prey",
)[0]
Totem.objects.get_or_create(
    name="Bear",
    cost=5,
    totem_type="war",
    individual_traits="1 dot of Strength, can use Mother's Touch once per day, hibernate for three months, lose 5 points of temporary Honor Renown and reduce all Honor Renown rewards by 1",
    pack_traits="3 dots of Medicine, friendship with Gurahl",
    ban="",
)[0]
Totem.objects.get_or_create(
    name="Boar",
    cost=5,
    totem_type="war",
    individual_traits="1 dot of Stamina",
    pack_traits="2 dots of Brawl",
    ban="Never hunt or eat wild boars",
)[0]
Totem.objects.get_or_create(
    name="Fenris",
    cost=5,
    totem_type="war",
    individual_traits="2 points of Glory Renown, increase 1 Physical Attribute by 1 dot",
    pack_traits="Respect of the Get of Fenris",
    ban="Never pass up a worthy fight",
)[0]
Totem.objects.get_or_create(
    name="Griffin",
    cost=4,
    totem_type="war",
    individual_traits="Communicate with birds of prey, gain 2 dots of Glory Renown",
    pack_traits="3 dots of Alertness and respect of Red Talons",
    ban="Cannot associate with humans, has never accepted a pack with a homid",
)[0]
Totem.objects.get_or_create(
    name="Rat",
    cost=5,
    totem_type="war",
    individual_traits="-1 difficulty on all bite rolls and rolls involving stealth or quiet",
    pack_traits="5 Willpower points per story, friendship of Bone Gnawers and some Ratkin",
    ban="Never kill vermin of any kind",
)[0]
Totem.objects.get_or_create(
    name="Wendigo",
    cost=7,
    totem_type="war",
    individual_traits="Start each story with +5 points of Rage, gain two dots of Glory Renown",
    pack_traits="Respect of the Wendigo tribe",
    ban="Must aid animists in need",
)[0]
Totem.objects.get_or_create(
    name="Chimera",
    cost=7,
    totem_type="wisdom",
    individual_traits="-2 difficulty to solve riddles, interpret dreams, or enigmas, and gain 2 points of Wisdom Renown. They can also disguise themselves as something else in the Umbra with a Gnosis roll at difficulty 7",
    pack_traits="3 dots of Enigmas and 1 dot of Perception",
    ban="Must seek enlightenment",
)[0]
Totem.objects.get_or_create(
    name="Cockroach",
    cost=6,
    totem_type="wisdom",
    individual_traits="-2 to all difficulties involving computers, electricity, and applied science. May perceive data streams in the Umbra, parsing it with Gnosis (difficulty 6)",
    pack_traits="3 dice to activate any Gift involving technology",
    ban="Never kill a cockroach",
)[0]
Totem.objects.get_or_create(
    name="Owl",
    cost=5,
    totem_type="wisdom",
    individual_traits="Wings in the Umbra, -2 difficulty for stealth and silence, and 2 points of Wisdom Renown",
    pack_traits="Premonitions and prophetic dreams, 3 dice for any Gift that uses air travel, movement, or darkness. May be aided by Silent Striders but will have the enmity of followers of Rat",
    ban="Must leave small rodents tied and helpless in the woods for Owl and his kind",
)[0]
Totem.objects.get_or_create(
    name="Raven",
    cost=5,
    totem_type="wisdom",
    individual_traits="One point of Wisdom Renown",
    pack_traits="3 dots of Survival, 1 of Subterfuge, 1 of Enigmas, friendship of Wereravens",
    ban="Cannot carry wealth",
)[0]
Totem.objects.get_or_create(
    name="Uktena",
    cost=7,
    totem_type="wisdom",
    individual_traits="3 dice to soak in the Umbra, 2 XP per story to be spent on Enigmas, Occult, Rituals, Gifts, or other mystical knowledge. Two points of Wisdom Renown. +1 difficulty on interacting with werewolves who are not Uktena or Wendigo",
    pack_traits="Treated by the Uktena as brothers",
    ban="Must recover mystical lore, objects, places, and animals from the minions of the Wyrm",
)[0]
Totem.objects.get_or_create(
    name="Unicorn",
    cost=7,
    totem_type="wisdom",
    individual_traits="Move at double speed in the Umbra, -2 to all difficulties on healing and empathy, +2 difficulty to attempts to harm Garou who are not Wyrm-tainted, gain 3 points of Wisdom Renown",
    pack_traits="3 dice when using Gifts of healing, strength, and protection. Children of Gaia will aid the pack.",
    ban="Must protect and aid the weak and exploited.",
)[0]
Totem.objects.get_or_create(
    name="Coyote",
    cost=7,
    totem_type="cunning",
    individual_traits="-1 from all temporary Wisdowm Renown awards",
    pack_traits="3 dots of stealth, 3 dots of streetwise, 1 dot of subterfuge, 1 dot of survival. Coyote's avatars can always find the pack.",
    ban="",
)[0]
Totem.objects.get_or_create(
    name="Cuckoo",
    cost=6,
    totem_type="cunning",
    individual_traits="-2 from awards of temporary Honor Renown",
    pack_traits="1 dot of Manipulation, 2 dots of Subterfuge, the ability to be overlooked",
    ban="Never pass up a chance to improve pack's position at the expense of others",
)[0]
Totem.objects.get_or_create(
    name="Fox",
    cost=7,
    totem_type="cunning",
    individual_traits="1 dot of Manipulation, -1 from awards of temporary Honor Renown",
    pack_traits="2 dots of Stealth, 2 dots of Streetwise, and 3 dots of Subterfuge",
    ban="May never participate in a fox hunt and must sabotage any they find",
)[0]

BattleScar.objects.get_or_create(name="Superficial Scars", glory=1)[0]
BattleScar.objects.get_or_create(name="Deep Scar", glory=1)[0]
BattleScar.objects.get_or_create(name="Improper Bone Setting", glory=1)[0]
BattleScar.objects.get_or_create(name="Cosmetic Damage", glory=2)[0]
BattleScar.objects.get_or_create(name="Broken Jaw", glory=1)[0]
BattleScar.objects.get_or_create(name="Missing Eye", glory=2)[0]
BattleScar.objects.get_or_create(name="Gelded", glory=1)[0]
BattleScar.objects.get_or_create(name="Collapsed Lung", glory=1)[0]
BattleScar.objects.get_or_create(name="Missing Fingers", glory=2)[0]
BattleScar.objects.get_or_create(name="Maimed Limb", glory=3)[0]
BattleScar.objects.get_or_create(name="Spinal Damage", glory=2)[0]
BattleScar.objects.get_or_create(name="Brain Damage", glory=2)[0]

FomoriPower.objects.get_or_create(name="Animal Control")[0]
FomoriPower.objects.get_or_create(name="Armored Hide")[0]
FomoriPower.objects.get_or_create(name="Armored Skin")[0]
FomoriPower.objects.get_or_create(name="Berserker")[0]
FomoriPower.objects.get_or_create(name="Bestial Mutation")[0]
FomoriPower.objects.get_or_create(name="Body-Barbs")[0]
FomoriPower.objects.get_or_create(name="Body Expansion")[0]
FomoriPower.objects.get_or_create(name="Brain Eating")[0]
FomoriPower.objects.get_or_create(name="Cancerous Carapace")[0]
FomoriPower.objects.get_or_create(name="Cause Insanity")[0]
FomoriPower.objects.get_or_create(name="Chameleon Coloration")[0]
FomoriPower.objects.get_or_create(name="Claws and Fangs")[0]
FomoriPower.objects.get_or_create(name="Darksight")[0]
FomoriPower.objects.get_or_create(name="Deception")[0]
FomoriPower.objects.get_or_create(name="Dentata Orifice")[0]
FomoriPower.objects.get_or_create(name="Echoes of Wrath")[0]
FomoriPower.objects.get_or_create(name="Ectoplasmic Extrusion")[0]
FomoriPower.objects.get_or_create(name="Exoskeleton")[0]
FomoriPower.objects.get_or_create(name="Extra Limbss")[0]
FomoriPower.objects.get_or_create(name="Extra Speed")[0]
FomoriPower.objects.get_or_create(name="Eyes of the Wyrm")[0]
FomoriPower.objects.get_or_create(name="Fiery Discharge")[0]
FomoriPower.objects.get_or_create(name="Footpads")[0]
FomoriPower.objects.get_or_create(name="Frog Tongue")[0]
FomoriPower.objects.get_or_create(name="Fungal Touch")[0]
FomoriPower.objects.get_or_create(name="Fungal Udder")[0]
FomoriPower.objects.get_or_create(name="Gaseous Form")[0]
FomoriPower.objects.get_or_create(name="Gifted Fomor")[0]
FomoriPower.objects.get_or_create(name="Hazardous Breath")[0]
FomoriPower.objects.get_or_create(name="Hazardous Heave")[0]
FomoriPower.objects.get_or_create(name="Hell's Hide")[0]
FomoriPower.objects.get_or_create(name="Homogeneity")[0]
FomoriPower.objects.get_or_create(name="Immunity to the Delirium")[0]
FomoriPower.objects.get_or_create(name="Infectious Touch")[0]
FomoriPower.objects.get_or_create(name="Invisibility")[0]
FomoriPower.objects.get_or_create(name="Lashing Tail")[0]
FomoriPower.objects.get_or_create(name="Malleate")[0]
FomoriPower.objects.get_or_create(name="Maw of the Wyrm")[0]
FomoriPower.objects.get_or_create(name="Mega-Attribute")[0]
FomoriPower.objects.get_or_create(name="Mind Blast")[0]
FomoriPower.objects.get_or_create(name="Molecular Weakening")[0]
FomoriPower.objects.get_or_create(name="Numbleness")[0]
FomoriPower.objects.get_or_create(name="Noxious Breath")[0]
FomoriPower.objects.get_or_create(name="Noxious Miasma")[0]
FomoriPower.objects.get_or_create(name="Numbing")[0]
FomoriPower.objects.get_or_create(name="Phoenix Form")[0]
FomoriPower.objects.get_or_create(name="Poison Tumors")[0]
FomoriPower.objects.get_or_create(name="Rat Head")[0]
FomoriPower.objects.get_or_create(name="Regeneration")[0]
FomoriPower.objects.get_or_create(name="Roar of the Wyrm")[0]
FomoriPower.objects.get_or_create(name="Sense Gaia")[0]
FomoriPower.objects.get_or_create(name="Sense the Unnatural")[0]
FomoriPower.objects.get_or_create(name="Shadowplay")[0]
FomoriPower.objects.get_or_create(name="Size Shift")[0]
FomoriPower.objects.get_or_create(name="Skittersight")[0]
FomoriPower.objects.get_or_create(name="Slither Skin")[0]
FomoriPower.objects.get_or_create(name="Slobbersnot")[0]
FomoriPower.objects.get_or_create(name="Spirit Ties")[0]
FomoriPower.objects.get_or_create(name="Stomach Pumper")[0]
FomoriPower.objects.get_or_create(name="Tar Skin")[0]
FomoriPower.objects.get_or_create(name="Toxic Secretions")[0]
FomoriPower.objects.get_or_create(name="Triatic Sense")[0]
FomoriPower.objects.get_or_create(name="Twisted Senses")[0]
FomoriPower.objects.get_or_create(name="Umbral Passage")[0]
FomoriPower.objects.get_or_create(name="Unnatural Strength")[0]
FomoriPower.objects.get_or_create(name="Venomous Bite")[0]
FomoriPower.objects.get_or_create(name="Viscous Form")[0]
FomoriPower.objects.get_or_create(name="Voice of the Wyrm")[0]
FomoriPower.objects.get_or_create(name="Wall Walking")[0]
FomoriPower.objects.get_or_create(name="Water Breathing")[0]
FomoriPower.objects.get_or_create(name="Webbing")[0]
FomoriPower.objects.get_or_create(name="Wings")[0]
FomoriPower.objects.get_or_create(name="Wrathful Invective")[0]

ObjectType.objects.get_or_create(
    name="Caern", type="loc", system="wod", gameline="Werewolf: the Apocalypse"
)[0]
ObjectType.objects.get_or_create(
    name="Werewolf", type="char", system="wod", gameline="Werewolf: the Apocalypse"
)[0]
ObjectType.objects.get_or_create(
    name="Fomor", type="char", system="wod", gameline="Werewolf: the Apocalypse"
)[0]
ObjectType.objects.get_or_create(
    name="Kinfolk", type="char", system="wod", gameline="Werewolf: the Apocalypse"
)[0]
ObjectType.objects.get_or_create(
    name="Fetish", type="obj", system="wod", gameline="Werewolf: the Apocalypse"
)[0]
