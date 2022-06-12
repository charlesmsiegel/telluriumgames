from time import time

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
Specialty.objects.create(skill="computer", name="Data Retrieval")
Specialty.objects.create(skill="computer", name="Digital Security")
Specialty.objects.create(skill="computer", name="Hacking")
Specialty.objects.create(skill="computer", name="Programming")
Specialty.objects.create(skill="computer", name="User Interface Design")
Specialty.objects.create(skill="crafts", name="Automotive")
Specialty.objects.create(skill="crafts", name="Carpentry")
Specialty.objects.create(skill="crafts", name="Jury Rigging")
Specialty.objects.create(skill="crafts", name="Sculpting")
Specialty.objects.create(skill="crafts", name="Welding")
Specialty.objects.create(skill="investigation", name="Crime Scenes")
Specialty.objects.create(skill="investigation", name="Cryptography")
Specialty.objects.create(skill="investigation", name="Dreams")
Specialty.objects.create(skill="investigation", name="Forensic Accounting")
Specialty.objects.create(skill="investigation", name="Riddles")
Specialty.objects.create(skill="medicine", name="Cardiology")
Specialty.objects.create(skill="medicine", name="First Aid")
Specialty.objects.create(skill="medicine", name="Pathology")
Specialty.objects.create(skill="medicine", name="Pharmacology")
Specialty.objects.create(skill="medicine", name="Surgery")
Specialty.objects.create(skill="occult", name="Eastern European Folktales")
Specialty.objects.create(skill="occult", name="Ghosts")
Specialty.objects.create(skill="occult", name="Mothman Sightings")
Specialty.objects.create(skill="occult", name="Psychic Phenomena")
Specialty.objects.create(skill="occult", name="Urban Legends")
Specialty.objects.create(skill="politics", name="Bureaucracy")
Specialty.objects.create(skill="politics", name="Local Politics")
Specialty.objects.create(skill="politics", name="National Politics")
Specialty.objects.create(skill="politics", name="Scandals")
Specialty.objects.create(skill="politics", name="Specific Political Party")
Specialty.objects.create(skill="science", name="Biology")
Specialty.objects.create(skill="science", name="Chemistry")
Specialty.objects.create(skill="science", name="Genetics")
Specialty.objects.create(skill="science", name="Optics")
Specialty.objects.create(skill="science", name="Particle Physics")
Specialty.objects.create(skill="athletics", name="Acrobatics")
Specialty.objects.create(skill="athletics", name="Basketball")
Specialty.objects.create(skill="athletics", name="Marathon Running")
Specialty.objects.create(skill="athletics", name="Rock Climbing")
Specialty.objects.create(skill="athletics", name="Throwing")
Specialty.objects.create(skill="brawl", name="Blocking")
Specialty.objects.create(skill="brawl", name="Boxing")
Specialty.objects.create(skill="brawl", name="Grappling")
Specialty.objects.create(skill="brawl", name="Muay Thai")
Specialty.objects.create(skill="brawl", name="Throws")
Specialty.objects.create(skill="drive", name="Evasion")
Specialty.objects.create(skill="drive", name="Motorcycles")
Specialty.objects.create(skill="drive", name="Piloting")
Specialty.objects.create(skill="drive", name="Racing")
Specialty.objects.create(skill="drive", name="Stunts")
Specialty.objects.create(skill="firearms", name="Fast-Draw")
Specialty.objects.create(skill="firearms", name="Handguns")
Specialty.objects.create(skill="firearms", name="Rifles")
Specialty.objects.create(skill="firearms", name="Shotguns")
Specialty.objects.create(skill="firearms", name="Sniping")
Specialty.objects.create(skill="larceny", name="Alarm Systems")
Specialty.objects.create(skill="larceny", name="Breaking and Entering")
Specialty.objects.create(skill="larceny", name="Lock Picking")
Specialty.objects.create(skill="larceny", name="Safecracking")
Specialty.objects.create(skill="larceny", name="Sleight of Hand")
Specialty.objects.create(skill="stealth", name="Crowds")
Specialty.objects.create(skill="stealth", name="Hiding")
Specialty.objects.create(skill="stealth", name="Moving Quietly")
Specialty.objects.create(skill="stealth", name="Shadowing")
Specialty.objects.create(skill="stealth", name="Stakeouts")
Specialty.objects.create(skill="survival", name="Foraging")
Specialty.objects.create(skill="survival", name="Hunting")
Specialty.objects.create(skill="survival", name="NAvigation")
Specialty.objects.create(skill="survival", name="Shelter")
Specialty.objects.create(skill="survival", name="Weather")
Specialty.objects.create(skill="weaponry", name="Clubs")
Specialty.objects.create(skill="weaponry", name="Duels")
Specialty.objects.create(skill="weaponry", name="Improvised Weapons")
Specialty.objects.create(skill="weaponry", name="Knives")
Specialty.objects.create(skill="weaponry", name="Swords")
Specialty.objects.create(skill="animal_ken", name="Dogs")
Specialty.objects.create(skill="animal_ken", name="Exotic Pets")
Specialty.objects.create(skill="animal_ken", name="Horses")
Specialty.objects.create(skill="animal_ken", name="Training")
Specialty.objects.create(skill="animal_ken", name="Wild Animals")
Specialty.objects.create(skill="empathy", name="Buried Feelings")
Specialty.objects.create(skill="empathy", name="Calming")
Specialty.objects.create(skill="empathy", name="Emotions")
Specialty.objects.create(skill="empathy", name="Lies")
Specialty.objects.create(skill="empathy", name="Motives")
Specialty.objects.create(skill="expression", name="Dance")
Specialty.objects.create(skill="expression", name="Journalism")
Specialty.objects.create(skill="expression", name="Music Composition")
Specialty.objects.create(skill="expression", name="Painting")
Specialty.objects.create(skill="expression", name="Speeches")
Specialty.objects.create(skill="intimidation", name="Direct Threats")
Specialty.objects.create(skill="intimidation", name="Interrogation")
Specialty.objects.create(skill="intimidation", name="Murderous Stare")
Specialty.objects.create(skill="intimidation", name="Torture")
Specialty.objects.create(skill="intimidation", name="Veiled Threats")
Specialty.objects.create(skill="persuasion", name="Fast Talking")
Specialty.objects.create(skill="persuasion", name="Inspiring")
Specialty.objects.create(skill="persuasion", name="Sales Pitches")
Specialty.objects.create(skill="persuasion", name="Seduction")
Specialty.objects.create(skill="persuasion", name="Sermons")
Specialty.objects.create(skill="socialize", name="Bar hopping")
Specialty.objects.create(skill="socialize", name="College parties")
Specialty.objects.create(skill="socialize", name="Formal events")
Specialty.objects.create(skill="socialize", name="Political Fundraisers")
Specialty.objects.create(skill="socialize", name="Private clubs")
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
    prereqs=[("athletics", 3), ("wits", 3), ("stamina", 3)],
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
    name="Fighting Finesse",
    requires_detail=True,
    ratings=[2],
    prereqs=[[("dexterity", 2), ("weaponry", "specialty")]],
    possible_details=[],
    merit_type="Fighting",
)
Merit.objects.create(
    name="Fighting Finesse",
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
