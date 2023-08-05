from game.models.chronicle import ObjectType
from wod.models.characters.human import Derangement, MeritFlaw
from wod.models.items.human import MeleeWeapon, RangedWeapon, ThrownWeapon

# W20
MeritFlaw.objects.get_or_create(
    name="Acute Sense (Werewolf)",
    ratings=[1],
    human=True,
    garou=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Alcohol Tolerance", ratings=[1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Ambidextrous",
    ratings=[1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Double-Jointed",
    ratings=[1],
    human=True,
    garou=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Mixed-morph", ratings=[1, 5], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Perfect Balance (Werewolf)", ratings=[1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(name="Wolf Sight", ratings=[1], human=True, garou=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Bad Taste", ratings=[2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Fair Glabro", ratings=[2], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Lack of Scent", ratings=[2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Physically Impressive",
    ratings=[2],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Daredevil", ratings=[3], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Long-Distance Runner", ratings=[3], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Natural Weapons", ratings=[3, 4], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Huge Size",
    ratings=[4],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(name="Metamorph", ratings=[7], human=True, garou=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Animal Musk", ratings=[-1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Anosmia", ratings=[-1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Hard of Hearing", ratings=[-1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Monochrome Vision", ratings=[-1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="No Partial Transformation", ratings=[-1], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Short (Werewolf)",
    ratings=[-1],
    human=True,
    garou=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Strict Carnivore", ratings=[-1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="One Eye", ratings=[-2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Bad Sight (Werewolf)", ratings=[-3], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Deformity", ratings=[-3], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Double Jeopardy", ratings=[-3], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Lame", ratings=[-3], human=True, garou=True, kinfolk=True, changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Monstrous", ratings=[-3], human=True, garou=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="One Arm", ratings=[-3], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Deaf", ratings=[-4], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Mute", ratings=[-4], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Blind", ratings=[-6], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Common Sense",
    ratings=[1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Computer Aptitude",
    ratings=[1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Concentration",
    ratings=[1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Expert Driver", ratings=[1], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Language",
    ratings=[1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Lightning Calculator",
    ratings=[1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Mechanical Aptitude",
    ratings=[1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Time Sense", ratings=[1], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Berserker (Werewolf)", ratings=[2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Code of Honor", ratings=[2], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Eidetic Memory",
    ratings=[2],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Inner Strength", ratings=[2], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Natural Linguist",
    ratings=[2],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Seldom Sleeps", ratings=[2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Calm Heart", ratings=[3], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Iron Will",
    ratings=[3],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Jack-of-all-Trades (Mage and Werewolf)",
    ratings=[3],
    human=True,
    garou=True,
    kinfolk=True,
    mage=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Self-Confident", ratings=[5], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Untamable", ratings=[5], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Compulsion", ratings=[-1], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Impatient",
    ratings=[-1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Intolerance (Werewolf)", ratings=[-1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Nightmares (Werewolf and Changeling)",
    ratings=[-1],
    human=True,
    garou=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Overconfident", ratings=[-1], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Shy", ratings=[-1], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Soft-Hearted (Werewolf and Mage)",
    ratings=[-1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Speech Impediment",
    ratings=[-1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Amnesia",
    ratings=[-2],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Curiosity",
    ratings=[-2],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Pack Mentality", ratings=[-2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Phobia (Werewolf and Mage)",
    ratings=[-2, -3],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Short Fuse",
    ratings=[-2],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Territorial", ratings=[-2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Vengeful",
    ratings=[-2],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Absent-Minded",
    ratings=[-3],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Deranged (Werewolf)", ratings=[-3], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Driving Goal", ratings=[-3], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Hatred", ratings=[-3], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Weak-Willed",
    ratings=[-3],
    human=True,
    garou=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Ability Deficit",
    ratings=[-5],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Flashbacks (Werewolf)", ratings=[-6], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Family Support (Werewolf)", ratings=[1], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Favor", ratings=[1, 2, 3], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Pitiable", ratings=[1], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Camp Goodwill", ratings=[1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Animal Magnetism",
    ratings=[2],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Natural Leader (Werewolf)", ratings=[2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Notable Heritage", ratings=[2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Reputation",
    ratings=[2],
    human=True,
    garou=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Supporter", ratings=[2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Noted Messenger", ratings=[3], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Supernatural Companion", ratings=[3], human=True, garou=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Conniver", ratings=[-1], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Dark Secret",
    ratings=[-1],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Enemy",
    ratings=[-1, -2, -3, -4, -5],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Naive", ratings=[-1], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Twisted Upbringing", ratings=[-1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Camp Enmity", ratings=[-1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Gullible", ratings=[-2], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Persistent Parents", ratings=[-2], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Notoriety", ratings=[-3], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Ward",
    ratings=[-3],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Hunted (Werewolf)", ratings=[-4], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Metis Child", ratings=[-4], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Ancestor Ally", ratings=[1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(name="Moon-Bound", ratings=[1], human=True, garou=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Spirit Magnet (Werewolf)", ratings=[1], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Danger Sense (Werewolf and Mage)",
    ratings=[3],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Lucky",
    ratings=[3],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Natural Channel", ratings=[3], human=True, garou=True, mage=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="True Love (Werewolf and Mage)",
    ratings=[4],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Immune to Wyrm Emanations", ratings=[6], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Silver Tolerance", ratings=[7], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Banned Transformation",
    ratings=[-1, -2, -3, -4, -5, -6],
    human=True,
    garou=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Cursed",
    ratings=[-1, -2, -3, -4, -5],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Foe from the Past", ratings=[-1, -2, -3], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Forced Transformation", ratings=[-1, -2], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Insane Ancestor", ratings=[-1], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Slip Sideways", ratings=[-1], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Docile", ratings=[-1, -2, -3], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Mark of the Predator", ratings=[-2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sign of the Wolf", ratings=[-2], human=True, garou=True, kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Pierced Veil", ratings=[-3], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Harano Prone", ratings=[-4], human=True, garou=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Dark Fate",
    ratings=[-5],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Taint of Corruption",
    ratings=[-7],
    human=True,
    garou=True,
    mage=True,
    kinfolk=True,
)[0]

MeritFlaw.objects.get_or_create(name="Feral Appearance", ratings=[1], kinfolk=True)[0]
MeritFlaw.objects.get_or_create(name="Barren/Sterile", ratings=[-4], kinfolk=True)[0]
MeritFlaw.objects.get_or_create(name="Wolf-Sense", ratings=[1], kinfolk=True)[0]
MeritFlaw.objects.get_or_create(name="Gall", ratings=[2], kinfolk=True)[0]
MeritFlaw.objects.get_or_create(name="Recognize Garou", ratings=[3], kinfolk=True)[0]
MeritFlaw.objects.get_or_create(name="Inferiority Complex", ratings=[-1], kinfolk=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Ulterior Motive", ratings=[-2], kinfolk=True)[0]
MeritFlaw.objects.get_or_create(
    name="Good Old Boy (or Girl)", ratings=[2], kinfolk=True
)[0]
MeritFlaw.objects.get_or_create(name="Outsider", ratings=[-2], kinfolk=True)[0]
MeritFlaw.objects.get_or_create(name="Fetish", ratings=[5, 6, 7], kinfolk=True)[0]
MeritFlaw.objects.get_or_create(name="Gnosis", ratings=[5, 6, 7], kinfolk=True)[0]
MeritFlaw.objects.get_or_create(name="Veiled", ratings=[-5], kinfolk=True)[0]

# M20
MeritFlaw.objects.get_or_create(
    name="Acute Sense (Mage)", ratings=[1, 3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Berserker (Mage)", ratings=[4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Dark Triad", ratings=[3], human=True, mage=True)[
    0
]
# MeritFlaw.objects.get_or_create(name="Language", ratings=[1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Stormwarden/Quantum Voyager", ratings=[3, 5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Ties", ratings=[3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Too Tough To Die", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="True Faith", ratings=[7], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Umbral Affinity", ratings=[4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Addiction (Mage)", ratings=[-1, -3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Construct", ratings=[-2], human=True, mage=True)[
    0
]
# MeritFlaw.objects.get_or_create(name="Cursed", ratings=[-1, -2, -3, -4, -5], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Deranged (Mage)", ratings=[-3, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Echoes (Mage)", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Enemy", ratings=[-1, -2, -3, -4, -5], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="PTSD", ratings=[-2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Stress Atavism", ratings=[-4], human=True, mage=True
)[0]

# Book of Secrets
MeritFlaw.objects.get_or_create(
    name="Alchohol/Drug Tolerance", ratings=[1, 2], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Ambidextrous", ratings=[1], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Animal Magnetism", ratings=[2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Artistically Gifted", ratings=[1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Avatar Companion", ratings=[7], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Bardic Gift", ratings=[2], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Burning Aura", ratings=[1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Cast-Iron Stomach", ratings=[1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Catlike Balance", ratings=[1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Celestial Affinity", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Circumspect Avatar", ratings=[2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Clear Sighted", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Cloak of the Seasons", ratings=[3], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Code of Honor", ratings=[2], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Common Sense", ratings=[1], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Computer Aptitude", ratings=[1], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Concentration", ratings=[1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Confidence", ratings=[2], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Cyclic Magick", ratings=[3, -3], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Danger Sense", ratings=[3], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Daredevil", ratings=[3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Deathwalker", ratings=[4], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Dual Affiliation", ratings=[7], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Eidetic Memory", ratings=[2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Enchanting Feature", ratings=[2], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Expert Driver", ratings=[1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Fae Blood", ratings=[4], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Faerie Affinity", ratings=[2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Family Support (Mage)", ratings=[1, 2, 3], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Favor", ratings=[1, 2, 3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Ghoul", ratings=[5], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Green Thumb", ratings=[1], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Guardian Angel", ratings=[6], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Hands of Daedalus", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Hideaway/Safehouse", ratings=[2, 4, 6], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Huge Size", ratings=[4], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Hyperflexible", ratings=[1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Hyperfocus", ratings=[3], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Hypersensitivity", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Immortal", ratings=[5, 7], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Inner Knight", ratings=[5], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Inner Strength", ratings=[2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Insensate to Pain", ratings=[5], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Iron Will", ratings=[3], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Jack-of-All-Trades", ratings=[3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Judge's Wisdom", ratings=[4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Legendary Attributes - Strength", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Legendary Attributes - Dexterity", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Legendary Attributes - Stamina", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Legendary Attributes - Charisma", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Legendary Attributes - Manipulation", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Legendary Attributes - Appearance", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Legendary Attributes - Perception", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Legendary Attributes - Intelligence", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Legendary Attributes - Wits", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Light Sleeper", ratings=[1], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Lightning Calculator", ratings=[1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Local Hero", ratings=[3], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Loyalty", ratings=[1], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Lucky", ratings=[3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Manifest Avatar", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Mark of Favor", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Master of Red Tape", ratings=[4], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Mechanical Aptitude", ratings=[1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Medium", ratings=[2], human=True, mage=True, changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Natural Channel", ratings=[3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Natural Leader (Mage)", ratings=[3], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Natural Linguist", ratings=[2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Natural Shapeshifter", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Nephilim/Laham", ratings=[7], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Nightsight (Mage)", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Nine Lives", ratings=[6], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Noble Blood", ratings=[1], human=True, mage=True)[
    0
]
# MeritFlaw.objects.get_or_create(name="Noted Messenger", ratings=[3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Officially Dead", ratings=[2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Oracular Ability", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Parlor Trick", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Perfect Liar", ratings=[2], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Physically Impressive", ratings=[2], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Pitiable", ratings=[1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Poison Resistance (Mage)", ratings=[2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Poker Face", ratings=[2], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Powerful Ally", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Prestige", ratings=[2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Property", ratings=[2, 3, 4, 5])[0]
MeritFlaw.objects.get_or_create(
    name="Regal Bearing", ratings=[1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Research Grant", ratings=[2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Rising Star", ratings=[3], human=True, mage=True, changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Sanctity", ratings=[2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Scientific Mystic/Techgnosi", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Secret Code Language", ratings=[2], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Self-Confident", ratings=[5], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Shapechanger Kin", ratings=[4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Shattered Avatar", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Socially Networked", ratings=[2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Spark of Life", ratings=[5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Natural - Correspondence", ratings=[6], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Natural - Time", ratings=[6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Natural - Spirit", ratings=[6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Natural - Life", ratings=[6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Natural - Matter", ratings=[6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Natural - Forces", ratings=[6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Natural - Entropy", ratings=[6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Natural - Prime", ratings=[6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Natural - Mind", ratings=[6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Spirit Magnet (Mage)", ratings=[3, 4, 5, 6, 7], human=True, mage=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Spirit Mentor", ratings=[3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Sterile", ratings=[1, -1], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Subculture Insider", ratings=[2], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Supernatural Companion", ratings=[3], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Time Sense", ratings=[1], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="True Love", ratings=[4], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Twin Souls", ratings=[4], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Unaging", ratings=[2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Unbondable", ratings=[4], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Unobtrusive", ratings=[1], human=True, mage=True)[
    0
]
# MeritFlaw.objects.get_or_create(name="Ability-Deficit", ratings=[-5], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Absent-Minded", ratings=[-3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Aging", ratings=[-2, -4, -6, -8, -10], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Amnesia", ratings=[-2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Anachronism", ratings=[-1, -2, -3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Apprentice", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Bard's Tongue", ratings=[-1], human=True, mage=True, changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Beast Within", ratings=[-5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Bedeviled", ratings=[-6], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Bigot", ratings=[-3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Bizarre Hunger", ratings=[-2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Blacklisted", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Blood Magick", ratings=[-5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Blood-Hungry Soul", ratings=[-2, -3, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Bound", ratings=[-5], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Branded", ratings=[-3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Cast No Shadow Or Reflection", ratings=[-1, -2], human=True, mage=True,
)[0]
MeritFlaw.objects.get_or_create(name="Catspaw", ratings=[-2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Child", ratings=[-1, -2, -3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Chronic Depression", ratings=[-3], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Compulsion", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Compulsive Speech", ratings=[-1, -2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Conflicting Loyalties", ratings=[-1, -2, -3], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Conniver", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Crucial Component", ratings=[-2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Cultural Other", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Curiosity", ratings=[-2], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Dark Fate", ratings=[-5], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Dark Secret", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Debts", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Degeneration", ratings=[-3, -6, -9], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Demented Eidolon", ratings=[-3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Devil's Mark", ratings=[-1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Diabolical Mentor", ratings=[-2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Discredited", ratings=[-1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Dogmatic", ratings=[-2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Double Agent", ratings=[-2], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Driving Goal", ratings=[-3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Easily Intoxicated", ratings=[-2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Echo Chamber", ratings=[-4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Esoteric Discourse/Technobabbler", ratings=[-1], human=True, mage=True,
)[0]
MeritFlaw.objects.get_or_create(name="Expendable", ratings=[-3], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Extreme Kink", ratings=[-3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Failure", ratings=[-2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Faithless", ratings=[-5], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Family Issues", ratings=[-1, -2, -3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Faulty Enhancements", ratings=[-2, -3, -4, -5], human=True, mage=True,
)[0]
MeritFlaw.objects.get_or_create(name="Feral Mind", ratings=[-3], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Fifth Degree", ratings=[-3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Flashbacks (Mage and Changeling)",
    ratings=[-3],
    human=True,
    mage=True,
    changeling=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Gremlin", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Gullible", ratings=[-2], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Hatred", ratings=[-3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Haunted", ratings=[-3], human=True, mage=True, changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Hero Worship", ratings=[-1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Hit List", ratings=[-4], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Horrific", ratings=[-5], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Icy", ratings=[-2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Immortal Enemy", ratings=[-5, -6, -7, -8], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Impatient", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Impediment", ratings=[-1, -2, -3, -4, -5, -6], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Inappropriate", ratings=[-1, -2, -3, -4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Infamy", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Insane/Infamous Mentor", ratings=[-1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Intemperate", ratings=[-2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Jinx/Infernal Contraption",
    ratings=[-2, -3, -4, -5, -6, -7, -8, -9, -10],
    human=True,
    mage=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Lifesaver", ratings=[-3], human=True, mage=True, changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Locked Vidare", ratings=[-1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Mayfly Curse", ratings=[-5, -10], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Mental Lock", ratings=[-1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Mistaken Identity", ratings=[-1], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Monstrous", ratings=[-3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Mr. Red Tape", ratings=[-4], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Naive", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Narc", ratings=[-3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="New Kid", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Nightmares (Mage)", ratings=[-1, -3], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Notoriety", ratings=[-3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Oathbreaker", ratings=[-4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Obsession", ratings=[-2], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(name="OCPD", ratings=[-3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Offline", ratings=[-1, -3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Old Flame", ratings=[-2], human=True, mage=True)[
    0
]
# MeritFlaw.objects.get_or_create(name="Overconfident", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Overextended", ratings=[-4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Paranormal Prohibition or Imperative",
    ratings=[-2, -3, -4, -5, -6, -7, -8],
    human=True,
    mage=True,
)[0]
MeritFlaw.objects.get_or_create(
    name="Permanent Paradox Flaw", ratings=[-2, -4, -6], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Permanent Wound", ratings=[-3], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Phobia", ratings=[-2, -3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Phylactery", ratings=[-7], human=True, mage=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Primal Marks", ratings=[-3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Probationary Member", ratings=[-4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Profiled Appearance", ratings=[-2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Prone to Quiet", ratings=[-4], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Psychic Vampire", ratings=[-5], human=True, mage=True, changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Repulsive Feature", ratings=[-2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Rival House", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Rivalry", ratings=[-3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Rogue", ratings=[-4], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Rose-Colored Glasses", ratings=[-2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Rotten Liar", ratings=[-3], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sect Enmity", ratings=[-1], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Short Fuse", ratings=[-2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Short (Mage)", ratings=[-3], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Shy", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Sleeping with the Enemy", ratings=[-3], human=True, mage=True, changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Soft-Hearted", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Special Responsibility", ratings=[-1], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Speech Impediment", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Inept - Correspondence", ratings=[-6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Inept - Spirit", ratings=[-6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Inept - Time", ratings=[-6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Inept - Life", ratings=[-6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Inept - Forces", ratings=[-6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Inept - Matter", ratings=[-6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Inept - Mind", ratings=[-6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Inept - Entropy", ratings=[-6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sphere Inept - Prime", ratings=[-6], human=False, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Strangeness", ratings=[-1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Sympathizer", ratings=[-1], human=True, mage=True
)[0]
# MeritFlaw.objects.get_or_create(name="Taint of Corruption", ratings=[-7], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Throwback", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Troublemaker", ratings=[-2], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Twisted Apprenticeship", ratings=[-1], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Uncanny", ratings=[-1, -2, -3, -4, -5], human=True, mage=True
)[0]
MeritFlaw.objects.get_or_create(name="Vanilla", ratings=[-1], human=True, mage=True)[0]
# MeritFlaw.objects.get_or_create(name="Vengeful", ratings=[-2], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Vulnerability", ratings=[-1, -2, -3, -4, -5, -6, -7], human=True, mage=True,
)[0]
# MeritFlaw.objects.get_or_create(name="Ward", ratings=[-3], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(name="Whimsy", ratings=[-1], human=True, mage=True)[0]
MeritFlaw.objects.get_or_create(
    name="Witch-Hunted", ratings=[-4], human=True, mage=True
)[0]

# Book of the Fallen
MeritFlaw.objects.get_or_create(
    name="Shadow Appeal", ratings=[3], human=True, mage=True
)[0].add_source("Book of the Fallen", 117)
MeritFlaw.objects.get_or_create(
    name="Innocuous Aura", ratings=[5], human=True, mage=True
)[0].add_source("Book of the Fallen", 117)
MeritFlaw.objects.get_or_create(
    name="Abyssal Mastery", ratings=[7], human=True, mage=True
)[0].add_source("Book of the Fallen", 117)
MeritFlaw.objects.get_or_create(
    name="Saint of the Pit", ratings=[3], human=True, mage=True
)[0].add_source("Book of the Fallen", 118)
MeritFlaw.objects.get_or_create(
    name="Qlippothic Radiance", ratings=[-1, -2, -3, -4, -5], human=True, mage=True,
)[0].add_source("Book of the Fallen", 119)
MeritFlaw.objects.get_or_create(
    name="Spectral Presence", ratings=[-3], human=True, mage=True
)[0].add_source("Book of the Fallen", 119)
MeritFlaw.objects.get_or_create(
    name="Abyssal Lunatic", ratings=[-5], human=True, mage=True
)[0].add_source("Book of the Fallen", 119)
MeritFlaw.objects.get_or_create(
    name="Widderslainte", ratings=[-7], human=True, mage=True
)[0].add_source("Book of the Fallen", 120)

# C20
MeritFlaw.objects.get_or_create(name="Friendly Face", ratings=[1], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Poison Resistance (Changeling)", ratings=[1], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Wheelman", ratings=[1], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Crack Shot", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Dextrous Toes", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Granite Skin", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Murderous Mien", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Nightsight (Changeling)", ratings=[2], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Surreal Beauty", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Increased Pain Threshold", ratings=[3], changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Perfect Balance (Changeling)", ratings=[3], changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Prehensile Tongue/Tail", ratings=[2, 4], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Sex Appeal", ratings=[3], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Huge Size", ratings=[4], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Eidetic Taste", ratings=[4], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Blessing of Atlas", ratings=[5], changeling=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Addiction (Changeling)", ratings=[-1, -2, -3], changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Allergic", ratings=[-1, -2, -3, -4], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Asthma", ratings=[-1], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Bad Sight (Changeling)", ratings=[-1, -3, -6], changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Impaired Hearing", ratings=[-1, -2, -4], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Short", ratings=[-1], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Twitch", ratings=[-1], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Deformed", ratings=[-2, -3], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Too Human", ratings=[-2, -5], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Lame", ratings=[-3], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Parfum de Goat", ratings=[-5], changeling=True)[0]

# MeritFlaw.objects.get_or_create(name="Common Sense", ratings=[1], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Concentration", ratings=[1], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Higher Purpose", ratings=[1], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Introspection", ratings=[1], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Language", ratings=[1], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Lightning Calculator", ratings=[1], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Mechanical Aptitude", ratings=[1], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Specific Interests", ratings=[1], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Eidetic Memory", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Loyal Heart", ratings=[2], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Natural Linguist", ratings=[2], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Iron Will", ratings=[3], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Master Crafsman", ratings=[3], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Gut Instincts", ratings=[4], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Jack-of-all-Trades (Changeling)", ratings=[5], changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Beacuse I Think I Can", ratings=[6], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Impatient", ratings=[-1], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Nightmares", ratings=[-1], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Amnesia", ratings=[-2], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Curiosity", ratings=[-2], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Phobia (Changeling)", ratings=[-2, -4], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Short Fuse", ratings=[-2], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Soft-Hearted (Changeling)", ratings=[-2], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Vengeful", ratings=[-2], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Wyld Mind", ratings=[-2], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Absent-Minded", ratings=[-3], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Flashbacks", ratings=[-3], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Lifesaver", ratings=[-3], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Weak-Willed", ratings=[-3], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Guilt-Wracked", ratings=[-4], changeling=True)[0]

MeritFlaw.objects.get_or_create(name="Benevolent Patron", ratings=[1], changeling=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Boon", ratings=[1, 2, 3, 4, 5, 6], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Calming Presence", ratings=[1], changeling=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Good Listener", ratings=[1], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="I Know You", ratings=[1], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Natural Leader (Changeling)", ratings=[1], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Protege", ratings=[1], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Your Best Advocate", ratings=[1], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Nature's Child", ratings=[2], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Reputation", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Scholar of Others", ratings=[2], changeling=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Voice of A Songbird", ratings=[2], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Sage", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Heir to the Throne", ratings=[3], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Fake It", ratings=[3], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Rising Star", ratings=[3], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Soul of the Muse", ratings=[4], changeling=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Trusty Companion", ratings=[4], changeling=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Dangerous Mentor", ratings=[-1], changeling=True)[
    0
]
# MeritFlaw.objects.get_or_create(name="Dark Secret", ratings=[-1], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Enemy", ratings=[-1, -2, -3, -4, -5], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Insubordinate", ratings=[-1], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Intolerance (Changeling)", ratings=[-2], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Foul Mouth", ratings=[-2], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Possessive", ratings=[-2], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Shrinking Violet", ratings=[-2], changeling=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Fallen Noble", ratings=[-3], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Recruitment Target", ratings=[-3], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Sleeping With the Enemy", ratings=[-3], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Ward", ratings=[-3], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Indecisive", ratings=[-3], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Hunted (Changeling)", ratings=[-4, -5], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="On Probation", ratings=[-4], changeling=True)[0]

MeritFlaw.objects.get_or_create(name="Faerie Eternity", ratings=[1], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="True Love (Changeling)", ratings=[1], changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Danger Sense (Changeling)", ratings=[2], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Medium", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Poetic Heart", ratings=[2], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Animalistic Favor", ratings=[3, 4, 5], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Lucky", ratings=[3], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Blood of the Wolf", ratings=[4], changeling=True)[
    0
]
MeritFlaw.objects.get_or_create(name="Iron Resistance", ratings=[4], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Art Affinity", ratings=[5], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Living Legend", ratings=[5], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Regeneration", ratings=[7], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Bard's Tongue", ratings=[-1], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Changeling's Eyes", ratings=[-1], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Cursed", ratings=[-1, -2, -3, -4, -5], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Geas", ratings=[-1, -2, -3, -4, -5], changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Oathbound", ratings=[-1, -2, -3, -4, -5], changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Slipped Seeming", ratings=[-1, -2, -3, -4, -5], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Bizarre Quality", ratings=[-2], changeling=True)[
    0
]
MeritFlaw.objects.get_or_create(
    name="Echoes (Changeling)", ratings=[-2, -3, -4, -5], changeling=True
)[0]
MeritFlaw.objects.get_or_create(name="Winged", ratings=[-2, 4], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Cleared Mists", ratings=[-3], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Haunted", ratings=[-3], changeling=True)[0]
MeritFlaw.objects.get_or_create(
    name="Iron Allergy", ratings=[-3, -4, -5], changeling=True
)[0]
MeritFlaw.objects.get_or_create(
    name="Chimerical Magnet", ratings=[-5], changeling=True
)[0]
# MeritFlaw.objects.get_or_create(name="Dark Fate", ratings=[-5], changeling=True)[0]
# MeritFlaw.objects.get_or_create(name="Psychic Vampire", ratings=[-5], changeling=True)[0]
MeritFlaw.objects.get_or_create(name="Sidhe's Curse", ratings=[-5], changeling=True)[0]

Derangement.objects.get_or_create(name="Fugue")[0]
Derangement.objects.get_or_create(name="Hysteria")[0]
Derangement.objects.get_or_create(name="Multiple Personalities")[0]
Derangement.objects.get_or_create(name="Obsessive-Compulsive")[0]
Derangement.objects.get_or_create(name="Paranoia")[0]
Derangement.objects.get_or_create(name="Schizophrenia")[0]

MeleeWeapon.objects.get_or_create(
    name="Sap", difficulty=4, damage=0, damage_type="B", conceal="P", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Whip", difficulty=6, damage=1, damage_type="L", conceal="J", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Spiked Gauntlet",
    difficulty=6,
    damage=1,
    damage_type="L",
    conceal="J",
    display=False,
)[0]
MeleeWeapon.objects.get_or_create(
    name="Broken Bottle",
    difficulty=6,
    damage=1,
    damage_type="L",
    conceal="P",
    display=False,
)[0]
MeleeWeapon.objects.get_or_create(
    name="Chair", difficulty=7, damage=2, damage_type="B", conceal="N", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Table", difficulty=8, damage=3, damage_type="B", conceal="N", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Chain", difficulty=5, damage=0, damage_type="B", conceal="J", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Staff", difficulty=5, damage=1, damage_type="B", conceal="N", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Mace", difficulty=6, damage=2, damage_type="L", conceal="N", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Baseball Bat",
    difficulty=5,
    damage=2,
    damage_type="B",
    conceal="T",
    display=False,
)[0]
MeleeWeapon.objects.get_or_create(
    name="Spiked Club",
    difficulty=6,
    damage=2,
    damage_type="L",
    conceal="T",
    display=False,
)[0]
MeleeWeapon.objects.get_or_create(
    name="Huge Spiked Club",
    difficulty=7,
    damage=4,
    damage_type="L",
    conceal="N",
    display=False,
)[0]
MeleeWeapon.objects.get_or_create(
    name="Knife", difficulty=4, damage=1, damage_type="L", conceal="P", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Sword", difficulty=6, damage=2, damage_type="L", conceal="T", display=False
)[0]
# MeleeWeapon.objects.get_or_create(name="Klaive", difficulty=6, damage=2, damage_type="A", conceal="J", display=False)[0]
# MeleeWeapon.objects.get_or_create(name="Grand Klaive", difficulty=7, damage=5, damage_type="A", conceal="T", display=False)[0]
MeleeWeapon.objects.get_or_create(
    name="Great Sword",
    difficulty=7,
    damage=6,
    damage_type="L",
    conceal="N",
    display=False,
)[0]
MeleeWeapon.objects.get_or_create(
    name="Axe", difficulty=7, damage=3, damage_type="L", conceal="T", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Great Axe",
    difficulty=7,
    damage=6,
    damage_type="L",
    conceal="N",
    display=False,
)[0]
MeleeWeapon.objects.get_or_create(
    name="Polearm", difficulty=7, damage=3, damage_type="L", conceal="N", display=False
)[0]
MeleeWeapon.objects.get_or_create(
    name="Chainsaw", difficulty=8, damage=7, damage_type="L", conceal="N", display=False
)[0]


ThrownWeapon.objects.get_or_create(
    name="Throwing Knife",
    difficulty=6,
    damage=0,
    damage_type="L",
    conceal="P",
    display=False,
)[0]
ThrownWeapon.objects.get_or_create(
    name="Shuriken", difficulty=7, damage=3, damage_type="L", conceal="P", display=False
)[0]
ThrownWeapon.objects.get_or_create(
    name="Spear", difficulty=6, damage=1, damage_type="L", conceal="N", display=False
)[0]
ThrownWeapon.objects.get_or_create(
    name="Stone", difficulty=5, damage=0, damage_type="B", conceal="N", display=False
)[0]
ThrownWeapon.objects.get_or_create(
    name="Stone, head-sized",
    difficulty=6,
    damage=3,
    damage_type="B",
    conceal="N",
    display=False,
)[0]
ThrownWeapon.objects.get_or_create(
    name="Tomahawk", difficulty=6, damage=1, damage_type="L", conceal="J", display=False
)[0]

RangedWeapon.objects.get_or_create(
    name="Revolver, Lt.", damage=4, range=12, rate=3, clip=6, conceal="P", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="Revolver, Hvy.",
    damage=6,
    range=35,
    rate=2,
    clip=6,
    conceal="J",
    display=False,
)[0]
RangedWeapon.objects.get_or_create(
    name="Semi-Automatic Pistol, Lt.",
    damage=4,
    range=20,
    rate=4,
    clip=18,
    conceal="P",
    display=False,
)[0]
RangedWeapon.objects.get_or_create(
    name="Semi-Automatic Pistol, Hvy.",
    damage=5,
    range=25,
    rate=3,
    clip=14,
    conceal="J",
    display=False,
)[0]
RangedWeapon.objects.get_or_create(
    name="Rifle", damage=8, range=200, rate=1, clip=6, conceal="N", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="SMG, Small", damage=4, range=25, rate=3, clip=31, conceal="J", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="SMG, Large", damage=4, range=50, rate=3, clip=31, conceal="T", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="Assault Rifle",
    damage=7,
    range=150,
    rate=3,
    clip=31,
    conceal="N",
    display=False,
)[0]
RangedWeapon.objects.get_or_create(
    name="Shotgun, Sawed-Off",
    damage=8,
    range=10,
    rate=2,
    clip=2,
    conceal="J",
    display=False,
)[0]
RangedWeapon.objects.get_or_create(
    name="Shotgun", damage=8, range=20, rate=1, clip=6, conceal="T", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="Shotgun, Semi-Automatic",
    damage=8,
    range=25,
    rate=3,
    clip=7,
    conceal="T",
    display=False,
)[0]
RangedWeapon.objects.get_or_create(
    name="Shotgun, Assault",
    damage=8,
    range=50,
    rate=0,
    clip=33,
    conceal="N",
    display=False,
)[0]
RangedWeapon.objects.get_or_create(
    name="Short Bow", damage=4, range=60, rate=1, clip=1, conceal="N", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="Hunting Bow", damage=5, range=100, rate=1, clip=1, conceal="N", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="Long Bow", damage=5, range=120, rate=1, clip=1, conceal="N", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="Crossbow, Commando",
    damage=3,
    range=20,
    rate=1,
    clip=1,
    conceal="J",
    display=False,
)[0]
RangedWeapon.objects.get_or_create(
    name="Crossbow", damage=5, range=90, rate=1, clip=1, conceal="T", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="Crossbow, Hvy.",
    damage=6,
    range=100,
    rate=1,
    clip=1,
    conceal="N",
    display=False,
)[0]
RangedWeapon.objects.get_or_create(
    name="Taser", damage=5, range=5, rate=1, clip=1, conceal="P", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="Tear Gas", damage=3, range=3, rate=1, clip=5, conceal="P", display=False
)[0]
RangedWeapon.objects.get_or_create(
    name="Bear Mace", damage=4, range=3, rate=1, clip=3, conceal="P", display=False
)[0]

ObjectType.objects.get_or_create(
    name="City", type="loc", system="wod", gameline="World of Darkness"
)[0]
ObjectType.objects.get_or_create(
    name="Location", type="loc", system="wod", gameline="World of Darkness"
)[0]
