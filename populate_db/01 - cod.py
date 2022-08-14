from time import time

from cod.models.characters.ephemera import Numina
from cod.models.characters.mage import (
    Attainment,
    Legacy,
    Order,
    Path,
    ProximiFamily,
    CoDRote,
)
from cod.models.characters.mortal import Condition, CoDMerit, CoDSpecialty, Tilt
from cod.models.items.mortal import Equipment
from core.models import Language, Material

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

CoDSpecialty.objects.create(skill="academics", name="English Literature")
CoDSpecialty.objects.create(skill="academics", name="History")
CoDSpecialty.objects.create(skill="academics", name="Law")
CoDSpecialty.objects.create(skill="academics", name="Linguistics")
CoDSpecialty.objects.create(skill="academics", name="Research")
CoDSpecialty.objects.create(skill="academics", name="Anthropology")
CoDSpecialty.objects.create(skill="academics", name="Art History")
CoDSpecialty.objects.create(skill="academics", name="Literature")
CoDSpecialty.objects.create(skill="academics", name="Religion")
CoDSpecialty.objects.create(skill="academics", name="Translation")
CoDSpecialty.objects.create(skill="computer", name="Data Retrieval")
CoDSpecialty.objects.create(skill="computer", name="Digital Security")
CoDSpecialty.objects.create(skill="computer", name="Hacking")
CoDSpecialty.objects.create(skill="computer", name="Programming")
CoDSpecialty.objects.create(skill="computer", name="User Interface Design")
CoDSpecialty.objects.create(skill="computer", name="Graphics")
CoDSpecialty.objects.create(skill="computer", name="Internet")
CoDSpecialty.objects.create(skill="computer", name="Security")
CoDSpecialty.objects.create(skill="computer", name="Social Media")
CoDSpecialty.objects.create(skill="crafts", name="Automotive")
CoDSpecialty.objects.create(skill="crafts", name="Carpentry")
CoDSpecialty.objects.create(skill="crafts", name="Jury Rigging")
CoDSpecialty.objects.create(skill="crafts", name="Sculpting")
CoDSpecialty.objects.create(skill="crafts", name="Welding")
CoDSpecialty.objects.create(skill="crafts", name="Cosmetics")
CoDSpecialty.objects.create(skill="crafts", name="Fashion")
CoDSpecialty.objects.create(skill="crafts", name="Forging")
CoDSpecialty.objects.create(skill="crafts", name="Graffiti")
CoDSpecialty.objects.create(skill="crafts", name="Painting")
CoDSpecialty.objects.create(skill="crafts", name="Perfumery")
CoDSpecialty.objects.create(skill="crafts", name="Repair")
CoDSpecialty.objects.create(skill="crafts", name="Sculpting")
CoDSpecialty.objects.create(skill="investigation", name="Crime Scenes")
CoDSpecialty.objects.create(skill="investigation", name="Cryptography")
CoDSpecialty.objects.create(skill="investigation", name="Dreams")
CoDSpecialty.objects.create(skill="investigation", name="Forensic Accounting")
CoDSpecialty.objects.create(skill="investigation", name="Riddles")
CoDSpecialty.objects.create(skill="investigation", name="Artifacts")
CoDSpecialty.objects.create(skill="investigation", name="Autopsy")
CoDSpecialty.objects.create(skill="investigation", name="Body Language")
CoDSpecialty.objects.create(skill="investigation", name="Lab Work")
CoDSpecialty.objects.create(skill="medicine", name="Cardiology")
CoDSpecialty.objects.create(skill="medicine", name="First Aid")
CoDSpecialty.objects.create(skill="medicine", name="Pathology")
CoDSpecialty.objects.create(skill="medicine", name="Pharmacology")
CoDSpecialty.objects.create(skill="medicine", name="Surgery")
CoDSpecialty.objects.create(skill="medicine", name="Physical Therapy")
CoDSpecialty.objects.create(skill="occult", name="Eastern European Folktales")
CoDSpecialty.objects.create(skill="occult", name="Ghosts")
CoDSpecialty.objects.create(skill="occult", name="Mothman Sightings")
CoDSpecialty.objects.create(skill="occult", name="Psychic Phenomena")
CoDSpecialty.objects.create(skill="occult", name="Urban Legends")
CoDSpecialty.objects.create(skill="occult", name="The Astral Realm")
CoDSpecialty.objects.create(skill="occult", name="Casting Lots")
CoDSpecialty.objects.create(skill="occult", name="Cryptids")
CoDSpecialty.objects.create(skill="occult", name="Fortean Phenomena")
CoDSpecialty.objects.create(skill="occult", name="Proximi")
CoDSpecialty.objects.create(skill="occult", name="Sleepwalkers")
CoDSpecialty.objects.create(skill="occult", name="Goetia")
CoDSpecialty.objects.create(skill="occult", name="Phrenology")
CoDSpecialty.objects.create(skill="occult", name="Spirits")
CoDSpecialty.objects.create(skill="occult", name="Superstition")
CoDSpecialty.objects.create(skill="politics", name="Bureaucracy")
CoDSpecialty.objects.create(skill="politics", name="Local Politics")
CoDSpecialty.objects.create(skill="politics", name="National Politics")
CoDSpecialty.objects.create(skill="politics", name="Scandals")
CoDSpecialty.objects.create(skill="politics", name="Specific Political Party")
CoDSpecialty.objects.create(skill="politics", name="Church")
CoDSpecialty.objects.create(skill="politics", name="Consilium")
CoDSpecialty.objects.create(skill="politics", name="Democratic")
CoDSpecialty.objects.create(skill="politics", name="Local")
CoDSpecialty.objects.create(skill="politics", name="Order")
CoDSpecialty.objects.create(skill="politics", name="Organized Crime")
CoDSpecialty.objects.create(skill="science", name="Biology")
CoDSpecialty.objects.create(skill="science", name="Chemistry")
CoDSpecialty.objects.create(skill="science", name="Genetics")
CoDSpecialty.objects.create(skill="science", name="Optics")
CoDSpecialty.objects.create(skill="science", name="Particle Physics")
CoDSpecialty.objects.create(skill="science", name="Physics")
CoDSpecialty.objects.create(skill="science", name="Neuroscience")
CoDSpecialty.objects.create(skill="science", name="Virology")
CoDSpecialty.objects.create(skill="science", name="Alchemy")
CoDSpecialty.objects.create(skill="science", name="Hematology")
CoDSpecialty.objects.create(skill="athletics", name="Acrobatics")
CoDSpecialty.objects.create(skill="athletics", name="Basketball")
CoDSpecialty.objects.create(skill="athletics", name="Marathon Running")
CoDSpecialty.objects.create(skill="athletics", name="Rock Climbing")
CoDSpecialty.objects.create(skill="athletics", name="Throwing")
CoDSpecialty.objects.create(skill="athletics", name="Aimed Spells")
CoDSpecialty.objects.create(skill="athletics", name="Archery")
CoDSpecialty.objects.create(skill="athletics", name="Climbing")
CoDSpecialty.objects.create(skill="athletics", name="Jumping")
CoDSpecialty.objects.create(skill="athletics", name="Parkour")
CoDSpecialty.objects.create(skill="athletics", name="Swimming")
CoDSpecialty.objects.create(skill="brawl", name="Blocking")
CoDSpecialty.objects.create(skill="brawl", name="Boxing")
CoDSpecialty.objects.create(skill="brawl", name="Grappling")
CoDSpecialty.objects.create(skill="brawl", name="Muay Thai")
CoDSpecialty.objects.create(skill="brawl", name="Throws")
CoDSpecialty.objects.create(skill="brawl", name="Biting")
CoDSpecialty.objects.create(skill="brawl", name="Claws")
CoDSpecialty.objects.create(skill="brawl", name="Dirty Fighting")
CoDSpecialty.objects.create(skill="brawl", name="Martial Arts")
CoDSpecialty.objects.create(skill="brawl", name="Threats")
CoDSpecialty.objects.create(skill="drive", name="Evasion")
CoDSpecialty.objects.create(skill="drive", name="Motorcycles")
CoDSpecialty.objects.create(skill="drive", name="Piloting")
CoDSpecialty.objects.create(skill="drive", name="Racing")
CoDSpecialty.objects.create(skill="drive", name="Stunts")
CoDSpecialty.objects.create(skill="drive", name="Defensive Driving")
CoDSpecialty.objects.create(skill="drive", name="Off-Road Driving")
CoDSpecialty.objects.create(skill="drive", name="Pursuit")
CoDSpecialty.objects.create(skill="firearms", name="Fast-Draw")
CoDSpecialty.objects.create(skill="firearms", name="Handguns")
CoDSpecialty.objects.create(skill="firearms", name="Rifles")
CoDSpecialty.objects.create(skill="firearms", name="Shotguns")
CoDSpecialty.objects.create(skill="firearms", name="Sniping")
CoDSpecialty.objects.create(skill="firearms", name="Trick Shots")
CoDSpecialty.objects.create(skill="larceny", name="Alarm Systems")
CoDSpecialty.objects.create(skill="larceny", name="Breaking and Entering")
CoDSpecialty.objects.create(skill="larceny", name="Lock Picking")
CoDSpecialty.objects.create(skill="larceny", name="Safecracking")
CoDSpecialty.objects.create(skill="larceny", name="Sleight of Hand")
CoDSpecialty.objects.create(skill="larceny", name="Concealment")
CoDSpecialty.objects.create(skill="larceny", name="Pickpocketing")
CoDSpecialty.objects.create(skill="larceny", name="Security Systems")
CoDSpecialty.objects.create(skill="stealth", name="Crowds")
CoDSpecialty.objects.create(skill="stealth", name="Hiding")
CoDSpecialty.objects.create(skill="stealth", name="Moving Quietly")
CoDSpecialty.objects.create(skill="stealth", name="Shadowing")
CoDSpecialty.objects.create(skill="stealth", name="Stakeouts")
CoDSpecialty.objects.create(skill="stealth", name="Camouflage")
CoDSpecialty.objects.create(skill="stealth", name="In Plain Sight")
CoDSpecialty.objects.create(skill="stealth", name="Rural")
CoDSpecialty.objects.create(skill="stealth", name="Staying Motionless")
CoDSpecialty.objects.create(skill="survival", name="Foraging")
CoDSpecialty.objects.create(skill="survival", name="Hunting")
CoDSpecialty.objects.create(skill="survival", name="Navigation")
CoDSpecialty.objects.create(skill="survival", name="Shelter")
CoDSpecialty.objects.create(skill="survival", name="Weather")
CoDSpecialty.objects.create(skill="weaponry", name="Clubs")
CoDSpecialty.objects.create(skill="weaponry", name="Duels")
CoDSpecialty.objects.create(skill="weaponry", name="Improvised Weapons")
CoDSpecialty.objects.create(skill="weaponry", name="Knives")
CoDSpecialty.objects.create(skill="weaponry", name="Swords")
CoDSpecialty.objects.create(skill="weaponry", name="Chains")
CoDSpecialty.objects.create(skill="weaponry", name="Spears")
CoDSpecialty.objects.create(skill="animal_ken", name="Dogs")
CoDSpecialty.objects.create(skill="animal_ken", name="Exotic Pets")
CoDSpecialty.objects.create(skill="animal_ken", name="Horses")
CoDSpecialty.objects.create(skill="animal_ken", name="Training")
CoDSpecialty.objects.create(skill="animal_ken", name="Wild Animals")
CoDSpecialty.objects.create(skill="animal_ken", name="Cats")
CoDSpecialty.objects.create(skill="animal_ken", name="Reptiles")
CoDSpecialty.objects.create(skill="animal_ken", name="Soothing")
CoDSpecialty.objects.create(skill="animal_ken", name="Threatening")
CoDSpecialty.objects.create(skill="empathy", name="Buried Feelings")
CoDSpecialty.objects.create(skill="empathy", name="Calming")
CoDSpecialty.objects.create(skill="empathy", name="Emotions")
CoDSpecialty.objects.create(skill="empathy", name="Lies")
CoDSpecialty.objects.create(skill="empathy", name="Motives")
CoDSpecialty.objects.create(skill="empathy", name="Personalities")
CoDSpecialty.objects.create(skill="expression", name="Dance")
CoDSpecialty.objects.create(skill="expression", name="Journalism")
CoDSpecialty.objects.create(skill="expression", name="Music Composition")
CoDSpecialty.objects.create(skill="expression", name="Painting")
CoDSpecialty.objects.create(skill="expression", name="Speeches")
CoDSpecialty.objects.create(skill="expression", name="Drama")
CoDSpecialty.objects.create(skill="expression", name="Musical Instrument")
CoDSpecialty.objects.create(skill="expression", name="Performance Art")
CoDSpecialty.objects.create(skill="expression", name="Singing")
CoDSpecialty.objects.create(skill="intimidation", name="Direct Threats")
CoDSpecialty.objects.create(skill="intimidation", name="Interrogation")
CoDSpecialty.objects.create(skill="intimidation", name="Murderous Stare")
CoDSpecialty.objects.create(skill="intimidation", name="Torture")
CoDSpecialty.objects.create(skill="intimidation", name="Veiled Threats")
CoDSpecialty.objects.create(skill="intimidation", name="Stare Down")
CoDSpecialty.objects.create(skill="persuasion", name="Fast Talking")
CoDSpecialty.objects.create(skill="persuasion", name="Inspiring")
CoDSpecialty.objects.create(skill="persuasion", name="Sales Pitches")
CoDSpecialty.objects.create(skill="persuasion", name="Seduction")
CoDSpecialty.objects.create(skill="persuasion", name="Sermons")
CoDSpecialty.objects.create(skill="persuasion", name="Confidence Scam")
CoDSpecialty.objects.create(skill="socialize", name="Bar hopping")
CoDSpecialty.objects.create(skill="socialize", name="College parties")
CoDSpecialty.objects.create(skill="socialize", name="Formal events")
CoDSpecialty.objects.create(skill="socialize", name="Political Fundraisers")
CoDSpecialty.objects.create(skill="socialize", name="Private clubs")
CoDSpecialty.objects.create(skill="socialize", name="Church Lock-In")
CoDSpecialty.objects.create(skill="socialize", name="Dress Balls")
CoDSpecialty.objects.create(skill="socialize", name="Frat Parties")
CoDSpecialty.objects.create(skill="socialize", name="The Club")
CoDSpecialty.objects.create(skill="streetwise", name="Black market")
CoDSpecialty.objects.create(skill="streetwise", name="Gangs")
CoDSpecialty.objects.create(skill="streetwise", name="Navigation")
CoDSpecialty.objects.create(skill="streetwise", name="Rumors")
CoDSpecialty.objects.create(skill="streetwise", name="Undercover work")
CoDSpecialty.objects.create(skill="subterfuge", name="Detecting lies")
CoDSpecialty.objects.create(skill="subterfuge", name="Hidden meanings")
CoDSpecialty.objects.create(skill="subterfuge", name="Hiding emotions")
CoDSpecialty.objects.create(skill="subterfuge", name="Long cons")
CoDSpecialty.objects.create(skill="subterfuge", name="Misdirection")
CoDSpecialty.objects.create(skill="subterfuge", name="Doublespeak")
CoDSpecialty.objects.create(skill="subterfuge", name="Little White Lies")

Condition.objects.create(
    name="Amnesia",
    persistent=True,
    resolution="Something problematic arises, such as a forgotten arrest warrant or an old enemy",
)
Condition.objects.create(
    name="Blind", persistent=True, resolution="Your character regains her sight",
)
Condition.objects.create(
    name="Broken",
    persistent=True,
    resolution="Regain a dot of Integrity or Wisdom, lose another dot of Integrity or Wisdom, or achieve an exceptional success on a breaking point or Act of Hubris",
)
Condition.objects.create(
    name="Bonded", persistent=False, resolution="The bonded animal dies"
)
Condition.objects.create(
    name="Connected", persistent=True, resolution="Condition shed, bridge burned"
)
Condition.objects.create(name="Crippled", persistent=True, resolution="")
Condition.objects.create(
    name="Deprived",
    persistent=False,
    resolution="Indulge in the deprived Vice, therapy",
)
Condition.objects.create(
    name="Embarrassing Secret", persistent=False, resolution="The secret gets out"
)
Condition.objects.create(
    name="Fugue",
    persistent=True,
    resolution="Regain a dot of Integrity or Wisdom, lose another dot of Integrity or Wisdom, or achieve an exceptional success on a breaking point or Act of Hubris",
)
Condition.objects.create(
    name="Guilty",
    persistent=False,
    resolution="The character makes restitution or confesses",
)
Condition.objects.create(
    name="Informed", persistent=False, resolution="Use the Condition for its benefit"
)
Condition.objects.create(
    name="Inspired", persistent=False, resolution="Use the Condition for its benefit"
)
Condition.objects.create(
    name="Leveraged",
    persistent=False,
    resolution="Turn the tables, do what is asked by the person with leverage",
)
Condition.objects.create(
    name="Lost",
    persistent=False,
    resolution="Abandoning the goal, successfully navigating",
)
Condition.objects.create(
    name="Madness",
    persistent=True,
    resolution="Regain a dot of Integrity or Wisdom, lose another dot of Integrity or Wisdom, or achieve an exceptional success on a breaking point or Act of Hubris",
)
Condition.objects.create(name="Mute", persistent=True, resolution="Regains voice.")
Condition.objects.create(
    name="Notoriety",
    persistent=False,
    resolution="The story is debunked or the character's name is cleared",
)
Condition.objects.create(
    name="Obsession", persistent=False, resolution="Fulfilling the obsession, therapy"
)
Condition.objects.create(
    name="Shaken", persistent=False, resolution="Fail a roll as noted"
)
Condition.objects.create(name="Soulless", persistent=True, resolution="Regain soul")
Condition.objects.create(
    name="Spooked",
    persistent=False,
    resolution="Shed when the character does something that hinders teh group or complicates things due to the Condition.",
)
Condition.objects.create(
    name="Steadfast", persistent=False, resolution="Use the Condition, as noted"
)
Condition.objects.create(
    name="Swooned",
    persistent=False,
    resolution="Do something for the object that puts your character in danger, opt to fail a roll to resist a social action by the object",
)

Condition.objects.create(
    name="Addicted",
    persistent=True,
    resolution="Regain a dot of Integrity or Wisdom, lose another dot of Integrity or Wisdom, or achieve an exceptional success on a breaking point or Act of Hubris",
)
Condition.objects.create(
    name="Charmed",
    persistent=False,
    resolution="Your character narrowly avoids some misfortune or enjoys a lucky break; the Condition is resolved as described in MtAw page 315",
)
Condition.objects.create(
    name="Defeated",
    persistent=False,
    resolution="This Condition lingers until the character can greatly humble himself in public at great personal cost or until the winner of the Duel takes advantage of the sympathy in a way that injures or abuses the loser.",
)
Condition.objects.create(
    name="Disabled", persistent=True, resolution="Disability is cured in some way",
)
Condition.objects.create(
    name="Enervated",
    persistent=True,
    resolution="Only cured if the character regains her soul.",
)
Condition.objects.create(
    name="Humbled",
    persistent=False,
    resolution="The character sacrifices of himself in dramatic fashion in the name of the person or symbol that humbled him in the first place.",
)
Condition.objects.create(
    name="Megalomaniacal",
    persistent=False,
    resolution="Hurt someone important to you in such a way that it risks further Wisdom loss",
)
Condition.objects.create(
    name="Mystery Commands",
    persistent=True,
    resolution="Your character cuts off ties to her Exarch. Traitors are not tolerated, and other characters with this Condition will be sent to punish her, or kill her if she will not return to the Throne's service",
)
Condition.objects.create(
    name="Rampant", persistent=False, resolution="Suffer a Paradox",
)
Condition.objects.create(
    name="Strained",
    persistent=False,
    resolution="The character suffers Integrity loss. Take an additional Beat atop that of the breaking point.",
)
Condition.objects.create(
    name="Soulless", persistent=True, resolution="Regain a soul",
)
Condition.objects.create(
    name="Soul Shocked", persistent=False, resolution="Regain full Willpower",
)
Condition.objects.create(
    name="Thrall", persistent=True, resolution="Regain a soul",
)
Condition.objects.create(
    name="Triumphant",
    persistent=False,
    resolution="The first time you fail a Social roll with a member of Awakened society, take a Beat and the Condition ends.",
)


CoDMerit.objects.create(
    name="Area of Expertise",
    requires_detail=True,
    ratings=[1],
    prereqs=[[("resolve", 2)]],
    merit_type="Mental",
    possible_details=[],
)
CoDMerit.objects.create(
    name="Common Sense", ratings=[3], merit_type="Mental",
)
CoDMerit.objects.create(
    name="Danger Sense", ratings=[2], merit_type="Mental",
)
CoDMerit.objects.create(
    name="Direction Sense", ratings=[1], merit_type="Mental",
)
CoDMerit.objects.create(
    name="Eidetic Memory", ratings=[2], merit_type="Mental",
)
CoDMerit.objects.create(
    name="Encyclopedia Knowledge",
    requires_detail=True,
    ratings=[2],
    possible_details=SKILLS,
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Eye for the Strange",
    ratings=[2],
    prereqs=[[("resolve", 2), ("occult", 1)]],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Fast Reflexes",
    ratings=[1, 2, 3],
    prereqs=[[("wits", 3)], [("dexterity", 3)]],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Good Time Management",
    ratings=[1],
    prereqs=[[("academics", 2)]],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Good Time Management",
    ratings=[1],
    prereqs=[[("science", 2)]],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Holistic Awareness", ratings=[1], merit_type="Mental",
)
CoDMerit.objects.create(
    name="Indomitable", ratings=[2], merit_type="Mental",
)
CoDMerit.objects.create(
    name="Interdisciplinary Specialty",
    requires_detail=True,
    ratings=[1],
    prereqs=[[("specialty", 3)]],
    possible_details=[],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Investigative Aide",
    requires_detail=True,
    ratings=[1],
    prereqs=[[("skill", 3)]],
    possible_details=[],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Language",
    requires_detail=True,
    ratings=[1],
    possible_details=[x.name for x in Language.objects.all()],
    merit_type="Mental",
)
CoDMerit.objects.create(
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
CoDMerit.objects.create(
    name="Library, Advanced",
    ratings=[1, 2, 3],
    prereqs=[[("Library", 3), ("Safe Place", 1)]],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Meditative Mind", ratings=[1, 2, 4], merit_type="Mental",
)
CoDMerit.objects.create(
    name="Multilingual",
    requires_detail=True,
    ratings=[1],
    possible_details=[],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Patient", ratings=[1], merit_type="Mental",
)
CoDMerit.objects.create(
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
CoDMerit.objects.create(
    name="Tolerance for Biology",
    ratings=[1],
    prereqs=[[("resolve", 3)]],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Trained Observer",
    ratings=[1, 3],
    prereqs=[[("wits", 3)], [("composure", 3)]],
    merit_type="Mental",
)
CoDMerit.objects.create(
    name="Vice-Ridden", ratings=[2], merit_type="Mental",
)
CoDMerit.objects.create(
    name="Virtuous", ratings=[2], merit_type="Mental",
)
CoDMerit.objects.create(
    name="Ambidextrous", ratings=[3], merit_type="Physical",
)
CoDMerit.objects.create(
    name="Automotive Genius",
    ratings=[1],
    prereqs=[[("crafts", 3), ("drive", 1), ("science", 1)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Crack Driver",
    ratings=[2, 3],
    prereqs=[[("drive", 3)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Demolisher",
    ratings=[1, 2, 3],
    prereqs=[[("strength", 3)], [("intelligence", 3)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Double Jointed",
    ratings=[2],
    prereqs=[[("dexterity", 3)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Fleet of Foot",
    ratings=[1, 2, 3],
    prereqs=[[("athletics", 2)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Giant", ratings=[4], merit_type="Physical",
)
CoDMerit.objects.create(
    name="Hardy", ratings=[1, 2, 3], prereqs=[[("stamina", 3)]], merit_type="Physical",
)
CoDMerit.objects.create(
    name="Greyhound",
    ratings=[1],
    prereqs=[[("athletics", 3), ("wits", 3), ("stamina", 3)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Iron Stamina",
    ratings=[1, 2, 3],
    prereqs=[[("stamina", 3)], [("resolve", 3)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Parkour",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("dexterity", 3), ("athletics", 2)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Quick Draw (Weaponry)",
    requires_detail=False,
    ratings=[1],
    prereqs=[[("wits", 3), ("weaponry", "specialty")]],
    possible_details=[],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Quick Draw (Firearms)",
    requires_detail=False,
    ratings=[1],
    prereqs=[[("wits", 3), ("firearms", "specialty")]],
    possible_details=[],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Relentless",
    ratings=[1],
    prereqs=[[("athletics", 2), ("stamina", 3)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Seizing the Edge",
    ratings=[2],
    prereqs=[[("wits", 3), ("composure", 3)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Sleight of Hand",
    ratings=[2],
    prereqs=[[("larceny", 3)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Small-Framed", ratings=[2], merit_type="Physical",
)
CoDMerit.objects.create(
    name="Stunt Driver",
    is_style=True,
    ratings=[1, 2, 3, 4],
    prereqs=[[("dexterity", 3), ("drive", 3), ("wits", 3)]],
    merit_type="Physical",
)
CoDMerit.objects.create(
    name="Allies",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Alternate Identity",
    requires_detail=True,
    ratings=[1, 2, 3],
    possible_details=[],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Anonymity", ratings=[1, 2, 3, 4, 5], merit_type="Social",
)
CoDMerit.objects.create(
    name="Barfly", ratings=[2], prereqs=[[("socialize", 2)]], merit_type="Social",
)
CoDMerit.objects.create(
    name="Closed Book",
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("manipulation", 3), ("resolve", 3)]],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Contacts",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Fame", ratings=[1, 2, 3], merit_type="Social",
)
CoDMerit.objects.create(
    name="Fast-Talking",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("manipulation", 3), ("subterfuge", 2)]],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Fixer",
    ratings=[2],
    prereqs=[[("wits", 3), ("Contacts", 2)]],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Hobbyist Clique",
    requires_detail=True,
    ratings=[2],
    prereqs=[[("skill", 2)]],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Inspiring", ratings=[3], prereqs=[[("presence", 3)]], merit_type="Social",
)
iron_will = CoDMerit.objects.create(
    name="Iron Will", ratings=[2], prereqs=[[("resolve", 4)]], merit_type="Social",
)
CoDMerit.objects.create(
    name="Mystery Cult Initiation",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Mentor",
    requires_detail=False,
    ratings=[1, 2, 3, 4, 5],
    possible_details=SKILLS,
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Pusher", ratings=[1], prereqs=[[("persuasion", 2)]], merit_type="Social",
)
CoDMerit.objects.create(
    name="Resources", ratings=[1, 2, 3, 4,], merit_type="Social",
)
CoDMerit.objects.create(
    name="Retainer",
    requires_detail=True,
    ratings=[1, 2, 3, 4, 5],
    possible_details=[],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Safe Place", ratings=[1, 2, 3, 4, 5], merit_type="Social",
)
CoDMerit.objects.create(
    name="Small Unit Tactics",
    ratings=[2],
    prereqs=[[("presence", 3)]],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Spin Doctor",
    ratings=[1],
    prereqs=[[("manipulation", 3), ("subterfuge", 2)]],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Staff",
    requires_detail=True,
    ratings=[1],
    possible_details=SKILLS,
    merit_type="Social",
)
CoDMerit.objects.create(
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
CoDMerit.objects.create(
    name="Striking Looks", ratings=[1, 2], merit_type="Social",
)
CoDMerit.objects.create(
    name="Sympathetic", ratings=[2], merit_type="Social",
)
CoDMerit.objects.create(
    name="Table Turner",
    ratings=[1],
    prereqs=[[("composure", 3), ("manipulation", 3), ("wits", 3)]],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Takes One to Know One", ratings=[1], merit_type="Social",
)
CoDMerit.objects.create(
    name="Taste",
    ratings=[1],
    prereqs=[
        [("crafts", 2), ("crafts", "specialty")],
        [("crafts", 2), ("expression", "specialty")],
    ],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="True Friend", ratings=[3], merit_type="Social",
)
CoDMerit.objects.create(
    name="Untouchable",
    ratings=[1],
    prereqs=[[("manipulation", 3), ("subterfuge", 2)]],
    merit_type="Social",
)
CoDMerit.objects.create(
    name="Aura Reading", ratings=[3], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Automatic Writing", ratings=[2], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Biokinesis", ratings=[1, 2, 3, 4, 5], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Clairvoyance", ratings=[3], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Cursed", ratings=[2], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Laying on Hands", ratings=[3], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Medium", ratings=[3], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Mind of a Madman",
    ratings=[2],
    prereqs=[[("empathy", 3)]],
    merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Omen Sensitivity", ratings=[3], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Numbing Touch", ratings=[1, 2, 3, 4, 5], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Psychokinesis", ratings=[3, 5], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Psychometry", ratings=[3], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Telekinesis", ratings=[1, 2, 3, 4, 5], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Telepathy", ratings=[3, 5], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Thief of Fate", ratings=[3], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Unseen Sense", ratings=[2], merit_type="Supernatural",
)
CoDMerit.objects.create(
    name="Armed Defense",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("dexterity", 3), ("weaponry", 2), ("Defensive Combat (Weaponry)", 1)]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Cheap Shot",
    ratings=[2],
    prereqs=[[("subterfuge", 2), ("Street Fighting", 3)]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Choke Hold", ratings=[2], prereqs=[[("brawl", 2)]], merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Close Quarters Combat",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("wits", 3), ("athletics", 2), ("brawl", 3)]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Defensive Combat (Weaponry)",
    ratings=[1],
    prereqs=[[("weaponry", 1)]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Defensive Combat (Brawl)",
    ratings=[1],
    prereqs=[[("brawl", 1)]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Fighting Finesse (Weaponry)",
    requires_detail=True,
    ratings=[2],
    prereqs=[[("dexterity", 2), ("weaponry", "specialty")]],
    possible_details=[],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Fighting Finesse (Brawl)",
    requires_detail=True,
    ratings=[2],
    prereqs=[[("dexterity", 2), ("brawl", "specialty")]],
    possible_details=[],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Firefight",
    is_style=True,
    ratings=[1, 2, 3],
    prereqs=[[("composure", 3), ("dexterity", 3), ("athletics", 2), ("firearms", 2),]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Grappling",
    is_style=True,
    ratings=[1, 2, 3],
    prereqs=[[("stamina", 3), ("strength", 2), ("athletics", 2), ("brawl", 2),]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Heavy Weapons",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("stamina", 3), ("strength", 3), ("athletics", 2), ("weaponry", 2),]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Improvised Weaponry",
    is_style=True,
    ratings=[1, 2, 3],
    prereqs=[[("wits", 3), ("weaponry", 1)]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Iron Skin",
    ratings=[2, 4],
    prereqs=[
        [("stamina", 3), ("Martial Arts", 2)],
        [("stamina", 3), ("Street Fighting", 2)],
    ],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Light Weapons",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[
        [("wits", 3), ("dexterity", 3), ("athletics", 2), ("weaponry", 2),],
        [("dexterity", 3), ("athletics", 2), ("weaponry", 2), ("Fighting Finesse", 1)],
    ],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Marksmanship",
    is_style=True,
    ratings=[1, 2, 3, 4],
    prereqs=[[("composure", 3), ("resolve", 3), ("firearms", 2)]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Martial Arts",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("resolve", 3), ("dexterity", 3), ("athletics", 2), ("brawl", 2),]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Police Tactics",
    is_style=True,
    ratings=[1, 2, 3],
    prereqs=[[("brawl", 2), ("weaponry", 1)]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Shiv",
    ratings=[1, 2],
    prereqs=[[("weaponry", 1), ("Street Fighting", 2)]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Street Fighting",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("stamina", 3), ("composure", 3), ("brawl", 2), ("streetwise", 2),]],
    merit_type="Fighting",
)
CoDMerit.objects.create(
    name="Unarmed Defense",
    is_style=True,
    ratings=[1, 2, 3, 4, 5],
    prereqs=[[("dexterity", 3), ("brawl", 2), ("Defensive Combat (Brawl)", 1)]],
    merit_type="Fighting",
)


acanthus = Path.objects.create(
    name="Acanthus",
    ruling_arcana=["fate", "time"],
    inferior_arcanum="forces",
    path_weapons=["Knife", "Rapier", "Bow"],
)
acanthus.path_materials.set(
    Material.objects.filter(name__in=["Glass", "Crystal", "Silver"])
)
acanthus.save()
mastigos = Path.objects.create(
    name="Mastigos",
    ruling_arcana=["mind", "space"],
    inferior_arcanum="matter",
    path_weapons=["Knife", "Curved Sword", "Whip"],
)
mastigos.path_materials.set(
    Material.objects.filter(name__in=["Iron", "Brass", "Leather"])
)
mastigos.save()
moros = Path.objects.create(
    name="Moros",
    ruling_arcana=["death", "matter"],
    inferior_arcanum="spirit",
    path_weapons=["Knife", "Hammer", "Mace"],
)
moros.path_materials.set(Material.objects.filter(name__in=["Lead", "Bone", "Gems"]))
moros.save()
obrimos = Path.objects.create(
    name="Obrimos",
    ruling_arcana=["forces", "prime"],
    inferior_arcanum="death",
    path_weapons=["Knife", "Double-Edged Sword", "Spear"],
)
obrimos.path_materials.set(
    Material.objects.filter(name__in=["Steel", "Petrified Wood", "Gold"])
)
obrimos.save()
thyrsus = Path.objects.create(
    name="Thyrsus",
    ruling_arcana=["life", "spirit"],
    inferior_arcanum="mind",
    path_weapons=["Knife", "Axe", "Sling"],
)
thyrsus.path_materials.set(
    Material.objects.filter(name__in=["Wood", "Copper", "Stone"])
)
thyrsus.save()

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
    name="Free Council", rote_skills=["crafts", "persuasion", "science"]
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

CoDMerit.objects.create(
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
CoDMerit.objects.create(
    name="Artifact", ratings=[3, 4, 5], merit_type="Mage",
)
CoDMerit.objects.create(
    name="Astral Adept", ratings=[4], merit_type="Mage",
)
CoDMerit.objects.create(
    name="Between the Ticks",
    ratings=[2],
    merit_type="Mage",
    prereqs=[[("wits", 3), ("time", 1)]],
)
CoDMerit.objects.create(name="Cabal Theme", ratings=[1], merit_type="Mage", prereqs=[])
CoDMerit.objects.create(
    name="Consilium Status", ratings=[1, 2, 3, 4, 5], merit_type="Mage",
)
CoDMerit.objects.create(
    name="Adamantine Arrow Status",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[],
)
CoDMerit.objects.create(
    name="Mysterium Status", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Guardians of the Veil Status",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[],
)
CoDMerit.objects.create(
    name="Silver Ladder Status", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Free Council Status", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Seers pf the Throne Status",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[],
)
CoDMerit.objects.create(
    name="Destiny", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Dream",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("composure", 3), ("wits", 3)]],
)
CoDMerit.objects.create(
    name="Egregore",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("Mysterium Status", 1)]],
)
CoDMerit.objects.create(
    name="Enhanced Item", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(name="Familiar", ratings=[2, 4], merit_type="Mage", prereqs=[])
CoDMerit.objects.create(
    name="Fast Spells",
    ratings=[2],
    merit_type="Mage",
    prereqs=[[("firearms", 2), ("time", 1)]],
)
CoDMerit.objects.create(
    name="Grimoire", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Hallow", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(name="High Speech", ratings=[1], merit_type="Mage", prereqs=[])
CoDMerit.objects.create(
    name="Imbued Item", ratings=[1, 2, 3, 4, 5], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Infamous Mentor",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("Mentor", "same")]],
)
CoDMerit.objects.create(
    name="Lex Magica",
    ratings=[2],
    merit_type="Mage",
    prereqs=[[("Silver Ladder Status", 1)]],
)
CoDMerit.objects.create(
    name="Mana Sensitivity",
    ratings=[1],
    merit_type="Mage",
    prereqs=[[("wits", 3), ("prime", 1)]],
)
CoDMerit.objects.create(
    name="Masque",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("Guardians of the Veil Status", 1)]],
    is_style=True,
)
CoDMerit.objects.create(
    name="Mystery Cult Influence", ratings=[3, 4, 5], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Occultation", ratings=[1, 2, 3], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Potent Nimbus", ratings=[1, 2], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Potent Resonance", ratings=[2], merit_type="Mage", prereqs=[[("gnosis", 3)]]
)
CoDMerit.objects.create(
    name="Prelacy",
    ratings=[1, 2, 3, 4],
    merit_type="Mage",
    prereqs=[[("Seers of the Throne Status", 3)]],
    is_style=True,
)
CoDMerit.objects.create(
    name="Sanctum",
    ratings=[1, 2, 3, 4, 5],
    merit_type="Mage",
    prereqs=[[("Safe Place", 1)]],
)
CoDMerit.objects.create(
    name="Shadow Name", ratings=[1, 2, 3], merit_type="Mage", prereqs=[]
)
CoDMerit.objects.create(
    name="Techne",
    ratings=[2],
    merit_type="Mage",
    prereqs=[[("Free Council Status", 1)]],
)
CoDMerit.objects.create(
    name="Actively Oblivious",
    ratings=[2],
    merit_type="Supernatural",
    prereqs=[[("Morality Name", "Integrity")]],
)
CoDMerit.objects.create(
    name="Communal Sleeper",
    ratings=[1],
    merit_type="Supernatural",
    prereqs=[[("Morality Name", "Integrity"), ("empathy", 2)]],
)
CoDMerit.objects.create(
    name="Detail Oriented",
    ratings=[2],
    merit_type="Supernatural",
    prereqs=[[("Morality Name", "Integrity")]],
)
CoDMerit.objects.create(
    name="Liar",
    ratings=[1],
    merit_type="Supernatural",
    prereqs=[[("Morality Name", "Integrity")]],
)
CoDMerit.objects.create(
    name="Strained",
    ratings=[2],
    merit_type="Supernatural",
    prereqs=[[("Morality Name", "Integrity"), ("morality", -5)]],
)

CoDMerit.objects.create(
    name="Banner-Bearer",
    ratings=[1, 2, 3],
    merit_type="Supernatural",
    prereqs=[[("Sleepwalker", 1)], [("Fitful Slumber", 1)]],
)
CoDMerit.objects.create(
    name="Deadpan",
    ratings=[3],
    merit_type="Supernatural",
    prereqs=[[("Sleepwalker", 1)], [("Fitful Slumber", 1)]],
)
CoDMerit.objects.create(
    name="Fitful Slumber", ratings=[1], merit_type="Supernatural", prereqs=[],
)
CoDMerit.objects.create(
    name="Loved",
    ratings=[3],
    merit_type="Supernatural",
    prereqs=[[("Sleepwalker", 1)], [("Fitful Slumber", 1)]],
)
CoDMerit.objects.create(
    name="Proxy Voice",
    ratings=[2],
    merit_type="Supernatural",
    prereqs=[
        [("Sleepwalker", 1), ("Mentor", 1)],
        [("Fitful Slumber", 1), ("Mentor", 1)],
    ],
)
CoDMerit.objects.create(
    name="Relic Attuned",
    ratings=[3],
    merit_type="Supernatural",
    prereqs=[[("Sleepwalker", 1)], [("Fitful Slumber", 1)]],
)
CoDMerit.objects.create(
    name="Ritual Martyr",
    ratings=[2],
    merit_type="Supernatural",
    prereqs=[[("Sleepwalker", 1)], [("Fitful Slumber", 1)]],
)
CoDMerit.objects.create(
    name="Ritual Savvy",
    ratings=[2],
    merit_type="Supernatural",
    prereqs=[
        [("Sleepwalker", 1), ("occult", 2)],
        [("Fitful Slumber", 1), ("occult", 2)],
    ],
)
CoDMerit.objects.create(
    name="Sleepwalker",
    ratings=[1],
    merit_type="Supernatural",
    prereqs=[[("Morality Name", "Integrity")]],
)
CoDMerit.objects.create(
    name="Slippery",
    ratings=[2],
    merit_type="Supernatural",
    prereqs=[[("Sleepwalker", 1)], [("Fitful Slumber", 1)]],
)

CoDRote.objects.create(
    name="Ectoplasmic Shaping",
    practice="compelling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["crafts", "occult", "larceny"],
    primary_factor="duration",
    withstand="resolve",
)
CoDRote.objects.create(
    name="Deepen Shadows",
    practice="compelling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["occult", "intimidation", "expression"],
    primary_factor="duration",
    reach_options=[
        (
            1,
            "Apply the Blinded Tilt to anyone within the spell's area of effect for the Duration of the spell",
        )
    ],
)
CoDRote.objects.create(
    name="Forensic Gaze",
    practice="knowing",
    arcanum="death",
    level=1,
    suggested_rote_skills=["medicine", "investigation", "expression"],
    primary_factor="potency",
    reach_options=[
        (
            1,
            "The mage can witness the final moments of a corpse's life just leading up to the death as though seeing through the corpse's eyes. Each rank of Potency reveals a minute of time prior to the corpse's demise.",
        )
    ],
)
CoDRote.objects.create(
    name="Shadow Sculpting",
    practice="compelling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["crafts", "science", "expression"],
    primary_factor="duration",
    reach_options=[(1, "Both change the shape of shadows and animate them")],
)
CoDRote.objects.create(
    name="Soul Marks",
    practice="unveiling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["medicine", "occult", "empathy"],
    primary_factor="potency",
    withstand="resolve",
    reach_options=[(1, "Can perform spell on an unattached soul")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Speak with the Dead",
    practice="unveiling",
    arcanum="death",
    level=1,
    suggested_rote_skills=["socialize", "expression", "investigation"],
    primary_factor="duration",
    reach_options=[
        (1, "Caster can determine if Anchors are temporary"),
        (
            1,
            "Caster can make themself understoof by Rank 2+ Ghosts, even without a common language",
        ),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Corpse Mask",
    practice="veiling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["subterfuge", "crafts", "medicine"],
    primary_factor="duration",
    reach_options=[
        (1, "Can cast on a living subject with injuries"),
        (1, "May completely chnage the corpse's appearance"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Decay",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["subterfuge", "science", "occult"],
    primary_factor="potency",
    reach_options=[(1, "Decrease object's Structure as well")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ectoplasm",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["occult", "expression", "academics"],
    primary_factor="duration",
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ghost Shield",
    practice="shielding",
    arcanum="death",
    level=2,
    suggested_rote_skills=["streetwise", "subterfuge", "survival"],
    primary_factor="potency",
    reach_options=[(1, "Also protects from physical attacks by the ghost")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shape Ephemera",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["crafts", "expression", "science"],
    primary_factor="duration",
    withstand="stamina",
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Soul Armor",
    practice="shielding",
    arcanum="death",
    level=2,
    suggested_rote_skills=["academics", "occult", "survival"],
    primary_factor="duration",
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Soul Jar",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["crafts", "occult", "persuasion"],
    primary_factor="duration",
    withstand="resolve",
    reach_options=[
        (1, "The mage may bind the soul to a person"),
        (
            2,
            "Spend a point of Mana. The spell is Lasting, and soul remains bound even when Duration ends",
        ),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Suppress Aura",
    practice="veiling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["subterfuge", "intimidation", "medicine"],
    primary_factor="duration",
    withstand="resolve",
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Suppress Life",
    practice="veiling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["subterfuge", "medicine", "academics"],
    primary_factor="duration",
    reach_options=[
        (
            2,
            "Spend a point of Mana, spell can be cast reflexively to respond to something that would be reasonably likely to cause death",
        )
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Touch of the Grave",
    practice="ruling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["survival", "crafts", "persuasion"],
    primary_factor="duration",
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Without a Trace",
    practice="veiling",
    arcanum="death",
    level=2,
    suggested_rote_skills=["science", "stealth", "subterfuge"],
    primary_factor="duration",
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Cold Snap",
    arcanum="death",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["survival", "intimidation", "science"],
    reach_options=[(1, "Causes the Extreme Cold Tilt")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Damage Ghost",
    arcanum="death",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["occult", "intimidation", "brawl"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Devouring the Slain",
    arcanum="death",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "medicine", "persuasion"],
    reach_options=[
        (1, "May affect a healthy target"),
        (1, "Does not count towards Scouring limit"),
        (1, "May affect a ghost with this spell"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ghost Gate",
    arcanum="death",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "academics", "expression"],
    reach_options=[(1, "Transforms subject to Twilight state without a gate")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ghost Summons",
    arcanum="death",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["persusion", "socialize", "occult"],
    reach_options=[
        (1, "Creates Open Condition on the area"),
        (1, "May give the ghost a single one-word command to follow"),
        (
            1,
            "Near an Openb Iris to the Underworld, can summon ghosts from the underworld",
        ),
        (2, "May give the ghost a complex command to follow"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Quicken Corpse",
    arcanum="death",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["medicine", "crafts", "persuasion"],
    reach_options=[
        (1, "May create a zombie suitable for combat"),
        (2, "Spend a point of Mana to make zombie stronger"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Quicken Ghost",
    arcanum="death",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["persuasion", "socialize", "medicine"],
    reach_options=[(2, "Increase ghost's rank by 1.")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Rotting Flesh",
    arcanum="death",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["intimidation", "occult", "empathy"],
    reach_options=[(1, "Additional -1 to Social rolls per Potency")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Sever Soul",
    arcanum="death",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "athletics", "expression"],
    reach_options=[
        (
            1,
            "Soul leaves body and enters Twilight and target skips Soulless Condition going straight to Enervated",
        )
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shadow Crafting",
    arcanum="death",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "intimidation", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Enervation",
    arcanum="death",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="stamina",
    suggested_rote_skills=["occult", "intimidation", "subterfuge"],
    reach_options=[
        (1, "Target's body seizes up with the Immobilized Tilt for the duration")
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Exorcism",
    arcanum="death",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["brawl", "expression", "occult"],
    reach_options=[
        (
            1,
            "Target cannot recreate the destroyed Conditions on the same victim or location until Duration ends",
        )
    ],
    optional_arcana=[
        ("Mind 4", "Also applies to Goetia"),
        ("Spirit 4", "Also applies to Spirits"),
    ],
)
CoDRote.objects.create(
    name="Revenant",
    arcanum="death",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["crafts", "brawl", "intimidation"],
    reach_options=[],
    optional_arcana=[
        ("Mind 4", "Also applies to Goetia"),
        ("Spirit 4", "Also applies to Spirits"),
    ],
)
CoDRote.objects.create(
    name="Shadow Flesh",
    arcanum="death",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["occult", "medicine", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Withering",
    arcanum="death",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["intimidation", "medicine", "science"],
    reach_options=[(1, "Spend one mana, inflict Aggravatated")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Create Anchor",
    arcanum="death",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["crafts", "occult", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Create Avernian Gate",
    arcanum="death",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "crafts", "persuasion"],
    reach_options=[(1, "The Iris leads anywhere they have been in the Underwr=orld")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Create Ghost",
    arcanum="death",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "expression", "academics"],
    reach_options=[(1, "For one mana, the ghost is rank 2.")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Deny the Reaper",
    arcanum="death",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["medicine", "occult", "subterfuge"],
    reach_options=[
        (
            1,
            "The mage may return the recently dead to life for the duration. The subject suffers Soul Loss.",
        )
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Empty Presence",
    arcanum="death",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    mana_cost=1,
    withstand="composure",
    suggested_rote_skills=["subterfuge", "persuasion", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Sever the Awakened Soul",
    arcanum="death",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["crafts", "intimidation", "medicine"],
    reach_options=[
        (1, "Subject is immediately Enervated"),
        (2, "Subject is under Thrall Condition"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Interconnection",
    arcanum="fate",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["empathy", "investigation", "medicine"],
    reach_options=[
        (
            1,
            "Mage can also detect possession, mind control, and alterations of destiny",
        ),
        (
            2,
            "The mage can also get information about the subject's destiny, including the Destiny merit or conditional durations",
        ),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Oaths Fulfilled",
    arcanum="fate",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "politics", "investigation"],
    reach_options=[
        (1, "Brief vision when the oath is fulfilled"),
        (1, "Track until spell expires"),
        (1, "May be triggered on things only Mage Sight can detect"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Quantum Flux",
    arcanum="fate",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "firearms", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Reading the Outmost Eddies",
    arcanum="fate",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["computer", "persuasion", "subterfuge"],
    reach_options=[(1, "Twist of fate occurs within an hour")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Serendipity",
    arcanum="fate",
    level=1,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["intimidation", "occult", "socialize"],
    reach_options=[
        (1, "May substitute any skill of the same type for the roll"),
        (2, "May substitute any skill."),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Exceptional Luck",
    arcanum="fate",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["intimidation", "occult", "socialize"],
    reach_options=[
        (
            2,
            ("Boon or hex can affect spellcasting"),
            (2, "Spend a point of mana to cast as reflexive action"),
        )
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Fabricate Fortune",
    arcanum="fate",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["larceny", "occult", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Fools Rush In",
    arcanum="fate",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "socialize", "streetwise"],
    reach_options=[
        (
            1,
            "Subject gets Potency as dice bonus on Potency number of rolls until duration",
        ),
        (3, "Can also affect spellcasting"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Lucky Number",
    arcanum="fate",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "larceny", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shifting the Odds",
    arcanum="fate",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "politics", "subterfuge"],
    reach_options=[(1, "Object is located within an hour")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Warding Gesture",
    arcanum="fate",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["brawl", "occult", "subterfuge"],
    reach_options=[
        (
            1,
            "May selectively exclude subject from any spell they cast or Attainment used",
        ),
        (2, "May selectively grant protection"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Grave Misfortune",
    arcanum="fate",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["intimidation", "occult", "weaponry"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Monkey's Paw",
    arcanum="fate",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["drive", "crafts", "science"],
    reach_options=[
        (1, "User of object gains boon or hex"),
        (1, "Spend a point of Mana, bonus or penalty can exceed five dice"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shared Fate",
    arcanum="fate",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["medicine", "persuasion", "politics"],
    reach_options=[
        (1, "Link only works one way for one of the subjects"),
        (2, "Subject isn't linked specifically, but has harm rebound"),
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Superlative Luck",
    arcanum="fate",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    mana_cost=1,
    suggested_rote_skills=["athletics", "crafts", "occult"],
    reach_options=[
        (2, "Spell's effects may affect ritual spellcasting, doubling casting time")
    ],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Sworn Oaths",
    arcanum="fate",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["expression", "occult", "politics"],
    reach_options=[(1, "Mage is aware if spell switches from boon to hex")],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Atonement",
    arcanum="fate",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="potency",
    suggested_rote_skills=["academics", "empathy", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Chaos Mastery",
    arcanum="fate",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "occult", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Divine Intervention",
    arcanum="fate",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "occult", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Strings of Fate",
    arcanum="fate",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["academics", "persuasion", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Sever Oaths",
    arcanum="fate",
    level=4,
    practice="unraveling",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["occult", "subterfuge", "weaponry"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Forge Destiny",
    arcanum="fate",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["intimidation", "occult", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Pariah",
    arcanum="fate",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["investigation", "medicine", "politics"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Miracle",
    arcanum="fate",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "persuasion", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Swarm of Locusts",
    arcanum="fate",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["intimidation", "occult", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Influence Electricity",
    arcanum="forces",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["computers", "crafts", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Influence Fire",
    arcanum="forces",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Kinetic Efficiency",
    arcanum="forces",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Influence Heat",
    arcanum="forces",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Nightvision",
    arcanum="forces",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "science", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Receiver",
    arcanum="forces",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "investigation", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Tune In",
    arcanum="forces",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["computers", "empathy", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Control Electricity",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "computers", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Control Fire",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Control Gravity",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "occult", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Control Heat",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Control Light",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "investigation", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Control Sound",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["expression", "stealth", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Control Weather",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Environmental Shield",
    arcanum="forces",
    level=2,
    practice="Shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Invisibility",
    arcanum="forces",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["larceny", "science", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Kinetic Blow",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Transmission",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Zoom In",
    arcanum="forces",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Call Lightning",
    arcanum="forces",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Gravitic Supremacy (Increase)",
    arcanum="forces",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Gravitic Supremacy (Decrease)",
    arcanum="forces",
    level=3,
    practice="fraying",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Telekinesis",
    arcanum="forces",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Telekinetic Strike",
    arcanum="forces",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Turn Momentum",
    arcanum="forces",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Velocity Control (Decrease)",
    arcanum="forces",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "drive", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Velocity Control (Increase)",
    arcanum="forces",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "drive", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Electromagnetic Pulse",
    arcanum="forces",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "computers", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Levitation",
    arcanum="forces",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["athletics", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Rend Friction",
    arcanum="forces",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "drive", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Thunderbolt",
    arcanum="forces",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Transform Energy",
    arcanum="forces",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Adverse Weather",
    arcanum="forces",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Create Energy",
    arcanum="forces",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Eradicate Energy",
    arcanum="forces",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["intimidation", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Earthquake",
    arcanum="forces",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Analyze Life",
    arcanum="life",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["animal_ken", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Cleanse the Body",
    arcanum="life",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Heightened Senses",
    arcanum="life",
    level=1,
    practice="unveilling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "investigation", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Speak With Beasts",
    arcanum="life",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["animal_ken", "empathy", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Web of Life",
    arcanum="life",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Body Control",
    arcanum="life",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Control Instincts",
    arcanum="life",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["animal_ken", "intimidation", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Lure and Repel",
    arcanum="life",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["animal_ken", "persuasion", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Mutable Mask",
    arcanum="life",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["medicine", "stealth", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Purge Illness",
    arcanum="life",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Bruise Flesh",
    arcanum="life",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["brawl", "intimidation", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Degrading the Form",
    arcanum="life",
    level=3,
    practice="fraying",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["brawl", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Honing the Form",
    arcanum="life",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Knit",
    arcanum="life",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Many Faces",
    arcanum="life",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["medicine", "stealth", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Transform Life",
    arcanum="life",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="stamina",
    suggested_rote_skills=["animal_ken", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Accelerate Growth",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["animal_ken", "medicine", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Animal Minion",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["animal_ken", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Life-Force Assault",
    arcanum="life",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["brawl", "intimidation", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Mend",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Regeneration",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    mana_cost=1,
    suggested_rote_skills=["athletics", "medicine", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shapechanging",
    arcanum="life",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="stamina",
    suggested_rote_skills=["animal_ken", "athletics", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Create Life",
    arcanum="life",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["medicine", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Contagion",
    arcanum="life",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["medicine", "occult", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Salt the Earth",
    arcanum="life",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["medicine", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Craftsman's Eye",
    arcanum="matter",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "investigation", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Detect Substance",
    arcanum="matter",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "investigation", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Discern Composition",
    arcanum="matter",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "investigation", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Lodestone",
    arcanum="matter",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "larceny", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Remote Control",
    arcanum="matter",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "drive", "intimidate"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Alchemist's Touch",
    arcanum="matter",
    level=2,
    practice="shielding",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "survival", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Find the Balance",
    arcanum="matter",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "persuasion", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Hidden Hoard",
    arcanum="matter",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["larceny", "occult", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Machine Invisibility",
    arcanum="matter",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["larceny", "science", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shaping",
    arcanum="matter",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["crafts", "expression", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Aegis",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "crafts", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Alter Conductivity",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["computers", "science", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Alter Integrity (Weaken)",
    arcanum="matter",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["crafts", "medicine", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Alter Integrity (Strengthen)",
    arcanum="matter",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["crafts", "medicine", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Crucible",
    arcanum="matter",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Nigredo and Albedo (Repair)",
    arcanum="matter",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "brawl", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Nigredo and Albedo (Destroy)",
    arcanum="matter",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "brawl", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shrink and Grow",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["crafts", "expression", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="State Change",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="durability",
    suggested_rote_skills=["crafts", "persuasion", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Windstrike",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "crafts"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Wonderful Machine",
    arcanum="matter",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "politics", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ghostwall",
    arcanum="matter",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "occult", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Golem",
    arcanum="matter",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Piercing Earth",
    arcanum="matter",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "crafts"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Transubstantiation",
    arcanum="matter",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "empathy", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Annihilate Matter",
    arcanum="matter",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["athletics", "intimidation", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ex Nihilo",
    arcanum="matter",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Self-Repairing Machine",
    arcanum="matter",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "medicine", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Know Nature",
    arcanum="mind",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "science", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Mental Scan",
    arcanum="mind",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["empathy", "investigation", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="One Mind, Two Thoughts",
    arcanum="mind",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "expression", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Perfect Recall",
    arcanum="mind",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "expression", "investigation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Alter Mental Pattern",
    arcanum="mind",
    level=2,
    practice="veiling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["science", "stealth", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Dream Reaching",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["empathy", "medicine", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Emotional Urging",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["empathy", "intimidation", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="First Impressions",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["crafts", "socialize", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Incognito Presence",
    arcanum="mind",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="resolve",
    mana_cost=1,
    suggested_rote_skills=["empathy", "stealth", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Memory Hole",
    arcanum="mind",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "medicine", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Mental Shield",
    arcanum="mind",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "intimidation", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Psychic Domination",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["expression", "intimidation", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Telepathy",
    arcanum="mind",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["crafts", "empathy", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Augment Mind",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "expression", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Befuddle (Social)",
    arcanum="mind",
    level=3,
    practice="fraying",
    primary_factor="potence",
    withstand="composure",
    suggested_rote_skills=["intimidation", "persuasion", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Befuddle (Mental)",
    arcanum="mind",
    level=3,
    practice="fraying",
    primary_factor="potence",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "persuasion", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Clear Thoughts",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["empathy", "intimidation", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Enhance Skill",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "expression", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Goetic Summons",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["persuasion", "socialize", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Imposter",
    arcanum="mind",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["persuasion", "stealth", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Psychic Assault",
    arcanum="mind",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "intimidation", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Sleep of the Just",
    arcanum="mind",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["academics", "athletics", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Read the Depths",
    arcanum="mind",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["empathy", "investigation", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Universal Language",
    arcanum="mind",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "investigation", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Gain Skill",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Hallucination",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["academics", "persuasion", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Mind Flay",
    arcanum="mind",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["expression", "intimidation", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Possession",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["medicine", "persuasion", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Psychic Projection",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["academics", "occult", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Psychic Reprogramming",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["intimidation", "medicine", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Terrorize",
    arcanum="mind",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["expression", "intimidation", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Amorality",
    arcanum="mind",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["crafts", "empathy", "expression"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="No Exit",
    arcanum="mind",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["expression", "persuasion", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Mind Wipe",
    arcanum="mind",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["academics", "intimidation", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Psychic Genesis",
    arcanum="mind",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "expression", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Social Networking",
    arcanum="mind",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["persuasion", "politics", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Dispel Magic",
    arcanum="prime",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="arcana",
    suggested_rote_skills=["athletics", "intimidation", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Pierce Deception",
    arcanum="prime",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["investigation", "medicine", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Supernal Vision",
    arcanum="prime",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "occult", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Sacred Geometry",
    arcanum="prime",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "occult", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Scribe Grimoire",
    arcanum="prime",
    level=1,
    practice="compelling",
    primary_factor="potency",
    mana_cost=1,
    withstand="arcanum_dots",
    suggested_rote_skills=["crafts", "expression", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Word of Command",
    arcanum="prime",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["craft", "occult", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="As Above, So Below",
    arcanum="prime",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "occult", "politics"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Cloak Nimbus",
    arcanum="prime",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["politics", "stealth", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Invisible Runes",
    arcanum="prime",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["expression", "intimidation", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Supernal Veil",
    arcanum="prime",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "subterfuge", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Wards and Signs",
    arcanum="prime",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["intimidation", "occult", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Words of Truth",
    arcanum="prime",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["expression", "intimidation", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Aetheric Winds",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "expression", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Channel Mana",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["occult", "politics", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Cleanse Pattern",
    arcanum="prime",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["investigation", "occult", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Display of Power",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["brawl", "occult", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ephemeral Enchantment",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "weaponry"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Geomancy",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academia", "expression", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Platonic Form",
    arcanum="prime",
    level=3,
    practice="weaving",
    primary_factor="potency",
    mana_cost=1,
    withstand="",
    suggested_rote_skills=["academics", "crafts", "expression"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Stealing Fire",
    arcanum="prime",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["expression", "larceny", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Apocalypse",
    arcanum="prime",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["occult", "persuasion", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Celestial Fire",
    arcanum="prime",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "expression", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Destroy Tass",
    arcanum="prime",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="durability",
    suggested_rote_skills=["brawl", "intimidation", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Hallow Dance",
    arcanum="prime",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="hallow_rating",
    suggested_rote_skills=["expression", "occult", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Supernal Dispellation",
    arcanum="prime",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="arcanum",
    suggested_rote_skills=["athletics", "intimidation", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Blasphemy",
    arcanum="prime",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="hallow_rating",
    suggested_rote_skills=["athletics", "occult", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Create Truth",
    arcanum="prime",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="hallow_rating",
    mana_cost=5,
    suggested_rote_skills=["expression", "occult", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Eidolon",
    arcanum="prime",
    level=5,
    practice="making",
    primary_factor="potency",
    mana_cost=1,
    withstand="",
    suggested_rote_skills=["academics", "crafts", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Forge Purpose",
    arcanum="prime",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["empathy", "expression", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Word of Unmaking",
    arcanum="prime",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="merit_rating",
    suggested_rote_skills=["intimidation", "occult", "weaponry"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Correspondence",
    arcanum="space",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "empathy", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ground-Eater",
    arcanum="space",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="stamina",
    suggested_rote_skills=["athletics", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Isolation",
    arcanum="space",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["academics", "intimidation", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Locate Object",
    arcanum="space",
    level=1,
    practice="knowing",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "occult", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="The Outward and Inward Eye",
    arcanum="space",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["firearms", "investigation", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Borrow Threads",
    arcanum="space",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="connection",
    suggested_rote_skills=["larceny", "occult", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Break Boundary",
    arcanum="space",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "larceny", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Lying Maps",
    arcanum="space",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="resolve",
    suggested_rote_skills=["academics", "politics", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Scrying",
    arcanum="space",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["computers", "occult", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Secret Door",
    arcanum="space",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "stealth", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Veil Sympathy",
    arcanum="space",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="sympathy_connection",
    suggested_rote_skills=["politics", "subterfuge", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ward",
    arcanum="space",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "subterfuge", "weaponry"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ban",
    arcanum="space",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["intimidation", "science", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Co-Location",
    arcanum="space",
    level=3,
    practice="fraying",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "firearms", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Perfect Sympathy",
    arcanum="space",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "empathy", "larceny"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Warp",
    arcanum="space",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "brawl", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Web-Weaver",
    arcanum="space",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="composure",
    suggested_rote_skills=["crafts", "empathy", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Alter Direction",
    arcanum="space",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "firearms", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Collapse",
    arcanum="space",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "firearms", "intimidation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Cut Threads",
    arcanum="space",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="symapthy_connection",
    suggested_rote_skills=["persuasion", "politics", "weaponry"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Secret Room",
    arcanum="space",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["expression", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Teleportation",
    arcanum="space",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["larceny", "persuasion", "science"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Create Sympathy",
    arcanum="space",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="connection",
    suggested_rote_skills=["empathy", "persuasion", "poltiics"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Forge No Chains",
    arcanum="space",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "subterfuge", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Pocket Dimension",
    arcanum="space",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Quarantine",
    arcanum="space",
    level=5,
    practice="unmaking",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "larceny", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Coaxing the Spirits",
    arcanum="spirit",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="composure",
    suggested_rote_skills=["politics", "athletics", "expression"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Exorcist's Eye",
    arcanum="spirit",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "survival", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Gremlins",
    arcanum="spirit",
    level=1,
    practice="compelling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["larceny", "politics", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Invoke Bane",
    arcanum="spirit",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["brawl", "intimidation", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Know Spirit",
    arcanum="spirit",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["academics", "brawl", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Cap the Well",
    arcanum="spirit",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["politics", "survival", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Channel Essence",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["occult", "persuasion", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Command Spirit",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["medicine", "athletics", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Ephemeral Shield",
    arcanum="spirit",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["animal_ken", "medicine", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Gossamer Touch",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["brawl", "crafts", "intimidation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Opener of the Way",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "computers", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shadow Walk",
    arcanum="spirit",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "stealth", "streetwise"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Slumber",
    arcanum="spirit",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["expression", "occult", "weaponry"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Bolster Spirit",
    arcanum="spirit",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["medicine", "occult", "expression"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Erode Resonance",
    arcanum="spirit",
    level=3,
    practice="fraying",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "brawl", "intimidation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Howl From Beyond",
    arcanum="spirit",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["expression", "firearms", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Place of Power (Lower Gauntlet)",
    arcanum="spirit",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="gauntlet",
    suggested_rote_skills=["academics", "expression", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Place of Power (Raise Gauntlet)",
    arcanum="spirit",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="gauntlet",
    suggested_rote_skills=["academics", "expression", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Reaching",
    arcanum="spirit",
    level=3,
    practice="weaving",
    primary_factor="duration",
    withstand="gauntlet",
    suggested_rote_skills=["athletics", "medicine", "socialize"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Rouse Spirit",
    arcanum="spirit",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["athletics", "expression", "investigation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Spirit Summoning",
    arcanum="spirit",
    level=3,
    practice="perfecting",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["persuasion", "socialize", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Banishment",
    arcanum="spirit",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["brawl", "expression", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Bind Spirit",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["crafts", "brawl", "intimidation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Craft Fetish",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="rank",
    suggested_rote_skills=["crafts", "occult", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Familiar",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["athletics", "expression", "intimidate"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shadow Scream",
    arcanum="spirit",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["expression", "firearms", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shape Spirit",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["crafts", "medicine", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Twilit Body",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "subterfuge", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="World Walker",
    arcanum="spirit",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="gaunlet",
    suggested_rote_skills=["athletics", "persuasion", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Annihilate Spirit",
    arcanum="spirit",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="rank",
    suggested_rote_skills=["intimidation", "science", "weaponry"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Birth Spirit",
    arcanum="spirit",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "medicine", "expression"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Create Locus",
    arcanum="spirit",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="gauntlet",
    suggested_rote_skills=["crafts", "empathy", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Essence Fountain",
    arcanum="spirit",
    level=5,
    practice="making",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["empathy", "expression", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Spirit Manse",
    arcanum="spirit",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "expression", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Divination",
    arcanum="time",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "empathy", "investigation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Green Light/Red Light",
    arcanum="time",
    level=1,
    practice="compelling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["computer", "larceny", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Momentary Flux",
    arcanum="time",
    level=1,
    practice="knowing",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["investigation", "streetwise", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Perfect Timing",
    arcanum="time",
    level=1,
    practice="unveiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["empathy", "socialize", "streetwise"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Postcognition",
    arcanum="time",
    level=1,
    practice="unveiling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "empathy", "investigation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Choose the Thread",
    arcanum="time",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["occult", "science", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Constance Presence",
    arcanum="time",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "persuasion", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Hung Spell",
    arcanum="time",
    level=2,
    practice="ruling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["crafts", "occult", "expression"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shield of Chronos",
    arcanum="time",
    level=2,
    practice="veiling",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["academics", "stealth", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Tipping the Hourglass",
    arcanum="time",
    level=2,
    practice="ruling",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["athletics", "crafts", "investigation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Veil of Moments",
    arcanum="time",
    level=2,
    practice="shielding",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["medicine", "investigation", "subterfuge"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Acceleration",
    arcanum="time",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    mana_cost=1,
    suggested_rote_skills=["athletics", "drive", "stealth"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Chronos' Curse",
    arcanum="time",
    level=3,
    practice="fraying",
    primary_factor="potency",
    mana_cost=1,
    withstand="stamina",
    suggested_rote_skills=["academics", "occult", "intimidation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Shifting Sands",
    arcanum="time",
    level=3,
    practice="fraying",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "occult", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Temporal Summoning",
    arcanum="time",
    level=3,
    practice="weaving",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "investigation", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Weight of Years",
    arcanum="time",
    level=3,
    practice="perfecting",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["crafts", "intimidation", "medicine"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Present as Past",
    arcanum="time",
    level=4,
    practice="patterning",
    primary_factor="potency",
    mana_cost=1,
    withstand="",
    suggested_rote_skills=["empathy", "investigation", "streetwise"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Prophecy",
    arcanum="time",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "expression", "investigation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Rend Lifespan",
    arcanum="time",
    level=4,
    practice="unraveling",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["athletics", "medicine", "intimidation"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Rewrite History",
    arcanum="time",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="resolve",
    suggested_rote_skills=["expression", "investigation", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Temporal Stutter",
    arcanum="time",
    level=4,
    practice="patterning",
    primary_factor="potency",
    withstand="stamina",
    suggested_rote_skills=["intimidation", "science", "survival"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Blink of an Eye",
    arcanum="time",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "crafts", "occult"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Corridors of Time",
    arcanum="time",
    level=5,
    practice="unmaking",
    primary_factor="potency",
    withstand="",
    suggested_rote_skills=["academics", "investigation", "persuasion"],
    reach_options=[],
    optional_arcana=[],
)
CoDRote.objects.create(
    name="Temporal Pocket",
    arcanum="time",
    level=5,
    practice="making",
    primary_factor="duration",
    withstand="",
    suggested_rote_skills=["occult", "science", "stealth"],
    reach_options=[],
    optional_arcana=[],
)

x = Legacy.objects.create(
    name="The Eleventh Question",
    path=moros,
    order=guardians_of_the_veil,
    ruling_arcanum="time",
    prereqs=[
        [("investigation", 2), ("academics", 2)],
        [("investigation", 2), ("larceny", 2)],
        [("investigation", 2), ("medicine", 2)],
        [("investigation", 2), ("occult", 2)],
        [("investigation", 2), ("science", 2)],
    ],
)

a1 = Attainment.objects.create(
    name="The Undisturbed Scene", prereqs=[[("legacy", "The Eleventh Question")]]
)
a2 = Attainment.objects.create(
    name="The Unobvious Answer",
    prereqs=[
        [("time", 2), ("investigation", 3), ("attainment", "The Undisturbed Scene")]
    ],
)
a3 = Attainment.objects.create(
    name="The Chance Answer",
    prereqs=[
        [("time", 3), ("attainment", "The Unobvious Answer"), ("academics", 3)],
        [("time", 3), ("attainment", "The Unobvious Answer"), ("larceny", 3)],
        [("time", 3), ("attainment", "The Unobvious Answer"), ("medicine", 3)],
        [("time", 3), ("attainment", "The Unobvious Answer"), ("occult", 2)],
        [("time", 3), ("attainment", "The Unobvious Answer"), ("science", 2)],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("academics", 2),
            ("larceny", 2),
        ],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("academics", 2),
            ("medicine", 2),
        ],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("academics", 2),
            ("occult", 2),
        ],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("academics", 2),
            ("science", 2),
        ],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("larceny", 2),
            ("medicine", 2),
        ],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("larceny", 2),
            ("occult", 2),
        ],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("larceny", 2),
            ("science", 2),
        ],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("medicine", 2),
            ("occult", 2),
        ],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("medicine", 2),
            ("science", 2),
        ],
        [
            ("time", 3),
            ("attainment", "The Unobvious Answer"),
            ("occult", 2),
            ("science", 2),
        ],
    ],
)
a4 = Attainment.objects.create(
    name="The Timely Answer",
    prereqs=[[("time", 4), ("investigation", 4), ("attainment", "The Chance Answer")]],
)
a5 = Attainment.objects.create(
    name="The Penultimate Answer",
    prereqs=[
        [("time", 5), ("attainment", "The Timely Answer"), ("academics", 4)],
        [("time", 5), ("attainment", "The Timely Answer"), ("larceny", 4)],
        [("time", 5), ("attainment", "The Timely Answer"), ("medicine", 4)],
        [("time", 5), ("attainment", "The Timely Answer"), ("occult", 4)],
        [("time", 5), ("attainment", "The Timely Answer"), ("science", 4)],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 3),
            ("larceny", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 3),
            ("medicine", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 3),
            ("occult", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 3),
            ("science", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("larceny", 3),
            ("medicine", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("larceny", 3),
            ("occult", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("larceny", 3),
            ("science", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("medicine", 3),
            ("occult", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("medicine", 3),
            ("science", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("occult", 3),
            ("science", 3),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 2),
            ("larceny", 2),
            ("medicine", 2),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 2),
            ("larceny", 2),
            ("occult", 2),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 2),
            ("larceny", 2),
            ("science", 2),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 2),
            ("medicine", 2),
            ("occult", 2),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 2),
            ("medicine", 2),
            ("science", 2),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("academics", 2),
            ("occult", 2),
            ("science", 2),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("larceny", 2),
            ("medicine", 2),
            ("occult", 2),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("larceny", 2),
            ("medicine", 2),
            ("science", 2),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("larceny", 2),
            ("occult", 2),
            ("science", 2),
        ],
        [
            ("time", 5),
            ("attainment", "The Timely Answer"),
            ("medicine", 2),
            ("occult", 2),
            ("science", 2),
        ],
    ],
)

x.attainments.add(a1)
x.attainments.add(a2)
x.attainments.add(a3)
x.attainments.add(a4)
x.attainments.add(a5)
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

c = Condition.objects.create(
    name="The Sisters of the Mountain family curse", persistent=True
)
pf = ProximiFamily.objects.create(
    name="The Sisters of the Mountain", path=thyrsus, blessing_arcana="fate", curse=c
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
pf.set_possible_blessings([CoDRote.objects.get(name=x) for x in rotes])

Equipment.objects.create(
    name="Basic Automotive Tool Kit",
    durability=2,
    size=2,
    structure=3,
    availability=1,
    die_bonus=1,
    display=False,
    description="Necessity for automobile repairs.",
)
Equipment.objects.create(
    name="Garage Automotive Tool Kit",
    durability=2,
    size=2,
    structure=3,
    availability=1,
    die_bonus=2,
    display=False,
    description="Necessity for automobile repairs.",
)
Equipment.objects.create(
    name="Cache 1",
    durability=2,
    size=1,
    structure=5,
    availability=1,
    die_bonus=1,
    display=False,
    description="Hidden storage for items, usually weapons. Must be at most half the Size of the thing containing it. Can hold two items of its Size and a reasonable number of smaller items. Die bonus adds to concealment and subtracts from rolls to find items",
)
Equipment.objects.create(
    name="Cache 2",
    durability=2,
    size=2,
    structure=5,
    availability=1,
    die_bonus=1,
    display=False,
    description="Hidden storage for items, usually weapons. Must be at most half the Size of the thing containing it. Can hold two items of its Size and a reasonable number of smaller items. Die bonus adds to concealment and subtracts from rolls to find items",
)
Equipment.objects.create(
    name="Cache 3",
    durability=2,
    size=3,
    structure=5,
    availability=2,
    die_bonus=1,
    display=False,
    description="Hidden storage for items, usually weapons. Must be at most half the Size of the thing containing it. Can hold two items of its Size and a reasonable number of smaller items. Die bonus adds to concealment and subtracts from rolls to find items",
)
Equipment.objects.create(
    name="Cache 4",
    durability=2,
    size=4,
    structure=5,
    availability=2,
    die_bonus=1,
    display=False,
    description="Hidden storage for items, usually weapons. Must be at most half the Size of the thing containing it. Can hold two items of its Size and a reasonable number of smaller items. Die bonus adds to concealment and subtracts from rolls to find items",
)
Equipment.objects.create(
    name="Cache 5",
    durability=2,
    size=5,
    structure=5,
    availability=3,
    die_bonus=1,
    display=False,
    description="Hidden storage for items, usually weapons. Must be at most half the Size of the thing containing it. Can hold two items of its Size and a reasonable number of smaller items. Die bonus adds to concealment and subtracts from rolls to find items",
)
Equipment.objects.create(
    name="Communications Headset",
    durability=0,
    size=1,
    structure=1,
    availability=2,
    die_bonus=2,
    display=False,
    description="Die bonus to coordinated efforts",
)
Equipment.objects.create(
    name="Crime Scene Kit",
    durability=2,
    size=3,
    structure=2,
    availability=2,
    die_bonus=2,
    display=False,
    description="Investigation",
)
Equipment.objects.create(
    name="Code Kit",
    durability=1,
    size=2,
    structure=1,
    availability=1,
    die_bonus=5,
    display=False,
    description="Encrypting and Decrypting information",
)
Equipment.objects.create(
    name="Cracking Software",
    durability=0,
    size=0,
    structure=0,
    availability=3,
    die_bonus=2,
    display=False,
    description="Hacking attempts",
)
Equipment.objects.create(
    name="Cheap Digital Recorder",
    durability=1,
    size=1,
    structure=2,
    availability=1,
    die_bonus=1,
    display=False,
    description="Bonus to concealing the device and to catching words and sounds",
)
Equipment.objects.create(
    name="Digital Recorder",
    durability=1,
    size=1,
    structure=2,
    availability=2,
    die_bonus=2,
    display=False,
    description="Bonus to concealing the device and to catching words and sounds",
)
Equipment.objects.create(
    name="Duct Tape",
    durability=1,
    size=1,
    structure=2,
    availability=1,
    die_bonus=1,
    display=False,
    description="Applies mostly to Crafts. If used as a restraint, -3 penalty to break free and must overcome Structure",
)
Equipment.objects.create(
    name="Basic First-Aid Kit",
    durability=1,
    size=2,
    structure=3,
    availability=1,
    die_bonus=0,
    display=False,
    description="Stabilizing injuries nad stopping wounds from getting worse.",
)
Equipment.objects.create(
    name="Advanced First-Aid Kit",
    durability=1,
    size=2,
    structure=3,
    availability=2,
    die_bonus=1,
    display=False,
    description="Stabilizing injuries nad stopping wounds from getting worse.",
)
Equipment.objects.create(
    name="Flashlight",
    durability=2,
    size=1,
    structure=3,
    availability=1,
    die_bonus=1,
    display=False,
    description="Adds die to rolls to see",
)
Equipment.objects.create(
    name="Glowstick",
    durability=1,
    size=1,
    structure=1,
    availability=1,
    die_bonus=2,
    display=False,
    description="Adds die to rolls to see",
)
Equipment.objects.create(
    name="GPS Tracker",
    durability=2,
    size=2,
    structure=2,
    availability=2,
    die_bonus=3,
    display=False,
    description="Following or tracking someone in places with a GPS signal",
)
Equipment.objects.create(
    name="Keylogging Software",
    durability=0,
    size=0,
    structure=0,
    availability=2,
    die_bonus=2,
    display=False,
    description="Hacking",
)
Equipment.objects.create(
    name="Luminol",
    durability=0,
    size=1,
    structure=1,
    availability=1,
    die_bonus=2,
    display=False,
    description="Tracking and Investigation involving body fluids",
)
Equipment.objects.create(
    name="Multi-Tool",
    durability=3,
    size=1,
    structure=4,
    availability=1,
    die_bonus=1,
    display=False,
    description="Crafts and related tasks",
)
Equipment.objects.create(
    name="Personal Computer 1",
    durability=2,
    size=3,
    structure=2,
    availability=1,
    die_bonus=1,
    display=False,
    description="Anything done on a computer",
)
Equipment.objects.create(
    name="Personal Computer 2",
    durability=2,
    size=3,
    structure=2,
    availability=2,
    die_bonus=2,
    display=False,
    description="Anything done on a computer",
)
Equipment.objects.create(
    name="Personal Computer 3",
    durability=2,
    size=3,
    structure=2,
    availability=3,
    die_bonus=3,
    display=False,
    description="Anything done on a computer",
)
Equipment.objects.create(
    name="Personal Computer 4",
    durability=2,
    size=3,
    structure=2,
    availability=4,
    die_bonus=4,
    display=False,
    description="Anything done on a computer",
)
Equipment.objects.create(
    name="Smartphone 1",
    durability=2,
    size=1,
    structure=1,
    availability=1,
    die_bonus=1,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Smartphone 2",
    durability=2,
    size=1,
    structure=1,
    availability=2,
    die_bonus=1,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Smartphone 3",
    durability=2,
    size=1,
    structure=1,
    availability=3,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Special Effects",
    durability=2,
    size=5,
    structure=3,
    availability=3,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Surveillance Equipment",
    durability=2,
    size=2,
    structure=2,
    availability=3,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Basic Survival Gear",
    durability=2,
    size=2,
    structure=3,
    availability=1,
    die_bonus=1,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Extreme Survival Gear",
    durability=2,
    size=3,
    structure=3,
    availability=3,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Talcum Powder",
    durability=0,
    size=1,
    structure=0,
    availability=1,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Ultraviolet Ink",
    durability=1,
    size=1,
    structure=2,
    availability=1,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Battering Ram",
    durability=3,
    size=4,
    structure=8,
    availability=2,
    die_bonus=4,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Bear Trap",
    durability=3,
    size=2,
    structure=5,
    availability=2,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Caltrops",
    durability=2,
    size=2,
    structure=3,
    availability=2,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Camouflage Clothing",
    durability=1,
    size=2,
    structure=3,
    availability=2,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Climbing Gear",
    durability=3,
    size=2,
    structure=2,
    availability=2,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Crowbar",
    durability=3,
    size=1,
    structure=4,
    availability=1,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Firearm Suppressor",
    durability=2,
    size=1,
    structure=2,
    availability=2,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Gas Mask",
    durability=1,
    size=2,
    structure=3,
    availability=2,
    die_bonus=5,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Handcuffs",
    durability=4,
    size=1,
    structure=4,
    availability=1,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Lockpicking Kit",
    durability=2,
    size=2,
    structure=2,
    availability=2,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Night Vision Goggles",
    durability=1,
    size=2,
    structure=1,
    availability=2,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Pepper Spray",
    durability=2,
    size=1,
    structure=1,
    availability=1,
    die_bonus=1,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Rope",
    durability=2,
    size=3,
    structure=2,
    availability=1,
    die_bonus=1,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Stun Gun 1",
    durability=2,
    size=1,
    structure=2,
    availability=1,
    die_bonus=0,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Stun Gun 2",
    durability=2,
    size=1,
    structure=2,
    availability=2,
    die_bonus=0,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Stun Gun 3",
    durability=2,
    size=1,
    structure=2,
    availability=3,
    die_bonus=0,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Cash 1",
    durability=1,
    size=2,
    structure=1,
    availability=1,
    die_bonus=1,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Cash 2",
    durability=1,
    size=2,
    structure=1,
    availability=2,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Cash 3",
    durability=1,
    size=2,
    structure=1,
    availability=3,
    die_bonus=3,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Cash 4",
    durability=1,
    size=2,
    structure=1,
    availability=4,
    die_bonus=4,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Cash 5",
    durability=1,
    size=2,
    structure=1,
    availability=5,
    die_bonus=5,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Disguise 1",
    durability=1,
    size=3,
    structure=2,
    availability=1,
    die_bonus=1,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Disguise 2",
    durability=1,
    size=3,
    structure=2,
    availability=2,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Disguise 3",
    durability=1,
    size=3,
    structure=2,
    availability=3,
    die_bonus=3,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Fashion 1",
    durability=1,
    size=2,
    structure=1,
    availability=1,
    die_bonus=1,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Fashion 2",
    durability=1,
    size=2,
    structure=1,
    availability=2,
    die_bonus=1,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Fashion 3",
    durability=1,
    size=2,
    structure=1,
    availability=3,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Fashion 4",
    durability=1,
    size=2,
    structure=1,
    availability=4,
    die_bonus=2,
    display=False,
    description="",
)
Equipment.objects.create(
    name="Fashion 5",
    durability=1,
    size=2,
    structure=1,
    availability=5,
    die_bonus=3,
    display=False,
    description="",
)

Tilt.objects.create(
    name="Arm Wrack",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Beaten Down",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Blinded",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Deafened",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Drugged",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Immobilized",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Insane",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Insensate",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Knocked Down",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Leg Wrack",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Poisoned",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Sick", tilt_type="personal", description="", effect="", causing="", ending="",
)
Tilt.objects.create(
    name="Stunned",
    tilt_type="personal",
    description="",
    effect="",
    causing="",
    ending="",
)

Tilt.objects.create(
    name="Blizzard",
    tilt_type="environmental",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Earthquake",
    tilt_type="environmental",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Extreme Cold",
    tilt_type="environmental",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Extreme Heat",
    tilt_type="environmental",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Flooded",
    tilt_type="environmental",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Heavy Rain",
    tilt_type="environmental",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Heavy Winds",
    tilt_type="environmental",
    description="",
    effect="",
    causing="",
    ending="",
)
Tilt.objects.create(
    name="Ice",
    tilt_type="environmental",
    description="",
    effect="",
    causing="",
    ending="",
)

Numina.objects.create(name="Awe")
Numina.objects.create(name="Blast")
Numina.objects.create(name="Dement")
Numina.objects.create(name="Drain")
Numina.objects.create(name="Emotional Aura")
Numina.objects.create(name="Entropic Decay")
Numina.objects.create(name="Firestarter")
Numina.objects.create(name="Hallucination")
Numina.objects.create(name="Implant Mission")
Numina.objects.create(name="Left-Handed Spanner")
Numina.objects.create(name="Mortal Mask")
Numina.objects.create(name="Pathfinder")
Numina.objects.create(name="Regenerate")
Numina.objects.create(name="Seek")
Numina.objects.create(name="Speed")
Numina.objects.create(name="Sign")
Numina.objects.create(name="Stalwart")
Numina.objects.create(name="Telekinesis")
