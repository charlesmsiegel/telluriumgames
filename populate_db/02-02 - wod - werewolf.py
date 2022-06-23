from wod.models.characters.human import Archetype, MeritFlaw, Specialty
from wod.models.characters.werewolf import (
    Camp,
    Gift,
    RenownIncident,
    Rite,
    Totem,
    Tribe,
)

black_furies = Tribe.objects.create(name="Black Furies", willpower=3)
bone_gnawers = Tribe.objects.create(name="Bone Gnawers", willpower=4)
children_of_gaia = Tribe.objects.create(name="Children of Gaia", willpower=4)
fianna = Tribe.objects.create(name="Fianna", willpower=3)
get_of_fenris = Tribe.objects.create(name="Get of Fenris", willpower=3)
glass_walker = Tribe.objects.create(name="Glass Walkers", willpower=3)
red_talons = Tribe.objects.create(name="Red Talons", willpower=3)
shadow_lords = Tribe.objects.create(name="Shadow Lords", willpower=3)
silent_striders = Tribe.objects.create(name="Silent Striders", willpower=3)
silver_fangs = Tribe.objects.create(name="Silver Fangs", willpower=3)
stargazers = Tribe.objects.create(name="Stargazers", willpower=4)
uktena = Tribe.objects.create(name="Uktena", willpower=3)
wendigo = Tribe.objects.create(name="Wendigo", willpower=4)

Tribe.objects.create(name="Black Spiral Dancers", willpower=3)

Tribe.objects.create(name="Bunyip", willpower=4)
Tribe.objects.create(name="Croatan", willpower=4)
Tribe.objects.create(name="White Howlers", willpower=3)

Specialty.objects.get_or_create(name="Steely Grip", stat="strength")
Specialty.objects.get_or_create(name="Lower Body", stat="strength")
Specialty.objects.get_or_create(name="Strength Reserves", stat="strength")
Specialty.objects.get_or_create(name="Lightning Reflexes", stat="dexterity")
Specialty.objects.get_or_create(name="Preternatural Grace", stat="dexterity")
Specialty.objects.get_or_create(name="Nimble Fingers", stat="dexterity")
Specialty.objects.get_or_create(name="Unbreakable", stat="stamina")
Specialty.objects.get_or_create(name="Tireless", stat="stamina")
Specialty.objects.get_or_create(name="Resilient", stat="stamina")
Specialty.objects.get_or_create(name="Air of Confidence", stat="charisma")
Specialty.objects.get_or_create(name="Captivating Voice", stat="charisma")
Specialty.objects.get_or_create(name="Infectious Humor", stat="charisma")
Specialty.objects.get_or_create(name="Forked Tongue", stat="manipulation")
Specialty.objects.get_or_create(name="Unswerving Logic", stat="manipulation")
Specialty.objects.get_or_create(name="Doubletalk", stat="manipulation")
Specialty.objects.get_or_create(name="Seduction", stat="manipulation")
Specialty.objects.get_or_create(name="Genial", stat="appearance")
Specialty.objects.get_or_create(name="Exotic", stat="appearance")
Specialty.objects.get_or_create(name="Alluring", stat="appearance")
Specialty.objects.get_or_create(name="Noble Bearing", stat="appearance")
Specialty.objects.get_or_create(name="Eyes in the Back of Your Head", stat="perception")
Specialty.objects.get_or_create(name="Farsighted", stat="perception")
Specialty.objects.get_or_create(name="Uncanny Instincts", stat="perception")
Specialty.objects.get_or_create(name="Detail-Oriented", stat="perception")
Specialty.objects.get_or_create(name="Lateral Problem Solver", stat="intelligence")
Specialty.objects.get_or_create(name="Creative Logic", stat="intelligence")
Specialty.objects.get_or_create(name="Probability Calculation", stat="intelligence")
Specialty.objects.get_or_create(name="Trivia", stat="intelligence")
Specialty.objects.get_or_create(name="Snappy Retorts", stat="wits")
Specialty.objects.get_or_create(name="Ambushes", stat="wits")
Specialty.objects.get_or_create(name="Cool-Headed", stat="wits")
Specialty.objects.get_or_create(name="Cunning", stat="wits")
Specialty.objects.get_or_create(name="Ambushes", stat="alertness")
Specialty.objects.get_or_create(name="Eavesdropping", stat="alertness")
Specialty.objects.get_or_create(name="Paranoia", stat="alertness")
Specialty.objects.get_or_create(name="Traps", stat="alertness")
Specialty.objects.get_or_create(name="Scents", stat="alertness")
Specialty.objects.get_or_create(name="Specific sports", stat="athletics")
Specialty.objects.get_or_create(name="Team Play", stat="athletics")
Specialty.objects.get_or_create(name="Swimming", stat="athletics")
Specialty.objects.get_or_create(name="Rock Climbing", stat="athletics")
Specialty.objects.get_or_create(name="Tumbling", stat="athletics")
Specialty.objects.get_or_create(name="Distance Trials", stat="athletics")
Specialty.objects.get_or_create(name="Pentathlon", stat="athletics")
Specialty.objects.get_or_create(name="Boxing", stat="brawl")
Specialty.objects.get_or_create(name="Wrestling", stat="brawl")
Specialty.objects.get_or_create(name="Dirty Infighting", stat="brawl")
Specialty.objects.get_or_create(name="Weaponless Martial Arts", stat="brawl")
Specialty.objects.get_or_create(name="Kailindo", stat="brawl")
Specialty.objects.get_or_create(name="Sense Lies", stat="empathy")
Specialty.objects.get_or_create(name="Hidden Motives", stat="empathy")
Specialty.objects.get_or_create(name="Emotional States", stat="empathy")
Specialty.objects.get_or_create(name="Personality Quirks", stat="empathy")
Specialty.objects.get_or_create(name="Affairs of the Heart", stat="empathy")
Specialty.objects.get_or_create(name="Rhetoric", stat="expression")
Specialty.objects.get_or_create(name="Inspiriting Speeches", stat="expression")
Specialty.objects.get_or_create(name="Poetry", stat="expression")
Specialty.objects.get_or_create(name="Drama", stat="expression")
Specialty.objects.get_or_create(name="Political Doubletalk", stat="expression")
Specialty.objects.get_or_create(name="Social Media", stat="expression")
Specialty.objects.get_or_create(name="Veiled Threats", stat="intimidation")
Specialty.objects.get_or_create(name="Good Cop/Bad Cop", stat="intimidation")
Specialty.objects.get_or_create(name="Blackmail", stat="intimidation")
Specialty.objects.get_or_create(name="Phyiscal Threats", stat="intimidation")
Specialty.objects.get_or_create(name="Revenge", stat="intimidation")
Specialty.objects.get_or_create(name="Compelling", stat="leadership")
Specialty.objects.get_or_create(name="Open", stat="leadership")
Specialty.objects.get_or_create(name="Military", stat="leadership")
Specialty.objects.get_or_create(name="Motivation", stat="leadership")
Specialty.objects.get_or_create(name="Combat Readiness", stat="leadership")
Specialty.objects.get_or_create(name="Shifting Forms", stat="primal_urge")
Specialty.objects.get_or_create(name="Hunting", stat="primal_urge")
Specialty.objects.get_or_create(name="Hunches", stat="primal_urge")
Specialty.objects.get_or_create(name="Reacting", stat="primal_urge")
Specialty.objects.get_or_create(name="Fencing", stat="streetwise")
Specialty.objects.get_or_create(name="Illegal Drugs", stat="streetwise")
Specialty.objects.get_or_create(name="Illegal Guns", stat="streetwise")
Specialty.objects.get_or_create(name="Gangs", stat="streetwise")
Specialty.objects.get_or_create(name="Unsecured Wifi", stat="streetwise")
Specialty.objects.get_or_create(name="White Lies", stat="subterfuge")
Specialty.objects.get_or_create(name="Seduction", stat="subterfuge")
Specialty.objects.get_or_create(name="The Long Con", stat="subterfuge")
Specialty.objects.get_or_create(name="Feigned Innocence", stat="subterfuge")
Specialty.objects.get_or_create(name="Falconry", stat="animal_ken")
Specialty.objects.get_or_create(name="Farm Animals", stat="animal_ken")
Specialty.objects.get_or_create(name="Feral Animals", stat="animal_ken")
Specialty.objects.get_or_create(name="Attack Training", stat="animal_ken")
Specialty.objects.get_or_create(name="Horses", stat="animal_ken")
Specialty.objects.get_or_create(name="Big Cats", stat="animal_ken")
Specialty.objects.get_or_create(name="Dogs", stat="animal_ken")
Specialty.objects.get_or_create(name="Woodwork", stat="crafts")
Specialty.objects.get_or_create(name="Drawing/Painting", stat="crafts")
Specialty.objects.get_or_create(name="Weaving", stat="crafts")
Specialty.objects.get_or_create(name="Carving", stat="crafts")
Specialty.objects.get_or_create(name="Sculpture", stat="crafts")
Specialty.objects.get_or_create(name="Metalworking", stat="crafts")
Specialty.objects.get_or_create(name="Auro Repair", stat="crafts")
Specialty.objects.get_or_create(name="Off-road", stat="drive")
Specialty.objects.get_or_create(name="Motorcycles", stat="drive")
Specialty.objects.get_or_create(name="Heavy Traffic", stat="drive")
Specialty.objects.get_or_create(name="High Speed", stat="drive")
Specialty.objects.get_or_create(name="High Society", stat="etiquette")
Specialty.objects.get_or_create(name="Moots", stat="etiquette")
Specialty.objects.get_or_create(name="Tribal", stat="etiquette")
Specialty.objects.get_or_create(name="Big Business", stat="etiquette")
Specialty.objects.get_or_create(name="Rifles", stat="firearms")
Specialty.objects.get_or_create(name="Pistols", stat="firearms")
Specialty.objects.get_or_create(name="Submachine Guns", stat="firearms")
Specialty.objects.get_or_create(name="Gunsmithing", stat="firearms")
Specialty.objects.get_or_create(name="Marksmanship", stat="firearms")
Specialty.objects.get_or_create(name="Trick Shots", stat="firearms")
Specialty.objects.get_or_create(name="Pickpocketing", stat="larceny")
Specialty.objects.get_or_create(name="Misdirection", stat="larceny")
Specialty.objects.get_or_create(name="Lockpicking", stat="larceny")
Specialty.objects.get_or_create(name="Hotwiring", stat="larceny")
Specialty.objects.get_or_create(name="Safecracking", stat="larceny")
Specialty.objects.get_or_create(name="Swords", stat="melee")
Specialty.objects.get_or_create(name="Spears", stat="melee")
Specialty.objects.get_or_create(name="Improvised Weaponry", stat="melee")
Specialty.objects.get_or_create(name="Klaives", stat="melee")
Specialty.objects.get_or_create(name="Dancing", stat="performance")
Specialty.objects.get_or_create(name="Singing", stat="performance")
Specialty.objects.get_or_create(name="Acting", stat="performance")
Specialty.objects.get_or_create(name="Rock and Roll", stat="performance")
Specialty.objects.get_or_create(name="Guitar Solos", stat="performance")
Specialty.objects.get_or_create(name="Opera", stat="performance")
Specialty.objects.get_or_create(name="Howling", stat="performance")
Specialty.objects.get_or_create(name="Shadowing", stat="stealth")
Specialty.objects.get_or_create(name="Urban", stat="stealth")
Specialty.objects.get_or_create(name="Taking Point", stat="stealth")
Specialty.objects.get_or_create(name="Crowds", stat="stealth")
Specialty.objects.get_or_create(name="Hiding Objects", stat="stealth")
Specialty.objects.get_or_create(name="Foraging", stat="survival")
Specialty.objects.get_or_create(name="Tracking", stat="survival")
Specialty.objects.get_or_create(name="Specific Environments", stat="survival")
Specialty.objects.get_or_create(name="Trapping", stat="survival")
Specialty.objects.get_or_create(name="Color Theory", stat="academics")
Specialty.objects.get_or_create(name="Linguistics", stat="academics")
Specialty.objects.get_or_create(name="Poststructuralism", stat="academics")
Specialty.objects.get_or_create(name="Ethics", stat="academics")
Specialty.objects.get_or_create(name="Metaphysics", stat="academics")
Specialty.objects.get_or_create(name="Sumeria", stat="academics")
Specialty.objects.get_or_create(name="Internet Research", stat="computer")
Specialty.objects.get_or_create(name="Video Editing", stat="computer")
Specialty.objects.get_or_create(name="Photo Manipulation", stat="computer")
Specialty.objects.get_or_create(name="Programming", stat="computer")
Specialty.objects.get_or_create(name="Computer Languages", stat="computer")
Specialty.objects.get_or_create(name="Logic Problems", stat="enigmas")
Specialty.objects.get_or_create(name="Lateral Thinking", stat="enigmas")
Specialty.objects.get_or_create(name="Ancient Mysteries", stat="enigmas")
Specialty.objects.get_or_create(
    name="Things Werewolves Were Not Meant to Know", stat="enigmas"
)
Specialty.objects.get_or_create(name="Evidence", stat="investigation")
Specialty.objects.get_or_create(name="Ballistics", stat="investigation")
Specialty.objects.get_or_create(name="Forensics", stat="investigation")
Specialty.objects.get_or_create(name="Fingerprints", stat="investigation")
Specialty.objects.get_or_create(name="Searches", stat="investigation")
Specialty.objects.get_or_create(name="Internet Research", stat="investigation")
Specialty.objects.get_or_create(name="Fitting Punishments", stat="law")
Specialty.objects.get_or_create(name="Litany Breaches", stat="law")
Specialty.objects.get_or_create(name="Human Field", stat="law")
Specialty.objects.get_or_create(name="Emergency Medicine", stat="medicine")
Specialty.objects.get_or_create(name="Forensic Pathology", stat="medicine")
Specialty.objects.get_or_create(name="Neurology", stat="medicine")
Specialty.objects.get_or_create(name="Pharmacology", stat="medicine")
Specialty.objects.get_or_create(name="Poison Treatments", stat="medicine")
Specialty.objects.get_or_create(name="Garou Physiology", stat="medicine")
Specialty.objects.get_or_create(name="Tarot", stat="occult")
Specialty.objects.get_or_create(name="Witchcraft", stat="occult")
Specialty.objects.get_or_create(name="Curses", stat="occult")
Specialty.objects.get_or_create(name="Ghosts", stat="occult")
Specialty.objects.get_or_create(name="Psychometry", stat="occult")
Specialty.objects.get_or_create(name="Garou Lore", stat="occult")
Specialty.objects.get_or_create(name="Accord", stat="rituals")
Specialty.objects.get_or_create(name="Caern", stat="rituals")
Specialty.objects.get_or_create(name="Death", stat="rituals")
Specialty.objects.get_or_create(name="Mystic", stat="rituals")
Specialty.objects.get_or_create(name="Punishment", stat="rituals")
Specialty.objects.get_or_create(name="Renown", stat="rituals")
Specialty.objects.get_or_create(name="Seasonal", stat="rituals")
Specialty.objects.get_or_create(name="Minor", stat="rituals")
Specialty.objects.get_or_create(name="Experiments", stat="science")
Specialty.objects.get_or_create(name="Theory", stat="science")
Specialty.objects.get_or_create(name="Chemistry", stat="science")
Specialty.objects.get_or_create(name="Physics", stat="science")
Specialty.objects.get_or_create(name="Biology", stat="science")
Specialty.objects.get_or_create(name="Mathematics", stat="science")
Specialty.objects.get_or_create(name="Astronomy", stat="science")
Specialty.objects.get_or_create(name="Telecoms", stat="technology")
Specialty.objects.get_or_create(name="Computers", stat="technology")
Specialty.objects.get_or_create(name="Security", stat="technology")
Specialty.objects.get_or_create(name="Communications", stat="technology")
Specialty.objects.get_or_create(name="Jury-Rigging", stat="technology")
Specialty.objects.get_or_create(name="Industrial Espionage", stat="technology")

Gift.objects.create(name="Aprecraft's Blessings", rank=1, allowed={"garou": ["homid"]})
Gift.objects.create(name="City Running", rank=1, allowed={"garou": ["homid"]})
Gift.objects.create(
    name="Master of Fire",
    rank=1,
    allowed={"garou": ["homid", "Get of Fenris", "Croatan"]},
)
Gift.objects.create(
    name="Persuasion",
    rank=1,
    allowed={"garou": ["homid", "philodox", "Fianna", "Glasswalkers"]},
)
Gift.objects.create(name="Smell of Man", rank=1, allowed={"garou": ["homid"]})
Gift.objects.create(
    name="Jam Technology", rank=2, allowed={"garou": ["homid", "Glasswalkers"]}
)
Gift.objects.create(name="Mark of the Wolf", rank=2, allowed={"garou": ["homid"]})
Gift.objects.create(
    name="Speech of the World", rank=2, allowed={"garou": ["homid", "Silent Striders"]}
)
Gift.objects.create(name="Staredown", rank=2, allowed={"garou": ["homid"]})
Gift.objects.create(
    name="Calm the Savage Beast",
    rank=3,
    allowed={"garou": ["homid", "Children of Gaia"]},
)
Gift.objects.create(name="Cowing the Bullet", rank=3, allowed={"garou": ["homid"]})
Gift.objects.create(name="Disquiet", rank=3, allowed={"garou": ["homid"]})
Gift.objects.create(
    name="Reshape Object",
    rank=3,
    allowed={"garou": ["homid", "Bone Gnawers", "Fianna"]},
)
Gift.objects.create(
    name="Body Shift", rank=4, allowed={"garou": ["homid", "ahroun", "Get of Fenris"]}
)
Gift.objects.create(name="Bury the Wolf", rank=4, allowed={"garou": ["homid"]})
Gift.objects.create(name="Cocoon", rank=4, allowed={"garou": ["homid"]})
Gift.objects.create(name="Spirit Ward", rank=4, allowed={"garou": ["homid", "theurge"]})
Gift.objects.create(name="Assimilation", rank=5, allowed={"garou": ["homid"]})
Gift.objects.create(name="Beyond Human", rank=5, allowed={"garou": ["homid"]})
Gift.objects.create(name="Part the Veil", rank=5, allowed={"garou": ["homid"]})
Gift.objects.create(name="Create Element", rank=1, allowed={"garou": ["metis"]})
Gift.objects.create(
    name="Primal Anger", rank=1, allowed={"garou": ["metis", "White Howler"]}
)
Gift.objects.create(name="Rat Head", rank=1, allowed={"garou": ["metis"]})
Gift.objects.create(
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
            "White Howler",
        ]
    },
)
Gift.objects.create(name="Shed", rank=1, allowed={"garou": ["metis"]})
Gift.objects.create(name="Burrow", rank=2, allowed={"garou": ["metis"]})
Gift.objects.create(name="Curse of Hatred", rank=2, allowed={"garou": ["metis"]})
Gift.objects.create(
    name="Form Mastery", rank=2, allowed={"garou": ["metis", "Black Furies", "Fianna"]}
)
Gift.objects.create(
    name="Sense Silver", rank=2, allowed={"garou": ["metis", "ahroun", "Silver Fangs"]}
)
Gift.objects.create(name="Chameleon", rank=2, allowed={"garou": ["metis"]})
Gift.objects.create(name="Eyes of the Cat", rank=3, allowed={"garou": ["metis"]})
Gift.objects.create(
    name="Mental Speech", rank=3, allowed={"garou": ["metis", "philodox"]}
)
Gift.objects.create(name="Shell", rank=3, allowed={"garou": ["metis", "Croatan"]})
Gift.objects.create(name="Gift of the Porcupine", rank=4, allowed={"garou": ["metis"]})
Gift.objects.create(name="Lash of Rage", rank=4, allowed={"garou": ["metis"]})
Gift.objects.create(name="Rattler's Bite", rank=4, allowed={"garou": ["metis"]})
Gift.objects.create(name="Wither Limb", rank=4, allowed={"garou": ["metis"]})
Gift.objects.create(name="Madness", rank=5, allowed={"garou": ["metis"]})
Gift.objects.create(name="Protean Form", rank=5, allowed={"garou": ["metis"]})
Gift.objects.create(name="Totem Gift", rank=5, allowed={"garou": ["metis"]})
Gift.objects.create(name="Hare's Leap", rank=1, allowed={"garou": ["lupus", "Fianna"]})
Gift.objects.create(
    name="Heightened Senses",
    rank=1,
    allowed={"garou": ["lupus", "galliard", "Black Furies"]},
)
Gift.objects.create(name="Sense Prey", rank=1, allowed={"garou": ["lupus", "Bunyip"]})
Gift.objects.create(name="Predator's Arsenal", rank=1, allowed={"garou": ["lupus"]})
Gift.objects.create(name="Prey Mind", rank=1, allowed={"garou": ["lupus"]})
Gift.objects.create(
    name="Axis Mundi", rank=2, allowed={"garou": ["lupus", "Silent Striders"]}
)
Gift.objects.create(name="Eye of the Eagle", rank=2, allowed={"garou": ["lupus"]})
Gift.objects.create(
    name="Name the Spirit", rank=2, allowed={"garou": ["lupus", "theurge"]}
)
Gift.objects.create(name="Scent of Sight", rank=2, allowed={"garou": ["lupus"]})
Gift.objects.create(name="Catfeet", rank=3, allowed={"garou": ["lupus"]})
Gift.objects.create(
    name="Monkey Tail", rank=3, allowed={"garou": ["lupus", "ragabash"]}
)
Gift.objects.create(
    name="Sense the Unnatural", rank=3, allowed={"garou": ["lupus", "Silent Striders"]}
)
Gift.objects.create(name="Silence the Weaver", rank=3, allowed={"garou": ["lupus"]})
Gift.objects.create(name="Strength of Gaia", rank=3, allowed={"garou": ["lupus"]})
Gift.objects.create(
    name="Beast Life",
    rank=4,
    allowed={"garou": ["lupus", "Black Furies", "Children of Gaia"]},
)
Gift.objects.create(name="Gnaw", rank=4, allowed={"garou": ["lupus"]})
Gift.objects.create(
    name="Scream of Gaia", rank=4, allowed={"garou": ["lupus", "Get of Fenris"]}
)
Gift.objects.create(
    name="Terror of the Dire Wolf", rank=4, allowed={"garou": ["lupus"]}
)
Gift.objects.create(name="Elemental Gift", rank=5, allowed={"garou": ["lupus"]})
Gift.objects.create(
    name="Song of the Great Beast", rank=5, allowed={"garou": ["lupus"]}
)
Gift.objects.create(
    name="Blur of the Milky Eye", rank=1, allowed={"garou": ["ragabash"]}
)
Gift.objects.create(name="Infectious Laughter", rank=1, allowed={"garou": ["ragabash"]})
Gift.objects.create(name="Liar's Face", rank=1, allowed={"garou": ["ragabash"]})
Gift.objects.create(name="Open Seal", rank=1, allowed={"garou": ["ragabash"]})
Gift.objects.create(
    name="Scent of Running Water", rank=1, allowed={"garou": ["ragabash", "Red Talons"]}
)
Gift.objects.create(
    name="Blissful Ignorance",
    rank=2,
    allowed={"garou": ["ragabash", "Bone Gnawers", "Silent Striders"]},
)
Gift.objects.create(
    name="Pulse of the Prey",
    rank=2,
    allowed={"garou": ["ragabash", "Black Furies", "Red Talons"]},
)
Gift.objects.create(name="Spider's Song", rank=2, allowed={"garou": ["ragabash"]})
Gift.objects.create(
    name="Taking the Forgotten", rank=2, allowed={"garou": ["ragabash"]}
)
Gift.objects.create(name="Gremlins", rank=3, allowed={"garou": ["ragabash"]})
Gift.objects.create(name="Liar's Craft", rank=3, allowed={"garou": ["ragabash"]})
Gift.objects.create(name="Open Moon Bridge", rank=3, allowed={"garou": ["ragabash"]})
Gift.objects.create(name="Pathfinder", rank=3, allowed={"garou": ["ragabash"]})
Gift.objects.create(name="Luna's Blessing", rank=4, allowed={"garou": ["ragabash"]})
Gift.objects.create(name="Umbral Dodge", rank=4, allowed={"garou": ["ragabash"]})
Gift.objects.create(name="Whelp Body", rank=4, allowed={"garou": ["ragabash"]})
Gift.objects.create(
    name="Thieving Talons of the Magpie", rank=5, allowed={"garou": ["ragabash"]}
)
Gift.objects.create(
    name="Thousand Forms", rank=5, allowed={"garou": ["ragabash", "Black Furies"]}
)
Gift.objects.create(name="Firebringer", rank=6, allowed={"garou": ["ragabash"]})
Gift.objects.create(
    name="Mother's Touch",
    rank=1,
    allowed={"garou": ["theurge", "Children of Gaia", "Bunyip"]},
)
Gift.objects.create(name="Spirit Snare", rank=1, allowed={"garou": ["theurge"]})
Gift.objects.create(
    name="Spirit Speech", rank=1, allowed={"garou": ["theurge", "Uktena"]}
)
Gift.objects.create(name="Umbral Tether", rank=1, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Battle Mandala", rank=2, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Command Spirit", rank=2, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Sight From Beyond", rank=2, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Exorcism", rank=3, allowed={"garou": ["theurge"]})
Gift.objects.create(
    name="Pulse of the Invisible", rank=3, allowed={"garou": ["theurge", "Bunyip"]}
)
Gift.objects.create(name="Umbral Camouflage", rank=3, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Web Walker", rank=3, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Blurring the Mirror", rank=4, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Grasp of Beyond", rank=4, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Spirit Drain", rank=4, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Feral Lobotomy", rank=5, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Malleable Spirit", rank=5, allowed={"garou": ["theurge"]})
Gift.objects.create(
    name="Ultimate Argument of Logic", rank=5, allowed={"garou": ["theurge"]}
)
Gift.objects.create(name="As in the Beginning", rank=6, allowed={"garou": ["theurge"]})
Gift.objects.create(name="Fangs of Judgment", rank=1, allowed={"garou": ["philodox"]})
Gift.objects.create(
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
)
Gift.objects.create(
    name="Scent of the True Form", rank=1, allowed={"garou": ["philodox"]}
)
Gift.objects.create(name="Truth of Gaia", rank=1, allowed={"garou": ["philodox"]})
Gift.objects.create(name="Call to Duty", rank=2, allowed={"garou": ["philodox"]})
Gift.objects.create(
    name="Command the Gathering", rank=2, allowed={"garou": ["philodox", "galliard"]}
)
Gift.objects.create(name="King of the Beasts", rank=2, allowed={"garou": ["philodox"]})
Gift.objects.create(
    name="Strength of Purpose", rank=2, allowed={"garou": ["philodox", "Croatan"]}
)
Gift.objects.create(
    name="Scent of the Oathbreaker", rank=3, allowed={"garou": ["philodox"]}
)
Gift.objects.create(
    name="Sense Balance", rank=3, allowed={"garou": ["philodox", "Stargazers"]}
)
Gift.objects.create(name="Weak Arm", rank=3, allowed={"garou": ["philodox"]})
Gift.objects.create(
    name="Wisdom of the Ancient Ways",
    rank=3,
    allowed={"garou": ["philodox", "Wendigo"]},
)
Gift.objects.create(name="Roll Over", rank=4, allowed={"garou": ["philodox"]})
Gift.objects.create(name="Scent of Beyond", rank=4, allowed={"garou": ["philodox"]})
Gift.objects.create(name="Take the True Form", rank=4, allowed={"garou": ["philodox"]})
Gift.objects.create(name="Geas", rank=5, allowed={"garou": ["philodox"]})
Gift.objects.create(name="Wall of Granite", rank=5, allowed={"garou": ["philodox"]})
Gift.objects.create(
    name="Break the Bonds", rank=6, allowed={"garou": ["philodox", "galliard"]}
)
Gift.objects.create(
    name="Beast Speech", rank=1, allowed={"garou": ["galliard", "Red Talons"]}
)
Gift.objects.create(name="Call of the Wyld", rank=1, allowed={"garou": ["galliard"]})
Gift.objects.create(
    name="Mindspeak", rank=1, allowed={"garou": ["galliard", "Croatan"]}
)
Gift.objects.create(name="Perfect Recall", rank=1, allowed={"garou": ["galliard"]})
Gift.objects.create(name="Call of the Wyrm", rank=2, allowed={"garou": ["galliard"]})
Gift.objects.create(name="Distractions", rank=2, allowed={"garou": ["galliard"]})
Gift.objects.create(name="Dreamspeak", rank=2, allowed={"garou": ["galliard"]})
Gift.objects.create(
    name="Howls in the Night",
    rank=2,
    allowed={"garou": ["galliard", "Red Talons", "Shadow Lords", "White Howler"]},
)
Gift.objects.create(name="Eye of the Cobra", rank=3, allowed={"garou": ["galliard"]})
Gift.objects.create(name="Song of Heroes", rank=3, allowed={"garou": ["galliard"]})
Gift.objects.create(name="Song of Rage", rank=3, allowed={"garou": ["galliard"]})
Gift.objects.create(
    name="Song of the Siren", rank=3, allowed={"garou": ["galliard", "Fianna"]}
)
Gift.objects.create(name="Bridge Walker", rank=4, allowed={"garou": ["galliard"]})
Gift.objects.create(name="Gift of Dreams", rank=4, allowed={"garou": ["galliard"]})
Gift.objects.create(
    name="Shadows by the Firelight", rank=4, allowed={"garou": ["galliard"]}
)
Gift.objects.create(
    name="Fabric of the Mind", rank=4, allowed={"garou": ["galliard", "Uktena"]}
)
Gift.objects.create(name="Head Games", rank=5, allowed={"garou": ["galliard"]})
Gift.objects.create(
    name="Falling Touch", rank=1, allowed={"garou": ["ahroun", "Stargazers"]}
)
Gift.objects.create(
    name="Inspiration", rank=1, allowed={"garou": ["ahroun", "Silver Fangs"]}
)
Gift.objects.create(name="Pack Tactics", rank=1, allowed={"garou": ["ahroun"]})
Gift.objects.create(
    name="Razor Claws", rank=1, allowed={"garou": ["ahroun", "Get of Fenris"]}
)
Gift.objects.create(name="Spur Claws", rank=1, allowed={"garou": ["ahroun"]})
Gift.objects.create(name="Shield of Rage", rank=2, allowed={"garou": ["ahroun"]})
Gift.objects.create(name="Spirit of the Fray", rank=2, allowed={"garou": ["ahroun"]})
Gift.objects.create(name="True Fear", rank=2, allowed={"garou": ["ahroun", "Wendigo"]})
Gift.objects.create(name="Combat Healing", rank=3, allowed={"garou": ["ahroun"]})
Gift.objects.create(name="Heart of Fury", rank=3, allowed={"garou": ["ahroun"]})
Gift.objects.create(
    name="Silver Claws", rank=3, allowed={"garou": ["ahroun", "Silver Fangs"]}
)
Gift.objects.create(name="Wind Claws", rank=3, allowed={"garou": ["ahroun"]})
Gift.objects.create(
    name="Clenched Jaw", rank=4, allowed={"garou": ["ahroun", "Kucha Ekundu"]}
)
Gift.objects.create(name="Full Moon's Light", rank=4, allowed={"garou": ["ahroun"]})
Gift.objects.create(
    name="Stoking Fury's Furnace", rank=4, allowed={"garou": ["ahroun"]}
)
Gift.objects.create(name="Kiss of Helios", rank=5, allowed={"garou": ["ahroun"]})
Gift.objects.create(name="Strength of Will", rank=5, allowed={"garou": ["ahroun"]})
Gift.objects.create(name="Unstoppable Warrior", rank=6, allowed={"garou": ["ahroun"]})
Gift.objects.create(
    name="Breath of the Wyld", rank=1, allowed={"garou": ["Black Furies"]}
)
Gift.objects.create(name="Man's Skin", rank=1, allowed={"garou": ["Black Furies"]})
Gift.objects.create(
    name="Wyld Resurgence", rank=1, allowed={"garou": ["Black Furies", "Croatan"]}
)
Gift.objects.create(name="Curse of Aeolus", rank=2, allowed={"garou": ["Black Furies"]})
Gift.objects.create(name="Kali's Tongue", rank=2, allowed={"garou": ["Black Furies"]})
Gift.objects.create(name="Kneel", rank=2, allowed={"garou": ["Black Furies"]})
Gift.objects.create(name="Coup de Grace", rank=3, allowed={"garou": ["Black Furies"]})
Gift.objects.create(name="Heart Claw", rank=3, allowed={"garou": ["Black Furies"]})
Gift.objects.create(name="Visceral Agony", rank=3, allowed={"garou": ["Black Furies"]})
Gift.objects.create(
    name="Wings of PEgasus", rank=3, allowed={"garou": ["Black Furies"]}
)
Gift.objects.create(name="Body Wrack", rank=4, allowed={"garou": ["Black Furies"]})
Gift.objects.create(name="Wasp Talons", rank=4, allowed={"garou": ["Black Furies"]})
Gift.objects.create(name="Gorgon's Gaze", rank=5, allowed={"garou": ["Black Furies"]})
Gift.objects.create(name="Wyld Warp", rank=5, allowed={"garou": ["Black Furies"]})
Gift.objects.create(name="Cooking", rank=1, allowed={"garou": ["Bone Gnawers"]})
Gift.objects.create(
    name="Desperate Strength",
    rank=1,
    allowed={"garou": ["Bone Gnawers", "White Howler"]},
)
Gift.objects.create(
    name="Resist Toxin",
    rank=1,
    allowed={"garou": ["Bone Gnawers", "Fianna", "Black Spiral Dancers", "Bunyip"]},
)
Gift.objects.create(
    name="Scent of Sweet Honey", rank=1, allowed={"garou": ["Bone Gnawers"]}
)
Gift.objects.create(
    name="Trash is Treasure", rank=1, allowed={"garou": ["Bone Gnawers"]}
)
Gift.objects.create(
    name="Between the Cracks", rank=2, allowed={"garou": ["Bone Gnawers"]}
)
Gift.objects.create(
    name="Cornered Rat's Ferocity", rank=2, allowed={"garou": ["Bone Gnawers"]}
)
Gift.objects.create(
    name="Guide of the Hound", rank=2, allowed={"garou": ["Bone Gnawers"]}
)
Gift.objects.create(name="Odious Aroma", rank=2, allowed={"garou": ["Bone Gnawers"]})
Gift.objects.create(name="Call the Rust", rank=3, allowed={"garou": ["Bone Gnawers"]})
Gift.objects.create(
    name="Gift of the Skunk", rank=3, allowed={"garou": ["Bone Gnawers"]}
)
Gift.objects.create(
    name="Gift of the Termite", rank=3, allowed={"garou": ["Bone Gnawers"]}
)
Gift.objects.create(
    name="Laugh of the Hyena", rank=3, allowed={"garou": ["Bone Gnawers"]}
)
Gift.objects.create(
    name="Attunement",
    rank=4,
    allowed={"garou": ["Bone Gnawers", "Glasswalkers", "Silent Striders"]},
)
Gift.objects.create(name="Blink", rank=4, allowed={"garou": ["Bone Gnawers"]})
Gift.objects.create(name="Infest", rank=4, allowed={"garou": ["Bone Gnawers"]})
Gift.objects.create(name="Riot", rank=5, allowed={"garou": ["Bone Gnawers"]})
Gift.objects.create(
    name="Survivor", rank=5, allowed={"garou": ["Bone Gnawers", "Croatan"]}
)
Gift.objects.create(
    name="Brother's Scent", rank=1, allowed={"garou": ["Children of Gaia"]}
)
Gift.objects.create(name="Jam Weapon", rank=1, allowed={"garou": ["Children of Gaia"]})
Gift.objects.create(name="Mercy", rank=1, allowed={"garou": ["Children of Gaia"]})
Gift.objects.create(name="Calm", rank=2, allowed={"garou": ["Children of Gaia"]})
Gift.objects.create(
    name="Grandmother's Touch", rank=2, allowed={"garou": ["Children of Gaia"]}
)
Gift.objects.create(
    name="Luna's Armor",
    rank=2,
    allowed={"garou": ["Children of Gaia", "Shadow Lords", "Silver Fangs"]},
)
Gift.objects.create(name="Para Bellum", rank=2, allowed={"garou": ["Children of Gaia"]})
Gift.objects.create(
    name="Unicorn's Arsenal", rank=2, allowed={"garou": ["Children of Gaia"]}
)
Gift.objects.create(name="Dazzle", rank=3, allowed={"garou": ["Children of Gaia"]})
Gift.objects.create(
    name="Lover's Touch", rank=3, allowed={"garou": ["Children of Gaia"]}
)
Gift.objects.create(
    name="Spirit Friend", rank=3, allowed={"garou": ["Children of Gaia"]}
)
Gift.objects.create(name="Serenity", rank=4, allowed={"garou": ["Children of Gaia"]})
Gift.objects.create(
    name="Strike the Air", rank=4, allowed={"garou": ["Children of Gaia", "Stargazers"]}
)
Gift.objects.create(
    name="Uncought Since the Primal Morn",
    rank=4,
    allowed={"garou": ["Children of Gaia"]},
)
Gift.objects.create(
    name="Halo of the Sun", rank=5, allowed={"garou": ["Children of Gaia"]}
)
Gift.objects.create(
    name="The Living Wood", rank=5, allowed={"garou": ["Children of Gaia"]}
)
Gift.objects.create(name="Faerie Light", rank=1, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Two Tongues", rank=1, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Glib Tongue", rank=2, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Flame Dance", rank=2, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Howl of the Banshee", rank=2, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Howl of the Unseen", rank=2, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Faerie Kin", rank=3, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Fair Fortune", rank=3, allowed={"garou": ["Fianna"]})
Gift.objects.create(
    name="Ley Lines", rank=3, allowed={"garou": ["Fianna", "White Howler"]}
)
Gift.objects.create(name="Balor's Gaze", rank=4, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Phantasm", rank=4, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Call the Hunt", rank=5, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Fog on the Moor", rank=5, allowed={"garou": ["Fianna"]})
Gift.objects.create(name="Gift of the Spriggan", rank=5, allowed={"garou": ["Fianna"]})
Gift.objects.create(
    name="Lightning Reflexes", rank=1, allowed={"garou": ["Get of Fenris"]}
)
Gift.objects.create(
    name="Visage of Fenris", rank=1, allowed={"garou": ["Get of Fenris"]}
)
Gift.objects.create(
    name="Fangs of the North", rank=2, allowed={"garou": ["Get of Fenris"]}
)
Gift.objects.create(
    name="Halt the Coward's Flight", rank=2, allowed={"garou": ["Get of Fenris"]}
)
Gift.objects.create(
    name="Snarl of the Predator", rank=2, allowed={"garou": ["Get of Fenris"]}
)
Gift.objects.create(name="Troll Skin", rank=2, allowed={"garou": ["Get of Fenris"]})
Gift.objects.create(name="Might of Thor", rank=3, allowed={"garou": ["Get of Fenris"]})
Gift.objects.create(name="Redirect Pain", rank=3, allowed={"garou": ["Get of Fenris"]})
Gift.objects.create(name="Venom Blood", rank=3, allowed={"garou": ["Get of Fenris"]})
Gift.objects.create(
    name="Heart of the Mountain", rank=4, allowed={"garou": ["Get of Fenris"]}
)
Gift.objects.create(
    name="Hero's Stand", rank=4, allowed={"garou": ["Get of Fenris", "White Howler"]}
)
Gift.objects.create(
    name="Endurance of Heimdall", rank=5, allowed={"garou": ["Get of Fenris"]}
)
Gift.objects.create(
    name="Horde of Valhalla", rank=5, allowed={"garou": ["Get of Fenris"]}
)
Gift.objects.create(name="Fenris' Bite", rank=5, allowed={"garou": ["Get of Fenris"]})
Gift.objects.create(
    name="Call Great Fenris", rank=6, allowed={"garou": ["Get of Fenris"]}
)
Gift.objects.create(
    name="Control Simple Machine", rank=1, allowed={"garou": ["Glass Walkers"]}
)
Gift.objects.create(name="Diagnostics", rank=1, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(name="Plug and Play", rank=1, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(name="Trick Shot", rank=1, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(name="Cybersenses", rank=2, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(
    name="Hands Full of Thunder", rank=2, allowed={"garou": ["Glass Walkers"]}
)
Gift.objects.create(name="Power Surge", rank=2, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(name="Steel Fur", rank=2, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(
    name="Control Complex Machine", rank=3, allowed={"garou": ["Glass Walkers"]}
)
Gift.objects.create(name="Intrusion", rank=3, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(name="Electroshock", rank=3, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(
    name="Elemental Favor", rank=3, allowed={"garou": ["Glass Walkers", "Red Talons"]}
)
Gift.objects.create(name="Doppelganger", rank=4, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(name="Signal Rider", rank=4, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(name="Tech Speak", rank=4, allowed={"garou": ["Glass Walkers"]})
Gift.objects.create(
    name="Chaos Mechanics", rank=5, allowed={"garou": ["Glass Walkers"]}
)
Gift.objects.create(
    name="Summon Net-Spider", rank=5, allowed={"garou": ["Glass Walkers"]}
)
Gift.objects.create(name="Eye of the Hunter", rank=1, allowed={"garou": ["Red Talons"]})
Gift.objects.create(name="Hidden Killer", rank=1, allowed={"garou": ["Red Talons"]})
Gift.objects.create(name="Wolf at the Door", rank=1, allowed={"garou": ["Red Talons"]})
Gift.objects.create(name="Beastmind", rank=2, allowed={"garou": ["Red Talons"]})
Gift.objects.create(
    name="Shadows of the Impergium", rank=2, allowed={"garou": ["Red Talons"]}
)
Gift.objects.create(name="Render Down", rank=3, allowed={"garou": ["Red Talons"]})
Gift.objects.create(name="Territory", rank=3, allowed={"garou": ["Red Talons"]})
Gift.objects.create(name="Trackless Waste", rank=3, allowed={"garou": ["Red Talons"]})
Gift.objects.create(name="Gorge", rank=4, allowed={"garou": ["Red Talons"]})
Gift.objects.create(name="Howl of Death", rank=4, allowed={"garou": ["Red Talons"]})
Gift.objects.create(
    name="Quicksand", rank=4, allowed={"garou": ["Red Talons", "Bunyip"]}
)
Gift.objects.create(name="Curse of Lycaon", rank=5, allowed={"garou": ["Red Talons"]})
Gift.objects.create(
    name="Gaia's Vengeance", rank=5, allowed={"garou": ["Red Talons", "White Howler"]}
)
Gift.objects.create(name="Scabwalker Curse", rank=5, allowed={"garou": ["Red Talons"]})
Gift.objects.create(name="Shield of Giaa", rank=6, allowed={"garou": ["Red Talons"]})
Gift.objects.create(
    name="Aura of Confidence", rank=1, allowed={"garou": ["Shadow Lords"]}
)
Gift.objects.create(name="Fatal Flaw", rank=1, allowed={"garou": ["Shadow Lords"]})
Gift.objects.create(
    name="Seizing the Edge", rank=1, allowed={"garou": ["Shadow Lords"]}
)
Gift.objects.create(name="Shadow Weaving", rank=1, allowed={"garou": ["Shadow Lords"]})
Gift.objects.create(
    name="Whisper Catching", rank=1, allowed={"garou": ["Shadow Lords"]}
)
Gift.objects.create(name="Clap of Thunder", rank=2, allowed={"garou": ["Shadow Lords"]})
Gift.objects.create(
    name="Cold Voice of Reason", rank=2, allowed={"garou": ["Shadow Lords"]}
)
Gift.objects.create(
    name="Song of the Earth Mother", rank=2, allowed={"garou": ["Shadow Lords"]}
)
Gift.objects.create(
    name="Direct the Storm", rank=3, allowed={"garou": ["Shadow Lords"]}
)
Gift.objects.create(
    name="Icy Chill of Despair", rank=3, allowed={"garou": ["Shadow Lords"]}
)
Gift.objects.create(
    name="Paralyzing Stare", rank=3, allowed={"garou": ["Shadow Lords"]}
)
Gift.objects.create(name="Shadow Cutting", rank=3, allowed={"garou": ["Shadow Lords"]})
Gift.objects.create(name="Under the Gun", rank=3, allowed={"garou": ["Shadow Lords"]})
Gift.objects.create(
    name="Open Wounds",
    rank=4,
    allowed={"garou": ["Shadow Lords", "Black Spiral Dancers"]},
)
Gift.objects.create(
    name="Durance", rank=4, allowed={"garou": ["Shadow Lords", "Uktena"]}
)
Gift.objects.create(
    name="Strength of the Dominator", rank=4, allowed={"garou": ["Shadow Lords"]}
)
Gift.objects.create(name="Obedience", rank=5, allowed={"garou": ["Shadow Lords"]})
Gift.objects.create(name="Shadow Pack", rank=5, allowed={"garou": ["Shadow Lords"]})
Gift.objects.create(
    name="Heaven's Guidance", rank=1, allowed={"garou": ["Silent Striders"]}
)
Gift.objects.create(name="Silence", rank=1, allowed={"garou": ["Silent Striders"]})
Gift.objects.create(
    name="Speed of Thought",
    rank=1,
    allowed={"garou": ["Silent Striders", "Kucha Ekundu"]},
)
Gift.objects.create(
    name="Visions of Duat", rank=1, allowed={"garou": ["Silent Striders"]}
)
Gift.objects.create(
    name="Messenger's Fortitude", rank=2, allowed={"garou": ["Silent Striders"]}
)
Gift.objects.create(
    name="Tread Sebek's Back", rank=2, allowed={"garou": ["Silent Striders"]}
)
Gift.objects.create(name="Adaptation", rank=3, allowed={"garou": ["Silent Striders"]})
Gift.objects.create(name="Great Leap", rank=3, allowed={"garou": ["Silent Striders"]})
Gift.objects.create(
    name="Mark of the Death-Wolf", rank=3, allowed={"garou": ["Silent Striders"]}
)
Gift.objects.create(name="Black Mark", rank=4, allowed={"garou": ["Silent Striders"]})
Gift.objects.create(
    name="Dam the Heartflood", rank=4, allowed={"garou": ["Silent Striders"]}
)
Gift.objects.create(
    name="Speed Beyond Thought", rank=4, allowed={"garou": ["Silent Striders"]}
)
Gift.objects.create(
    name="Gate of the Moon", rank=5, allowed={"garou": ["Silent Striders"]}
)
Gift.objects.create(
    name="Reach the Umbra", rank=5, allowed={"garou": ["Silent Striders"]}
)
Gift.objects.create(
    name="Eye of the Falcon", rank=1, allowed={"garou": ["Silver Fangs"]}
)
Gift.objects.create(name="Falcon's Grasp", rank=1, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(name="Lambent Flame", rank=1, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(name="Empathy", rank=2, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(name="Hand Blade", rank=2, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(
    name="Unity of the Pack", rank=2, allowed={"garou": ["Silver Fangs"]}
)
Gift.objects.create(name="Burning Blade", rank=3, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(
    name="Talons of the Falcon", rank=3, allowed={"garou": ["Silver Fangs"]}
)
Gift.objects.create(name="Wrath of Gaia", rank=3, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(name="Mastery", rank=4, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(
    name="Mindblock", rank=4, allowed={"garou": ["Silver Fangs", "Stargazers"]}
)
Gift.objects.create(name="Sidestep Death", rank=4, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(name="Luna's Avenger", rank=5, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(
    name="Paws of the Newborn Cub", rank=5, allowed={"garou": ["Silver Fangs"]}
)
Gift.objects.create(name="Renew the Cycle", rank=6, allowed={"garou": ["Silver Fangs"]})
Gift.objects.create(name="Balance", rank=1, allowed={"garou": ["Stargazers"]})
Gift.objects.create(name="Channeling", rank=1, allowed={"garou": ["Stargazers"]})
Gift.objects.create(name="Iron Resolve", rank=1, allowed={"garou": ["Stargazers"]})
Gift.objects.create(name="Inner Light", rank=2, allowed={"garou": ["Stargazers"]})
Gift.objects.create(name="Inner Strength", rank=2, allowed={"garou": ["Stargazers"]})
Gift.objects.create(name="Resist Temptation", rank=2, allowed={"garou": ["Stargazers"]})
Gift.objects.create(
    name="Surface Attunement", rank=2, allowed={"garou": ["Stargazers"]}
)
Gift.objects.create(name="Wuxing", rank=2, allowed={"garou": ["Stargazers"]})
Gift.objects.create(name="Clarity", rank=3, allowed={"garou": ["Stargazers"]})
Gift.objects.create(name="Mericful Blow", rank=3, allowed={"garou": ["Stargazers"]})
Gift.objects.create(
    name="Wind's Returning Favor", rank=3, allowed={"garou": ["Stargazers"]}
)
Gift.objects.create(
    name="Preternatural Awareness", rank=4, allowed={"garou": ["Stargazers"]}
)
Gift.objects.create(name="Circular Attack", rank=5, allowed={"garou": ["Stargazers"]})
Gift.objects.create(
    name="Harmorious Unity of the Emeral Mother",
    rank=5,
    allowed={"garou": ["Stargazers"]},
)
Gift.objects.create(
    name="Wisdom of the Seer", rank=5, allowed={"garou": ["Stargazers"]}
)
Gift.objects.create(name="Sense Magic", rank=1, allowed={"garou": ["Uktena"]})
Gift.objects.create(
    name="Shroud", rank=1, allowed={"garou": ["Uktena", "Black Spiral Dancers"]}
)
Gift.objects.create(name="Spirit of the Lizard", rank=1, allowed={"garou": ["Uktena"]})
Gift.objects.create(
    name="Coils of the Serpent", rank=2, allowed={"garou": ["Uktena", "Bunyip"]}
)
Gift.objects.create(name="Fetish Fetch", rank=2, allowed={"garou": ["Uktena"]})
Gift.objects.create(name="Shadows at Dawn", rank=2, allowed={"garou": ["Uktena"]})
Gift.objects.create(name="Spirit of the Bird", rank=2, allowed={"garou": ["Uktena"]})
Gift.objects.create(name="Spirit of the Fish", rank=2, allowed={"garou": ["Uktena"]})
Gift.objects.create(name="Banish Totem", rank=3, allowed={"garou": ["Uktena"]})
Gift.objects.create(name="Chains of Mist", rank=3, allowed={"garou": ["Uktena"]})
Gift.objects.create(name="Invisibility", rank=3, allowed={"garou": ["Uktena"]})
Gift.objects.create(name="Rending the Craft", rank=3, allowed={"garou": ["Uktena"]})
Gift.objects.create(name="Scrying", rank=3, allowed={"garou": ["Uktena"]})
Gift.objects.create(
    name="Call Elemental", rank=4, allowed={"garou": ["Uktena", "Black Spiral Dancers"]}
)
Gift.objects.create(
    name="Hand of the Earth Lords", rank=4, allowed={"garou": ["Uktena", "Croatan"]}
)
Gift.objects.create(name="Fetosj Dp;;", rank=5, allowed={"garou": ["Uktena"]})
Gift.objects.create(
    name="Beat of the Heart-Drum", rank=1, allowed={"garou": ["Wendigo"]}
)
Gift.objects.create(name="Call the Breeze", rank=1, allowed={"garou": ["Wendigo"]})
Gift.objects.create(name="Camouflage", rank=1, allowed={"garou": ["Wendigo"]})
Gift.objects.create(name="Ice Echo", rank=1, allowed={"garou": ["Wendigo"]})
Gift.objects.create(name="Cutting Wind", rank=2, allowed={"garou": ["Wendigo"]})
Gift.objects.create(
    name="Claws of Frozen Death", rank=2, allowed={"garou": ["Wendigo"]}
)
Gift.objects.create(name="Salmon Swim", rank=2, allowed={"garou": ["Wendigo"]})
Gift.objects.create(
    name="Speak with Wind Spirits", rank=2, allowed={"garou": ["Wendigo"]}
)
Gift.objects.create(name="Blood of the North", rank=3, allowed={"garou": ["Wendigo"]})
Gift.objects.create(name="Bloody Feast", rank=3, allowed={"garou": ["Wendigo"]})
Gift.objects.create(name="Sky Running", rank=3, allowed={"garou": ["Wendigo"]})
Gift.objects.create(
    name="Call of the Cannibal Spirit", rank=4, allowed={"garou": ["Wendigo"]}
)
Gift.objects.create(name="Chill of Early Frost", rank=4, allowed={"garou": ["Wendigo"]})
Gift.objects.create(
    name="Invoke the Spirits of the Storm", rank=5, allowed={"garou": ["Wendigo"]}
)
Gift.objects.create(name="Heart of Ice", rank=5, allowed={"garou": ["Wendigo"]})
Gift.objects.create(
    name="See Past the Skin", rank=1, allowed={"garou": ["Black Spiral Dancers"]}
)
Gift.objects.create(
    name="Mask Taint", rank=5, allowed={"garou": ["Black Spiral Dancers"]}
)
Gift.objects.create(
    name="Bane Protector", rank=1, allowed={"garou": ["Black Spiral Dancers"]}
)
Gift.objects.create(
    name="Smell Fear", rank=2, allowed={"garou": ["Black Spiral Dancers", "philodox"]}
)
Gift.objects.create(
    name="Ears of the Bat", rank=2, allowed={"garou": ["Black Spiral Dancers"]}
)
Gift.objects.create(
    name="Wyrm Hide", rank=2, allowed={"garou": ["Black Spiral Dancers"]}
)
Gift.objects.create(
    name="A Thousand Voices",
    rank=2,
    allowed={"garou": ["Black Spiral Dancers", "theurge"]},
)
Gift.objects.create(
    name="Allies Below", rank=2, allowed={"garou": ["Black Spiral Dancers", "galliard"]}
)
Gift.objects.create(
    name="Horns of the Impaler",
    rank=2,
    allowed={"garou": ["Black Spiral Dancers", "ahroun"]},
)
Gift.objects.create(name="Patagia", rank=3, allowed={"garou": ["Black Spiral Dancers"]})
Gift.objects.create(
    name="Foaming Fury", rank=3, allowed={"garou": ["Black Spiral Dancers"]}
)
Gift.objects.create(
    name="Beautiful Lie", rank=3, allowed={"garou": ["Black Spiral Dancers"]}
)
Gift.objects.create(
    name="Touch of the Eer",
    rank=3,
    allowed={"garou": ["Black Spiral Dancers", "ragabash"]},
)
Gift.objects.create(
    name="Crawling Poison", rank=4, allowed={"garou": ["Black Spiral Dancers"]}
)
Gift.objects.create(
    name="Balefire", rank=5, allowed={"garou": ["Black Spiral Dancers"]}
)
Gift.objects.create(
    name="Dream of a Thousand Cranes", rank=1, allowed={"garou": ["Hakken"]}
)
Gift.objects.create(name="Fair Path", rank=1, allowed={"garou": ["Hakken"]})
Gift.objects.create(name="Storm Winds Slash", rank=2, allowed={"garou": ["Hakken"]})
Gift.objects.create(name="Dark of Night", rank=3, allowed={"garou": ["Hakken"]})
Gift.objects.create(name="Living Treasure", rank=4, allowed={"garou": ["Hakken"]})
Gift.objects.create(name="Divine Wind", rank=5, allowed={"garou": ["Hakken"]})

Gift.objects.create(
    name="Sheng-Nong's Eyes", rank=1, allowed={"garou": ["Boli Zousizhe"]}
)
Gift.objects.create(name="Fu Xi's Honor", rank=2, allowed={"garou": ["Boli Zousizhe"]})
Gift.objects.create(name="Yao's Commands", rank=3, allowed={"garou": ["Boli Zousizhe"]})
Gift.objects.create(name="Yu's Endurance", rank=4, allowed={"garou": ["Boli Zousizhe"]})
Gift.objects.create(
    name="Huang Di's Sacrifice", rank=5, allowed={"garou": ["Boli Zousizhe"]}
)

Gift.objects.create(name="Feed the Pack", rank=2, allowed={"garou": ["Kucha Ekundu"]})
Gift.objects.create(
    name="Predator's Many Eyes", rank=3, allowed={"garou": ["Kucha Ekundu"]}
)
Gift.objects.create(name="Crocodile Pact", rank=5, allowed={"garou": ["Kucha Ekundu"]})

Gift.objects.create(name="Bunyip's Spell", rank=1, allowed={"garou": ["Bunyip"]})
Gift.objects.create(name="Crocodile's Cunning", rank=2, allowed={"garou": ["Bunyip"]})
Gift.objects.create(
    name="Lonesome Voice of the Bunyip", rank=3, allowed={"garou": ["Bunyip"]}
)
Gift.objects.create(
    name="Dance of the Lightning Snakes", rank=4, allowed={"garou": ["Bunyip"]}
)
Gift.objects.create(name="Billabong Bridge", rank=5, allowed={"garou": ["Bunyip"]})

Gift.objects.create(name="Turtle Body", rank=1, allowed={"garou": ["Croatan"]})
Gift.objects.create(name="Turtle Shell", rank=2, allowed={"garou": ["Croatan"]})
Gift.objects.create(name="Call Earth Spirit", rank=3, allowed={"garou": ["Croatan"]})
Gift.objects.create(name="Stronger on Stone", rank=4, allowed={"garou": ["Croatan"]})
Gift.objects.create(
    name="Katanka-Sonnak's Spear", rank=5, allowed={"garou": ["Croatan"]}
)

Gift.objects.create(name="Haunting Howl", rank=1, allowed={"garou": ["White Howler"]})
Gift.objects.create(name="Pain-Strength", rank=2, allowed={"garou": ["White Howler"]})
Gift.objects.create(
    name="Sense of the Deep", rank=3, allowed={"garou": ["White Howler"]}
)
Gift.objects.create(name="Maddening Howl", rank=4, allowed={"garou": ["White Howler"]})
Gift.objects.create(name="Mad Strength", rank=5, allowed={"garou": ["White Howler"]})


Rite.objects.create(name="Rite of Cleansing", level=1, type="accord")
Rite.objects.create(name="Rite of Contrition", level=1, type="accord")
Rite.objects.create(name="Rite of Renunciation", level=2, type="accord")
Rite.objects.create(name="Rite of the Loyal PAck", level=3, type="accord")
Rite.objects.create(name="Enchant the Forest", level=4, type="accord")
Rite.objects.create(name="Rite of the Opened Sky", level=4, type="accord")
moot_rite = Rite.objects.create(name="Moot Rite", level=1, type="caern")
Rite.objects.create(name="Rite of the Opened Caern", level=1, type="caern")
Rite.objects.create(name="Rite of the Glorious Past", level=3, type="caern")
Rite.objects.create(name="The Badger's Burrow", level=4, type="caern")
Rite.objects.create(name="Rite of the Opened Bridge", level=4, type="caern")
Rite.objects.create(name="Rite of the Shrouded Glen", level=4, type="caern")
rite_of_caern_building = Rite.objects.create(
    name="Rite of Caern Building", level=5, type="caern"
)
Rite.objects.create(name="Gathering for the Departed", level=1, type="death")
Rite.objects.create(name="Last Blessing", level=1, type="death")
Rite.objects.create(name="Rite of the Winter Wolf", level=3, type="death")
Rite.objects.create(name="Baptism of Fire", level=1, type="mystic")
Rite.objects.create(name="Rite of Binding", level=1, type="mystic")
Rite.objects.create(name="Rite of Growth", level=1, type="mystic")
Rite.objects.create(name="Rite of Heritage", level=1, type="mystic")
Rite.objects.create(name="Rite of the Cardboard Palace", level=1, type="mystic")
Rite.objects.create(name="Rite of the Questing Stone", level=1, type="mystic")
Rite.objects.create(name="Rite of Talisman Dedication", level=1, type="mystic")
Rite.objects.create(name="Rite of Becoming", level=2, type="mystic")
Rite.objects.create(name="Rite of Spirit Awakening", level=2, type="mystic")
Rite.objects.create(name="Rite of Summoning", level=2, type="mystic")
Rite.objects.create(name="Rite of Sacred Rebirth", level=5, type="mystic")
Rite.objects.create(name="Descent Into the Underworld", level=3, type="mystic")
Rite.objects.create(name="Rite of the Fetish", level=3, type="mystic")
Rite.objects.create(name="Rite of the Totem", level=3, type="mystic")
Rite.objects.create(name="Rite of the Jackdaw", level=1, type="punishment")
rite_of_ostracism = Rite.objects.create(
    name="Rite of Ostracism", level=2, type="punishment"
)
stone_of_scorn = Rite.objects.create(name="Stone of Scorn", level=2, type="punishment")
rite_of_the_jackal = Rite.objects.create(
    name="Voice of the Jackal", level=2, type="punishment"
)
Rite.objects.create(name="The Hunt", level=3, type="punishment")
Rite.objects.create(name="Rite of the Omega Wolf", level=3, type="punishment")
Rite.objects.create(name="Satire Rite", level=3, type="punishment")
Rite.objects.create(name="The Rending of the Veil", level=4, type="punishment")
Rite.objects.create(name="Gaia's Vengeful Teeth", level=5, type="punishment")
Rite.objects.create(name="Rite of Boasting", level=1, type="renown")
rite_of_wounding = Rite.objects.create(name="Rite of Wounding", level=1, type="renown")
Rite.objects.create(name="Rite of Accomplishment", level=2, type="renown")
rite_of_passage = Rite.objects.create(name="Rite of Passage", level=2, type="renown")
Rite.objects.create(name="Rite of Praise", level=2, type="renown")
Rite.objects.create(name="Rite of the Winter Winds", level=2, type="seasonal")
Rite.objects.create(name="Rite of Reawakening", level=2, type="seasonal")
Rite.objects.create(name="The Great Hunt", level=2, type="seasonal")
Rite.objects.create(name="The Long Vigil", level=3, type="seasonal")
Rite.objects.create(name="Bone Rhythms", level=0, type="minor")
Rite.objects.create(name="Breath of Gaia", level=0, type="minor")
Rite.objects.create(name="Greet the Moon", level=0, type="minor")
Rite.objects.create(name="Greet the Sun", level=0, type="minor")
Rite.objects.create(name="Hunting Prayer", level=0, type="minor")
Rite.objects.create(name="Prayer for the Prey", level=0, type="minor")

RenownIncident.objects.create(
    name="Besting someone (including a spirit) in a riddle contest",
    glory=0,
    honor=0,
    wisdom=3,
)
RenownIncident.objects.create(
    name="Showing restriant in the face of certain death", glory=0, honor=1, wisdom=3
)
RenownIncident.objects.create(
    name="Ending a threat without serious harm to any Garou", glory=0, honor=0, wisdom=5
)
RenownIncident.objects.create(
    name="Surviving an Incapacitating wound", glory=2, honor=0, wisdom=0
)
RenownIncident.objects.create(
    name="Surviving any toxic waste attack", glory=2, honor=0, wisdom=0
)
RenownIncident.objects.create(
    name="Attacking a much more powerful force without aid", glory=0, honor=0, wisdom=-3
)
RenownIncident.objects.create(
    name="Attacking a minion of the Wyrm without regard to personal safety",
    glory=3,
    honor=0,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Defeating a formidable supernatural threat not of the Wyrm (strand spider, master mage, fae warrior, Fera, etc.)",
    glory=2,
    honor=0,
    wisdom=0,
)

RenownIncident.objects.create(
    name="Defeating a very powerful supernatual threat not of the Wyrm (archmage, fae sorcerer, etc.)",
    glory=3,
    honor=0,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Defeating a minor Wyrm threat (Kalus, a Bane-infested animal, young vampire, etc.)",
    glory=2,
    honor=0,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Defeating an average Wyrm threat (Blight Child, fomori, etc.)",
    glory=3,
    honor=0,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Defeating a strong Wyrm threat (Psychomachie, Black Spiral Dancer pack, etc.)",
    glory=5,
    honor=0,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Defeating a very powerful Wyrm threat (Nexus Crawler, elder vampires, etc.)",
    glory=7,
    honor=0,
    wisdom=0,
)
# We are currently ignoring the four modifiers on 247 for killing, no other Garou harmed, not being hurt, and enemy with silver
RenownIncident.objects.create(
    name='Revealing, with certain proof, that a human or Kinfolk is "of the Wyrm"',
    glory=0,
    honor=0,
    wisdom=2,
)
RenownIncident.objects.create(
    name='Falsely accusing a Kinfolk of being "of the Wyrm"',
    glory=0,
    honor=-2,
    wisdom=-3,
)
RenownIncident.objects.create(
    name='Revealing, with certain proof, that an area or object is "of the Wyrm"',
    glory=0,
    honor=0,
    wisdom=3,
)
RenownIncident.objects.create(
    name='Revealing, with certain proof, that a Garou is "of the Wyrm"',
    glory=0,
    honor=0,
    wisdom=6,
)
RenownIncident.objects.create(
    name='Falsely accusing a Garou of being "of the Wyrm"', glory=0, honor=-5, wisdom=-4
)
RenownIncident.objects.create(
    name="Purifying a Wyrm-tainted object, person, or place", glory=0, honor=0, wisdom=2
)
RenownIncident.objects.create(
    name="Summoning an Incarna avatar", glory=0, honor=0, wisdom=2
)
RenownIncident.objects.create(
    name="Traveling to any of the Umbral Realms and surviving",
    glory=3,
    honor=0,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Successfully completing a spirit quest in the Umbra",
    glory=0,
    honor=0,
    wisdom=3,
)
RenownIncident.objects.create(
    name="Failing to succeed in a spirit quest in the Umbra",
    glory=0,
    honor=0,
    wisdom=-3,
)
RenownIncident.objects.create(
    name="Having and properly following a prophetic dream", glory=0, honor=0, wisdom=5
)
RenownIncident.objects.create(
    name="Giving a prophetic warning that later comes true", glory=0, honor=0, wisdom=5
)
RenownIncident.objects.create(
    name="Ignoring omens, dreams, and the like for no good reason (i.e., suspecting they may be of the Wyrm)",
    glory=0,
    honor=0,
    wisdom=-3,
)
RenownIncident.objects.create(
    name='Binding "inappropriate" items to oneself through the Rite of Talisman Dedication',
    glory=0,
    honor=0,
    wisdom=-2,
)
RenownIncident.objects.create(
    name="Spending a year in ritualistic seclusion (fasting, meditation, etc.)",
    glory=0,
    honor=0,
    wisdom=5,
)
RenownIncident.objects.create(name="Discovering a talen", glory=0, honor=0, wisdom=1)
RenownIncident.objects.create(name="Discovering a fetish", glory=0, honor=0, wisdom=2)
RenownIncident.objects.create(
    name="Discovering ancient Garou lore", glory=0, honor=0, wisdom=3
)
RenownIncident.objects.create(
    name="Discovering a Pathstone", glory=0, honor=0, wisdom=4
)
RenownIncident.objects.create(
    name="Discovering an ancient caern that was lost", glory=0, honor=0, wisdom=7
)
RenownIncident.objects.create(
    name="Perfomring a Moot Rite", glory=0, honor=2, wisdom=0, rite=moot_rite
)
RenownIncident.objects.create(
    name="Refusing to perform a Moot Rite when asked",
    glory=0,
    honor=-3,
    wisdom=0,
    rite=moot_rite,
)
RenownIncident.objects.create(name="Missing a Moot Rite", glory=0, honor=0, wisdom=-1)

RenownIncident.objects.create(
    name="Performing a Rite of Passage",
    glory=0,
    honor=2,
    wisdom=1,
    rite=rite_of_passage,
)
RenownIncident.objects.create(
    name="Receiving a Rite of Wounding",
    glory=2,
    honor=0,
    wisdom=0,
    rite=rite_of_wounding,
)
RenownIncident.objects.create(
    name="Performing a Rite of Caern Building",
    glory=3,
    honor=5,
    wisdom=7,
    rite=rite_of_caern_building,
)
RenownIncident.objects.create(
    name="Participating in a Rite of Caern Building", glory=0, honor=5, wisdom=3
)
RenownIncident.objects.create(
    name="Participating in a successful Great Hunt rite", glory=3, honor=0, wisdom=0
)
RenownIncident.objects.create(
    name="Participating in a failed Great Hunt rite", glory=-2, honor=0, wisdom=0
)
RenownIncident.objects.create(
    name="Suffering the Rite of Ostracism",
    glory=-1,
    honor=-7,
    wisdom=-1,
    rite=rite_of_ostracism,
)
RenownIncident.objects.create(
    name="Suffering the Stone of Scorn",
    glory=0,
    honor=-8,
    wisdom=-2,
    rite=stone_of_scorn,
)
RenownIncident.objects.create(
    name="Suffering the Rite of the Jackal",
    glory=-2,
    honor=-7,
    wisdom=0,
    rite=rite_of_the_jackal,
)
# No test currently for "has a punishment rite"
RenownIncident.objects.create(
    name="Performing a Punishment Rite", glory=0, honor=2, wisdom=0
)
RenownIncident.objects.create(
    name="Performing a Punishment Rite unjustly", glory=0, honor=-5, wisdom=0
)
RenownIncident.objects.create(
    name="Refusing to participate in a rite", glory=0, honor=0, wisdom=-1
)
RenownIncident.objects.create(
    name="Giggling, joking, or otherwise being disrespectful during a rite",
    glory=0,
    honor=0,
    wisdom=-3,
)
RenownIncident.objects.create(name="Learning a new rite", glory=0, honor=0, wisdom=1)
RenownIncident.objects.create(
    name="Discovering/creating a new rite", glory=0, honor=0, wisdom=5
)
RenownIncident.objects.create(
    name="Discovering/creating a new gift", glory=0, honor=0, wisdom=7
)
RenownIncident.objects.create(name="Creating a talen", glory=0, honor=0, wisdom=1)
RenownIncident.objects.create(
    name="Using a fetish for the good of the sept or tribe", glory=0, honor=0, wisdom=2
)
RenownIncident.objects.create(
    name="Using a fetish for selfish reasons only", glory=0, honor=0, wisdom=-1
)
RenownIncident.objects.create(name="Creating a fetish", glory=0, honor=0, wisdom=4)
RenownIncident.objects.create(
    name="Owning a klaive (awarded once, only after three moons of use)",
    glory=2,
    honor=1,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Owning a grand klaive (awarded once, only after three moons of use)",
    glory=3,
    honor=2,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Sacrificing a fetish for the good of the sept or tribe",
    glory=0,
    honor=0,
    wisdom=4,
)
RenownIncident.objects.create(
    name="Accidentally breaking a fetish or talen", glory=0, honor=0, wisdom=-3
)
RenownIncident.objects.create(
    name="Accidentally breaking or losing a klaive", glory=0, honor=-3, wisdom=0
)
RenownIncident.objects.create(name="Helping guard a caern", glory=0, honor=1, wisdom=0)
RenownIncident.objects.create(
    name="Staying at your post when on caern watch, even when tempted not to",
    glory=0,
    honor=2,
    wisdom=1,
)
RenownIncident.objects.create(
    name="Not staying at your post when on watch", glory=0, honor=-3, wisdom=0
)
RenownIncident.objects.create(
    name="Not helping guard a caern, even when asked to", glory=0, honor=-3, wisdom=0
)
RenownIncident.objects.create(
    name="Keeping a caern safe from humans through trickery or negotiation",
    glory=0,
    honor=0,
    wisdom=4,
)
RenownIncident.objects.create(
    name="Helping to prevent a caern from being overrun by the Wyrm",
    glory=3,
    honor=4,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Not prevenitng a caern from being overrun by the Wyrm",
    glory=-3,
    honor=-7,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Dying while defending a caern (posthumous)",
    glory=5,
    honor=8,
    wisdom=0,
    posthumous=True,
)
RenownIncident.objects.create(
    name="Single-handedly preventing a caern from being taken by the Wyrm",
    glory=5,
    honor=8,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Teaching other Garou (depends on the depth of study)",
    glory=0,
    honor=3,
    wisdom=4,
)
RenownIncident.objects.create(
    name="Learning the complete Silver Record (a lifetime's work)",
    glory=0,
    honor=7,
    wisdom=8,
)
RenownIncident.objects.create(
    name="For a homid Garou, surviving to age 75",
    glory=0,
    honor=8,
    wisdom=10,
    breed="homid",
)
RenownIncident.objects.create(
    name="For a lupus Garou, surviving to age 65",
    glory=0,
    honor=8,
    wisdom=10,
    breed="lupus",
)

RenownIncident.objects.create(
    name="For a homid, ignoring one's wold nature for too long",
    glory=0,
    honor=0,
    wisdom=-3,
    breed="homid",
)
RenownIncident.objects.create(
    name="For a metis, attempting to hide one's deformity",
    glory=0,
    honor=0,
    wisdom=-3,
    breed="metis",
)
RenownIncident.objects.create(
    name="For a lupus, using too many human tools and other Weaver things",
    glory=0,
    honor=0,
    wisdom=-1,
    breed="lupus",
)
RenownIncident.objects.create(
    name="Gaining the position of Pack leader", glory=0, honor=3, wisdom=0
)
RenownIncident.objects.create(
    name="Living alone, without one's pack, except for ritual reasons",
    glory=0,
    honor=0,
    wisdom=-3,
)
RenownIncident.objects.create(
    name="Performing regular duties and chores for the sept (gained at monthly Moot Rite)",
    glory=0,
    honor=1,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Failing to perform regular duties and chores for the sept (subtracted at monthly Moot Rite)",
    glory=0,
    honor=0,
    wisdom=-3,
)
RenownIncident.objects.create(
    name="Disobeying a caern officer without good reason", glory=0, honor=-2, wisdom=0
)
RenownIncident.objects.create(
    name="Serving in any sept position for a year", glory=1, honor=3, wisdom=1
)
RenownIncident.objects.create(
    name="Refusing any sept position", glory=-1, honor=-2, wisdom=-1
)
RenownIncident.objects.create(
    name="Maintaining loyal service to a sept for a year", glory=1, honor=2, wisdom=1
)
RenownIncident.objects.create(
    name="Maintaining loyal service to a tribe for a year", glory=1, honor=3, wisdom=1
)
RenownIncident.objects.create(name="Upholding the Litany", glory=0, honor=3, wisdom=2)
RenownIncident.objects.create(name="Breaking the Litany", glory=0, honor=-6, wisdom=-3)
RenownIncident.objects.create(
    name="Participating in a just challenge", glory=1, honor=2, wisdom=0
)
RenownIncident.objects.create(
    name="Participating in an unjust challenge", glory=0, honor=-3, wisdom=0
)
RenownIncident.objects.create(
    name="Challenging someone too far above or too far below your Rank",
    glory=0,
    honor=-3,
    wisdom=0,
)
RenownIncident.objects.create(name="Giving good advice", glory=0, honor=0, wisdom=2)
RenownIncident.objects.create(name="Giving bad advice", glory=0, honor=0, wisdom=-2)
RenownIncident.objects.create(
    name="Mediating a dispute fairly", glory=0, honor=3, wisdom=0
)
RenownIncident.objects.create(
    name="Mediating a dispute unfairly", glory=0, honor=-4, wisdom=0
)
RenownIncident.objects.create(name="Keeping one's promises", glory=0, honor=2, wisdom=0)
RenownIncident.objects.create(
    name="Failing to keep one's promises", glory=0, honor=-3, wisdom=0
)
RenownIncident.objects.create(name="Being truthful", glory=0, honor=2, wisdom=0)
RenownIncident.objects.create(
    name="Being truthful in the face of extreme adversity", glory=0, honor=5, wisdom=0
)
RenownIncident.objects.create(name="Being deceptive", glory=0, honor=-3, wisdom=0)
RenownIncident.objects.create(
    name="Being deceptive in the face of extreme adversity", glory=0, honor=-1, wisdom=0
)
RenownIncident.objects.create(
    name="Having your trickery backfire", glory=0, honor=0, wisdom=-2
)
RenownIncident.objects.create(
    name="Attempting to openly act outside one's auspice", glory=1, honor=-3, wisdom=0
)
RenownIncident.objects.create(
    name="Telling a good story at a moot", glory=2, honor=0, wisdom=2
)
RenownIncident.objects.create(
    name="Telling a true epic at a moot that is later retorld by others",
    glory=3,
    honor=1,
    wisdom=3,
)
RenownIncident.objects.create(
    name="Telling an epic that is entered into the Silver Record",
    glory=0,
    honor=4,
    wisdom=6,
)
RenownIncident.objects.create(
    name="Speaking dishonorably to one's elders", glory=0, honor=-3, wisdom=0
)
RenownIncident.objects.create(
    name="Speaking without permission at a moot", glory=0, honor=-1, wisdom=0
)
RenownIncident.objects.create(
    name="Speaking poorly of the Garou as a whole", glory=0, honor=-2, wisdom=0
)
RenownIncident.objects.create(
    name="Speaking poorly of one's auspice", glory=0, honor=-4, wisdom=0
)
RenownIncident.objects.create(
    name="Speaking poorly of one's tribe", glory=0, honor=-4, wisdom=0
)
RenownIncident.objects.create(
    name="Speaking poorly of one's pack", glory=0, honor=-6, wisdom=0
)

RenownIncident.objects.create(
    name="Speaking poorly of another tribe (except Bone Gnawers)",
    glory=0,
    honor=-1,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Summoning help when there is no real danger present",
    glory=0,
    honor=-5,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Healing a fellow Garou (non-pack member) unselifishly",
    glory=0,
    honor=0,
    wisdom=1,
)
RenownIncident.objects.create(
    name="Showing mercy to a wayward Garou", glory=0, honor=0, wisdom=3
)
RenownIncident.objects.create(
    name="Protecting a helpless Garou", glory=0, honor=4, wisdom=0
)
RenownIncident.objects.create(
    name="Not protecting a helpless Garou", glory=0, honor=-5, wisdom=0
)
RenownIncident.objects.create(
    name="Protecting a helpless human", glory=0, honor=2, wisdom=0
)
RenownIncident.objects.create(
    name="Not protecting a helpless human", glory=0, honor=-1, wisdom=0
)
RenownIncident.objects.create(
    name="Protecting a helpless wolf", glory=0, honor=5, wisdom=0
)
RenownIncident.objects.create(
    name="Not protecting a helpless wolf", glory=0, honor=-6, wisdom=0
)
RenownIncident.objects.create(
    name="Supporting an innocent being accused of a crime (who is later proven innocent)",
    glory=0,
    honor=5,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Supporting an innocent being accused of a crime (who is later proven guilty)",
    glory=0,
    honor=-4,
    wisdom=0,
)
RenownIncident.objects.create(
    name="Dying while defending your pack (posthumous)",
    glory=4,
    honor=6,
    wisdom=0,
    posthumous=True,
)
RenownIncident.objects.create(
    name="Dying in defense of Gaia (posthumous)",
    glory=7,
    honor=7,
    wisdom=0,
    posthumous=True,
)
RenownIncident.objects.create(
    name="Succumbing to a berserk frenzy", glory=0, honor=0, wisdom=-1
)
RenownIncident.objects.create(
    name="Succumbing to a fox frenzy", glory=-1, honor=0, wisdom=-1
)
RenownIncident.objects.create(
    name="Succumbing to a fox frenzy and abandoning your pack in time of need",
    glory=0,
    honor=-1,
    wisdom=-2,
)
RenownIncident.objects.create(
    name="Succumbing to a berserk frenzy and injuring fellow Garou",
    glory=0,
    honor=0,
    wisdom=-3,
)
RenownIncident.objects.create(
    name="Succumbing to the thrall of the Wyrm", glory=0, honor=0, wisdom=-4
)
RenownIncident.objects.create(
    name="Performing a heinous act while in the thrall of the Wyrm (cannibalism, perversion, attacking your own packmates, etc.)",
    glory=0,
    honor=-3,
    wisdom=-1,
)
RenownIncident.objects.create(
    name="Maintaining good relations with nearby Kinfolk", glory=0, honor=0, wisdom=2
)
RenownIncident.objects.create(
    name="Having poor relations with nearby Kinfolk", glory=0, honor=0, wisdom=-3
)
RenownIncident.objects.create(
    name="Choosing a mate and breeding", glory=0, honor=0, wisdom=3
)
RenownIncident.objects.create(
    name="Choosing a mate, but not breeding", glory=0, honor=0, wisdom=-1
)
RenownIncident.objects.create(
    name="Staying honorably mated for a year", glory=0, honor=2, wisdom=0
)
RenownIncident.objects.create(name="Protecting the Veil", glory=0, honor=4, wisdom=0)
RenownIncident.objects.create(
    name="Harming or rending the Veil", glory=0, honor=-5, wisdom=0
)
RenownIncident.objects.create(name="Repairing the Veil", glory=0, honor=3, wisdom=1)

# Totem.objects.create(name="", cost=0)

Archetype.objects.get_or_create(name="Alpha")
Archetype.objects.get_or_create(name="Architect")
Archetype.objects.get_or_create(name="Barterer")
Archetype.objects.get_or_create(name="Big Bad Wolf")
Archetype.objects.get_or_create(name="Bon Vivant")
Archetype.objects.get_or_create(name="Bravo")
Archetype.objects.get_or_create(name="Caregiver")
Archetype.objects.get_or_create(name="Celebrant")
Archetype.objects.get_or_create(name="Competitor")
Archetype.objects.get_or_create(name="Conformist")
Archetype.objects.get_or_create(name="Conniver")
Archetype.objects.get_or_create(name="Contrary")
Archetype.objects.get_or_create(name="Cub")
Archetype.objects.get_or_create(name="Director")
Archetype.objects.get_or_create(name="Fanatic")
Archetype.objects.get_or_create(name="Fatalist")
Archetype.objects.get_or_create(name="Gallant")
Archetype.objects.get_or_create(name="Guru")
Archetype.objects.get_or_create(name="Idealist")
Archetype.objects.get_or_create(name="Judge")
Archetype.objects.get_or_create(name="Loner")
Archetype.objects.get_or_create(name="Martyr")
Archetype.objects.get_or_create(name="Pedagogue")
Archetype.objects.get_or_create(name="Penitent")
Archetype.objects.get_or_create(name="Perfectionist")
Archetype.objects.get_or_create(name="Rebel")
Archetype.objects.get_or_create(name="Rogue")
Archetype.objects.get_or_create(name="Scientist")
Archetype.objects.get_or_create(name="Soldier")
Archetype.objects.get_or_create(name="Survivor")
Archetype.objects.get_or_create(name="Thrill-Seeker")
Archetype.objects.get_or_create(name="Traditionalist")
Archetype.objects.get_or_create(name="Trickster")
Archetype.objects.get_or_create(name="Visionary")

Camp.objects.create(name="Amazons of Diana", tribe=bone_gnawers)
Camp.objects.create(name="Bacchantes/Maenads", tribe=bone_gnawers)
Camp.objects.create(name="Freebooters", tribe=bone_gnawers)
Camp.objects.create(name="Moon-Daughters", tribe=bone_gnawers)
Camp.objects.create(name="Order of Our Merciful Mother", tribe=bone_gnawers)
Camp.objects.create(name="The Sisterhood", tribe=bone_gnawers)
Camp.objects.create(name="The Temple of Artemis", tribe=bone_gnawers)
Camp.objects.create(name="Deserters", tribe=bone_gnawers)
Camp.objects.create(name="Frankenweilers", tribe=bone_gnawers)
Camp.objects.create(name="Maneaters", tribe=bone_gnawers)
Camp.objects.create(name="Hillfolk", tribe=bone_gnawers)
Camp.objects.create(name="The Hood", tribe=bone_gnawers)
Camp.objects.create(name="Rat Finks", tribe=bone_gnawers)
Camp.objects.create(name="Road Warders", tribe=bone_gnawers)
Camp.objects.create(name="The Swarm", tribe=bone_gnawers)
Camp.objects.create(name="Aethera Inamorata", tribe=children_of_gaia)
Camp.objects.create(name="Angels in the Garden", tribe=children_of_gaia)
Camp.objects.create(name="The Anounted Ones", tribe=children_of_gaia)
Camp.objects.create(name="Bringers of Eternal Peace", tribe=children_of_gaia)
Camp.objects.create(name="Demeter's Daughters", tribe=children_of_gaia)
Camp.objects.create(name="Imminent Strike", tribe=children_of_gaia)
Camp.objects.create(name="The One Tree", tribe=children_of_gaia)
Camp.objects.create(name="The Patient Deed", tribe=children_of_gaia)
Camp.objects.create(name="Seekers of the Lost Tribes", tribe=children_of_gaia)
Camp.objects.create(name="Servants of Unicorn", tribe=children_of_gaia)
Camp.objects.create(name="Brotherhood of Herne", tribe=fianna)
Camp.objects.create(name="Children of Dire", tribe=fianna)
Camp.objects.create(name="Grandchildren of Fionn", tribe=fianna)
Camp.objects.create(name="Mother's Fundamentalists", tribe=fianna)
Camp.objects.create(name="Songkeepers", tribe=fianna)
Camp.objects.create(name="Tuatha de Fionn", tribe=fianna)
Camp.objects.create(name="Whispering Rovers", tribe=fianna)
Camp.objects.create(name="The Fangs of Garm", tribe=get_of_fenris)
Camp.objects.create(name="The Glorious Fist of Wotan", tribe=get_of_fenris)
Camp.objects.create(name="The Hand of Tyr", tribe=get_of_fenris)
Camp.objects.create(name="Loki's Smile", tribe=get_of_fenris)
Camp.objects.create(name="Mjolnir's Thunder", tribe=get_of_fenris)
Camp.objects.create(name="The Swords of Heimdall", tribe=get_of_fenris)
Camp.objects.create(name="The Valkyria of Freya", tribe=get_of_fenris)
Camp.objects.create(name="Ymir's Sweat", tribe=get_of_fenris)
Camp.objects.create(name="City Farmers", tribe=glass_walker)
Camp.objects.create(name="Corporate Wolves", tribe=glass_walker)
Camp.objects.create(name="Cyber Dogs", tribe=glass_walker)
Camp.objects.create(name="Dies Ultimae", tribe=glass_walker)
Camp.objects.create(name="Mechanical Awakening", tribe=glass_walker)
Camp.objects.create(name="Random Interrupts", tribe=glass_walker)
Camp.objects.create(name="Umbral Pilots", tribe=glass_walker)
Camp.objects.create(name="Urban Primitives", tribe=glass_walker)
Camp.objects.create(name="Wise Guys", tribe=glass_walker)
Camp.objects.create(name="The Dying Cubs", tribe=red_talons)
Camp.objects.create(name="The Lodge of the Predator Kings", tribe=red_talons)
Camp.objects.create(name="Warders of the Land", tribe=red_talons)
Camp.objects.create(name="Whelp's Compromise", tribe=red_talons)
Camp.objects.create(name="The Masks", tribe=shadow_lords)
Camp.objects.create(name="Bringers of Light", tribe=shadow_lords)
Camp.objects.create(name="Children of Crow", tribe=shadow_lords)
Camp.objects.create(name="Judges of Doom", tribe=shadow_lords)
Camp.objects.create(name="Lords of the Summit", tribe=shadow_lords)
Camp.objects.create(name="Revolutionary Guard", tribe=shadow_lords)
Camp.objects.create(name="Society of Nidhogg", tribe=shadow_lords)
Camp.objects.create(name="The Bitter Hex", tribe=silent_striders)
Camp.objects.create(name="The Dispossessed", tribe=silent_striders)
Camp.objects.create(name="Harbingers", tribe=silent_striders)
Camp.objects.create(name="Eaters of the Dead", tribe=silent_striders)
Camp.objects.create(name="Seekers", tribe=silent_striders)
Camp.objects.create(name="Swords of Night", tribe=silent_striders)
Camp.objects.create(name="Wayfarers", tribe=silent_striders)
Camp.objects.create(name="Grey Raptors", tribe=silver_fangs)
Camp.objects.create(name="Ivory Priesthood", tribe=silver_fangs)
Camp.objects.create(name="Masters of the Seal", tribe=silver_fangs)
Camp.objects.create(name="Renewal", tribe=silver_fangs)
Camp.objects.create(name="Ana-gamin", tribe=stargazers)
Camp.objects.create(name="The Heavenly Successors of the Demon-Eater", tribe=stargazers)
Camp.objects.create(name="The Inner Path", tribe=stargazers)
Camp.objects.create(name="Klaital Puk", tribe=stargazers)
Camp.objects.create(name="Ouroboroans", tribe=stargazers)
Camp.objects.create(name="The Sacred Thread", tribe=stargazers)
Camp.objects.create(name="Trance Runners", tribe=stargazers)
Camp.objects.create(name="The World Tree", tribe=stargazers)
Camp.objects.create(name="The Zephyr", tribe=stargazers)
Camp.objects.create(name="The Metastic Birth", tribe=stargazers)
Camp.objects.create(name="Bane Tenders", tribe=uktena)
Camp.objects.create(name="Earth Guides", tribe=uktena)
Camp.objects.create(name="Path Dancers", tribe=uktena)
Camp.objects.create(name="Scouts", tribe=uktena)
Camp.objects.create(name="Skywalkers", tribe=uktena)
Camp.objects.create(name="Society of Bitter Frost", tribe=uktena)
Camp.objects.create(name="Web Walkers", tribe=uktena)
Camp.objects.create(name="Wyld Children", tribe=uktena)
Camp.objects.create(name="Gluskap's Lodge", tribe=wendigo)
Camp.objects.create(name="Myeengun's Lodge", tribe=wendigo)
Camp.objects.create(name="The Sacred Hoop", tribe=wendigo)
Camp.objects.create(name="The Secret Hoop", tribe=wendigo)
Camp.objects.create(name="The Warpath", tribe=wendigo)
Camp.objects.create(name="Fang Breakers", tribe=None)
Camp.objects.create(name="Ghost Dancers", tribe=None)
Camp.objects.create(name="Lazarite Movement", tribe=None)
Camp.objects.create(name="Hakken", tribe=shadow_lords)
Camp.objects.create(name="Boli Zousizhe", tribe=glass_walker)
Camp.objects.create(name="Kucha Ekundu", tribe=red_talons)
