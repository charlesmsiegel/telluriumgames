from time import time

from cod.models.characters.mage import Legacy, Order, Path, ProximiFamily, Rote
from cod.models.characters.mortal import Merit, Specialty
from core.models import Language

SKILLS = [
    "Academics",
    "Computer",
    "Crafts",
    "Investigation",
    "Medicine",
    "Occult",
    "Politics",
    "Science",
    "Athletics",
    "Brawl",
    "Drive",
    "Firearms",
    "Larceny",
    "Stealth",
    "Survival",
    "Weaponry",
    "Animal Ken",
    "Empathy",
    "Expression",
    "Intimidation",
    "Persuasion",
    "Socialize",
    "Streetwise",
    "Subterfuge",
]

Specialty.objects.create(skill="academics", name="English Literature")
Specialty.objects.create(skill="academics", name="History")
Specialty.objects.create(skill="academics", name="Law")
Specialty.objects.create(skill="academics", name="Linguistics")
Specialty.objects.create(skill="academics", name="Research")
Specialty.objects.create(skill="academics", name="Anthropology")
Specialty.objects.create(skill="academics", name="Art History")
Specialty.objects.create(skill="academics", name="Literature")
Specialty.objects.create(skill="academics", name="Religion")
Specialty.objects.create(skill="academics", name="Translation")
Specialty.objects.create(skill="computer", name="Data Retrieval")
Specialty.objects.create(skill="computer", name="Digital Security")
Specialty.objects.create(skill="computer", name="Hacking")
Specialty.objects.create(skill="computer", name="Programming")
Specialty.objects.create(skill="computer", name="User Interface Design")
Specialty.objects.create(skill="computer", name="Graphics")
Specialty.objects.create(skill="computer", name="Internet")
Specialty.objects.create(skill="computer", name="Security")
Specialty.objects.create(skill="computer", name="Social Media")
Specialty.objects.create(skill="crafts", name="Automotive")
Specialty.objects.create(skill="crafts", name="Carpentry")
Specialty.objects.create(skill="crafts", name="Jury Rigging")
Specialty.objects.create(skill="crafts", name="Sculpting")
Specialty.objects.create(skill="crafts", name="Welding")
Specialty.objects.create(skill="crafts", name="Cosmetics")
Specialty.objects.create(skill="crafts", name="Fashion")
Specialty.objects.create(skill="crafts", name="Forging")
Specialty.objects.create(skill="crafts", name="Graffiti")
Specialty.objects.create(skill="crafts", name="Painting")
Specialty.objects.create(skill="crafts", name="Perfumery")
Specialty.objects.create(skill="crafts", name="Repair")
Specialty.objects.create(skill="crafts", name="Sculpting")
Specialty.objects.create(skill="investigation", name="Crime Scenes")
Specialty.objects.create(skill="investigation", name="Cryptography")
Specialty.objects.create(skill="investigation", name="Dreams")
Specialty.objects.create(skill="investigation", name="Forensic Accounting")
Specialty.objects.create(skill="investigation", name="Riddles")
Specialty.objects.create(skill="investigation", name="Artifacts")
Specialty.objects.create(skill="investigation", name="Autopsy")
Specialty.objects.create(skill="investigation", name="Body Language")
Specialty.objects.create(skill="investigation", name="Lab Work")
Specialty.objects.create(skill="medicine", name="Cardiology")
Specialty.objects.create(skill="medicine", name="First Aid")
Specialty.objects.create(skill="medicine", name="Pathology")
Specialty.objects.create(skill="medicine", name="Pharmacology")
Specialty.objects.create(skill="medicine", name="Surgery")
Specialty.objects.create(skill="medicine", name="Physical Therapy")
Specialty.objects.create(skill="occult", name="Eastern European Folktales")
Specialty.objects.create(skill="occult", name="Ghosts")
Specialty.objects.create(skill="occult", name="Mothman Sightings")
Specialty.objects.create(skill="occult", name="Psychic Phenomena")
Specialty.objects.create(skill="occult", name="Urban Legends")
Specialty.objects.create(skill="occult", name="The Astral Realm")
Specialty.objects.create(skill="occult", name="Casting Lots")
Specialty.objects.create(skill="occult", name="Cryptids")
Specialty.objects.create(skill="occult", name="Fortean Phenomena")
Specialty.objects.create(skill="occult", name="Proximi")
Specialty.objects.create(skill="occult", name="Sleepwalkers")
Specialty.objects.create(skill="occult", name="Goetia")
Specialty.objects.create(skill="occult", name="Phrenology")
Specialty.objects.create(skill="occult", name="Spirits")
Specialty.objects.create(skill="occult", name="Superstition")
Specialty.objects.create(skill="politics", name="Bureaucracy")
Specialty.objects.create(skill="politics", name="Local Politics")
Specialty.objects.create(skill="politics", name="National Politics")
Specialty.objects.create(skill="politics", name="Scandals")
Specialty.objects.create(skill="politics", name="Specific Political Party")
Specialty.objects.create(skill="politics", name="Church")
Specialty.objects.create(skill="politics", name="Consilium")
Specialty.objects.create(skill="politics", name="Democratic")
Specialty.objects.create(skill="politics", name="Local")
Specialty.objects.create(skill="politics", name="Order")
Specialty.objects.create(skill="politics", name="Organized Crime")
Specialty.objects.create(skill="science", name="Biology")
Specialty.objects.create(skill="science", name="Chemistry")
Specialty.objects.create(skill="science", name="Genetics")
Specialty.objects.create(skill="science", name="Optics")
Specialty.objects.create(skill="science", name="Particle Physics")
Specialty.objects.create(skill="science", name="Physics")
Specialty.objects.create(skill="science", name="Neuroscience")
Specialty.objects.create(skill="science", name="Virology")
Specialty.objects.create(skill="science", name="Alchemy")
Specialty.objects.create(skill="science", name="Hematology")
Specialty.objects.create(skill="athletics", name="Acrobatics")
Specialty.objects.create(skill="athletics", name="Basketball")
Specialty.objects.create(skill="athletics", name="Marathon Running")
Specialty.objects.create(skill="athletics", name="Rock Climbing")
Specialty.objects.create(skill="athletics", name="Throwing")
Specialty.objects.create(skill="athletics", name="Aimed Spells")
Specialty.objects.create(skill="athletics", name="Archery")
Specialty.objects.create(skill="athletics", name="Climbing")
Specialty.objects.create(skill="athletics", name="Jumping")
Specialty.objects.create(skill="athletics", name="Parkour")
Specialty.objects.create(skill="athletics", name="Swimming")
Specialty.objects.create(skill="brawl", name="Blocking")
Specialty.objects.create(skill="brawl", name="Boxing")
Specialty.objects.create(skill="brawl", name="Grappling")
Specialty.objects.create(skill="brawl", name="Muay Thai")
Specialty.objects.create(skill="brawl", name="Throws")
Specialty.objects.create(skill="brawl", name="Biting")
Specialty.objects.create(skill="brawl", name="Claws")
Specialty.objects.create(skill="brawl", name="Dirty Fighting")
Specialty.objects.create(skill="brawl", name="Martial Arts")
Specialty.objects.create(skill="brawl", name="Threats")
Specialty.objects.create(skill="drive", name="Evasion")
Specialty.objects.create(skill="drive", name="Motorcycles")
Specialty.objects.create(skill="drive", name="Piloting")
Specialty.objects.create(skill="drive", name="Racing")
Specialty.objects.create(skill="drive", name="Stunts")
Specialty.objects.create(skill="drive", name="Defensive Driving")
Specialty.objects.create(skill="drive", name="Off-Road Driving")
Specialty.objects.create(skill="drive", name="Pursuit")
Specialty.objects.create(skill="firearms", name="Fast-Draw")
Specialty.objects.create(skill="firearms", name="Handguns")
Specialty.objects.create(skill="firearms", name="Rifles")
Specialty.objects.create(skill="firearms", name="Shotguns")
Specialty.objects.create(skill="firearms", name="Sniping")
Specialty.objects.create(skill="firearms", name="Trick Shots")
Specialty.objects.create(skill="larceny", name="Alarm Systems")
Specialty.objects.create(skill="larceny", name="Breaking and Entering")
Specialty.objects.create(skill="larceny", name="Lock Picking")
Specialty.objects.create(skill="larceny", name="Safecracking")
Specialty.objects.create(skill="larceny", name="Sleight of Hand")
Specialty.objects.create(skill="larceny", name="Concealment")
Specialty.objects.create(skill="larceny", name="Pickpocketing")
Specialty.objects.create(skill="larceny", name="Security Systems")
Specialty.objects.create(skill="stealth", name="Crowds")
Specialty.objects.create(skill="stealth", name="Hiding")
Specialty.objects.create(skill="stealth", name="Moving Quietly")
Specialty.objects.create(skill="stealth", name="Shadowing")
Specialty.objects.create(skill="stealth", name="Stakeouts")
Specialty.objects.create(skill="stealth", name="Camouflage")
Specialty.objects.create(skill="stealth", name="In Plain Sight")
Specialty.objects.create(skill="stealth", name="Rural")
Specialty.objects.create(skill="stealth", name="Staying Motionless")
Specialty.objects.create(skill="survival", name="Foraging")
Specialty.objects.create(skill="survival", name="Hunting")
Specialty.objects.create(skill="survival", name="Navigation")
Specialty.objects.create(skill="survival", name="Shelter")
Specialty.objects.create(skill="survival", name="Weather")
Specialty.objects.create(skill="weaponry", name="Clubs")
Specialty.objects.create(skill="weaponry", name="Duels")
Specialty.objects.create(skill="weaponry", name="Improvised Weapons")
Specialty.objects.create(skill="weaponry", name="Knives")
Specialty.objects.create(skill="weaponry", name="Swords")
Specialty.objects.create(skill="weaponry", name="Chains")
Specialty.objects.create(skill="weaponry", name="Spears")
Specialty.objects.create(skill="animal_ken", name="Dogs")
Specialty.objects.create(skill="animal_ken", name="Exotic Pets")
Specialty.objects.create(skill="animal_ken", name="Horses")
Specialty.objects.create(skill="animal_ken", name="Training")
Specialty.objects.create(skill="animal_ken", name="Wild Animals")
Specialty.objects.create(skill="animal_ken", name="Cats")
Specialty.objects.create(skill="animal_ken", name="Reptiles")
Specialty.objects.create(skill="animal_ken", name="Soothing")
Specialty.objects.create(skill="animal_ken", name="Threatening")
Specialty.objects.create(skill="empathy", name="Buried Feelings")
Specialty.objects.create(skill="empathy", name="Calming")
Specialty.objects.create(skill="empathy", name="Emotions")
Specialty.objects.create(skill="empathy", name="Lies")
Specialty.objects.create(skill="empathy", name="Motives")
Specialty.objects.create(skill="empathy", name="Personalities")
Specialty.objects.create(skill="expression", name="Dance")
Specialty.objects.create(skill="expression", name="Journalism")
Specialty.objects.create(skill="expression", name="Music Composition")
Specialty.objects.create(skill="expression", name="Painting")
Specialty.objects.create(skill="expression", name="Speeches")
Specialty.objects.create(skill="expression", name="Drama")
Specialty.objects.create(skill="expression", name="Musical Instrument")
Specialty.objects.create(skill="expression", name="Performance Art")
Specialty.objects.create(skill="expression", name="Singing")
Specialty.objects.create(skill="intimidation", name="Direct Threats")
Specialty.objects.create(skill="intimidation", name="Interrogation")
Specialty.objects.create(skill="intimidation", name="Murderous Stare")
Specialty.objects.create(skill="intimidation", name="Torture")
Specialty.objects.create(skill="intimidation", name="Veiled Threats")
Specialty.objects.create(skill="intimidation", name="Stare Down")
Specialty.objects.create(skill="persuasion", name="Fast Talking")
Specialty.objects.create(skill="persuasion", name="Inspiring")
Specialty.objects.create(skill="persuasion", name="Sales Pitches")
Specialty.objects.create(skill="persuasion", name="Seduction")
Specialty.objects.create(skill="persuasion", name="Sermons")
Specialty.objects.create(skill="persuasion", name="Confidence Scam")
Specialty.objects.create(skill="socialize", name="Bar hopping")
Specialty.objects.create(skill="socialize", name="College parties")
Specialty.objects.create(skill="socialize", name="Formal events")
Specialty.objects.create(skill="socialize", name="Political Fundraisers")
Specialty.objects.create(skill="socialize", name="Private clubs")
Specialty.objects.create(skill="socialize", name="Church Lock-In")
Specialty.objects.create(skill="socialize", name="Dress Balls")
Specialty.objects.create(skill="socialize", name="Frat Parties")
Specialty.objects.create(skill="socialize", name="The Club")
Specialty.objects.create(skill="streetwise", name="Black market")
Specialty.objects.create(skill="streetwise", name="Gangs")
Specialty.objects.create(skill="streetwise", name="Navigation")
Specialty.objects.create(skill="streetwise", name="Rumors")
Specialty.objects.create(skill="streetwise", name="Undercover work")
Specialty.objects.create(skill="subterfuge", name="Detecting lies")
Specialty.objects.create(skill="subterfuge", name="Hidden meanings")
Specialty.objects.create(skill="subterfuge", name="Hiding emotions")
Specialty.objects.create(skill="subterfuge", name="Long cons")
Specialty.objects.create(skill="subterfuge", name="Misdirection")
Specialty.objects.create(skill="subterfuge", name="Doublespeak")
Specialty.objects.create(skill="subterfuge", name="Little White Lies")

Merit.objects.create(
    name="Area of Expertise",
    requires_detail=True,
    ratings=[1],
    prereqs=[[("resolve", 2)]],
    merit_type="Mental",
    possible_details=[],
)
Merit.objects.create(
    name="Common Sense", ratings=[3], merit_type="Mental",
)
Merit.objects.create(
    name="Danger Sense", ratings=[2], merit_type="Mental",
)
Merit.objects.create(
    name="Direction Sense", ratings=[1], merit_type="Mental",
)
Merit.objects.create(
    name="Eidetic Memory", ratings=[2], merit_type="Mental",
)
Merit.objects.create(
    name="Encyclopedia Knowledge",
    requires_detail=True,
    ratings=[2],
    possible_details=SKILLS,
    merit_type="Mental",
)
Merit.objects.create(
    name="Eye for the Strange",
    ratings=[2],
    prereqs=[[("resolve", 2), ("occult", 1)]],
    merit_type="Mental",
)
Merit.objects.create(
    name="Fast Reflexes",
    ratings=[1, 2, 3],
    prereqs=[[("wits", 3)], [("dexterity", 3)]],
    merit_type="Mental",
)
Merit.objects.create(
    name="Good Time Management",
    ratings=[1],
    prereqs=[[("academics", 2)]],
    merit_type="Mental",
)
Merit.objects.create(
    name="Good Time Management",
    ratings=[1],
    prereqs=[[("science", 2)]],
    merit_type="Mental",
)
Merit.objects.create(
    name="Holistic Awareness", ratings=[1], merit_type="Mental",
)
Merit.objects.create(
    name="Indomitable", ratings=[2], merit_type="Mental",
)
Merit.objects.create(
    name="Interdisciplinary Specialty",
    requires_detail=True,
    ratings=[1],
    prereqs=[[("specialty", 3)]],
    possible_details=[],
    merit_type="Mental",
)
Merit.objects.create(
    name="Investigative Aide",
    requires_detail=True,
    ratings=[1],
    prereqs=[[("skill", 3)]],
    possible_details=[],
    merit_type="Mental",
)
Merit.objects.create(
    name="Language",
    requires_detail=True,
    ratings=[1],
    possible_details=[x.name for x in Language.objects.all()],
    merit_type="Mental",
)
Merit.objects.create(
    name="Library",
    requires_detail=True,
    ratings=[1, 2, 3],
    possible_details=[
        "Academics",
        "Computer",
        "Crafts",
        "Investigation",
        "Medicine",
        "Occult",
        "Politics",
        "Science",
    ],
    merit_type="Mental",
)
Merit.objects.create(
    name="Library, Advanced",
    ratings=[1, 2, 3],
    prereqs=[[("Library", 3), ("Safe Place", 1)]],
    merit_type="Mental",
)
Merit.objects.create(
    name="Meditative Mind", ratings=[1, 2, 4], merit_type="Mental",
)
Merit.objects.create(
    name="Multilingual",
    requires_detail=True,
    ratings=[1],
    possible_details=[],
    merit_type="Mental",
)
Merit.objects.create(
    name="Patient", ratings=[1], merit_type="Mental",
)
Merit.objects.create(
    name="Professional Training",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[
        "Academic (Academics, Science)",
        "Artist (Crafts, Expression)",
        "Athlete (Athletics, Medicine)",
        "Cop (Streetwise, Firearms)",
        "Criminal (Larceny, Streetwise)",
        "Detective (Empathy, Investigation)",
        "Doctor (Empathy, Medicine)",
        "Engineer (Crafts, Science)",
        "Hacker (Computer, Science)",
        "Hit Man (Firearms, Stealth)",
        "Journalist (Expression, Investigation)",
        "Laborer (Athletics, Crafts)",
        "Occultist (Investigation, Occult)",
        "Politician (Politics, Subterfuge)",
        "Professional (Academics, Persuasion)",
        "Religious Leader (Academics, Occult)",
        "Scientist (Investigation, Science)",
        "Socialite (Politics, Socialize)",
        "Stuntman (Athletics, Drive)",
        "Survivalist (Animal Ken, Survival)",
        "Soldier (Firearms, Survival)",
        "Technician (Crafts, Investigation)",
        "Thug (Brawl, Intimidation)",
        "Vagrant (Streetwise, Survival)",
    ],
    merit_type="Mental",
)
Merit.objects.create(
    name="Tolerance for Biology",
    ratings=[1],
    prereqs=[[("resolve", 3)]],
    merit_type="Mental",
)
Merit.objects.create(
    name="Trained Observer",
    ratings=[1, 3],
    prereqs=[[("wits", 3)], [("composure", 3)]],
    merit_type="Mental",
)
Merit.objects.create(
    name="Vice-Ridden", ratings=[2], merit_type="Mental",
)
Merit.objects.create(
    name="Virtuous", ratings=[2], merit_type="Mental",
)
Merit.objects.create(
    name="Ambidextrous", ratings=[3], merit_type="Physical",
)
Merit.objects.create(
    name="Automotive Genius",
    ratings=[1],
    prereqs=[[("crafts", 3), ("drive", 1), ("science", 1)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Crack Driver",
    ratings=[2, 3],
    prereqs=[[("drive", 3)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Demolisher",
    ratings=[1, 2, 3],
    prereqs=[[("strength", 3)], [("intelligence", 3)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Double Jointed",
    ratings=[2],
    prereqs=[[("dexterity", 3)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Fleet of Foot",
    ratings=[1, 2, 3],
    prereqs=[[("athletics", 2)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Giant", ratings=[4], merit_type="Physical",
)
Merit.objects.create(
    name="Hardy", ratings=[1, 2, 3], prereqs=[[("stamina", 3)]], merit_type="Physical",
)
Merit.objects.create(
    name="Greyhound",
    ratings=[1],
    prereqs=[[("athletics", 3), ("wits", 3), ("stamina", 3)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Iron Stamina",
    ratings=[1, 2, 3],
    prereqs=[[("stamina", 3)], [("resolve", 3)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Parkour",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("dexterity", 3), ("athletics", 2)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Quick Draw (Weaponry)",
    requires_detail=False,
    ratings=[1],
    prereqs=[[("wits", 3), ("weaponry", "specialty")]],
    possible_details=[],
    merit_type="Physical",
)
Merit.objects.create(
    name="Quick Draw (Firearms)",
    requires_detail=False,
    ratings=[1],
    prereqs=[[("wits", 3), ("firearms", "specialty")]],
    possible_details=[],
    merit_type="Physical",
)
Merit.objects.create(
    name="Relentless",
    ratings=[1],
    prereqs=[[("athletics", 2), ("stamina", 3)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Seizing the Edge",
    ratings=[2],
    prereqs=[[("wits", 3), ("composure", 3)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Sleight of Hand",
    ratings=[2],
    prereqs=[[("larceny", 3)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Small-Framed", ratings=[2], merit_type="Physical",
)
Merit.objects.create(
    name="Stunt Driver",
    is_style=True,
    ratings=[1, 2, 3, 4],
    prereqs=[[("dexterity", 3), ("drive", 3), ("wits", 3)]],
    merit_type="Physical",
)
Merit.objects.create(
    name="Allies",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[],
    merit_type="Social",
)
Merit.objects.create(
    name="Alternate Identity",
    requires_detail=True,
    ratings=[1, 2, 3],
    possible_details=[],
    merit_type="Social",
)
Merit.objects.create(
    name="Anonymity", ratings=[1, 2, 3, 4, 5], merit_type="Social",
)
Merit.objects.create(
    name="Barfly", ratings=[2], prereqs=[[("socialize", 2)]], merit_type="Social",
)
Merit.objects.create(
    name="Closed Book",
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("manipulation", 3), ("resolve", 3)]],
    merit_type="Social",
)
Merit.objects.create(
    name="Contacts",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[],
    merit_type="Social",
)
Merit.objects.create(
    name="Fame", ratings=[1, 2, 3], merit_type="Social",
)
Merit.objects.create(
    name="Fast-Talking",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("manipulation", 3), ("subterfuge", 2)]],
    merit_type="Social",
)
Merit.objects.create(
    name="Fixer",
    ratings=[2],
    prereqs=[[("wits", 3), ("Contacts", 2)]],
    merit_type="Social",
)
Merit.objects.create(
    name="Hobbyist Clique",
    requires_detail=True,
    ratings=[2],
    prereqs=[[("skill", 2)]],
    merit_type="Social",
)
Merit.objects.create(
    name="Inspiring", ratings=[3], prereqs=[[("presence", 3)]], merit_type="Social",
)
iron_will = Merit.objects.create(
    name="Iron Will", ratings=[2], prereqs=[[("resolve", 4)]], merit_type="Social",
)
Merit.objects.create(
    name="Mystery Cult Initiation",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[],
    merit_type="Social",
)
Merit.objects.create(
    name="Mentor",
    requires_detail=False,
    ratings=[1, 2, 3, 4, 5],
    possible_details=SKILLS,
    merit_type="Social",
)
Merit.objects.create(
    name="Pusher", ratings=[1], prereqs=[[("persuasion", 2)]], merit_type="Social",
)
Merit.objects.create(
    name="Resources", ratings=[1, 2, 3, 4,], merit_type="Social",
)
Merit.objects.create(
    name="Retainer",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[],
    merit_type="Social",
)
Merit.objects.create(
    name="Safe Place", ratings=[1, 2, 3, 4, 5], merit_type="Social",
)
Merit.objects.create(
    name="Small Unit Tactics",
    ratings=[2],
    prereqs=[[("presence", 3)]],
    merit_type="Social",
)
Merit.objects.create(
    name="Spin Doctor",
    ratings=[1],
    prereqs=[[("manipulation", 3), ("subterfuge", 2)]],
    merit_type="Social",
)
Merit.objects.create(
    name="Staff",
    requires_detail=True,
    ratings=[1],
    possible_details=SKILLS,
    merit_type="Social",
)
Merit.objects.create(
    name="Status",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[
        "Police",
        "Hellfire Club",
        "Gang",
        "Military",
        "Medical",
        "Corporate",
    ],
    merit_type="Social",
)
Merit.objects.create(
    name="Striking Looks", ratings=[1, 2], merit_type="Social",
)
Merit.objects.create(
    name="Sympathetic", ratings=[2], merit_type="Social",
)
Merit.objects.create(
    name="Table Turner",
    ratings=[1],
    prereqs=[[("composure", 3), ("manipulation", 3), ("wits", 3)]],
    merit_type="Social",
)
Merit.objects.create(
    name="Takes One to Know One", ratings=[1], merit_type="Social",
)
Merit.objects.create(
    name="Taste",
    ratings=[1],
    prereqs=[
        [("crafts", 2), ("crafts", "specialty")],
        [("crafts", 2), ("expression", "specialty")],
    ],
    merit_type="Social",
)
Merit.objects.create(
    name="True Friend", ratings=[3], merit_type="Social",
)
Merit.objects.create(
    name="Untouchable",
    ratings=[1],
    prereqs=[[("manipulation", 3), ("subterfuge", 2)]],
    merit_type="Social",
)
Merit.objects.create(
    name="Aura Reading", ratings=[3], merit_type="Supernatural",
)
Merit.objects.create(
    name="Automatic Writing", ratings=[2], merit_type="Supernatural",
)
Merit.objects.create(
    name="Biokinesis", ratings=[1, 2, 3, 4, 5], merit_type="Supernatural",
)
Merit.objects.create(
    name="Clairvoyance", ratings=[3], merit_type="Supernatural",
)
Merit.objects.create(
    name="Cursed", ratings=[2], merit_type="Supernatural",
)
Merit.objects.create(
    name="Laying on Hands", ratings=[3], merit_type="Supernatural",
)
Merit.objects.create(
    name="Medium", ratings=[3], merit_type="Supernatural",
)
Merit.objects.create(
    name="Mind of a Madman",
    ratings=[2],
    prereqs=[[("empathy", 3)]],
    merit_type="Supernatural",
)
Merit.objects.create(
    name="Omen Sensitivity", ratings=[3], merit_type="Supernatural",
)
Merit.objects.create(
    name="Numbing Touch", ratings=[1, 2, 3, 4, 5], merit_type="Supernatural",
)
Merit.objects.create(
    name="Psychokinesis", ratings=[3, 5], merit_type="Supernatural",
)
Merit.objects.create(
    name="Psychometry", ratings=[3], merit_type="Supernatural",
)
Merit.objects.create(
    name="Telekinesis", ratings=[1, 2, 3, 4, 5], merit_type="Supernatural",
)
Merit.objects.create(
    name="Telepathy", ratings=[3, 5], merit_type="Supernatural",
)
Merit.objects.create(
    name="Thief of Fate", ratings=[3], merit_type="Supernatural",
)
Merit.objects.create(
    name="Unseen Sense", ratings=[2], merit_type="Supernatural",
)
Merit.objects.create(
    name="Armed Defense",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("dexterity", 3), ("weaponry", 2), ("Defensive Combat (Weaponry)", 1)]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Cheap Shot",
    ratings=[2],
    prereqs=[[("subterfuge", 2), ("Street Fighting", 3)]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Choke Hold", ratings=[2], prereqs=[[("brawl", 2)]], merit_type="Fighting",
)
Merit.objects.create(
    name="Close Quarters Combat",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("wits", 3), ("athletics", 2), ("brawl", 3)]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Defensive Combat (Weaponry)",
    ratings=[1],
    prereqs=[[("weaponry", 1)]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Defensive Combat (Brawl)",
    ratings=[1],
    prereqs=[[("brawl", 1)]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Fighting Finesse (Weaponry)",
    requires_detail=True,
    ratings=[2],
    prereqs=[[("dexterity", 2), ("weaponry", "specialty")]],
    possible_details=[],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Fighting Finesse (Brawl)",
    requires_detail=True,
    ratings=[2],
    prereqs=[[("dexterity", 2), ("brawl", "specialty")]],
    possible_details=[],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Firefight",
    is_style=True,
    ratings=[1, 2, 3],
    prereqs=[[("composure", 3), ("dexterity", 3), ("athletics", 2), ("firearms", 2),]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Grappling",
    is_style=True,
    ratings=[1, 2, 3],
    prereqs=[[("stamina", 3), ("strength", 2), ("athletics", 2), ("brawl", 2),]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Heavy Weapons",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("stamina", 3), ("strength", 3), ("athletics", 2), ("weaponry", 2),]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Improvised Weaponry",
    is_style=True,
    ratings=[1, 2, 3],
    prereqs=[[("wits", 3), ("weaponry", 1)]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Iron Skin",
    ratings=[2, 4],
    prereqs=[
        [("stamina", 3), ("Martial Arts", 2)],
        [("stamina", 3), ("Street Fighting", 2)],
    ],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Light Weapons",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[
        [("wits", 3), ("dexterity", 3), ("athletics", 2), ("weaponry", 2),],
        [("dexterity", 3), ("athletics", 2), ("weaponry", 2), ("Fighting Finesse", 1)],
    ],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Marksmanship",
    is_style=True,
    ratings=[1, 2, 3, 4],
    prereqs=[[("composure", 3), ("resolve", 3), ("firearms", 2)]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Martial Arts",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("resolve", 3), ("dexterity", 3), ("athletics", 2), ("brawl", 2),]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Police Tactics",
    is_style=True,
    ratings=[1, 2, 3],
    prereqs=[[("brawl", 2), ("weaponry", 1)]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Shiv",
    ratings=[1, 2],
    prereqs=[[("weaponry", 1), ("Street Fighting", 2)]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Street Fighting",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("stamina", 3), ("composure", 3), ("brawl", 2), ("streetwise", 2),]],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Unarmed Defense",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("dexterity", 3), ("brawl", 2), ("Defensive Combat (Brawl)", 1)]],
    merit_type="Fighting",
)


acanthus = Path.objects.create(
    name="Acanthus", ruling_arcana=["fate", "time"], inferior_arcanum="forces"
)
mastigos = Path.objects.create(
    name="Mastigos", ruling_arcana=["mind", "space"], inferior_arcanum="matter"
)
moros = Path.objects.create(
    name="Moros", ruling_arcana=["death", "matter"], inferior_arcanum="spirit"
)
obrimos = Path.objects.create(
    name="Obrimos", ruling_arcana=["forces", "prime"], inferior_arcanum="death"
)
thyrsus = Path.objects.create(
    name="Thyrsus", ruling_arcana=["life", "spirit"], inferior_arcanum="mind"
)

adamantine_arrow = Order.objects.create(
    name="Adamantine Arrow", rote_skills=["athletics", "intimidation", "medicine"]
)
guardians_of_the_veil = Order.objects.create(
    name="Guardians of the Veil", rote_skills=["investigation", "stealth", "subterfuge"]
)
mysterium = Order.objects.create(
    name="Mysterium", rote_skills=["investigation", "occult", "survival"]
)
silver_ladder = Order.objects.create(
    name="Silver Ladder", rote_skills=["expression", "persuasion", "subterfuge"]
)
free_council = Order.objects.create(
    name="Free Councl", rote_skills=["crafts", "persuasion", "science"]
)
seers_of_the_throne = Order.objects.create(
    name="Seers of the Throne", rote_skills=["investigation", "occult", "persuasion"]
)

hegemony = Order.objects.create(
    name="Hegemony", rote_skills=["politics", "persuasion", "empathy"]
)
panopticon = Order.objects.create(
    name="Panopticon", rote_skills=["investigation", "stealth", "subterfuge"]
)
paternoster = Order.objects.create(
    name="Paternoster", rote_skills=["academics", "occult", "expression"]
)
praetorian = Order.objects.create(
    name="Praetorian", rote_skills=["athletics", "larceny", "intimidation"]
)

Merit.objects.create(
    name="Adamant Hand",
    requires_detail=True,
    possible_details=["Athletics", "Weaponry", "Brawl"],
    ratings=[2],
    prereqs=[
        [("athletics", 3), ("Adamantine Arrow Status", 1)],
        [("brawl", 3), ("Adamantine Arrow Status", 1)],
        [("weaponry", 3), ("Adamantine Arrow Status", 1)],
    ],
    merit_type="Mage",
)
Merit.objects.create(
    name="Artifact", ratings=[3, 4, 5], merit_type="Mage",
)
Merit.objects.create(
    name="Astral Adept", ratings=[4], merit_type="Mage",
)
Merit.objects.create(
    name="Between the Ticks",
    ratings=[2],
    merit_type="Mage",
    prereqs=[[("wits", 3), ("time", 1)]],
)
Merit.objects.create(name="Cabal Theme", ratings=[1], merit_type="Mage", prereqs=[])
Merit.objects.create(
    name="Consilium Status", ratings=[1, 2, 3, 4, 5], merit_type="Mage",
)
Merit.objects.create(
    name="Adamantine Arrow Status",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[],
)
Merit.objects.create(
    name="Mysterium Status", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Guardians of the Veil Status",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[],
)
Merit.objects.create(
    name="Silver Ladder Status", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Free Council Status", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Seers pf the Throne Status",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[],
)
Merit.objects.create(
    name="Destiny", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Dream",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("composure", 3), ("wits", 3)]],
)
Merit.objects.create(
    name="Egregore",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("Mysterium Status", 1)]],
)
Merit.objects.create(
    name="Enhanced Item", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
Merit.objects.create(name="Familiar", ratings=[2, 4], merit_type="Mage", prereqs=[])
Merit.objects.create(
    name="Fast Spells",
    ratings=[2],
    merit_type="Mage",
    prereqs=[[("firearms", 2), ("time", 1)]],
)
Merit.objects.create(
    name="Grimoire", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Hallow", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
Merit.objects.create(name="High Speech", ratings=[1], merit_type="Mage", prereqs=[])
Merit.objects.create(
    name="Imbued Item", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Infamous Mentor",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("Mentor", 1)]],
)
Merit.objects.create(
    name="Lex Magica",
    ratings=[2],
    merit_type="Mage",
    prereqs=[[("Silver Ladder Status", 1)]],
)
Merit.objects.create(
    name="Mana Sensitivity",
    ratings=[1],
    merit_type="Mage",
    prereqs=[[("wits", 3), ("prime", 1)]],
)
Merit.objects.create(
    name="Masque",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("Guardians of the Veil Status", 1)]],
    is_style=True,
)
Merit.objects.create(
    name="Mystery Cult Influence", ratings=[3, 4, 5], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Occultation", ratings=[1, 2, 3], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Potent Nimbus", ratings=[1, 2], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Potent Resonance", ratings=[2], merit_type="Mage", prereqs=[[("gnosis", 3)]]
)
Merit.objects.create(
    name="Prelacy",
    ratings=[1, 2, 3, 4],
    merit_type="Mage",
    prereqs=[[("Seers of the Throne Status", 3)]],
    is_style=True,
)
Merit.objects.create(
    name="Sanctum",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("Safe Place", 1)]],
)
Merit.objects.create(
    name="Shadow Name", ratings=[1, 2, 3], merit_type="Mage", prereqs=[]
)
Merit.objects.create(
    name="Techne",
    ratings=[2],
    merit_type="Mage",
    prereqs=[[("Free Council Status", 1)]],
)

Rote.objects.create(
    name="Ectoplasmic Shaping",
    practice="compelling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["crafts", "occult", "larceny"],
    primary_factor="duration",
    withstand="resolve",
)
Rote.objects.create(
    name="Deepen Shadows",
    practice="compelling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["occult", "intimidation", "expression"],
    primary_factor="duration",
)
Rote.objects.create(
    name="Forensic Gaze",
    practice="knowing",
    arcanum="death",
    level=1,
    suggested_rote_skills=["medicine", "investigation", "expression"],
    primary_factor="potency",
)
Rote.objects.create(
    name="Shadow Sculpting",
    practice="compelling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["crafts", "science", "expression"],
    primary_factor="duration",
)
Rote.objects.create(
    name="Soul Marks",
    practice="unveiling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["medicine", "occult", "empathy"],
    primary_factor="potency",
    withstand="resolve",
)
Rote.objects.create(
    name="Speak with the Dead",
    practice="unveiling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["socialize", "expression", "investigation"],
    primary_factor="duration",
)
Rote.objects.create(
    name="Corpse Mask",
    practice="veiling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["subterfuge", "crafts", "medicine"],
    primary_factor="duration",
)
Rote.objects.create(
    name="Decay",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["subterfuge", "science", "occult"],
    primary_factor="potency",
)
Rote.objects.create(
    name="Ectoplasm",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["occult", "expression", "academics"],
    primary_factor="duration",
)
Rote.objects.create(
    name="Ghost Shield",
    practice="shielding",
    arcanum="death",
    level=2,
    suggested_rote_skills=["streetwise", "subterfuge", "survival"],
    primary_factor="potency",
)
Rote.objects.create(
    name="Shape Ephemera",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["crafts", "expression", "science"],
    primary_factor="duration",
    withstand="stamina",
)
Rote.objects.create(
    name="Soul Armor",
    practice="shielding",
    arcanum="death",
    level=2,
    suggested_rote_skills=["academics", "occult", "survival"],
    primary_factor="duration",
)
Rote.objects.create(
    name="Soul Jar",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["crafts", "occult", "persuasion"],
    primary_factor="duration",
    withstand="resolve",
)
Rote.objects.create(
    name="Suppress Aura",
    practice="veiling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["subterfuge", "intimidation", "medicine"],
    primary_factor="duration",
    withstand="resolve",
)
Rote.objects.create(
    name="Suppress Life",
    practice="veiling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["subterfuge", "medicine", "academics"],
    primary_factor="duration",
)
Rote.objects.create(
    name="Touch of the Grave",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["survival", "crafts", "persuasion"],
    primary_factor="duration",
)
Rote.objects.create(
    name="Without a Trace",
    practice="veiling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["science", "stealth", "subterfuge"],
    primary_factor="duration",
)
Rote.objects.create(
    name="Cold Snap",
    arcanum="death",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["survival", "intimidation", "science"],
)
Rote.objects.create(
    name="Damage Ghost",
    arcanum="death",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["occult", "intimidation", "brawl"],
)
Rote.objects.create(
    name="Devouring the Slain",
    arcanum="death",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "medicine", "persuasion"],
)
Rote.objects.create(
    name="Ghost Gate",
    arcanum="death",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "academics", "expression"],
)
Rote.objects.create(
    name="Ghost Summons",
    arcanum="death",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["persusion", "socialize", "occult"],
)
Rote.objects.create(
    name="Quicken Corpse",
    arcanum="death",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["medicine", "crafts", "persuasion"],
)
Rote.objects.create(
    name="Quicken Ghost",
    arcanum="death",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["persuasion", "socialize", "medicine"],
)
Rote.objects.create(
    name="Rotting Flesh",
    arcanum="death",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["intimidation", "occult", "empathy"],
)
Rote.objects.create(
    name="Sever Soul",
    arcanum="death",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "athletics", "expression"],
)
Rote.objects.create(
    name="Shadow Crafting",
    arcanum="death",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "intimidation", "occult"],
)
Rote.objects.create(
    name="Enervation",
    arcanum="death",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="stamina",
    suggested_rote_skills=["occult", "intimidation", "subterfuge"],
)
Rote.objects.create(
    name="Exorcism",
    arcanum="death",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["brawl", "expression", "occult"],
)
Rote.objects.create(
    name="Revenant",
    arcanum="death",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["crafts", "brawl", "intimidation"],
)
Rote.objects.create(
    name="Shadow Flesh",
    arcanum="death",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["occult", "medicine", "subterfuge"],
)
Rote.objects.create(
    name="Withering",
    arcanum="death",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["intimidation", "medicine", "science"],
)
Rote.objects.create(
    name="Create Anchor",
    arcanum="death",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["crafts", "occult", "persuasion"],
)
Rote.objects.create(
    name="Create Avernian Gate",
    arcanum="death",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "crafts", "persuasion"],
)
Rote.objects.create(
    name="Create Ghost",
    arcanum="death",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "expression", "academics"],
)
Rote.objects.create(
    name="Deny the Reaper",
    arcanum="death",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["medicine", "occult", "subterfuge"],
)
Rote.objects.create(
    name="Empty Presence",
    arcanum="death",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    mana_cost=1,
    withstand="composure",
    suggested_rote_skills=["subterfuge", "persuasion", "stealth"],
)
Rote.objects.create(
    name="Sever the Awakened Soul",
    arcanum="death",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["crafts", "intimidation", "medicine"],
)
Rote.objects.create(
    name="Interconnection",
    arcanum="fate",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["empathy", "investigation", "medicine"],
)
Rote.objects.create(
    name="Oaths Fulfilled",
    arcanum="fate",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "politics", "investigation"],
)
Rote.objects.create(
    name="Quantum Flux",
    arcanum="fate",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "firearms", "occult"],
)
Rote.objects.create(
    name="Reading the Outmost Eddies",
    arcanum="fate",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["computer", "persuasion", "subterfuge"],
)
Rote.objects.create(
    name="Serendipity",
    arcanum="fate",
    level=1,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["intimidation", "occult", "socialize"],
)
Rote.objects.create(
    name="Exceptional Luck",
    arcanum="fate",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["intimidation", "occult", "socialize"],
)
Rote.objects.create(
    name="Fabricate Fortune",
    arcanum="fate",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["larceny", "occult", "subterfuge"],
)
Rote.objects.create(
    name="Fools Rush In",
    arcanum="fate",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "socialize", "streetwise"],
)
Rote.objects.create(
    name="Lucky Number",
    arcanum="fate",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "larceny", "science"],
)
Rote.objects.create(
    name="Shifting the Odds",
    arcanum="fate",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "politics", "subterfuge"],
)
Rote.objects.create(
    name="Warding Gesture",
    arcanum="fate",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["brawl", "occult", "subterfuge"],
)
Rote.objects.create(
    name="Grave Misfortune",
    arcanum="fate",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["intimidation", "occult", "weaponry"],
)
Rote.objects.create(
    name="Monkey's Paw",
    arcanum="fate",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["drive", "crafts", "science"],
)
Rote.objects.create(
    name="Shared Fate",
    arcanum="fate",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["medicine", "persuasion", "politics"],
)
Rote.objects.create(
    name="Superlative Luck",
    arcanum="fate",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    mana_cost=1,
    suggested_rote_skills=["athletics", "crafts", "occult"],
)
Rote.objects.create(
    name="Sworn Oaths",
    arcanum="fate",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["expression", "occult", "politics"],
)
Rote.objects.create(
    name="Atonement",
    arcanum="fate",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="potency",
    suggested_rote_skills=["academics", "empathy", "survival"],
)
Rote.objects.create(
    name="Chaos Mastery",
    arcanum="fate",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "occult", "science"],
)
Rote.objects.create(
    name="Divine Intervention",
    arcanum="fate",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "occult", "subterfuge"],
)
Rote.objects.create(
    name="Strings of Fate",
    arcanum="fate",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["academics", "persuasion", "stealth"],
)
Rote.objects.create(
    name="Sever Oaths",
    arcanum="fate",
    level=4,
    practice="unraveling",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["occult", "subterfuge", "weaponry"],
)
Rote.objects.create(
    name="Forge Destiny",
    arcanum="fate",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["intimidation", "occult", "persuasion"],
)
Rote.objects.create(
    name="Pariah",
    arcanum="fate",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["investigation", "medicine", "politics"],
)
Rote.objects.create(
    name="Miracle",
    arcanum="fate",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "persuasion", "subterfuge"],
)
Rote.objects.create(
    name="Swarm of Locusts",
    arcanum="fate",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["intimidation", "occult", "science"],
)
Rote.objects.create(
    name="Influence Electricity",
    arcanum="forces",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["computers", "crafts", "science"],
)
Rote.objects.create(
    name="Influence Fire",
    arcanum="forces",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "science", "survival"],
)
Rote.objects.create(
    name="Kinetic Efficiency",
    arcanum="forces",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "science", "survival"],
)
Rote.objects.create(
    name="Influence Heat",
    arcanum="forces",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "science", "survival"],
)
Rote.objects.create(
    name="Nightvision",
    arcanum="forces",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "science", "stealth"],
)
Rote.objects.create(
    name="Receiver",
    arcanum="forces",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "investigation", "science"],
)
Rote.objects.create(
    name="Tune In",
    arcanum="forces",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["computers", "empathy", "science"],
)
Rote.objects.create(
    name="Control Electricity",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "computers", "science"],
)
Rote.objects.create(
    name="Control Fire",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "science", "survival"],
)
Rote.objects.create(
    name="Control Gravity",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "occult", "science"],
)
Rote.objects.create(
    name="Control Heat",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "science", "survival"],
)
Rote.objects.create(
    name="Control Light",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "investigation", "science"],
)
Rote.objects.create(
    name="Control Sound",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["expression", "stealth", "science"],
)
Rote.objects.create(
    name="Control Weather",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "science", "survival"],
)
Rote.objects.create(
    name="Environmental Shield",
    arcanum="forces",
    level=2,
    practice="Shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "science", "survival"],
)
Rote.objects.create(
    name="Invisibility",
    arcanum="forces",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["larceny", "science", "stealth"],
)
Rote.objects.create(
    name="Kinetic Blow",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "science"],
)
Rote.objects.create(
    name="Transmission",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "science"],
)
Rote.objects.create(
    name="Zoom In",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "science", "survival"],
)
Rote.objects.create(
    name="Call Lightning",
    arcanum="forces",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
)
Rote.objects.create(
    name="Gravitic Supremacy (Increase)",
    arcanum="forces",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "science", "survival"],
)
Rote.objects.create(
    name="Gravitic Supremacy (Decrease)",
    arcanum="forces",
    level=3,
    practice="fraying",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "science", "survival"],
)
Rote.objects.create(
    name="Telekinesis",
    arcanum="forces",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "science"],
)
Rote.objects.create(
    name="Telekinetic Strike",
    arcanum="forces",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
)
Rote.objects.create(
    name="Turn Momentum",
    arcanum="forces",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
)
Rote.objects.create(
    name="Velocity Control (Decrease)",
    arcanum="forces",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "drive", "science"],
)
Rote.objects.create(
    name="Velocity Control (Increase)",
    arcanum="forces",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "drive", "science"],
)
Rote.objects.create(
    name="Electromagnetic Pulse",
    arcanum="forces",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "computers", "science"],
)
Rote.objects.create(
    name="Levitation",
    arcanum="forces",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["athletics", "science", "survival"],
)
Rote.objects.create(
    name="Rend Friction",
    arcanum="forces",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "drive", "science"],
)
Rote.objects.create(
    name="Thunderbolt",
    arcanum="forces",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
)
Rote.objects.create(
    name="Transform Energy",
    arcanum="forces",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "science"],
)
Rote.objects.create(
    name="Adverse Weather",
    arcanum="forces",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "science"],
)
Rote.objects.create(
    name="Create Energy",
    arcanum="forces",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "science"],
)
Rote.objects.create(
    name="Eradicate Energy",
    arcanum="forces",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["intimidation", "science", "survival"],
)
Rote.objects.create(
    name="Earthquake",
    arcanum="forces",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "science", "survival"],
)
Rote.objects.create(
    name="Analyze Life",
    arcanum="life",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["animal_ken", "medicine", "survival"],
)
Rote.objects.create(
    name="Cleanse the Body",
    arcanum="life",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "survival"],
)
Rote.objects.create(
    name="Heightened Senses",
    arcanum="life",
    level=1,
    practice="unveilling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "investigation", "survival"],
)
Rote.objects.create(
    name="Speak With Beasts",
    arcanum="life",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["animal_ken", "empathy", "survival"],
)
Rote.objects.create(
    name="Web of Life",
    arcanum="life",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "medicine", "survival"],
)
Rote.objects.create(
    name="Body Control",
    arcanum="life",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "survival"],
)
Rote.objects.create(
    name="Control Instincts",
    arcanum="life",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["animal_ken", "intimidation", "persuasion"],
)
Rote.objects.create(
    name="Lure and Repel",
    arcanum="life",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["animal_ken", "persuasion", "survival"],
)
Rote.objects.create(
    name="Mutable Mask",
    arcanum="life",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["medicine", "stealth", "subterfuge"],
)
Rote.objects.create(
    name="Purge Illness",
    arcanum="life",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "survival"],
)
Rote.objects.create(
    name="Bruise Flesh",
    arcanum="life",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["brawl", "intimidation", "medicine"],
)
Rote.objects.create(
    name="Degrading the Form",
    arcanum="life",
    level=3,
    practice="fraying",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["brawl", "medicine", "survival"],
)
Rote.objects.create(
    name="Honing the Form",
    arcanum="life",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "survival"],
)
Rote.objects.create(
    name="Knit",
    arcanum="life",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "medicine", "survival"],
)
Rote.objects.create(
    name="Many Faces",
    arcanum="life",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["medicine", "stealth", "subterfuge"],
)
Rote.objects.create(
    name="Transform Life",
    arcanum="life",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="stamina",
    suggested_rote_skills=["animal_ken", "science", "survival"],
)
Rote.objects.create(
    name="Accelerate Growth",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["animal_ken", "medicine", "science"],
)
Rote.objects.create(
    name="Animal Minion",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["animal_ken", "science", "survival"],
)
Rote.objects.create(
    name="Life-Force Assault",
    arcanum="life",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["brawl", "intimidation", "medicine"],
)
Rote.objects.create(
    name="Mend",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "medicine", "survival"],
)
Rote.objects.create(
    name="Regeneration",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    mana_cost=1,
    suggested_rote_skills=["athletics", "medicine", "survival"],
)
Rote.objects.create(
    name="Shapechanging",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["animal_ken", "athletics", "science"],
)
Rote.objects.create(
    name="Create Life",
    arcanum="life",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["medicine", "science", "survival"],
)
Rote.objects.create(
    name="Contagion",
    arcanum="life",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["medicine", "occult", "science"],
)
Rote.objects.create(
    name="Salt the Earth",
    arcanum="life",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["medicine", "science", "survival"],
)
Rote.objects.create(
    name="Craftsman's Eye",
    arcanum="matter",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "investigation", "science"],
)
Rote.objects.create(
    name="Detect Substance",
    arcanum="matter",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "investigation", "science"],
)
Rote.objects.create(
    name="Discern Composition",
    arcanum="matter",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "investigation", "science"],
)
Rote.objects.create(
    name="Lodestone",
    arcanum="matter",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "larceny", "science"],
)
Rote.objects.create(
    name="Remote Control",
    arcanum="matter",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "drive", "intimidate"],
)
Rote.objects.create(
    name="Alchemist's Touch",
    arcanum="matter",
    level=2,
    practice="shielding",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "survival", "persuasion"],
)
Rote.objects.create(
    name="Find the Balance",
    arcanum="matter",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "persuasion", "science"],
)
Rote.objects.create(
    name="Hidden Hoard",
    arcanum="matter",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["larceny", "occult", "subterfuge"],
)
Rote.objects.create(
    name="Machine Invisibility",
    arcanum="matter",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["larceny", "science", "stealth"],
)
Rote.objects.create(
    name="Shaping",
    arcanum="matter",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["crafts", "expression", "persuasion"],
)
Rote.objects.create(
    name="Aegis",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "crafts", "science"],
)
Rote.objects.create(
    name="Alter Conductivity",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["computers", "science", "subterfuge"],
)
Rote.objects.create(
    name="Alter Integrity (Weaken)",
    arcanum="matter",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["crafts", "medicine", "subterfuge"],
)
Rote.objects.create(
    name="Alter Integrity (Strengthen)",
    arcanum="matter",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["crafts", "medicine", "subterfuge"],
)
Rote.objects.create(
    name="Crucible",
    arcanum="matter",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "science"],
)
Rote.objects.create(
    name="Nigredo and Albedo (Repair)",
    arcanum="matter",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "brawl", "medicine"],
)
Rote.objects.create(
    name="Nigredo and Albedo (Destroy)",
    arcanum="matter",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "brawl", "medicine"],
)
Rote.objects.create(
    name="Shrink and Grow",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["crafts", "expression", "science"],
)
Rote.objects.create(
    name="State Change",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="durability",
    suggested_rote_skills=["crafts", "persuasion", "science"],
)
Rote.objects.create(
    name="Windstrike",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "crafts"],
)
Rote.objects.create(
    name="Wonderful Machine",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "politics", "science"],
)
Rote.objects.create(
    name="Ghostwall",
    arcanum="matter",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "occult", "stealth"],
)
Rote.objects.create(
    name="Golem",
    arcanum="matter",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "occult"],
)
Rote.objects.create(
    name="Piercing Earth",
    arcanum="matter",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "crafts"],
)
Rote.objects.create(
    name="Transubstantiation",
    arcanum="matter",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "empathy", "science"],
)
Rote.objects.create(
    name="Annihilate Matter",
    arcanum="matter",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["athletics", "intimidation", "science"],
)
Rote.objects.create(
    name="Ex Nihilo",
    arcanum="matter",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "science"],
)
Rote.objects.create(
    name="Self-Repairing Machine",
    arcanum="matter",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "medicine", "occult"],
)
Rote.objects.create(
    name="Know Nature",
    arcanum="mind",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "science", "subterfuge"],
)
Rote.objects.create(
    name="Mental Scan",
    arcanum="mind",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["empathy", "investigation", "occult"],
)
Rote.objects.create(
    name="One Mind, Two Thoughts",
    arcanum="mind",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "expression", "science"],
)
Rote.objects.create(
    name="Perfect Recall",
    arcanum="mind",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "expression", "investigation"],
)
Rote.objects.create(
    name="Alter Mental Pattern",
    arcanum="mind",
    level=2,
    practice="veiling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["science", "stealth", "subterfuge"],
)
Rote.objects.create(
    name="Dream Reaching",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["empathy", "medicine", "persuasion"],
)
Rote.objects.create(
    name="Emotional Urging",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["empathy", "intimidation", "subterfuge"],
)
Rote.objects.create(
    name="First Impressions",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["crafts", "socialize", "subterfuge"],
)
Rote.objects.create(
    name="Incognito Presence",
    arcanum="mind",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="resolve",
    mana_cost=1,
    suggested_rote_skills=["empathy", "stealth", "subterfuge"],
)
Rote.objects.create(
    name="Memory Hole",
    arcanum="mind",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "medicine", "subterfuge"],
)
Rote.objects.create(
    name="Mental Shield",
    arcanum="mind",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "intimidation", "survival"],
)
Rote.objects.create(
    name="Psychic Domination",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["expression", "intimidation", "subterfuge"],
)
Rote.objects.create(
    name="Telepathy",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["crafts", "empathy", "socialize"],
)
Rote.objects.create(
    name="Augment Mind",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "expression", "survival"],
)
Rote.objects.create(
    name="Befuddle (Social)",
    arcanum="mind",
    level=3,
    practice="fraying",
    primary_factor="potence",
    withstand="composure",
    suggested_rote_skills=["intimidation", "persuasion", "science"],
)
Rote.objects.create(
    name="Befuddle (Mental)",
    arcanum="mind",
    level=3,
    practice="fraying",
    primary_factor="potence",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "persuasion", "science"],
)
Rote.objects.create(
    name="Clear Thoughts",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["empathy", "intimidation", "persuasion"],
)
Rote.objects.create(
    name="Enhance Skill",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "expression", "survival"],
)
Rote.objects.create(
    name="Goetic Summons",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["persuasion", "socialize", "occult"],
)
Rote.objects.create(
    name="Imposter",
    arcanum="mind",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["persuasion", "stealth", "subterfuge"],
)
Rote.objects.create(
    name="Psychic Assault",
    arcanum="mind",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "intimidation", "medicine"],
)
Rote.objects.create(
    name="Sleep of the Just",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["academics", "athletics", "occult"],
)
Rote.objects.create(
    name="Read the Depths",
    arcanum="mind",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["empathy", "investigation", "medicine"],
)
Rote.objects.create(
    name="Universal Language",
    arcanum="mind",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "investigation", "persuasion"],
)
Rote.objects.create(
    name="Gain Skill",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "science"],
)
Rote.objects.create(
    name="Hallucination",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["academics", "persuasion", "subterfuge"],
)
Rote.objects.create(
    name="Mind Flay",
    arcanum="mind",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["expression", "intimidation", "science"],
)
Rote.objects.create(
    name="Possession",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["medicine", "persuasion", "subterfuge"],
)
Rote.objects.create(
    name="Psychic Projection",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["academics", "occult", "socialize"],
)
Rote.objects.create(
    name="Psychic Reprogramming",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "medicine", "persuasion"],
)
Rote.objects.create(
    name="Terrorize",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["expression", "intimidation", "medicine"],
)
Rote.objects.create(
    name="Amorality",
    arcanum="mind",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["crafts", "empathy", "expression"],
)
Rote.objects.create(
    name="No Exit",
    arcanum="mind",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["expression", "persuasion", "science"],
)
Rote.objects.create(
    name="Mind Wipe",
    arcanum="mind",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["academics", "intimidation", "occult"],
)
Rote.objects.create(
    name="Psychic Genesis",
    arcanum="mind",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "expression", "science"],
)
Rote.objects.create(
    name="Social Networking",
    arcanum="mind",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["persuasion", "politics", "socialize"],
)
Rote.objects.create(
    name="Dispel Magic",
    arcanum="prime",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="arcana",
    suggested_rote_skills=["athletics", "intimidation", "occult"],
)
Rote.objects.create(
    name="Pierce Deception",
    arcanum="prime",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "medicine", "occult"],
)
Rote.objects.create(
    name="Supernal Vision",
    arcanum="prime",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "occult", "survival"],
)
Rote.objects.create(
    name="Sacred Geometry",
    arcanum="prime",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "occult", "survival"],
)
Rote.objects.create(
    name="Scribe Grimoire",
    arcanum="prime",
    level=1,
    practice="compelling",
    primary_factor="potency",
    mana_cost=1,
    withstand="arcanum_dots",
    suggested_rote_skills=["crafts", "expression", "occult"],
)
Rote.objects.create(
    name="Word of Command",
    arcanum="prime",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["craft", "occult", "persuasion"],
)
Rote.objects.create(
    name="As Above, So Below",
    arcanum="prime",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "occult", "politics"],
)
Rote.objects.create(
    name="Cloak Nimbus",
    arcanum="prime",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["politics", "stealth", "subterfuge"],
)
Rote.objects.create(
    name="Invisible Runes",
    arcanum="prime",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["expression", "intimidation", "persuasion"],
)
Rote.objects.create(
    name="Supernal Veil",
    arcanum="prime",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "subterfuge", "survival"],
)
Rote.objects.create(
    name="Wards and Signs",
    arcanum="prime",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["intimidation", "occult", "survival"],
)
Rote.objects.create(
    name="Words of Truth",
    arcanum="prime",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["expression", "intimidation", "persuasion"],
)
Rote.objects.create(
    name="Aetheric Winds",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "expression", "occult"],
)
Rote.objects.create(
    name="Channel Mana",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["occult", "politics", "socialize"],
)
Rote.objects.create(
    name="Cleanse Pattern",
    arcanum="prime",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["investigation", "occult", "stealth"],
)
Rote.objects.create(
    name="Display of Power",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["brawl", "occult", "socialize"],
)
Rote.objects.create(
    name="Ephemeral Enchantment",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "weaponry"],
)
Rote.objects.create(
    name="Geomancy",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academia", "expression", "occult"],
)
Rote.objects.create(
    name="Platonic Form",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="potency",
    mana_cost=1,
    withstand="",
    suggested_rote_skills=["academics", "crafts", "expression"],
)
Rote.objects.create(
    name="Stealing Fire",
    arcanum="prime",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["expression", "larceny", "persuasion"],
)
Rote.objects.create(
    name="Apocalypse",
    arcanum="prime",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["occult", "persuasion", "socialize"],
)
Rote.objects.create(
    name="Celestial Fire",
    arcanum="prime",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "expression", "occult"],
)
Rote.objects.create(
    name="Destroy Tass",
    arcanum="prime",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["brawl", "intimidation", "occult"],
)
Rote.objects.create(
    name="Hallow Dance",
    arcanum="prime",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="hallow_rating",
    suggested_rote_skills=["expression", "occult", "survival"],
)
Rote.objects.create(
    name="Supernal Dispellation",
    arcanum="prime",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="arcanum",
    suggested_rote_skills=["athletics", "intimidation", "occult"],
)
Rote.objects.create(
    name="Blasphemy",
    arcanum="prime",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="hallow_rating",
    suggested_rote_skills=["athletics", "occult", "survival"],
)
Rote.objects.create(
    name="Create Truth",
    arcanum="prime",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="hallow_rating",
    mana_cost=5,
    suggested_rote_skills=["expression", "occult", "persuasion"],
)
Rote.objects.create(
    name="Eidolon",
    arcanum="prime",
    level=5,
    practice="making",
    primary_factor="potency",
    mana_cost=1,
    withstand="",
    suggested_rote_skills=["academics", "crafts", "occult"],
)
Rote.objects.create(
    name="Forge Purpose",
    arcanum="prime",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["empathy", "expression", "medicine"],
)
Rote.objects.create(
    name="Word of Unmaking",
    arcanum="prime",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="merit_rating",
    suggested_rote_skills=["intimidation", "occult", "weaponry"],
)
Rote.objects.create(
    name="Correspondence",
    arcanum="space",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "empathy", "medicine"],
)
Rote.objects.create(
    name="Ground-Eater",
    arcanum="space",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="stamina",
    suggested_rote_skills=["athletics", "science", "survival"],
)
Rote.objects.create(
    name="Isolation",
    arcanum="space",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["academics", "intimidation", "subterfuge"],
)
Rote.objects.create(
    name="Locate Object",
    arcanum="space",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "occult", "science"],
)
Rote.objects.create(
    name="The Outward and Inward Eye",
    arcanum="space",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["firearms", "investigation", "occult"],
)
Rote.objects.create(
    name="Borrow Threads",
    arcanum="space",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="connection",
    suggested_rote_skills=["larceny", "occult", "subterfuge"],
)
Rote.objects.create(
    name="Break Boundary",
    arcanum="space",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "larceny", "persuasion"],
)
Rote.objects.create(
    name="Lying Maps",
    arcanum="space",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["academics", "politics", "survival"],
)
Rote.objects.create(
    name="Scrying",
    arcanum="space",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["computers", "occult", "subterfuge"],
)
Rote.objects.create(
    name="Secret Door",
    arcanum="space",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "stealth", "subterfuge"],
)
Rote.objects.create(
    name="Veil Sympathy",
    arcanum="space",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="sympathy_connection",
    suggested_rote_skills=["politics", "subterfuge", "survival"],
)
Rote.objects.create(
    name="Ward",
    arcanum="space",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "subterfuge", "weaponry"],
)
Rote.objects.create(
    name="Ban",
    arcanum="space",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["intimidation", "science", "stealth"],
)
Rote.objects.create(
    name="Co-Location",
    arcanum="space",
    level=3,
    practice="fraying",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
)
Rote.objects.create(
    name="Perfect Sympathy",
    arcanum="space",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "empathy", "larceny"],
)
Rote.objects.create(
    name="Warp",
    arcanum="space",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "medicine"],
)
Rote.objects.create(
    name="Web-Weaver",
    arcanum="space",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["crafts", "empathy", "persuasion"],
)
Rote.objects.create(
    name="Alter Direction",
    arcanum="space",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "firearms", "persuasion"],
)
Rote.objects.create(
    name="Collapse",
    arcanum="space",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "firearms", "intimidation"],
)
Rote.objects.create(
    name="Cut Threads",
    arcanum="space",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="symapthy_connection",
    suggested_rote_skills=["persuasion", "politics", "weaponry"],
)
Rote.objects.create(
    name="Secret Room",
    arcanum="space",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["expression", "science", "survival"],
)
Rote.objects.create(
    name="Teleportation",
    arcanum="space",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["larceny", "persuasion", "science"],
)
Rote.objects.create(
    name="Create Sympathy",
    arcanum="space",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="connection",
    suggested_rote_skills=["empathy", "persuasion", "poltiics"],
)
Rote.objects.create(
    name="Forge No Chains",
    arcanum="space",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "subterfuge", "survival"],
)
Rote.objects.create(
    name="Pocket Dimension",
    arcanum="space",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "survival"],
)
Rote.objects.create(
    name="Quarantine",
    arcanum="space",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "larceny", "socialize"],
)
Rote.objects.create(
    name="Coaxing the Spirits",
    arcanum="spirit",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["politics", "athletics", "expression"],
)
Rote.objects.create(
    name="Exorcist's Eye",
    arcanum="spirit",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "survival", "socialize"],
)
Rote.objects.create(
    name="Gremlins",
    arcanum="spirit",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["larceny", "politics", "subterfuge"],
)
Rote.objects.create(
    name="Invoke Bane",
    arcanum="spirit",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["brawl", "intimidation", "occult"],
)
Rote.objects.create(
    name="Know Spirit",
    arcanum="spirit",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["academics", "brawl", "socialize"],
)
Rote.objects.create(
    name="Cap the Well",
    arcanum="spirit",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["politics", "survival", "persuasion"],
)
Rote.objects.create(
    name="Channel Essence",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["occult", "persuasion", "survival"],
)
Rote.objects.create(
    name="Command Spirit",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["medicine", "athletics", "persuasion"],
)
Rote.objects.create(
    name="Ephemeral Shield",
    arcanum="spirit",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["animal_ken", "medicine", "stealth"],
)
Rote.objects.create(
    name="Gossamer Touch",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["brawl", "crafts", "intimidation"],
)
Rote.objects.create(
    name="Opener of the Way",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "computers", "socialize"],
)
Rote.objects.create(
    name="Shadow Walk",
    arcanum="spirit",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "stealth", "streetwise"],
)
Rote.objects.create(
    name="Slumber",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["expression", "occult", "weaponry"],
)
Rote.objects.create(
    name="Bolster Spirit",
    arcanum="spirit",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["medicine", "occult", "expression"],
)
Rote.objects.create(
    name="Erode Resonance",
    arcanum="spirit",
    level=3,
    practice="fraying",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "brawl", "intimidation"],
)
Rote.objects.create(
    name="Howl From Beyond",
    arcanum="spirit",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["expression", "firearms", "medicine"],
)
Rote.objects.create(
    name="Place of Power (Lower Gauntlet)",
    arcanum="spirit",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="gauntlet",
    suggested_rote_skills=["academics", "expression", "survival"],
)
Rote.objects.create(
    name="Place of Power (Raise Gauntlet)",
    arcanum="spirit",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="gauntlet",
    suggested_rote_skills=["academics", "expression", "survival"],
)
Rote.objects.create(
    name="Reaching",
    arcanum="spirit",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="gauntlet",
    suggested_rote_skills=["athletics", "medicine", "socialize"],
)
Rote.objects.create(
    name="Rouse Spirit",
    arcanum="spirit",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["athletics", "expression", "investigation"],
)
Rote.objects.create(
    name="Spirit Summoning",
    arcanum="spirit",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["persuasion", "socialize", "occult"],
)
Rote.objects.create(
    name="Banishment",
    arcanum="spirit",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["brawl", "expression", "occult"],
)
Rote.objects.create(
    name="Bind Spirit",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["crafts", "brawl", "intimidation"],
)
Rote.objects.create(
    name="Craft Fetish",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["crafts", "occult", "persuasion"],
)
Rote.objects.create(
    name="Familiar",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "expression", "intimidate"],
)
Rote.objects.create(
    name="Shadow Scream",
    arcanum="spirit",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["expression", "firearms", "medicine"],
)
Rote.objects.create(
    name="Shape Spirit",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["crafts", "medicine", "persuasion"],
)
Rote.objects.create(
    name="Twilit Body",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "subterfuge", "survival"],
)
Rote.objects.create(
    name="World Walker",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="gaunlet",
    suggested_rote_skills=["athletics", "persuasion", "survival"],
)
Rote.objects.create(
    name="Annihilate Spirit",
    arcanum="spirit",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["intimidation", "science", "weaponry"],
)
Rote.objects.create(
    name="Birth Spirit",
    arcanum="spirit",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "medicine", "expression"],
)
Rote.objects.create(
    name="Create Locus",
    arcanum="spirit",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="gauntlet",
    suggested_rote_skills=["crafts", "empathy", "survival"],
)
Rote.objects.create(
    name="Essence Fountain",
    arcanum="spirit",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "expression", "occult"],
)
Rote.objects.create(
    name="Spirit Manse",
    arcanum="spirit",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "survival"],
)
Rote.objects.create(
    name="Divination",
    arcanum="time",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "empathy", "investigation"],
)
Rote.objects.create(
    name="Green Light/Red Light",
    arcanum="time",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["computer", "larceny", "subterfuge"],
)
Rote.objects.create(
    name="Momentary Flux",
    arcanum="time",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["investigation", "streetwise", "survival"],
)
Rote.objects.create(
    name="Perfect Timing",
    arcanum="time",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "socialize", "streetwise"],
)
Rote.objects.create(
    name="Postcognition",
    arcanum="time",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "empathy", "investigation"],
)
Rote.objects.create(
    name="Choose the Thread",
    arcanum="time",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["occult", "science", "subterfuge"],
)
Rote.objects.create(
    name="Constance Presence",
    arcanum="time",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "persuasion", "survival"],
)
Rote.objects.create(
    name="Hung Spell",
    arcanum="time",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "expression"],
)
Rote.objects.create(
    name="Shield of Chronos",
    arcanum="time",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "stealth", "subterfuge"],
)
Rote.objects.create(
    name="Tipping the Hourglass",
    arcanum="time",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["athletics", "crafts", "investigation"],
)
Rote.objects.create(
    name="Veil of Moments",
    arcanum="time",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["medicine", "investigation", "subterfuge"],
)
Rote.objects.create(
    name="Acceleration",
    arcanum="time",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    mana_cost=1,
    suggested_rote_skills=["athletics", "drive", "stealth"],
)
Rote.objects.create(
    name="Chronos' Curse",
    arcanum="time",
    level=3,
    practice="fraying",
    primary_factor="potency",
    mana_cost=1,
    withstand="stamina",
    suggested_rote_skills=["academics", "occult", "intimidation"],
)
Rote.objects.create(
    name="Shifting Sands",
    arcanum="time",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "occult", "survival"],
)
Rote.objects.create(
    name="Temporal Summoning",
    arcanum="time",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "investigation", "persuasion"],
)
Rote.objects.create(
    name="Weight of Years",
    arcanum="time",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "intimidation", "medicine"],
)
Rote.objects.create(
    name="Present as Past",
    arcanum="time",
    level=4,
    practice="patterning",
    primary_factor="potency",
    mana_cost=1,
    withstand="",
    suggested_rote_skills=["empathy", "investigation", "streetwise"],
)
Rote.objects.create(
    name="Prophecy",
    arcanum="time",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "expression", "investigation"],
)
Rote.objects.create(
    name="Rend Lifespan",
    arcanum="time",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "intimidation"],
)
Rote.objects.create(
    name="Rewrite History",
    arcanum="time",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["expression", "investigation", "persuasion"],
)
Rote.objects.create(
    name="Temporal Stutter",
    arcanum="time",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="stamina",
    suggested_rote_skills=["intimidation", "science", "survival"],
)
Rote.objects.create(
    name="Blink of an Eye",
    arcanum="time",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "crafts", "occult"],
)
Rote.objects.create(
    name="Corridors of Time",
    arcanum="time",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "investigation", "persuasion"],
)
Rote.objects.create(
    name="Temporal Pocket",
    arcanum="time",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "science", "stealth"],
)

Legacy.objects.create(
    name="The Eleventh Question",
    path=moros,
    order=guardians_of_the_veil,
    ruling_arcanum="time",
)
Legacy.objects.create(name="Walkers in Mists", path=acanthus, ruling_arcanum="space")
Legacy.objects.create(name="House of Ariadne", path=acanthus, ruling_arcanum="time")
Legacy.objects.create(
    name="Sisterhood of the Blessed", path=acanthus, ruling_arcanum="fate"
)
Legacy.objects.create(name="Pygmalion Society", path=acanthus, ruling_arcanum="mind")
Legacy.objects.create(name="Blank Badge", path=acanthus, ruling_arcanum="mind")
Legacy.objects.create(
    name="Carnival Melancholy",
    path=acanthus,
    ruling_arcanum="death",
    is_left_handed=True,
)
Legacy.objects.create(name="Clavicularius", path=mastigos, ruling_arcanum="spirit")
Legacy.objects.create(name="Bene Ashmedai", path=mastigos, ruling_arcanum="spirit")
Legacy.objects.create(
    name="Bearers of the Eternal Voice", path=mastigos, ruling_arcanum="mind"
)
Legacy.objects.create(name="Cryptologos", path=mastigos, ruling_arcanum="prime")
Legacy.objects.create(
    name="Brotherhood of the Demon Wind", path=mastigos, ruling_arcanum="time"
)
Legacy.objects.create(
    name="Legion", path=mastigos, ruling_arcanum="death", is_left_handed=True
)
Legacy.objects.create(name="Uncrowned Kings", path=moros, ruling_arcanum="mind")
Legacy.objects.create(name="Stone Scribes", path=moros, ruling_arcanum="time")
Legacy.objects.create(name="Bokor", path=moros, ruling_arcanum="death")
Legacy.objects.create(name="Forge Masters", path=moros, ruling_arcanum="prime")
Legacy.objects.create(
    name="Votaries of the Ordained", path=moros, ruling_arcanum="fate"
)
Legacy.objects.create(
    name="Logophages", path=moros, ruling_arcanum="prime", is_left_handed=True
)
Legacy.objects.create(name="Perfected Adepts", path=obrimos, ruling_arcanum="life")
Legacy.objects.create(name="Daksha", path=obrimos, ruling_arcanum="life")
Legacy.objects.create(name="Thrice-Great", path=obrimos, ruling_arcanum="spirit")
Legacy.objects.create(name="Tamers of Fire", path=obrimos, ruling_arcanum="mind")
Legacy.objects.create(
    name="Transhuman Engineers", path=obrimos, ruling_arcanum="matter"
)
Legacy.objects.create(
    name="Echo Walkers", path=obrimos, ruling_arcanum="life", is_left_handed=True
)
Legacy.objects.create(name="Orphans of Proteus", path=thyrsus, ruling_arcanum="life")
Legacy.objects.create(name="Dreamspeakers", path=thyrsus, ruling_arcanum="mind")
Legacy.objects.create(name="Illumined Path", path=thyrsus, ruling_arcanum="prime")
Legacy.objects.create(
    name="Keepers of the Covenant", path=thyrsus, ruling_arcanum="fate"
)
Legacy.objects.create(name="Chrysalides", path=thyrsus, ruling_arcanum="life")
Legacy.objects.create(
    name="Tamers of Blood", path=thyrsus, ruling_arcanum="space", is_left_handed=True
)

pf = ProximiFamily.objects.create(
    name="The Sisters of the Mountain", path=thyrsus, blessing_arcana="fate",
)
rotes = [
    "Oaths Fulfilled",
    "Exceptional Luck",
    "Shifting the Odds",
    "Monkey's Paw",
    "Shared Fate",
    "Cleanse the Body",
    "Analyze Life",
    "Body Control",
    "Lure and Repel",
    "Purge Illness",
    "Degrading the Form",
    "Honing the Form",
    "Knit",
    "Coaxing the Spirits",
    "Gremlins",
]
pf.set_possible_blessings([Rote.objects.get(name=x) for x in rotes])
